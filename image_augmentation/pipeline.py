from abc import ABC, abstractmethod
import visualization
import torch
import torch.nn as nn
import kornia
import random
import functools
from operations import utils
import test

device = 'cuda'
cuda = torch.device('cuda')
one_torch = torch.tensor(1, device=cuda)
one_torch = torch.ones(1, device=cuda)
ones_torch = torch.ones(1, 2, device=cuda)
data_types_2d = {"image", "mask", "heatmap"}
identity = torch.eye(3, 3, device=cuda)


def get_compose_matrix(operations):
    matrix = identity.clone()
    for operation in operations:
        if operation.apply_according_to_probability():
            matrix = torch.matmul(operation.get_op_matrix(), matrix)
    return matrix


def get_compose_matrix_and_configure_parameters(operations, data_info):
    matrix = identity.clone()
    for operation in operations:
        if operation.need_data_info():
            operation.config_parameters(data_info)
        if operation.apply_according_to_probability():
            matrix = torch.matmul(operation.get_op_matrix(), matrix)
    return matrix


def split_operations_by_type(operations):
    color, geometry, independent = [], [],  []
    normalize = None
    for op in operations:
        if op.get_op_type() == 'color':
            color.append(op)
        elif op.get_op_type() == 'geometry':
            geometry.append(op)
        elif op.get_op_type() == 'normalize':
            normalize = op
        else:
            independent.append(op)
    if normalize is not None: color.append(normalize) #normalization must be last color operation
    return color, geometry, independent


def compose(*functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)


def get_compose_function(operations):
    funcs = [op.transform_function for op in operations if op.apply_according_to_probability()]
    # compose_function = compose(tuple(funcs))
    compose_function = functools.reduce(lambda f, g: lambda x: f(g(x)), tuple(funcs), lambda x: x)
    lookUpTable = np.empty((1, 256), np.int16)
    for i in range(256):
        lookUpTable[0, i] = compose_function(i)
    lookUpTable[0, :] = np.clip(lookUpTable[0, :], 0, 255)
    return np.uint8(lookUpTable)


def map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


class pipeline_operation(ABC):
    def __init__(self, type, probability=1):
        self.probability = probability
        self.type = type

    @abstractmethod
    def get_op_matrix(self):
        pass

    def get_op_type(self):
        return self.type

    def apply_according_to_probability(self):
        return random.uniform(0, 1) < self.probability


class contrast_pipeline(pipeline_operation):
    def __init__(self, probability, contrast_factor):
        pipeline_operation.__init__(self, probability=probability, type='color')
        self.contrast = contrast_factor

    def get_op_matrix(self):
        raise Exception("Color operations doesnt have matrix")

    def transform_function(self, x):
        contrast = random.randint(self.contrast_range[0], self.contrast_range[1])
        return contrast * (x - 127) + 127

    def transform_function(self, x): return self.contrast * (x - 127) + 127


class random_contrast_pipeline(pipeline_operation):
    def __init__(self, probability, contrast_range):
        pipeline_operation.__init__(self, probability=probability, type='color')
        if not isinstance(contrast_range, tuple) or len(contrast_range) != 2:
            raise Exception("Contrast factor must be tuple of 2 elements")
        self.contrast_range = contrast_range

    def get_op_matrix(self):
        raise Exception("Color operations doesnt have matrix")

    def transform_function(self, x):
        contrast = random.randint(self.contrast_range[0], self.contrast_range[1])
        return contrast * (x - 127) + 127


class gaussian_noisse_pipeline(pipeline_operation):
    def __init__(self, probability, var=0.5):
        pipeline_operation.__init__(self, probability=probability, type='independent_op')
        self.var = var

    def get_op_matrix(self):
        raise Exception("Independent operations doesnt have matrix")

    def _apply_to_image_if_probability(self, img):
        if pipeline_operation.apply_according_to_probability(self):
            img = utils._apply_gaussian_noise(img, self.var)
        return img


class salt_and_pepper_noisse_pipeline(pipeline_operation):
    def __init__(self, probability, amount=0.01, s_vs_p=0.5):
        pipeline_operation.__init__(self, probability=probability, type='independent_op')
        self.amount = amount
        self.s_vs_p = s_vs_p

    def get_op_matrix(self):
        raise Exception("Independent operations doesnt have matrix")

    def _apply_to_image_if_probability(self, img):
        if pipeline_operation.apply_according_to_probability(self):
            img = utils._apply_salt_and_pepper_noise(img, self.amount, self.s_vs_p)
        return img


class spekle_noisse_pipeline(pipeline_operation):
    def __init__(self, probability, intensity=0.2):
        pipeline_operation.__init__(self, probability=probability, type='independent_op')
        self.intensity = intensity

    def get_op_matrix(self):
        raise Exception("Independent operations doesnt have matrix")

    def _apply_to_image_if_probability(self, img):
        if pipeline_operation.apply_according_to_probability(self):
            img = utils._apply_spekle_noise(img, self.intensity)
        return img


class poisson_noisse_pipeline(pipeline_operation):
    def __init__(self, probability):
        pipeline_operation.__init__(self, probability=probability, type='independent_op')

    def get_op_matrix(self):
        raise Exception("Independent operations doesnt have matrix")

    def _apply_to_image_if_probability(self, img):
        if pipeline_operation.apply_according_to_probability(self):
            img = utils._apply_poisson_noise(img)
        return img


class gaussian_blur_pipeline(pipeline_operation):
    def __init__(self, probability):
        pipeline_operation.__init__(self, probability=probability, type='independent_op')

    def get_op_matrix(self):
        raise Exception("Independent operations doesnt have matrix")

    def _apply_to_image_if_probability(self, img):
        if pipeline_operation.apply_according_to_probability(self):
            img = utils.apply_gaussian_blur(img)
        return img


class blur_pipeline(pipeline_operation):
    def __init__(self, probability):
        pipeline_operation.__init__(self, probability=probability, type='independent_op')

    def get_op_matrix(self):
        raise Exception("Independent operations doesnt have matrix")

    def _apply_to_image_if_probability(self, img):
        if pipeline_operation.apply_according_to_probability(self):
            img = utils._apply_blur(img)
        return img


class resize_pipeline(pipeline_operation):
    def __init__(self, probability, new_size):
        pipeline_operation.__init__(self, probability=probability, type='independent_op')
        self.new_size = new_size

    def get_op_matrix(self):
        raise Exception("Independent operations doesnt have matrix")

    def _apply_to_image_if_probability(self, img):
        if pipeline_operation.apply_according_to_probability(self):
            img = utils._resize_image(img, self.new_size)
        return img


class brightness_pipeline(pipeline_operation):
    def __init__(self, probability, brightness_factor):
        pipeline_operation.__init__(self, probability=probability, type='color')
        self.brigthness = brightness_factor

    def get_op_matrix(self):
        raise Exception("Color operations doesnt have matrix")

    def get_op_type(self):
        return 'color'

    def transform_function(self, x): return x + self.brigthness


class random_brightness_pipeline(pipeline_operation):
    def __init__(self, probability, brightness_range):
        pipeline_operation.__init__(self, probability=probability, type='color')
        if not isinstance(brightness_range, tuple) or len(brightness_range) != 2:
            raise Exception("Contrast factor must be tuple of 2 elements")
        self.brightness_range = brightness_range

    def get_op_matrix(self):
        raise Exception("Color operations doesnt have matrix")

    def get_op_type(self):
        return 'color'

    def transform_function(self, x):
        brigthness = random.randint(self.brightness_range[0], self.brightness_range[1])
        return x + brigthness


class gamma_pipeline(pipeline_operation):
    def __init__(self, probability, gamma_factor):
        pipeline_operation.__init__(self, probability=probability, type='color')
        self.gamma = gamma_factor

    def get_op_matrix(self):
        raise Exception("Color operations doesnt have matrix")

    def transform_function(self, x): return pow(x / 255.0, self.gamma) * 255.0


class random_gamma_pipeline(pipeline_operation):
    def __init__(self, probability, gamma_range):
        pipeline_operation.__init__(self, probability=probability, type='color')
        if not isinstance(gamma_range, tuple) or len(gamma_range) != 2:
            raise Exception("Contrast factor must be tuple of 2 elements")
        self.gamma_range = gamma_range

    def get_op_matrix(self):
        raise Exception("Color operations doesnt have matrix")

    def transform_function(self, x):
        gamma = random.randint(self.gamma_range[0], self.gamma_range[1])
        return pow(x / 255.0, gamma) * 255.0


class normalize_pipeline(pipeline_operation):
    def __init__(self, probability=1, old_range=(0, 255), new_range=(0, 1)):
        pipeline_operation.__init__(self, probability=probability, type='normalize')
        self.new_range = new_range
        self.old_range = old_range

    def get_op_matrix(self):
        raise Exception("Color operations doesnt have matrix")

    def transform_function(self, x): return (x + self.old_range[0]) / (self.old_range[1] - self.old_range[0])

class desnormalize_pipeline(pipeline_operation):
    def __init__(self, probability=1, old_range=(0, 1), new_range=(0, 255)):
        pipeline_operation.__init__(self, probability=probability, type='normalize')
        self.new_range = new_range
        self.old_range = old_range

    def get_op_matrix(self):
        raise Exception("Color operations doesnt have matrix")

    def transform_function(self, x): return (x + self.old_range[0]) / (self.old_range[1] - self.old_range[0])

class scale_pipeline(pipeline_operation):
    def __init__(self, probability, scale_factor, center=None):
        pipeline_operation.__init__(self, probability=probability, type='geometry')
        if center is None:
            self.config = True
            self.center = ones_torch
        else:
            self.center = center
            self.config = False
        self.matrix = identity.clone()
        self.ones_2 = torch.ones(2, device=cuda)
        self.scale_factor = self.ones_2
        if isinstance(self.scale_factor,
                      float):  # si solo se proporciona un valor; se escala por igual en ambos ejes
            self.scale_factor = self.ones_2 * scale_factor
        else:
            self.scale_factor[0] *= scale_factor[0]
            self.scale_factor[1] *= scale_factor[1]

    def config_parameters(self, data_info):
        self.config = False
        self.center[..., 1] = data_info['shape'][-1] // 2
        self.center[..., 0] = data_info['shape'][-2] // 2

    def get_op_matrix(self):
        self.matrix[0, 0] = self.scale_factor[0]
        self.matrix[1, 1] = self.scale_factor[1]
        self.matrix[0, 2] = (-self.scale_factor[0] + 1) * self.center[:, 0]
        self.matrix[1, 2] = (-self.scale_factor[1] + 1) * self.center[:, 1]
        return self.matrix

    def need_data_info(self):
        return self.config


class random_scale_pipeline(pipeline_operation):
    def __init__(self, probability, scale_range, keep_aspect=True, center_desviation=None, center=None):
        pipeline_operation.__init__(self, probability=probability, type='geometry')
        self.keep_aspect = keep_aspect
        if center is None:
            self.config = True
            self.center = ones_torch
        else:
            self.center = center
            self.config = False
        self.matrix = identity.clone()
        self.ones_2 = torch.ones(2, device=cuda)
        self.scale_factor = self.ones_2
        if not isinstance(scale_range, tuple):
            raise Exception("Scale range must be a tuple")
        else:
            self.scale_factor[0] = one_torch * scale_range[0]
            self.scale_factor[1] = one_torch * scale_range[1]
        self.center_desviation = center_desviation

    def config_parameters(self, data_info):
        self.config = False
        self.center[..., 1] = data_info['shape'][-1] // 2
        self.center[..., 0] = data_info['shape'][-2] // 2

    def get_op_matrix(self):
        scale_factor_x = random.uniform(self.scale_factor[0], self.scale_factor[1])
        if self.keep_aspect:
            scale_factor_y = scale_factor_x
        else:
            scale_factor_y = random.uniform(self.scale_factor[0], self.scale_factor[1])
        self.matrix[0, 0] = scale_factor_x
        self.matrix[1, 1] = scale_factor_y
        if self.center_desviation is not None:
            self.center[:, 0] += random.randint(0, self.center_desviation)
            self.matrix[0, 2] = (-scale_factor_x + 1) * (
                        self.center[:, 0] + random.randint(-self.center_desviation, self.center_desviation))
            self.matrix[1, 2] = (-scale_factor_y + 1) * (
                        self.center[:, 1] + random.randint(-self.center_desviation, self.center_desviation))
        else:
            self.matrix[0, 2] = (-scale_factor_x + 1) * self.center[:, 0]
            self.matrix[1, 2] = (-scale_factor_y + 1) * self.center[:, 1]
        return self.matrix

    def need_data_info(self):
        return self.config


class rotate_pipeline(pipeline_operation):
    def __init__(self, probability, degrees, center=None):
        pipeline_operation.__init__(self, probability=probability, type='geometry')
        self.degrees = degrees
        self.degrees = degrees * one_torch
        self.new_row = torch.Tensor(1, 3).to(device)
        if center is None:
            self.config = True
            self.center = ones_torch.clone()
        else:
            self.config = False
            self.center = center

    def get_op_matrix(self):
        return torch.cat(((kornia.geometry.get_rotation_matrix2d(angle=self.degrees, center=self.center,
                                                                 scale=one_torch)).reshape(2, 3), self.new_row))

    def need_data_info(self):
        return self.config

    def config_parameters(self, data_info):
        self.center[..., 0] = data_info['shape'][-2] // 2  # x
        self.center[..., 1] = data_info['shape'][-1] // 2
        self.config = False


class random_rotate_pipeline(pipeline_operation):
    def __init__(self, probability, degrees_range, center_desviation=None, center=None):
        pipeline_operation.__init__(self, probability=probability, type='geometry')
        self.center_desviation = center_desviation
        if not isinstance(degrees_range, tuple):
            raise Exception("Degrees range must be a tuple (min, max)")
        self.degrees_range = degrees_range
        self.new_row = torch.Tensor(1, 3).to(device)
        if center is None:
            self.config = True
            self.center = ones_torch.clone()
        else:
            self.config = False
            self.center = center

    def get_op_matrix(self):
        degrees = random.randint(self.degrees_range[0], self.degrees_range[1]) * one_torch
        center = self.center
        if self.center_desviation is not None:
            center += random.randint(-self.center_desviation, self.center_desviation)
        return torch.cat(((kornia.geometry.get_rotation_matrix2d(angle=degrees, center=center,
                                                                 scale=one_torch)).reshape(2, 3), self.new_row))

    def need_data_info(self):
        return self.config

    def config_parameters(self, data_info):
        self.center[..., 0] = data_info['shape'][-2] // 2  # x
        self.center[..., 1] = data_info['shape'][-1] // 2
        self.config = False


class translate_pipeline(pipeline_operation):
    def __init__(self, probability, translation):
        pipeline_operation.__init__(self, probability=probability, type='geometry')
        self.translation_x = translation[0] * one_torch
        self.translation_y = translation[1] * one_torch
        self.matrix = identity.clone()

    def get_op_matrix(self):
        self.matrix[0, 2] = self.translation_x
        self.matrix[1, 2] = self.translation_y
        return self.matrix

    def need_data_info(self):
        return False

class random_translate_pipeline(pipeline_operation):
    def __init__(self, probability, translation_range, keep_dim = False):
        pipeline_operation.__init__(self, probability=probability, type='geometry')
        if not isinstance(translation_range, tuple):
            raise Exception("Translation range must be a tuple (min, max)")
        self.translation_range = translation_range
        self.keep_dim = keep_dim
        self.matrix = identity.clone()

    def get_op_matrix(self):
        translation_x = random.uniform(self.translation_range[0], self.translation_range[1])
        if self.keep_dim:
            translation_y = translation_x
        else:
            translation_y = random.uniform(self.translation_range[0], self.translation_range[1])
        self.matrix[0, 2] = translation_x
        self.matrix[1, 2] = translation_y
        return self.matrix

    def need_data_info(self):
        return False


class shear_pipeline(pipeline_operation):
    def __init__(self, probability, shear):
        pipeline_operation.__init__(self, probability=probability, type='geometry')
        self.shear_x = shear[0]
        self.shear_y = shear[1]
        self.matrix = identity.clone()

    def get_op_matrix(self):
        self.matrix[0, 1] = self.shear_x
        self.matrix[1, 0] = self.shear_y
        return self.matrix

    def need_data_info(self):
        return False

class random_shear_pipeline(pipeline_operation):
    def __init__(self, probability, shear_range):
        pipeline_operation.__init__(self, probability=probability, type='geometry')
        if not isinstance(shear_range, tuple):
            raise Exception("Translation range must be a tuple (min, max)")
        self.shear_range = shear_range
        self.matrix = identity.clone()

    def get_op_matrix(self):
        self.matrix[0, 1] = random.uniform(self.shear_range[0], self.shear_range[1]) #x
        self.matrix[1, 0] = random.uniform(self.shear_range[0], self.shear_range[1]) #y
        return self.matrix

    def need_data_info(self):
        return False


class hflip_pipeline(pipeline_operation):
    def __init__(self, probability):
        pipeline_operation.__init__(self, probability=probability, type='geometry')
        self.config = True
        self.matrix = identity.clone()
        self.matrix[0, 0] = -1
        # self.matrix[0, 2] = self.width

    def need_data_info(self):
        return self.config

    def config_parameters(self, data_info):
        self.matrix[0, 2] = data_info['shape'][1]
        self.config = False

    def get_op_matrix(self):
        return self.matrix


class vflip_pipeline(pipeline_operation):
    def __init__(self, probability, heigth=256):
        pipeline_operation.__init__(self, probability=probability, type='geometry')
        self.matrix = identity.clone()
        self.config = True
        self.matrix[1, 1] = -1
        self.matrix[1, 2] = heigth

    def need_data_info(self):
        return self.config

    def config_parameters(self, data_info):
        self.matrix[1, 2] = data_info['shape'][1]
        self.config = False

    def get_op_matrix(self):
        return self.matrix


def preprocess_dict_data_and_2dtypes(data):
    p_data = {}
    types_2d = {}
    compose_data = torch.tensor([])
    for type in data.keys():
        if type in data_types_2d:
            if data[type].dim() > 3: data[type] = data[type][0, :]
            compose_data = torch.cat((compose_data, data[type]),
                                     0)  # concatenate data into one multichannel pytoch tensor
            types_2d[type] = data[type].shape[0]
        else:
            p_data['points_matrix'] = data[type]
    p_data['data_2d'] = compose_data.to(device)
    if p_data.keys().__contains__('points_matrix'):  p_data[
        'points_matrix'] = utils.keypoints_to_homogeneus_and_concatenate(
        p_data['points_matrix'])
    return p_data, types_2d


def preprocess_dict_data(data):
    p_data = {}
    compose_data = torch.tensor([])
    for type in data.keys():
        if type in data_types_2d:
            data[type] = kornia.image_to_tensor(data[type])
            if data[type].dim() > 3: data[type] = data[type][0, :]
            compose_data = torch.cat((compose_data, data[type]),
                                     0)  # concatenate data into one multichannel pytoch tensor
        else:
            p_data['points_matrix'] = data[type]
    p_data['data_2d'] = compose_data.to(device)
    if p_data.keys().__contains__('points_matrix'):  p_data[
        'points_matrix'] = utils.keypoints_to_homogeneus_and_concatenate(
        p_data['points_matrix'])
    return p_data


def preprocess_dict_data_and_data_info(data):
    p_data = {}
    data_info = {}
    data_info['types_2d'] = {}
    compose_data = torch.tensor([])
    for type in data.keys():
        if type in data_types_2d:
            if not data_info.keys().__contains__('shape'):
                data_info['shape'] = data[type].shape
                data_info['bpp'] = data[type].dtype
            data[type] = kornia.image_to_tensor(data[type])
            if data[type].dim() > 3: data[type] = data[type][0, :]
            compose_data = torch.cat((compose_data, data[type]),
                                     0)  # concatenate data into one multichannel pytoch tensor
            data_info['types_2d'][type] = data[type].shape[0]
        else:
            p_data['points_matrix'] = data[type]
    p_data['data_2d'] = compose_data.to(device)
    if p_data.keys().__contains__('points_matrix'):  p_data[
        'points_matrix'] = utils.keypoints_to_homogeneus_and_concatenate(
        p_data['points_matrix'])
    return p_data, data_info


def postprocess_data(batch, batch_info):
    process_data = []
    for data in batch:
        if batch_info.keys().__contains__('types_2d'):
            data_output = {}
            data_split = torch.split(data['data_2d'], list(batch_info['types_2d'].values()), dim=0)
            for index, type in enumerate(batch_info['types_2d']):
                data_output[type] = data_split[index]
            if data_output.keys().__contains__('mask'): data_output['mask'] = utils.mask_change_to_01_functional(
                data_output['mask'])
            if data.keys().__contains__('points_matrix'): data_output['keypoints'] = [
                ((dato)[:2, :]).reshape(2) for dato in torch.split(data['points_matrix'], 1, dim=1)]
        else:
            data_output = data['data_2d']
        process_data.append(data_output)
    return process_data


def postprocess_data_and_visualize(batch, data_original, batch_info):
    process_data = []
    for data in batch:
        if batch_info.keys().__contains__('types_2d'):
            data_output = {}
            data_split = torch.split(data['data_2d'], list(batch_info['types_2d'].values()), dim=0)
            for index, type in enumerate(batch_info['types_2d']):
                data_output[type] = data_split[index]
            if data_output.keys().__contains__('mask'): data_output['mask'] = utils.mask_change_to_01_functional(
                data_output['mask'])
            if data.keys().__contains__('points_matrix'): data_output['keypoints'] = [
                ((dato)[:2, :]).reshape(2) for dato in torch.split(data['points_matrix'], 1, dim=1)]
        else:
            data_output = data['data_2d']
        process_data.append(data_output)
    test.visualize(process_data[0:10], data_original[0:10])
    return process_data


class pipeline(object):
    def __init__(self, pipeline_operations):
        self.color_ops, self.geom_ops, self.indep_ops = split_operations_by_type(pipeline_operations)
        self.geom_ops.reverse() #to apply matrix multiplication in the user order
        self.info_data = None

    def apply_geometry_transform_data2d(self, image, matrix):
        return kornia.geometry.affine(image, matrix[:2, :])

    def apply_geometry_transform_points(self, points_matrix, matrix):
        return torch.matmul(matrix, points_matrix)

    def __call__(self, batch_data, visualize=False):
        if visualize: original = [d.copy() for d in batch_data]
        self.process_data = []
        if self.info_data is None:  # First iteration to configure parameters and scan data info while the first item is being processed
            data = batch_data[0]
            batch_data = batch_data[1:]  # exclude the first item in the batch to be processed on the second loop
            lut = get_compose_function(self.color_ops)
            data['image'] = cv2.LUT(data['image'], lut)
            for op in self.indep_ops: data['image'] = op._apply_to_image_if_probability(data['image'])
            p_data, self.info_data = preprocess_dict_data_and_data_info(data)
            matrix = get_compose_matrix_and_configure_parameters(self.geom_ops, self.info_data)
            p_data['data_2d'] = self.apply_geometry_transform_data2d(p_data['data_2d'], matrix)
            p_data['points_matrix'] = self.apply_geometry_transform_points(p_data['points_matrix'], matrix)
            self.process_data.append(p_data)

        for data in batch_data:
            lut = get_compose_function(self.color_ops)
            data['image'] = cv2.LUT(data['image'], lut)
            for op in self.indep_ops: data['image'] = op._apply_to_image_if_probability(data['image'])
            p_data = preprocess_dict_data(data)
            matrix = get_compose_matrix(self.geom_ops)
            p_data['data_2d'] = self.apply_geometry_transform_data2d(p_data['data_2d'], matrix)
            p_data['points_matrix'] = self.apply_geometry_transform_points(p_data['points_matrix'], matrix)
            self.process_data.append(p_data)
        if visualize:
            return postprocess_data_and_visualize(self.process_data, original, self.info_data)
        else:
            return postprocess_data(self.process_data, self.info_data)


import numpy as np
import cv2

img: np.ndarray = cv2.imread('../bird.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

keypoints = ([img.shape[0] // 2, img.shape[1] // 2], [img.shape[0] // 2 + 15, img.shape[1] // 2 - 50],
             [img.shape[0] // 2 + 85, img.shape[1] // 2 - 80], [img.shape[0] // 2 - 105, img.shape[1] // 2 + 60])

points = [torch.from_numpy(np.asarray(point)) for point in keypoints]
# data: torch.tensor = kornia.image_to_tensor(img, keepdim=False)  # BxCxHxW


from operations import utils

# data = color.equalize_histogram(data, visualize=True)

data = {'image': img, 'keypoints': points}
samples = 50

batch = [data.copy() for _ in range(samples)]
batch2 = [data.copy() for _ in range(samples)]

from time import time

start_time = time()
pip = pipeline(pipeline_operations=(
    translate_pipeline(probability=0, translation=(3, 0.05)),
    vflip_pipeline(probability=0),
    hflip_pipeline(probability=0),
    random_contrast_pipeline(probability=0, contrast_range=(0, 50)),
    #normalize_pipeline(),
    #desnormalize_pipeline(),
    resize_pipeline(probability = 1, new_size= (50,50)),
    brightness_pipeline(probability=0, brightness_factor=10),
    random_scale_pipeline(probability=0, scale_range=(0.5, 1.5), center_desviation=20),
    random_rotate_pipeline(probability=0, degrees_range=(-50,50), center_desviation=20),
    random_translate_pipeline(probability=0, translation_range=(20,100)),
    random_shear_pipeline(probability=1, shear_range=(0,0.5))
))
''',
  shear_pipeline(probability=0.9, shear = (0.01, 0.01)),
  
  
  shear_pipeline(probability=0.9, shear = (0.05, 0.01)),
  translate_pipeline(probability=0.2, translation=(0.03,0.05)),
  vflip_pipeline(probability=1),
  hflip_pipeline(probability=1),
  gaussian_noisse_pipeline(probability=0),
  salt_and_pepper_noisse_pipeline(probability=0, amount = 0.1),
  spekle_noisse_pipeline(probability=0),
  poisson_noisse_pipeline(probability=0),
  gaussian_blur_pipeline(probability=0),
  blur_pipeline(probability=1)'''
batch = pip(batch, visualize=True)

operations = (brightness_pipeline(probability=1, brightness_factor=150),
              contrast_pipeline(probability=1, contrast_factor=2))

get_compose_function(operations)
consumed_time = time() - start_time
print(consumed_time)
print(consumed_time / samples)
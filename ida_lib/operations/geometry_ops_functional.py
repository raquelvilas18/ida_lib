from functools import wraps
from string import digits
from typing import Union

import kornia
import torch


from . import utils
from ida_lib.global_parameters import data_types_2d, device, one_torch, internal_type
from .utils import add_new_axis, data_to_numpy, get_principal_type, dtype_to_torch_type
from ..core.pipeline_functional import preprocess_dict_data_and_data_info, postprocess_data
from ..visualization import _get_image_types, plot_image_tranformation


def prepare_data(func):
    """
    Decorator that prepares the input data to apply the geometric transformation. For this purpose, it concatenates all
    the two-dimensional elements of the input data in the same tensor on which a single transformation is applied.  If
    the input data contains point coordinates, they are grouped in a matrix as homogeneous coordinates, over which a
    single matrix multiplication is performed.

    :param func: geometric function to be applied to the data
    :return: processed data
    """

    @wraps(func)
    def wrapped_function(data: dict, visualize: bool, interpolation:str = 'bilinear',  *args, **kwargs):
        principal_type = get_principal_type(data)
        data = data_to_numpy(data)
        original_type = dtype_to_torch_type(data[principal_type].dtype)
        data_original = data.copy()
        p_data, data_info = preprocess_dict_data_and_data_info(data, interpolation)
        data_output = func(p_data, *args, **kwargs) #Execute transform

        data_output = postprocess_data(batch = [data_output], batch_info= data_info, data_original = None, original_type= original_type)
        if visualize:
            plot_image_tranformation(data_output, data_original)
        return data_output

    return wrapped_function


"""---Vertical Flip---"""
def vflip_image(img: torch.tensor)-> torch.tensor:
    return kornia.vflip(img)

def vflip_coordiantes_matrix(matrix: torch.tensor, heigth: int)-> torch.tensor:
    matrix[1] = torch.ones(1, matrix.shape[1]).to(device) * (heigth) - \
    matrix[1]
    return matrix

@prepare_data
def vflip_compose_data(data: dict)->dict:
    """
    :param data : dict of elements to be transformed
    :return: transformed data
    """
    data['data_2d'] = vflip_image(data['data_2d'])
    heigth = data['data_2d'].shape[-2]
    if 'mask'in data:
        data['points_matrix'] = vflip_coordiantes_matrix(data['points_matrix'], heigth)
    return data

"""--- Horizontal Flip---"""

def hflip_image(img: torch.tensor)-> torch.tensor:
    return kornia.hflip(img)

def hflip_coordinates_matrix(matrix: torch.tensor, width: int)-> torch.tensor:
    matrix[0] = torch.ones(1, matrix.shape[1]).to(device) * (width) - \
                               matrix[0]
    return matrix

@prepare_data
def hflip_compose_data(data: dict) -> dict:
    """
    :param data : dict of elements to be transformed
    :return: transformed data
    """
    data['data_2d'] = hflip_image(data['data_2d'])
    width = data['data_2d'].shape[-1]
    if 'points_matrix' in data:
        data['points_matrix'] = hflip_coordinates_matrix(data['points_matrix'], width)
    return data

""" --- Afine transform ---"""

def affine_image(img: torch.tensor, matrix: torch.tensor)-> torch.tensor:
    return  kornia.geometry.affine(img, matrix)

def affine_coordinates_matrix(matrix_coordinates: torch.tensor, matrix_transformation: torch.tensor) -> torch.tensor:
    return torch.matmul(matrix_transformation, matrix_coordinates)

@prepare_data
def affine_compose_data(data: dict, matrix: torch.tensor) -> dict:
    """
    :param data : dict of elements to be transformed
    :param matrix : matrix of transformation
    :return: transformed data
    """
    matrix = matrix.to(device)
    data['data_2d'] = affine_image(data['data_2d'], matrix)
    if 'points_matrix' in data:
        data['points_matrix'] = affine_coordinates_matrix(data['points_matrix'], matrix)
    return data

""" --- Rotate transform --- """
def get_rotation_matrix(center: torch.tensor, degrees: torch.tensor):
    return ( kornia.geometry.get_rotation_matrix2d(angle=degrees, center=center, scale=one_torch)).reshape(2, 3)

def rotate_image(img: torch.tensor, degrees: torch.tensor, center: torch.tensor)-> torch.tensor:
    '''mode'''
    return  kornia.geometry.rotate(img, angle=degrees, center=center)

def rotate_coordinates_matrix(matrix_coordinates: torch.tensor, matrix: torch.tensor)-> torch.tensor:
    return torch.matmul(matrix, matrix_coordinates)

@prepare_data
def rotate_compose_data(data: dict, degrees: torch.tensor, center: torch.tensor):
    """
    :param data : dict of elements to be transformed
    :param degrees : counterclockwise degrees of rotation
    :param center : center of rotation. Default, center of the image
    :return: transformed data
    """
    degrees = degrees * one_torch
    if center is None:
        center = utils.get_torch_image_center(data['data_2d'])
    else:
        center = center
    center = center.to(device)
    data['data_2d'] = rotate_image(data['data_2d'], degrees, center)
    matrix = get_rotation_matrix(center, degrees)
    if 'points_matrix' in data:
        data['points_matrix'] = rotate_coordinates_matrix(data['points_matrix'], matrix)
    return data

""" ---Scale Transform----"""
def get_scale_matrix(center: torch.tensor, scale_factor: Union[float, torch.tensor]):
    if isinstance(scale_factor,
                  float) or scale_factor.dim() == 1:  # si solo se proporciona un valor; se escala por igual en ambos ejes
        scale_factor = torch.ones(2).to(device) * scale_factor
    matrix = torch.zeros(2, 3).to(device)
    matrix[0, 0] = scale_factor[0]
    matrix[1, 1] = scale_factor[1]
    matrix[0, 2] = (-scale_factor[0] + 1) * center[:, 0]
    matrix[1, 2] = (-scale_factor[1] + 1) * center[:, 1]
    return matrix

def scale_image(img: torch.tensor, scale_factor: torch.tensor, center: torch.tensor) -> torch.tensor:
    return  kornia.geometry.scale(img, scale_factor=scale_factor, center=center)

def scale_coordinates_matrix(matrix_coordinates: torch.tensor, matrix: torch.tensor) -> torch.tensor:
    return torch.matmul(matrix, matrix_coordinates)

@prepare_data
def scale_compose_data(data: dict, scale_factor: Union[float, torch.tensor], center: Union[torch.tensor, None]=None) -> dict:
    """
    :param data: dict of elements to be transformed
    :param scale_factor  : factor of scaling
    :param center : center of scaling. By default its taken the center of the image
    :return: transformed data
    """
    scale_factor = (torch.ones(1) * scale_factor).to(device)
    if center is None:
        center = utils.get_torch_image_center(data['data_2d'])
    center = center.to(device)
    data['data_2d'] = scale_image(data['data_2d'], scale_factor, center)
    matrix = get_scale_matrix(center, scale_factor)
    if 'points_matrix' in data:
        data['points_matrix'] = scale_coordinates_matrix( data['points_matrix'], matrix)
    return data

""" --- Translation transform ---"""
def translate_image(img: torch.tensor, translation: torch.tensor)-> torch.tensor:
    return kornia.geometry.translate(img, translation)

def translate_coordinates_matrix(matrix_coordinates: torch.tensor, translation: torch.tensor) -> torch.tensor:
    matrix = torch.zeros((3, matrix_coordinates.shape[1])).to(device)
    row = torch.ones((1, matrix_coordinates.shape[1])).to(device)
    matrix[0] = row * translation[:, 0]
    matrix[1] = row * translation[:, 1]
    return  matrix_coordinates + matrix

@prepare_data
def translate_compose_data(data: dict, translation: Union[int, torch.tensor]) -> dict:
    """
    :param data : dict of elements to be transformed
    :param translation : number of pixels to translate
    :return: transformed data
    """
    if not torch.is_tensor(translation):
        translation = (torch.tensor(translation).float().reshape((1, 2)))
    translation = translation.to(device)
    data['data_2d'] = translate_image(data['data_2d'], translation)
    if 'points_matrix' in data:
        data['points_matrix'] =  translate_coordinates_matrix(data['points_matrix'], translation)
    return data


""" --- Shear Transform ---"""
def get_shear_matrix(shear_factor: torch.tensor) -> torch.tensor:
    matrix = torch.eye(2, 3).to(device)
    matrix[0, 1] = shear_factor[...,0]
    matrix[1, 0] = shear_factor[...,1]
    return matrix

def shear_image(img: torch.tensor, shear_factor: torch.tensor) -> torch.tensor:
    return kornia.geometry.affine(img, shear_factor)

def shear_coordinates_matrix(matrix_coordinates: torch.tensor, matrix: torch.tensor) -> torch.tensor:
    return  torch.matmul(matrix, matrix_coordinates)

@prepare_data
def shear_compose_data(data: dict, shear_factor: Union[float, torch.tensor]) -> dict:
    """
    :param data : dict of elements to be transformed
    :param shear_factor : pixels of shearing
    :return:
    """
    shear_factor = (torch.tensor(shear_factor).reshape(1,2)).to(device)
    matrix = get_shear_matrix(shear_factor)
    data['data_2d'] = shear_image(data['data_2d'], matrix)
    matrix = get_shear_matrix(shear_factor)
    if 'points_matrix' in data:
        data['points_matrix'] =  shear_coordinates_matrix(data['points_matrix'], matrix)
    return data


def own_affine(tensor: torch.Tensor, matrix: torch.Tensor, interpolation: str = 'bilinear',
               padding_mode: str = 'border') -> torch.Tensor:
    """Apply an affine transformation to the image.

    :param tensor :     The image tensor to be warped.
    :param matrix :     The 2x3 affine transformation matrix.
    :param interpolation : interpolation mode to calculate output values
          'bilinear' | 'nearest'. Default: 'bilinear'.
    :param padding_mode : padding mode for outside grid values
          'zeros' | 'border' | 'reflection'. Default: 'zeros'.

    :return : The warped image.
    """
    # warping needs data in the shape of BCHW
    is_unbatched: bool = tensor.ndimension() == 3
    if is_unbatched:
        tensor = torch.unsqueeze(tensor, dim=0)
    matrix = matrix.expand(tensor.shape[0], -1, -1)
    # warp the input tensor
    height: int = tensor.shape[-2]
    width: int = tensor.shape[-1]
    warped: torch.Tensor = kornia.warp_affine(tensor, matrix, (height, width), flags=interpolation, padding_mode=padding_mode)
    # return in the original shape
    if is_unbatched:
        warped = torch.squeeze(warped, dim=0)
    return warped

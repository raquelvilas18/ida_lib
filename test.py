import cv2
import kornia
import matplotlib.pyplot as plt
import numpy as np
import torch

from ida_lib.core.pipeline import Pipeline
from ida_lib.core.pipeline_geometric_ops import ScalePipeline, ShearPipeline
from ida_lib.core.pipeline_local_ops import GaussianNoisePipeline
from ida_lib.global_parameters import identity
from ida_lib.operations import transforms

# read the image with OpenCV
img: np.ndarray = cv2.imread('./micky.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = img.astype(np.float)

keypoints = ([img.shape[0] // 2, img.shape[1] // 2], [img.shape[0] // 2 + 15, img.shape[1] // 2 - 50],
             [img.shape[0] // 2 + 85, img.shape[1] // 2 - 80], [img.shape[0] // 2 - 105, img.shape[1] // 2 + 60])

# convert to torch tensor


points = [torch.from_numpy(np.asarray(point)) for point in keypoints]
data: torch.tensor = kornia.image_to_tensor(img, keepdim=False)  # BxCxHxW
matrix = torch.eye(3, 3)
matrix[0,1]=0.5
matrix[1,1]=0.5
data = {'image': data}

data = transforms.affine(data,matrix=matrix, visualize=True)

'''keypoints = ([img.shape[0] // 2, img.shape[1] // 2], [img.shape[0] // 2 + 15, img.shape[1] // 2 - 50],
             [img.shape[0] // 2 + 85, img.shape[1] // 2 - 80], [img.shape[0] // 2 - 105, img.shape[1] // 2 + 60])
points = [torch.from_numpy(np.asarray(point)) for point in keypoints]
mask_example1 = np.zeros((img.shape[0], img.shape[1], 1), dtype=np.float)
mask_example1[0:50, 0:50] = 1
# data = color.equalize_histogram(data, visualize=True)


data = {'image': torch.from_numpy(np.random.randint(low=0, high=256, size=(100,100, 3), dtype=np.uint8))}

#data = {'image': data, 'mask': mask_example1, 'keypoints': points}
matrix = torch.eye(2, 3).to('cuda')

center = torch.ones(1, 2)
center[..., 0] = data['image'].shape[-2] // 2  # x
center[..., 1] = data['image'].shape[-1] // 2  # y

size = (100, 100)
def numpy_float_all_elements_item():
    img = np.random.randint(low=0, high=256, size=(size[0], size[1], 3)).astype(np.float)
    # Generate an example of segmentation map over the image
    segmap = np.zeros((img.shape[0], img.shape[1], 1), dtype=np.float)
    segmap[28:171, 35:485, 0] = 1
    segmap[10:25, 30:245, 0] = 2
    segmap[10:25, 70:385, 0] = 3
    segmap[10:110, 5:210, 0] = 4
    segmap[18:223, 10:110, 0] = 5

    # Generate 2 examples of masks
    mask_example1 = np.zeros((img.shape[0], img.shape[1], 1), dtype=np.float)
    mask_example1[0:50, 0:50] = 1
    # Generate an example of heatmap over the image


    return {'segmap': segmap, 'mask': mask_example1}
'''
'''samples = 10
data = {'image': np.random.randint(low=0, high=256, size=(size[0], size[1], 3), dtype=np.uint8)}
batch = [data.copy() for _ in range(samples)]
shape = (10, 20)
pip = Pipeline(interpolation='nearest',
                   resize=shape,
                   pipeline_operations=(
                       ScalePipeline(probability=1, scale_factor=0.5),
                       ShearPipeline(probability=0.5, shear=(0.2, 0.2)),
                       GaussianNoisePipeline(probability=0.5)))
augmented = pip(batch)'''
print('hoi')
# data = geometry.translate(data, visualize = False, translation = (20,-10))
# data = geometry.scale(data, visualize = False, scale_factor=0.75)

# data = geometry.affine(data, visualize=False, matrix=matrix)
# data = geometry.shear(data, visualize=False, shear_factor=(0.1,0.3))
# data = geometry.rotate(data, visualize=False, degrees=35.8, center = center)
# data = transforms.change_brigntness(data, visualize=False, bright=0.8)
# data = color.change_contrast(data, visualize=False, contrast=0.1)
# data = color.equalize_histogram(data, visualize=False)
# data = color.change_gamma(data, gamma=1.5, visualize=False)
# data = color.gaussian_blur(data)
# data = color.blur(data)
# data = color.inyect_salt_and_pepper_noise(data)
# data = color.inyect_spekle_noise(data)
# data = color.inyect_poisson_noise(data) (!!!!)
# data['image'] = color.inyect_gaussian_noise(data['image'], var=0.5)


"""


from operations import utils

utils.keypoints_to_homogeneous_and_concatenate(points)

#data_warped: torch.tensor = kornia.warp_affine(data.float(), M, dsize=(h, w))
#data_warped: torch.tensor = kornia.hflip(data_warped)
#data_warped: torch.tensor = geometry.scale(data, 0.8)


center = torch.ones(1, 2)
center[..., 0] = img.shape[2] / 2  # x
center[..., 1] = img.shape[1] / 2  # y
alpha = 45.0
angle = torch.ones(1) * alpha
scale= torch.ones(1)
tr = kornia.get_rotation_matrix2d(center, angle, scale).to('cuda')
data_warped = geometry.vflip(data, True)
#data_warped = geometry.rotate(data, degrees=25,visualize=True)
#data_warped: torch.tensor = geometry.rotate(data_warped, 30)
# convert back to numpy
img_warped: np.ndarray = kornia.tensor_to_image(data_warped['image'].byte()[0])"""

'''# create the plot
img_warped: np.ndarray = kornia.tensor_to_image(data['image'].byte()[0])
fig, axs = plt.subplots(1, 2, figsize=(16, 10))
axs = axs.ravel()

axs[0].axis('off')
axs[0].set_title('image source')
xvalues = [value[0] for value in keypoints]
yvalues = [value[1] for value in keypoints]
axs[0].scatter(x=xvalues, y=yvalues, s=80)
axs[0].imshow(img)

axs[1].axis('off')
axs[1].set_title('image warped')
xvalues_warped = [value[0].cpu().numpy() for value in data['keypoints']]
yvalues_warped = [value[1].cpu().numpy() for value in data['keypoints']]
axs[1].scatter(x=xvalues_warped, y=yvalues_warped, s=80)
axs[1].imshow(img_warped)
plt.show()'''

"""
image = torch.rand(2, 50 , 50)
keypoints = (torch.rand(1,2), torch.rand(1,2))


mask = torch.rand(1,50,50)
for i in range(mask.shape[1]):
    for j in range(mask.shape[2]):
        if mask[0,i,j] < 0.3:
            mask[0,i,j] = 0
        else:
            mask[0,i,j] = 1
center = torch.ones(1, 2)
center[..., 0] = 25  # x
center[..., 1] = 25  # y
alpha = 4.0
angle = torch.ones(1) * alpha
scale= torch.ones(1)
tr = kornia.get_rotation_matrix2d(center, angle, scale)

point = torch.rand(1,2)
point = torch.cat((point, torch.ones(1,1)), axis = 1)



data = {"image": image, "mask": image, "keypoints": keypoints}
#image = geometry.preprocess_data(data)


center = torch.ones(1, 2)
center[..., 0] = 25  # x
center[..., 1] = 25 # y
alpha = 45.0
angle = torch.ones(1) * alpha
scale= torch.ones(1)
tr = kornia.get_rotation_matrix2d(center, angle, scale)
degrees = 20
data= kornia.geometry.rotate(image, angle=degrees*torch.ones(1))


"""

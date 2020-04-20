import numpy as np
import torch
from operations import geometry, color
import kornia
from matplotlib import image
import matplotlib.pyplot as plt
import cv2


# read the image with OpenCV
img: np.ndarray = cv2.imread('../gato.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

keypoints = ([img.shape[0]//2, img.shape[1]//2], [img.shape[0]//2  + 15, img.shape[1]//2 - 50], [img.shape[0]//2  + 85, img.shape[1]//2 - 80], [img.shape[0]//2  - 105, img.shape[1]//2 +60])

# convert to torch tensor




points = [torch.from_numpy(np.asarray(point)) for point in keypoints]
#data: torch.tensor = kornia.image_to_tensor(img, keepdim=False)  # BxCxHxW


from operations import utils
data = color.bright_lut(img, brigth=155, visualize=True)

data = {'image':data, 'keypoints': points, 'mask': data}

#data = geometry.vflip(data, True)

from time import time


'''


from operations import utils

utils.keypoints_to_homogeneus_and_concatenate(points)

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
img_warped: np.ndarray = kornia.tensor_to_image(data_warped['image'].byte()[0])'''

# create the plot
img_warped: np.ndarray = kornia.tensor_to_image(data['image'].byte()[0])
fig, axs = plt.subplots(1, 2, figsize=(16, 10))
axs = axs.ravel()

axs[0].axis('off')
axs[0].set_title('image source')
xvalues = [value[0] for value in keypoints]
yvalues = [value[1] for value in keypoints]
axs[0].scatter(x = xvalues, y = yvalues, s=80)
axs[0].imshow(img)

axs[1].axis('off')
axs[1].set_title('image warped')
xvalues_warped = [value[0].numpy() for value in data['keypoints']]
yvalues_warped = [value[1].numpy() for value in data['keypoints']]
axs[1].scatter(x = xvalues_warped, y = yvalues_warped, s=80)
axs[1].imshow(img_warped)
plt.show()

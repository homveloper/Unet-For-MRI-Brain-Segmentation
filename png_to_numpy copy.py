import numpy as np
import os
import cv2

t1w_images = []
t2f_images = []
t2w_images = []
masks = []

# T1W 이미지들 load
path_T1W = r'C:/MRI_Brain/dataset/T1W_brain_pic/'
file_list = os.listdir(path_T1W)

for img in file_list:
    img_path = path_T1W + img
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, dsize=(512, 512), interpolation=cv2.INTER_CUBIC)
    t1w_images.append(image)

# T2F 이미지들 load
path_T2F = 'C:/MRI_Brain/dataset/T2F_brain_pic/'
file_list = os.listdir(path_T2F)

for img in file_list:
    img_path = path_T2F + img
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, dsize=(512, 512), interpolation=cv2.INTER_CUBIC)
    t2f_images.append(image)

# T2W 이미지들 load
path_T2W = 'C:/MRI_Brain/dataset/T2W_brain_pic/'
file_list = os.listdir(path_T2W)

for img in file_list:
    img_path = path_T2W + img
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, dsize=(512, 512), interpolation=cv2.INTER_CUBIC)
    t2w_images.append(image)

# mask 이미지들 load
path_mask = 'C:/MRI_Brain/dataset/mask/'
file_list = os.listdir(path_mask)

for img in file_list:
    img_path = path_mask + img
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, dsize=(512, 512), interpolation=cv2.INTER_CUBIC)
    masks.append(image)

# numpy array로 변환 후 저장
t1w_images = np.array(t1w_images)
t2f_images = np.array(t2f_images)
t2w_images = np.array(t2w_images)
masks = np.array(masks)

np.save(r"dataset\numpy\t1w_images.npy", t1w_images)
np.save(r"dataset\numpy\t2f_images.npy", t2f_images)
np.save(r"dataset\numpy\t2w_images.npy", t2w_images)
np.save(r"dataset\numpy\masks.npy", masks)
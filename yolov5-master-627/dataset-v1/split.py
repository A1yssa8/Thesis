import os
import random
import shutil

# 定义数据集的根目录
data_dir = 'datav1'

# 定义训练集和验证集的目录
train_dir = 'D:\\thesis\\datav1\\train'
val_dir = 'D:\\thesis\\datav1\\val'

# 定义训练集和验证集的比例
train_ratio = 0.8

# 获取所有图像文件的路径
image_paths = [os.path.join(data_dir, 'images', filename) for filename in os.listdir(os.path.join(data_dir, 'images'))]

# 随机打乱图像文件的路径
random.shuffle(image_paths)

# 计算训练集和验证集的边界
train_end = int(len(image_paths) * train_ratio)
val_end = len(image_paths)

# 将图像文件和标注文件复制到训练集和验证集的目录中
for i, image_path in enumerate(image_paths):
    filename = os.path.basename(image_path)
    if i < train_end:
        dst_dir = train_dir
    else:
        dst_dir = val_dir
    shutil.copy(image_path, os.path.join(dst_dir, 'images', filename))
    shutil.copy(os.path.join(data_dir, 'labels', filename.replace('.jpg', '.txt')), os.path.join(dst_dir, 'labels', filename.replace('.jpg', '.txt')))
import cv2
import numpy as np
import os
from shutil import copy

# 生成掩码文件函数_区分出不同颜色的色块
def generate_Manual(temp_dir, newManual_name):

    src = cv2.imread(temp_dir+'/label.png')
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

    # 绿色区域
    low_hsv = np.array([35,43,46])
    high_hsv = np.array([77,255,255])

    # 红色区域
    # low_hsv = np.array([0,43,46])
    # high_hsv = np.array([10,255,255])

    # 黄色区域
    # low_hsv = np.array([26,43,46])
    # high_hsv = np.array([34,255,255])

    # 蓝色区域
    # low_hsv = np.array([100,43,46])
    # high_hsv = np.array([124,255,255])

    mask = cv2.inRange(hsv, lowerb=low_hsv, upperb=high_hsv)
    cv2.imwrite(temp_dir + '/'+newManual_name, mask)


# 保存路径
save_dir_manual = './1st_manual'
save_dir_image = './Image'
if not os.path.isdir(save_dir_manual):
    os.makedirs(save_dir_manual)
if not os.path.isdir(save_dir_image):
    os.makedirs(save_dir_image)

# 遍历当前文件夹
pathdir = os.listdir('./label')
count =0
for dir in pathdir:
    print(dir)
    temp_dir = './label/'+dir

    # 新文件夹中的原图像
    newImage_name = str(count) + "_Training.png"
    # 新文件夹中的掩码文件
    newManual_name = str(count) + "_Manual.png"

    # 生成掩码文件
    generate_Manual(temp_dir, newManual_name)

    # 将文件复制到新文件夹
    from_path_manual = temp_dir + '/'+ newManual_name
    from_path_newImage = temp_dir  + '/img.png'

    to_path_manual = save_dir_manual + '/' + newManual_name
    to_path_Image = save_dir_image + '/' + newImage_name

    copy(from_path_manual, to_path_manual)
    print("From "+from_path_manual + " copy to " + to_path_manual)

    copy(from_path_newImage, to_path_Image)
    print("From " + from_path_newImage + " copy to " + to_path_Image)

    count = count + 1



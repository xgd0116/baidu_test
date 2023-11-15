# -*- coding:utf8 -*-
"""公共类方法"""
import os, time, requests
from PIL import Image
from PIL import ImageChops
from skimage import io
from skimage.metrics import structural_similarity as ssim
from skimage.transform import resize
import numpy as np

from selenium.webdriver.common.by import By


# 获取当前项目根路径
def get_project_path():
    project_path = os.path.abspath(os.path.dirname(__file__))
    file_path = project_path[:-5]
    return file_path

def save_screen(driver, file_name):
    project_path = get_project_path()
    today = time.strftime("%Y%m%d", time.localtime())
    screen_path = f"{project_path}/screen/{today}"

    if os.path.exists(screen_path) and os.path.isdir(screen_path):
        pass
    else:
        os.mkdir(screen_path)

    save_path = f"{project_path}/screen/{today}"
    driver.save_screenshot(f"{save_path}/{file_name}.png")

def get_img(img_url):
    # 下载图片到临时文件夹，去除水印，改变图片大小与被测图片一致
    r = requests.get(img_url)
    img_path = f"{get_project_path()}/temp/temp.png"
    with open(img_path, "wb") as f:
        f.write(r.content)

def delete_img():
    # 删除临时存储的图片
    img_path = f"{get_project_path()}/temp/temp.png"
    os.remove(img_path)

def is_alike_pic(path_one, path_two):
    """
    比较图片相似度，相似度在90%以上，返回TRUE
    :param path_one:
    :param path_two:
    :return:
    """
    # 载入图像
    imageA = io.imread(path_one)
    imageB = io.imread(path_two)

    # 将图像转换为灰度图，因为ssim在灰度图上计算
    imageA_gray = Image.fromarray(imageA).convert('L')
    imageB_gray = Image.fromarray(imageB).convert('L')

    # 转换回numpy数组以便处理
    imageA_gray = np.array(imageA_gray)
    imageB_gray = np.array(imageB_gray)

    # 调整图像大小使得它们具有相同的维度
    imageA_gray = resize(imageA_gray, (imageB_gray.shape[0], imageB_gray.shape[1]),
                         anti_aliasing=True)
    imageB_gray = resize(imageB_gray, (imageA_gray.shape[0], imageA_gray.shape[1]),
                         anti_aliasing=True)

    # 计算SSIM
    similarity_index, _ = ssim(imageA_gray, imageB_gray, data_range=imageA_gray.max() - imageB.min(), full=True,
                               multichannel=True)
    if similarity_index > 0.9:
        return True
    return False
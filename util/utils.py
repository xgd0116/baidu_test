# -*- coding:utf8 -*-
"""公共类方法"""
import os


# 获取当前项目根路径
def get_project_path():
    project_path = os.path.abspath(os.path.dirname(__file__))
    file_path = project_path[:-5]
    return file_path

def save_screen(driver, file_name):
    save_path = f"{get_project_path()}/screen"
    driver.save_screenshot(f"{save_path}/{file_name}.png")

if __name__ == '__main__':
    print(get_project_path())
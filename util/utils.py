# -*- coding:utf8 -*-
"""公共类方法"""
import os, time


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

if __name__ == '__main__':
    print(get_project_path())
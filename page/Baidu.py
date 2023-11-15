# -*- coding:utf8 -*-
import time

from util.logs import logs
from selenium.webdriver.common.by import By
from util.utils import get_project_path

class BaiduPage:

    def __init__(self, driver):
        self.driver = driver
        self.log = logs()

    # def search(self, search_key):
    #     """
    #     在百度首页输入内容，并执行搜索
    #     :param search_key:
    #     :return:
    #     """
    #     self.driver.find_element(By.ID, "kw").send_keys(search_key)
    #     self.log.info(f"输入要搜索的内容：{search_key}")
    #     self.driver.find_element(By.ID, "su").click()
    #     self.log.info("点击<百度一下>按钮")
    #
    # def search_click(self, visit_result):
    #     """
    #     在百度搜索结果页，根据传入参数，打开对应的结果页
    #     :param visit_result:
    #     :return:
    #     """
    #     self.driver.find_element(By.XPATH, f'//div[@id="{int(visit_result)}"]//span').click()
    #     self.log.info(f"点击第{visit_result}个搜索结果")

    def search_by_image(self, search_key):
        """
        search by image
        :return:
        """
        self.driver.find_element(By.XPATH, '//span[@class="soutu-btn"]').click()
        self.log.info("点击按钮：按图片搜索")
        self.driver.find_element(By.XPATH, '//input[@class="upload-pic"]').send_keys(f"{get_project_path()}/TestData/pic/{search_key}")
        self.log.info("发送本地文件路径执行搜索")

    def search_by_image_click(self, visit_result):
        """
        在按图片搜索结果页，根据传入参数，打开对应的结果页
        :param visit_result:
        :return:
        """
        self.driver.find_element(By.XPATH, f'//div[2]/div[{visit_result}]/div[@class="graph-same-list-item"]').click()
        self.log.info(f"打开第{visit_result}个搜素结果")

# -*- coding:utf8 -*-
from util.logs import logs
from selenium.webdriver.common.by import By

class BaiduPage:

    def __init__(self, driver):
        self.driver = driver
        self.log = logs()

    def search(self, search_key):
        """
        在百度首页输入内容，并执行搜索
        :param search_key:
        :return:
        """
        self.driver.find_element(By.ID, "kw").send_keys(search_key)
        self.log.info(f"输入要搜索的内容：{search_key}")
        self.driver.find_element(By.ID, "su").click()
        self.log.info("点击<百度一下>按钮")

    def search_click(self, visit_result):
        """
        在百度搜索结果页，根据传入参数，打开对应的结果页
        :param visit_result:
        :return:
        """
        self.driver.find_element(By.XPATH, f'//div[@id="{int(visit_result)}"]//span').click()
        self.log.info(f"点击第{visit_result}个搜索结果")

# -*- coding:utf8 -*-
"""测试百度搜索功能"""
from time import sleep

import pytest
from selenium.webdriver.common.by import By

from base_conf import BaseConf
from page.Baidu import BaiduPage
from util.yamls import UtilYaml
from util.logs import logs
from util.utils import save_screen, get_img, delete_img, is_alike_pic, get_project_path

class TestSearch:
    # _driver = None
    _yaml_file = "search.yaml" # 搜索数据配置文件
    _log = logs()

    def setup_class(self):
        # 测试执行前，打开百度首页，获取到driver
        self.driver = BaseConf().get_driver()

    def teardown_class(self):
        # 每一个类中的用例执行完成后，自动退出driver
        self.driver.quit()
        self._log.info("退出浏览器driver")

    # @pytest.mark.parametrize("search_key, visit_result",
    #                          UtilYaml("search.yaml").get_yaml_list("BAIDU", "search_data"))
    # @pytest.mark.skip
    # def test_baidu_search(self, search_key, visit_result):
    #     """百度搜索功能测试"""
    #     BaiduPage(self.driver).search(search_key)
    #     BaiduPage(self.driver).search_click(visit_result)
    #     self.driver.switch_to.window(self.driver.window_handles[-1])
    #     sleep(2)
    #     save_screen(self.driver, f"search_result{visit_result}_image")
    #     self._log.info(f"验证搜索内容：{search_key}是否与第{visit_result}个结果的title相匹配")
    #     assert search_key.lower() in self.driver.title

    @pytest.mark.parametrize("search_key, visit_result",
                             UtilYaml("search.yaml").get_yaml_list("BAIDU", "search_data"))
    def test_search_by_image(self, search_key, visit_result):
        BaiduPage(self.driver).search_by_image(search_key)
        BaiduPage(self.driver).search_by_image_click(visit_result)
        sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        save_screen(self.driver, f"search_by_image_result{visit_result}_image")
        self._log.info(f"验证搜索的图片是否与第{visit_result}结果中的内容相匹配")

        # 获取搜索结果页面内所有的图片元素，循环访问图片元素并下载到本地temp文件夹中
        # 下载完成后，与被测文件进行对比
        # 如果判定图片相似度超过90%，则测试通过，否则测试失败
        img_list = self.driver.find_elements(By.XPATH,
                                      '//div[@class="_1NCGf"]//img[1]')
        result = False
        for i in range(len(img_list)):
            img_src = img_list[i].get_attribute("src")
            # 下载图片到本地
            get_img(img_src)
            img_path_one = f"{get_project_path()}/TestData/pic/1.png"
            img_path_two = f"{get_project_path()}/temp/temp.png"
            is_alike = is_alike_pic(img_path_one, img_path_two)
            self._log.info(f"第{i+1}个图片的匹配结果是：{is_alike}")
            delete_img()
            if is_alike is True:
                result = True
                break
        assert True == result


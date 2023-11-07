# -*- coding:utf8 -*-
"""测试百度搜索功能"""
from time import sleep

import pytest
from base_conf import BaseConf
from page.Baidu import BaiduPage
from util.yamls import UtilYaml
from util.logs import logs
from util.utils import save_screen

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

    @pytest.mark.parametrize("search_key, visit_result",
                             UtilYaml("search.yaml").get_yaml_list("BAIDU", "search_data"))
    def test_baidu_search(self, search_key, visit_result):
        """百度搜索功能测试"""
        BaiduPage(self.driver).search(search_key)
        BaiduPage(self.driver).search_click(visit_result)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        sleep(2)
        save_screen(self.driver, f"search_result{visit_result}_image")
        self._log.info(f"验证搜索内容：{search_key}是否与第{visit_result}个结果的title相匹配")
        assert search_key.lower() in self.driver.title

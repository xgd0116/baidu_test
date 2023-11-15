# -*- coding:utf8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from util.logs import logs
from util.yamls import UtilYaml
from util.utils import get_project_path

class BaseConf:

    _yaml_file = "conf.yaml"
    _url = UtilYaml(_yaml_file).get_env()
    _project_path = get_project_path()

    def __init__(self):
        self.log = logs()

        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        # options.add_argument("--headless")
        options.add_argument('window-size=1920x1080')
        driver_path = f"{self._project_path}/driver/chromedriver"
        service = webdriver.ChromeService(executable_path=driver_path)
        self.driver = webdriver.Chrome(options=options, service=service)
        self.log.info("初始化chrome driver")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.log.info("窗口最大化")

        self.driver.get(self._url)
        self.log.info(f"访问待测地址：{self._url}")

    def get_driver(self):
        return self.driver

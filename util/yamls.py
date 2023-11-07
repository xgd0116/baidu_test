# -*- coding:utf8 -*-
"""读取YAML配置文件"""

import yaml
import os
from util.utils import get_project_path

class UtilYaml:
    def __init__(self, file_name):
        self.conf_path = f"{get_project_path()}/TestData/{file_name}"

    def get_yaml(self, sec, key):
        """不解析，直接返回内容，包括：dict, str等"""
        sec = sec.upper()
        with open(self.conf_path, encoding="utf-8") as fp:
            yaml_data = yaml.load(fp, Loader=yaml.FullLoader)
            data = yaml_data[sec][key]
            return data

    def get_yaml_list(self, sec, key):
        """取出dict中的value进行返回"""
        with open(self.conf_path, encoding="utf-8") as fp:
            yaml_data = yaml.load(fp, Loader=yaml.FullLoader)
            data_list = yaml_data[sec][key]
            result_list = []
            for i in data_list:
                value_list = []
                for key, value in i.items():
                    value_list.append(value)
                result_list.append(value_list)
        return result_list

    def write_yaml(self, sec, key, value):
        sec = sec.upper()
        with open(self.conf_path, encoding="utf-8") as fp:
            yaml_data = yaml.safe_load(fp)
        yaml_data[sec][key] = value
        with open(self.conf_path, 'w', encoding="utf-8") as fp:
            yaml.safe_dump(yaml_data, fp, default_flow_style=False)

    def write_env(self, value):
        self.write_yaml("ENV_RUN", "env", value)

    def get_env(self):
        env = self.get_yaml("ENV_RUN", "env")
        url = self.get_yaml(env, "url")
        return url


if __name__ == '__main__':
    print(UtilYaml("search.yaml").get_yaml_list("BAIDU", "search_data")[0])
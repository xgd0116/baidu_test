# -*- coding:utf8 -*-
import pytest
import sys
from util.logs import logs
from util.yamls import UtilYaml
import log_zip

_log = logs()
log_zip.run()

if __name__ == '__main__':

    env = "live" # 默认的运行环境
    # 读取参数，配置本次运行的环境
    param = sys.argv[1:]
    for p in param:
        if "env" in p:
            env = p.split("=")[1]
    UtilYaml("conf.yaml").write_env(env)
    _log.info(f"本次运行环境：{env}")

    _log.info("开始执行用例")
    pytest.main()
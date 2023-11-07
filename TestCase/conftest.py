# -*- coding:utf8 -*-

import pytest
from util.logs import logs
_log = logs()

@pytest.hookimpl(hookwrapper=True, tryfirst=False)
def collect_result(item):
    """
    收集测试结果，并在日志中输出
    :param item:
    :return:
    """
    outcome = yield
    report = outcome.get_result()
    case = item.function.__doc__
    print(case)
    if report.outcome == "failed":
        print("11111111")
        _log.info(f"用例<{case}>运行失败，请检查。")
    else:
        print('222222222')
        _log.info(f"用例<{case}>运行成功!!!!")

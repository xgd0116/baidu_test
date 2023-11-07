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
    print(111)
    outcome = yield
    report = outcome.get_result()
    case = item.function.__doc__
    print(1111)
    if report.outcome == "failed":
        _log.info(f"用例<{case}>运行失败，请检查。")
    if report.outcome == "passed":
        _log.info(f"用例<{case}>运行成功!!!!")

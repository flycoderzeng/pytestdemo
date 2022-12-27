# -*- coding: UTF-8 -*-
import os
import pytest
from time import strftime
from py.xml import html
from datetime import datetime


def pytest_configure(config):
    """ 测试运行之前修改环境参数 """
    config._metadata["测试人员"] = "tester"
    config._metadata['开始时间'] = strftime('%Y-%m-%d %H:%M:%S')
    config._metadata.pop("JAVA_HOME")


# 编辑报告标题
def pytest_html_report_title(report):
    report.title = "自动化测试报告"

def pytest_addoption(parser):
    '''增加命令行参数 --env_name'''
    parser.addoption(
        '--env_name',
        action='store',
        # default: 默认值
        default='A',
        help='测试环境'
    )

@pytest.fixture(scope='session', autouse=True)  # autouse=True自动执行该前置操作
def env_name(request):
    '''获取命令行参数，给到环境变量'''
    os.environ['env_name'] = request.config.getoption('--env_name')
    return request.config.getoption('--env_name')

def pytest_html_results_table_header(cells):
    cells.insert(1, html.th("用例描述", id='description'))
    cells.insert(2, html.th("Time", class_="sortable time", col="time"))
    cells.pop()

def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))

def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(datetime.utcnow(), class_="col-time"))
    cells.pop()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
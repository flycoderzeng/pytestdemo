# -*- coding: UTF-8 -*-
import pytest

from pytestdemo.utils.file_utils import FileUtils

 




if __name__ == '__main__':
    pytest.main(['-s', '-v', 'autotest/testcases/', '--env_name=B',
     r'--html=C:\Users\zengb\Documents\ci\logs\report.html', '--self-contained-html', '--capture=sys'])
    FileUtils.change_file(r'C:\Users\zengb\Documents\ci\logs\report.html', '<meta charset="utf-8"/>', '<meta charset="gb2312"/>', 'gb2312')
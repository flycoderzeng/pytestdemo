# -*- coding: UTF-8 -*-
from pytestdemo.common.logger_handler import logger


class Test_DEF():

    def setup_class(self):
        logger.info("------->setup_class 初始化类")

    def teardown_class(self):
        logger.info("------->teardown_class")

    def test_a(self, env_name):
        '''
        用户名为空
        '''
        logger.info("------->test_d: %s" % env_name)
        assert 1 == 0

    def test_b(self):
        logger.info("------->test_e")
        raise Exception('hello, world!')

    def test_c(self):
        logger.info("------->test_f")

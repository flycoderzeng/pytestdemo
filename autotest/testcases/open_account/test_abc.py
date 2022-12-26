# -*- coding: UTF-8 -*-
from pytestdemo.common.logger_handler import logger


class Test_ABC():

    def setup_class(self):
        logger.info("------->setup_class")

    def teardown_class(self):
        logger.info("------->teardown_class")

    def test_a(self, env_name):
        logger.info("------->test_a: %s" % env_name)
        assert 1 == 1

    def test_b(self):
        logger.info("------->test_b")

    def test_c(self):
        logger.info("------->test_c")

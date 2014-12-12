from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import six
import logging
import unittest

import trackpy
import trackpy.diag


class DiagTests(unittest.TestCase):
    def test_performance_report(self):
        trackpy.diag.performance_report()

class LoggerTests(unittest.TestCase):
    def test_heirarchy(self):
        self.assertTrue(trackpy.linking.logger.parent is trackpy.logger)
        self.assertTrue(trackpy.feature.logger.parent is trackpy.logger)
        self.assertTrue(trackpy.preprocessing.logger.parent is trackpy.logger)

    def test_convenience_funcs(self):
        trackpy.quiet(True)
        self.assertEqual(trackpy.logger.level, logging.WARN)
        trackpy.quiet(False)
        self.assertEqual(trackpy.logger.level, logging.INFO)

        trackpy.ignore_logging()
        self.assertEqual(len(trackpy.logger.handlers), 0)
        self.assertEqual(trackpy.logger.level, logging.NOTSET)
        self.assertTrue(trackpy.logger.propagate)

        trackpy.handle_logging()
        self.assertEqual(len(trackpy.logger.handlers), 1)
        self.assertEqual(trackpy.logger.level, logging.INFO)
        self.assertEqual(trackpy.logger.propagate, 1)

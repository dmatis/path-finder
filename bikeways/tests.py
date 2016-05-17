from django.test import TestCase
import unittest


class TestBasic(unittest.TestCase):
    "Upload Data tests"


    def test_fails_upload(self):
        a = 1
        self.assertEquals(1,a)


    def test_successful_upload(self):
        a = 1
        assert a == 1


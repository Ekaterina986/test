import unittest
from nose.tools import *
from unittest.mock import patch
from app import secretary_program_start


class TestFunction(unittest.TestCase):
    def test_secretary_program_start(self):
        with patch("builtins.input", side_effect=['p', '10006']):
            self.assertEqual(secretary_program_start(), "Владелец документа - Аристарх Павлов")

test_1 = TestFunction()
test_1.test_secretary_program_start()

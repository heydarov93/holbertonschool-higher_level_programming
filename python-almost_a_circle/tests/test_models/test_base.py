#!/usr/bin/python3
"""The test module for Base class"""


import unittest
from models.base import Base


class Test_Base(unittest.TestCase):

    def test_id_none(self):
        shape = Base()
        self.assertEqual(shape.id, 1, "Id should be 1")

    def test_id_negative(self):
        shape = Base(-1)
        self.assertEqual(shape.id, -1, "Id should be negative")

    def test_id_positive(self):
        id = 5
        shape = Base(id)
        self.assertEqual(shape.id, id, f"Id should be {id}")

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string([{'age': 30}]), '[{"age": 30}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string('[{"age": 30}]'), [{"age": 30}])

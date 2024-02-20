#!/usr/bin/python3

"""Tests Rectangle Class"""


import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch
import os


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r = Rectangle(1, 2, 3, 4, 5)

    def test_attributes(self):
        self.assertEqual(self.r.width, 1)
        self.assertEqual(self.r.height, 2)
        self.assertEqual(self.r.x, 3)
        self.assertEqual(self.r.y, 4)
        self.assertEqual(self.r.id, 5)

    def test_attributes_2(self):
        # without x y
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

        # without y
        r1 = Rectangle(1, 2, 3)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

        # all attributes
        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_area(self):
        self.assertEqual(self.r.area(), 2)

    def test_to_dictionary(self):
        dictionary = {"width": 1, "height": 2, "x": 3, "y": 4, "id": 5}
        self.assertEqual(self.r.to_dictionary(), dictionary)

    def test_update(self):
        self.r.update(10, 20, 30, 40, 50)
        self.assertEqual(self.r.width, 20)
        self.assertEqual(self.r.height, 30)
        self.assertEqual(self.r.x, 40)
        self.assertEqual(self.r.y, 50)
        self.assertEqual(self.r.id, 10)

    def test_typeErrors(self):
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)
        with self.assertRaises(TypeError):
            Rectangle("5", 7)
        with self.assertRaises(TypeError):
            Rectangle(5, "7")
        with self.assertRaises(TypeError):
            Rectangle(5, 7, "4")
        with self.assertRaises(TypeError):
            Rectangle(5, 7, 4, "3")

    def test_valueErrors(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_str(self):
        self.assertEqual(str(self.r), "[Rectangle] (5) 3/4 - 1/2")

    def test_display(self):
        # without x and y exists
        r = Rectangle(3, 3, 0, 0)
        output = "###\n###\n###\n"
        with patch("sys.stdout", new=StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), output)

    def test_display_2(self):
        output = "\n\n\n\n   #\n   #\n"
        with patch("sys.stdout", new=StringIO()) as out:
            self.r.display()
            self.assertEqual(out.getvalue(), output)

    def test_create(self):
        dictionary = {"height": 2, "width": 1, "x": 3, "y": 4, "id": 89}
        r3 = Rectangle.create(**dictionary)
        self.assertEqual(str(r3), "[Rectangle] (89) 3/4 - 1/2")

    def test_save_to_file(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file([Rectangle(1, 2, id=13)])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                file.read(), '[{"id": 13, "width": 1, "height": 2, "x": 0, "y": 0}]')

    def test_load_from_file1(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass

        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_2(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass

        r1 = Rectangle(5, 5)

        inp = [r1]
        Rectangle.save_to_file(inp)
        out = Rectangle.load_from_file()

        self.assertEqual(inp[0].__str__(), out[0].__str__())

#!/usr/bin/python3
""" Unit test for Amenity """

import unittest
import pycodestyle
import json
import os
import inspect
import datetime
from uuid import uuid4

from models.amenity import Amenity
from models.base_model import BaseModel


class TestDocs(unittest.TestCase):
    """ tests for docs and style """

    @classmethod
    def setUpClass(cls):
        """ setup for function doc tests"""
        cls.base_funcs = inspect.getmembers(Amenity, inspect.isfunction)

    def test_class_style(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_test_style(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_doc(self):
        """ Tests for class docs """
        self.assertTrue(len(Amenity.__doc__) >= 1)

    def test_func_doc(self):
        """Tests for docstrings in all functions """
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestAmenity(unittest.TestCase):
    """ tests for class functions and attributes """

    def setUp(self):
        """ initialising for tests """
        self.am = Amenity()
        self.am1 = Amenity()
        self.am1.name = "gym"

    def test_class_type(self):
        """ test if Amenity inherits from BaseModel """
        self.assertEqual(issubclass(Amenity, BaseModel), True)

    def test_instance_type(self):
        """test if amenity is a subclass of basemodel"""
        self.assertEqual(type(self.am), Amenity)

    def test_attr_not_none(self):
        """ test if id, create and update exit """
        self.assertIsNotNone(self.am.id)
        self.assertIsNotNone(self.am.created_at)
        self.assertIsNotNone(self.am.updated_at)

    def test_attr_name_value(self):
        """ test the attribute name value """
        self.assertEqual(self.am1.name, "gym")
        self.assertEqual(self.am.name, "")

    def test_id_value(self):
        """ test id value is unique """
        self.assertNotEqual(self.am.id, self.am1.id)

    def test_attr_type(self):
        """ test the type of id, created_at and updated_at """
        self.assertEqual(type(self.am.id), str)
        self.assertEqual(type(self.am.created_at), datetime.datetime)
        self.assertEqual(type(self.am.updated_at), datetime.datetime)

    def test_str(self):
        """test __str__method"""
        strclass = f"[Amenity] ({self.am.id}) {self.am.__dict__}"
        self.assertEqual(str(self.am), strclass)

    def test_save(self):
        """ test save method for class Amenity """
        self.am.save()
        self.assertNotEqual(self.am.created_at, self.am.updated_at)

    def test_dict(self):
        """ test to dict method"""
        dic = {"__class__": "Amenity", "id": self.am.id,
               "created_at": self.am.created_at.isoformat(),
               "updated_at": self.am.updated_at.isoformat()}
        self.assertDictEqual(dic, self.am.to_dict())


if __name__ == "__main__":
    unitest.main()

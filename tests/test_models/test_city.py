#!/usr/bin/python3
""" Unit test for City """

import unittest
import pycodestyle
import json
import os
import inspect
import datetime
from uuid import uuid4

from models.city import City
from models.state import State
from models.base_model import BaseModel


class TestDocs(unittest.TestCase):
    """ tests for docs and style """

    @classmethod
    def setUpClass(cls):
        """ setup for function doc tests"""
        cls.base_funcs = inspect.getmembers(City, inspect.isfunction)

    def test_class_style(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_test_style(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_doc(self):
        """ Tests for class docs """
        self.assertTrue(len(City.__doc__) >= 1)

    def test_func_doc(self):
        """Tests for docstrings in all functions """
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestCity(unittest.TestCase):
    """ tests for class functions and attributes """

    def setUp(self):
        """ initialising for tests """
        self.city = City()
        self.city1 = City()
        self.state1 = State()
        self.city1.name = "Melbourne"
        self.city1.state_id = self.state1.id

    def test_class_type(self):
        """ test if Amenity inherits from BaseModel """
        self.assertEqual(issubclass(City, BaseModel), True)

    def test_instance_type(self):
        """test if amenity is a subclass of basemodel"""
        self.assertEqual(type(self.city), City)

    def test_attr_not_none(self):
        """ test if id, create and update exit """
        self.assertIsNotNone(self.city.id)
        self.assertIsNotNone(self.city.created_at)
        self.assertIsNotNone(self.city.updated_at)

    def test_attr_name_value(self):
        """ test the attribute name value """
        self.assertEqual(self.city1.name, "Melbourne")
        self.assertEqual(self.city.name, "")

    def test_id_value(self):
        """ test id value is unique """
        self.assertNotEqual(self.city.id, self.city1.id)

    def test_state_id_value(self):
        """ test if city1.state_id euqals self.state.state_id """
        self.assertEqual(self.city1.state_id, self.state1.id)

    def test_attr_type(self):
        """ test the type of id, created_at and updated_at """
        self.assertEqual(type(self.city.id), str)
        self.assertEqual(type(self.city1.name), str)
        self.assertEqual(type(self.city1.state_id), str)
        self.assertEqual(type(self.city.created_at), datetime.datetime)
        self.assertEqual(type(self.city.updated_at), datetime.datetime)

    def test_str(self):
        """test __str__method"""
        strclass = f"[City] ({self.city.id}) {self.city.__dict__}"
        self.assertEqual(str(self.city), strclass)

    def test_save(self):
        """ test save method """
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_dict(self):
        """ test to dict method"""
        dic = {"__class__": "City", "id": self.city1.id,
               "name": self.city1.name,
               "state_id": self.state1.id,
               "created_at": self.city1.created_at.isoformat(),
               "updated_at": self.city1.updated_at.isoformat()}
        self.assertDictEqual(dic, self.city1.to_dict())


if __name__ == "__main__":
    unitest.main()

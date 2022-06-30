#!/usr/bin/python3
""" Unit test for State """

import unittest
import pycodestyle
import json
import os
import inspect
import datetime
from uuid import uuid4

from models.state import State
from models.base_model import BaseModel


class TestDocs(unittest.TestCase):
    """ tests for docs and style """

    @classmethod
    def setUpClass(cls):
        """ setup for function doc tests"""
        cls.base_funcs = inspect.getmembers(State, inspect.isfunction)

    def test_class_style(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_test_style(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_doc(self):
        """ Tests for class docs """
        self.assertTrue(len(State.__doc__) >= 1)

    def test_func_doc(self):
        """Tests for docstrings in all functions """
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestCity(unittest.TestCase):
    """ tests for class functions and attributes """

    def setUp(self):
        """ initialising for tests """
        self.state = State()
        self.state.name = "VIC"
        self.state1 = State()

    def test_class_type(self):
        """ test if Amenity inherits from BaseModel """
        self.assertEqual(issubclass(State, BaseModel), True)

    def test_instance_type(self):
        """test if amenity is a subclass of basemodel"""
        self.assertEqual(type(self.state), State)

    def test_attr_not_none(self):
        """ test if id, create and update exit """
        self.assertIsNotNone(self.state.id)
        self.assertIsNotNone(self.state.created_at)
        self.assertIsNotNone(self.state.updated_at)

    def test_attr_name_value(self):
        """ test the attribute name value """
        self.assertEqual(self.state.name, "VIC")

    def test_id_value(self):
        """ test id value is unique """
        self.assertNotEqual(self.state.id, self.state1.id)

    def test_attr_type(self):
        """ test the type of id, created_at and updated_at """
        self.assertEqual(type(self.state.id), str)
        self.assertEqual(type(self.state.name), str)
        self.assertEqual(type(self.state.created_at), datetime.datetime)
        self.assertEqual(type(self.state.updated_at), datetime.datetime)

    def test_str(self):
        """test __str__method"""
        strclass = f"[State] ({self.state.id}) {self.state.__dict__}"
        self.assertEqual(str(self.state), strclass)

    def test_save(self):
        """ test save method """
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_dict(self):
        """ test to dict method"""
        dic = {"__class__": "State", "id": self.state.id,
               "name": self.state.name,
               "created_at": self.state.created_at.isoformat(),
               "updated_at": self.state.updated_at.isoformat()}
        self.assertDictEqual(dic, self.state.to_dict())


if __name__ == "__main__":
    unitest.main()

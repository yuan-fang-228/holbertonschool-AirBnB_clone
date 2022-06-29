#!/usr/bin/python3
""" Unit test for the BaseModel class """

import unittest
import pycodestyle
import json
import os
import inspect
import datetime
from uuid import uuid4

from models.base_model import BaseModel


class TestDocs(unittest.TestCase):
    """ tests for docs and style """

    @classmethod
    def setUpClass(cls):
        """ setup for function doc tests"""
        cls.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_class_style(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_test_style(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_doc(self):
        """ Tests for class docs """
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_func_doc(self):
        """Tests for docstrings in all functions """
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestBase(unittest.TestCase):
    """ tests for class functions and attributes """

    @classmethod
    def setUpClass(cls):
        """ initialising for tests """
        cls.new = BaseModel()
        cls.new.name = 'James'
        cls.new.my_number = 27

    def test_init(self):
        self.assertTrue(isinstance(self.new, BaseModel))
        self.assertEqual(self.new.name, 'James')

    def test_save(self):
        """ save function test """
        self.new.save()
        key = 'BaseModel' + "." + self.new.id
        with open('file.json', 'r') as myfile:
            j = json.load(myfile)
            self.assertEqual(j[key], self.new.to_dict())

    def test_str(self):
        """ __str__ override test """
        self.assertEqual(str(self.new), '[{}] ({}) {}'.format('BaseModel',
                         self.new.id, self.new.__dict__))

    def test_to_dict(self):
        """ to_dict function test """
        j = self.new.to_dict()
        self.assertEqual(self.new.to_dict(), j)

    def test_id(self):
        """ testing id """
        self.assertEqual(type(self.new.id), str)

    def test_created_at(self):
        """ created_at_test """
        self.assertEqual(type(self.new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ updated_at_test """
        self.assertEqual(type(self.new.updated_at), datetime.datetime)


if __name__ == "__main__":
    unitest.main()

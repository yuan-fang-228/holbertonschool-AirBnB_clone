#!/usr/bin/python3
""" Unit test for User """

import unittest
import pycodestyle
import json
import os
import inspect
import datetime
from uuid import uuid4

from models.user import User
from models.base_model import BaseModel


class TestDocs(unittest.TestCase):
    """ tests for docs and style """

    @classmethod
    def setUpClass(cls):
        """ setup for function doc tests"""
        cls.base_funcs = inspect.getmembers(User, inspect.isfunction)

    def test_class_style(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_test_style(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_doc(self):
        """ Tests for class docs """
        self.assertTrue(len(User.__doc__) >= 1)

    def test_func_doc(self):
        """Tests for docstrings in all functions """
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestCity(unittest.TestCase):
    """ tests for class functions and attributes """

    def setUp(self):
        """ initialising for tests """
        self.user = User()
        self.user1 = User()
        self.user1.email = "123@456.com"
        self.user1.password = "12345678"
        self.user1.first_name = "Amy"
        self.user1.last_name = "Cheng"

    def test_class_type(self):
        """ test if User inherits from BaseModel """
        self.assertEqual(issubclass(User, BaseModel), True)

    def test_instance_type(self):
        """test if user is a subclass of basemodel"""
        self.assertEqual(type(self.user), User)

    def test_attr_not_none(self):
        """ test if id, create and update exit """
        self.assertIsNotNone(self.user.id)
        self.assertIsNotNone(self.user.created_at)
        self.assertIsNotNone(self.user.updated_at)

    def test_attr_value(self):
        """ test the attribute value """
        self.assertEqual(self.user1.email, "123@456.com")
        self.assertEqual(self.user1.password, "12345678")
        self.assertEqual(self.user1.first_name, "Amy")
        self.assertEqual(self.user1.last_name, "Cheng")

    def test_id_value(self):
        """ test id value is unique """
        self.assertNotEqual(self.user.id, self.user1.id)

    def test_attr_type(self):
        """ test the type of id, created_at and updated_at """
        self.assertEqual(type(self.user1.email), str)
        self.assertEqual(type(self.user1.password), str)
        self.assertEqual(type(self.user1.first_name), str)
        self.assertEqual(type(self.user1.last_name), str)
        self.assertEqual(type(self.user1.created_at), datetime.datetime)
        self.assertEqual(type(self.user1.updated_at), datetime.datetime)

    def test_str(self):
        """test __str__method"""
        strclass = f"[User] ({self.user.id}) {self.user.__dict__}"
        self.assertEqual(str(self.user), strclass)

    def test_save(self):
        """ test save method """
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_dict(self):
        """ test to dict method"""
        dic = {"__class__": "User", "id": self.user1.id,
               "email": self.user1.email,
               "password": self.user1.password,
               "first_name": self.user1.first_name,
               "last_name": self.user1.last_name,
               "created_at": self.user1.created_at.isoformat(),
               "updated_at": self.user1.updated_at.isoformat()}
        self.assertDictEqual(dic, self.user1.to_dict())


if __name__ == "__main__":
    unitest.main()

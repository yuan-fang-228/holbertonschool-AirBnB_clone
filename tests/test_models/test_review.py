#!/usr/bin/python3
""" Unit test for Review """

import unittest
import pycodestyle
import json
import os
import inspect
import datetime
from uuid import uuid4

from models.place import Place
from models.user import User
from models.review import Review
from models.base_model import BaseModel


class TestDocs(unittest.TestCase):
    """ tests for docs and style """

    @classmethod
    def setUpClass(cls):
        """ setup for function doc tests"""
        cls.base_funcs = inspect.getmembers(Review, inspect.isfunction)

    def test_class_style(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_test_style(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_doc(self):
        """ Tests for class docs """
        self.assertTrue(len(Review.__doc__) >= 1)

    def test_func_doc(self):
        """Tests for docstrings in all functions """
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestCity(unittest.TestCase):
    """ tests for class functions and attributes """

    def setUp(self):
        """ initialising for tests """
        self.review = Review()
        self.review.text = "this is a good place"
        self.place = Place()
        self.review.place_id = self.place.id
        self.user = User()
        self.review.user_id = self.user.id
        self.review1 = Review()

    def test_class_type(self):
        """ test if Amenity inherits from BaseModel """
        self.assertEqual(issubclass(Review, BaseModel), True)

    def test_instance_type(self):
        """test if amenity is a subclass of basemodel"""
        self.assertEqual(type(self.review), Review)

    def test_attr_not_none(self):
        """ test if id, create and update exit """
        self.assertIsNotNone(self.review.id)
        self.assertIsNotNone(self.review.created_at)
        self.assertIsNotNone(self.review.updated_at)

    def test_attr_value(self):
        """ test the attribute value """
        self.assertEqual(self.review.text, "this is a good place")
        self.assertEqual(self.review.user_id, self.user.id)
        self.assertEqual(self.review.place_id, self.place.id)

    def test_id_value(self):
        """ test id value is unique """
        self.assertNotEqual(self.review.id, self.review1.id)

    def test_attr_type(self):
        """ test the type of id, created_at and updated_at """
        self.assertEqual(type(self.review.id), str)
        self.assertEqual(type(self.review.text), str)
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)
        self.assertEqual(type(self.review.created_at), datetime.datetime)
        self.assertEqual(type(self.review.updated_at), datetime.datetime)

    def test_str(self):
        """test __str__method"""
        strclass = f"[Review] ({self.review.id}) {self.review.__dict__}"
        self.assertEqual(str(self.review), strclass)

    def test_save(self):
        """ test save method """
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def test_dict(self):
        """ test to dict method"""
        dic = {"__class__": "Review", "id": self.review.id,
               "text": self.review.text,
               "user_id": self.user.id,
               "place_id": self.place.id,
               "created_at": self.review.created_at.isoformat(),
               "updated_at": self.review.updated_at.isoformat()}
        self.assertDictEqual(dic, self.review.to_dict())


if __name__ == "__main__":
    unitest.main()

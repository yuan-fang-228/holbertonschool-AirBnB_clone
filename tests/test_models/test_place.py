#!/usr/bin/python3
""" Unit test for Place """

import unittest
import pycodestyle
import json
import os
import inspect
import datetime
from uuid import uuid4

from models.amenity import Amenity
from models.user import User
from models.city import City
from models.place import Place
from models.base_model import BaseModel


class TestDocs(unittest.TestCase):
    """ tests for docs and style """

    @classmethod
    def setUpClass(cls):
        """ setup for function doc tests"""
        cls.base_funcs = inspect.getmembers(Place, inspect.isfunction)

    def test_class_style(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_test_style(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_doc(self):
        """ Tests for class docs """
        self.assertTrue(len(Place.__doc__) >= 1)

    def test_func_doc(self):
        """Tests for docstrings in all functions """
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestPlace(unittest.TestCase):
    """ tests for class functions and attributes """

    def setUp(self):
        """ initialising for tests """
        self.city = City()
        self.user = User()
        self.amenity = Amenity()
        self.place = Place()
        self.place1 = Place()
        self.place.city_id = self.city.id
        self.place.user_id = self.user.id
        self.place.name = "ABC"
        self.place.description = "good place"
        self.place.number_rooms = 100
        self.place.number_bathrooms = 120
        self.place.max_guest = 500
        self.place.price_by_night = 300
        self.place.latitude = 37.00
        self.place.longitude = 42.00
        self.place.amenity_ids = [self.amenity.id]

    def test_class_type(self):
        """ test if this class inherits from BaseModel """
        self.assertEqual(issubclass(Place, BaseModel), True)

    def test_instance_type(self):
        """test if this class is a subclass of basemodel"""
        self.assertEqual(type(self.place), Place)

    def test_attr_not_none(self):
        """ test if id, create and update exit """
        self.assertIsNotNone(self.place.id)
        self.assertIsNotNone(self.place.created_at)
        self.assertIsNotNone(self.place.updated_at)

    def test_attr_name_value(self):
        """ test the attribute name value """
        self.assertEqual(self.place.city_id, self.city.id)
        self.assertEqual(self.place.user_id, self.user.id)
        self.assertEqual(self.place.name, "ABC")
        self.assertEqual(self.place.description, "good place")
        self.assertEqual(self.place.number_rooms, 100)
        self.assertEqual(self.place.number_bathrooms, 120)
        self.assertEqual(self.place.max_guest, 500)
        self.assertEqual(self.place.price_by_night, 300)
        self.assertEqual(self.place.latitude, 37.00)
        self.assertEqual(self.place.longitude, 42.00)
        self.assertEqual(self.place.amenity_ids, [self.amenity.id])

    def test_id_value(self):
        """ test id value is unique """
        self.assertNotEqual(self.place.id, self.place1.id)

    def test_attr_type(self):
        """ test the type of id, created_at and updated_at """
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)
        self.assertEqual(type(self.city.created_at), datetime.datetime)
        self.assertEqual(type(self.city.updated_at), datetime.datetime)

    def test_str(self):
        """test __str__method"""
        strclass = f"[Place] ({self.place.id}) {self.place.__dict__}"
        self.assertEqual(str(self.place), strclass)

    def test_save(self):
        """ test save method """
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_dict(self):
        """ test to dict method"""
        dic = {"__class__": "Place", "id": self.place1.id,
               "created_at": self.place1.created_at.isoformat(),
               "updated_at": self.place1.updated_at.isoformat()}
        self.assertDictEqual(dic, self.place1.to_dict())


if __name__ == "__main__":
    unitest.main()

#!/usr/bin/python3
""" filestorage test module """

import unittest
from models.base_model import BaseModel
from models import storage
import os


class test_filestorage(unittest.TestCase):
    """ unittest class for the filestorage test """

    @classmethod
    def setUpClass(cls):
        """ initialise test """
        cls.new = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """ removes file after each test is completed """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_all(self):
        """  test for the all method """
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_new(self):
        """ tests for the new method """
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_save(self):
        """ test for the save method """
        storage.save()
        self.assertTrue(os.path.exists('file.json'))
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_reload(self):
        """ tests for the reload method """
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            myobj = obj
        print(myobj)
        self.assertEqual(self.new.to_dict()['id'], myobj.to_dict()['id'])
        os.remove('file.json')
        with open('file.json', 'w') as myfile:
            pass
        with self.assertRaises(ValueError):
            storage.reload()
        os.remove('file.json')
        self.assertEqual(storage.reload(), None)


if __name__ == "__main__":
    unittest.main()

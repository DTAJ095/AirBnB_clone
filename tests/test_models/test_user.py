#!/usr/bin/python3
""" Unitest for class User """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new_model = self.value()
        self.assertEqual(type(new_model.first_name), str)

    def test_last_name(self):
        """ """
        new_model = self.value()
        self.assertEqual(type(new_model.last_name), str)

    def test_email(self):
        """ """
        new_model = self.value()
        self.assertEqual(type(new_model.email), str)

    def test_password(self):
        """ """
        new_model = self.value()
        self.assertEqual(type(new_model.password), str)

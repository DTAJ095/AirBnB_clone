#!/usr/bin/python3
""" Unitest for class City """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new_model = self.value()
        self.assertEqual(type(new_model.state_id), str)

    def test_name(self):
        """ """
        new_model = self.value()
        self.assertEqual(type(new_model.name), str)

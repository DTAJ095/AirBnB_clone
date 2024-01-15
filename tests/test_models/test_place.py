#!/usr/bin/python3
""" Unitest for class Place """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new_model = self.value()
        self.assertEqual(type(new_model.city_id), str)

    def test_user_id(self):
        """ """
        new_model = self.value()
        self.assertEqual(type(new_model.user_id), str)

    def test_name(self):
        """ """
        new_model = self.value()
        self.assertEqual(type(new_model.name), str)

    def test_description(self):
        """ """
        new_model = self.value()
        self.assertEqual(type(new_model.description), str)

    def test_number_rooms(self):
        """ """
        new_model = self.value()
        self.assertEqual(type(new_model.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new_model = self.value()
        self.assertEqual(type(new_model.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new_model = self.value()
        self.assertEqual(type(new_model.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

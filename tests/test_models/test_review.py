#!/usr/bin/python3
""" Unitest for class Review """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new_model = self.value()
        self.assertEqual(type(new_model.place_id), str)

    def test_user_id(self):
        """ """
        new_model = self.value()
        self.assertEqual(type(new_model.user_id), str)

    def test_text(self):
        """ """
        new_model = self.value()
        self.assertEqual(type(new_model.text), str)

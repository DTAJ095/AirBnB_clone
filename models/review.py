#!/usr/bin/python3
""" Review module for HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class to store review data """
    place_id = ""
    user_id = ""
    text = ""

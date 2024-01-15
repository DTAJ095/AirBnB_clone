#!/usr/bin/python3
""" User module for HBNB project """
from models.base_model import BaseModel


class User(BaseModel):
    """ User attributes """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

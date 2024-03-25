#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """
    A class User that inherits from basemodel
    Public class attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string

    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')

    def to_dict(self):
        """ set to a dictionary which would later be serialized
        """
        obj_dict = super().to_dict()
        obj_dict['email'] = self.email
        obj_dict['password'] = self.password
        obj_dict['first_name'] = self.first_name
        obj_dict['last_name'] = self.last_name
        return obj_dict

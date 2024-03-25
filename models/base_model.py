#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    """
    This model serves as the base models
    Public instance attributes:
    id - Id from uuid4(),
    created at and updated at from datetime
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                formats = "%Y-%m-%dT%H:%M:%S.%f"
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, formats))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """ updates the time an instance is being saved"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Converts the strings to a dictionary. """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """Arranges the presentation of the dictionary
        """
        return f"{type(self).__name__,} ({self.id}) {self.__dict__}"

#!/usr/bin/python3

from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    class that inherits from basemodel and sets amenities available

    Public class attributes:
        name: string - empty string
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')

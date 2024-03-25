#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """
    class that inherits from base class and takes reviews
    Public class attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get('place_id', '')
        self.user_id = kwargs.get('user_id', '')
        self.text = kwargs.get('text', '')

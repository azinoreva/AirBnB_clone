#!/usr/bin/python3

from models.base_model import BaseModel


class State(BaseModel):
    """
    class that inherit from BaseModel
    Public class attributes:
        name: string - empty string
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '') 

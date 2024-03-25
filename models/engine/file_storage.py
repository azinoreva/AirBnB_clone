#!/usr/bin/python3

import json
from os.path import exists
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    The FileStorage Class serializes and deserializes
    Private class attributes: file_path - path for file
    objects - A dictionary that temporarily stores dict

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the objects that were serialized
        """
        return self.__objects

    def new(self, obj):
        """
        returns the dictionary __objects
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
         sets in __objects the obj with key <obj class name>.id
        """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name == 'Place':
                        obj = Place(**value)
                    elif class_name == 'State':
                        obj = State(**value)
                    elif class_name == 'City':
                        obj = City(**value)
                    elif class_name == 'Amenity':
                        obj = Amenity(**value)
                    elif class_name == 'Review':
                        obj = Review(**value)
                    else:
                        # Handle other classes if needed
                        continue
                    self.__objects[key] = obj

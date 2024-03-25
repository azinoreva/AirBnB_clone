#!/usr/bin/python3

import cmd
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine import storage


class HBNBCommand(cmd.Cmd):
    """ This is the console class terminal that extends cmd.Cmd
    public class attribute: prompt """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exits the program"""
        return True

    def do_EOF(self, arg):
        """Exits the program but adds a new line before exiting """
        print()
        return True

    def emptyline(self):
        """ Does nothing when an empty line is entered """
        pass

    def do_create(self, arg):
        """ Create a new instance of BaseModel
        args: arg refers to user input
        returns: object print or closes"""
        if not arg:
            print("** class name missing **")
            return
        classes = {
            'Place': Place,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Review': Review
        }
        if arg not in classes:
            print("** class doesn't exist **")
            return
        obj = classes[arg]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance .
            args: arguments are the classes """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in {'Place', 'State', 'City', 'Amenity', 'Review'}:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance
        args: class name """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in {'Place', 'State', 'City', 'Amenity', 'Review'}:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of instances."""
        args = arg.split()
        objects = storage.all()
        if len(args) == 0:
            print([str(obj) for obj in objects.values()])
        elif args[0] in {'Place', 'State', 'City', 'Amenity', 'Review'}:
            print([str(obj) for key, obj in objects.items() if key.startswith(args[0])])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates an instance
        args: based on the class name in args."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in {'Place', 'State', 'City', 'Amenity', 'Review'}:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = objects[key]
        setattr(obj, args[2], args[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

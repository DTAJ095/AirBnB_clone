#!/usr/bin/python3
""" HBNB console """
import cmd
import sys
from models.amenity import Amenity
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """ HBNB console functionality """
    prompt = '(hbnb) ' if sys.stdin.isatty() else ''

    classes = {
        'BaseModel': BaseModel, 'User': User, 'City': City,
        'Place': Place, 'State': State, 'Amenity': Amenity,
        'Review': Review
    }

    cmd_options = ['create', 'show', 'destroy', 'all', 'update', 'count']
    data = {
        'number_rooms': int, 'number_bathrooms': int,
        'max_guest': int, 'price_by_night': int,
        'longitude': float, 'latitude': float
    }

    def precmd(self, line):
        """ Format the command line for advanced command syntax
        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
            (Brackets are for optional fields in usage example.)
        """
        # initialize line elements
        _cmd = _cls = _id = _args = ''

        if not ('.' in line and '(' in line and ')' in line):
            return (line)
        try:
            # read line from left to right
            read_line = line[:]
            # isolate <class name>
            _cls = read_line[:read_line.find('.')]
            # isolate and validate <command>
            _cmd = read_line[read_line.find('.') + 1:read_line.find('(')]
            if _cmd not in HBNBCommand.cmd_options:
                raise Exception

            # parentheses contain arguments, read them
            read_line = read_line[read_line.find('(') + 1:read_line.find(')')]
            if read_line:
                # partition args: (<id>, [<delim>], [<*args>])
                read_line = read_line.partition(', ')
                # isolate _id, stripping quotes
                _id = read_line[0].replace('\"', '')

                # if arguments exist beyond _id
                read_line = read_line[2].strip()
                if read_line:
                    # check for *args and **kwargs
                    if read_line[0] == "{" and read_line[-1] == '}'\
                       and type(eval(read_line)) == dict:
                        _args = read_line
                    else:
                        _args = read_line.replace(',', '')
            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as e:
            pass
        finally:
            return line

    def do_quit(self, command):
        """ exit the hbnb console """
        exit()

    def help_quit(self):
        """ prints the help documentation for quit function """
        print("Exiting the console with formatting\n")

    def do_EOF(self, arg):
        """ handles EOF to exit the console """
        print()
        exit()

    def help_EOF(self):
        """ prints the help documentation for EOF """
        print("Exiting the console without formatting")

    def emptyline(self):
        """ overrides empty line method of CMD """
        pass

    def do_create(self, args):
        """ Creates objects for any class """
        if not args:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.classes:
            print("** class doesn't exits **")
            return
        new_instance = HBNBCommand.classes[args]()
        storage.save()
        print(new_instance.id)
        storage.save()

    def help_create(self):
        """ Help documentation for create method """
        print("Creates a class of any type")
        print("[Usage]: create <class_name>\n")

    def do_show(self, args):
        """ Show a string representation of an instance """
        args = args.partition(" ")
        cls_name = args[0]
        cls_id = args[2]
        if cls_name and ' ' in cls_id:
            cls_id = cls_id.partition(' ')[0]

            if not cls_name:
                print("** class name missing **")
                return

            if cls_name not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return

            if not cls_id:
                print("** instance id missing **")
                return

            key = cls_name + "." + cls_id
            try:
                print(storage._FileStorage__objects[key])
            except KeyError:
                print("** no instance found **")

    def help_show(self):
        """ Help documentation for show method """
        print("Show a string representation of an instance")
        print("[Usage]: <class_name>.show(<object_id>)\n")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name for id """
        args = args.partition(" ")
        cls_name = args[0]
        cls_id = args[2]

        if cls_name and ' ' in cls_id:
            cls_id = cls_id.partition(' ')[0]

        if not cls_name:
            print("** class name missing **")
            return

        if cls_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not cls_id:
            print("** instance id missing **")
            return

        key = cls_name + "." + cls_id
        try:
            del(storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """ Help documentation for destroy method """
        print("Destroy instance base on class name for id")
        print("[Usage]: <class_name>.destroy(<object_id)")

    def do_all(self, args):
        """ Show all objects of a class """
        my_list = []
        if args:
            args = args.split(' ')[0]
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")

            for key, value in storage._FileStorage__objects.items():
                if key.split('.')[0] == args:
                    my_list.append(str(value))
        else:
            for key, value in storage._FileStorage__objects.items():
                my_list.append(str(value))
        print(my_list)

    def help_all(self):
        """ Help documentation for all method """
        print("Show all objects of a class")
        print('[Usage]: <class_name>.all()\n')

    def do_update(self, args):
        """ Updates an instance based on the class name and id by
            adding or updating attribute
        """
        cls_name = cls_id = attr_name = attr_val = kwargs = ''

        # Let's isolate cls
        args = args.partition(' ')
        if args[0]:
            cls_name = args[0]
        else:
            print("** Class name missing **")
            return

        if cls_name not in HBNBCommand.classes:
            print("** Class doesn't exist **")
            return

        # Let's isolate id
        args = args[2].partition(' ')
        if args[0]:
            cls_id = args[0]
        else:
            print("** instance id missing **")
            return

        # Generate key from class name and id
        key = cls_name + '.' + cls_id

        if key not in storage.all():
            print("** instance not found **")
            return

        # Determine if args or kwargs
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []
            for key, val in kwargs.items():
                args.append(key)
                args.append(val)
        else:
            args = args[2]
            if args and args[0] == '\"':
                second_quote = args.find('\"', 1)
                attr_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            # if attr_name wasn't quoted arg
            if not attr_name and args[0] != ' ':
                attr_name = args[0]

            # check for quoted val arg
            if args[2] and args[2][0] == '\"':
                attr_val = args[2][1:args[2].find('\"', 1)]

            # if attr_val wasn't quoted arg
            if not attr_val and args[2]:
                attr_val = args[2].partition(' ')[0]

            args = [attr_name, attr_val]

        # retrieve current objects in a dict
        new_dict = storage.all()[key]

        # iterate through attributes names and values
        for i, attr_name in enumerate(args):
            if (i % 2 == 0):
                attr_val = args[i + 1]
                if not attr_name:
                    print("** attribute name missing **")
                if not attr_val:
                    print("** value missing **")
                if attr_name in HBNBCommand.data:
                    attr_val = HBNBCommand.data[attr_name](attr_val)

                # let's update the dict
                new_dict.__dict__.update({attr_name: attr_val})
        new_dict.save()

    def help_update(self):
        """ Help documentation for update method """
        print("Updates an object with new data")
        print("[Usage]: <class_name>.update(<id> <attr_name> <attr_val>)\n")

    def do_count(self, args):
        """ Return the number of instance of a class """
        counter = 0
        for key, value in storage._FileStorage__objects.items():
            if args == key.split('.')[0]:
                counter += 1
        print(counter)

    def help_count(self):
        """ Help documentation for count method """
        print("Count all instance of an object")
        print("[Usage]: <class nam> .count()")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

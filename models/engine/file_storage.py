#!/usr/bin/python3
"""comment for the checker"""
import json


class FileStorage:
    """comment for class filestorage"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """all fun"""
        if cls is not None:
            dic = {}
            for key, value in FileStorage.__objects.items():
                cls_name = key.split(".")
                if cls_name[0] == cls.__name__:
                    dic[key] = value
            return dic
        else:
            return FileStorage.__objects

    def new(self, obj):
        """new fun"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """save fun"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def delete(self, obj=None):
        """delete fun"""
        if not obj:
            return
        else:
            cp_objects = FileStorage.__objects.copy()
            for key, value in cp_objects.items():
                if value == obj:
                    del FileStorage.__objects[key]
                    self.save()

    def reload(self):
        """reload fun"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """deserialize json""" 
        self.reload()

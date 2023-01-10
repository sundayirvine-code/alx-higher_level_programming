#!/usr/bin/python3
'''Module that defines a Student class'''

class Student:
    '''class: Student
    Attribute:
        first_name
        last_name
        age
    '''
    def __init__(self, first_name, last_name, age):
        """
        Creates a new Student object with the given first name, last name, and age.
        :param first_name: The student's first name (string)
        :param last_name: The student's last name (string)
        :param age: The student's age (integer)
        """
        self.first_name = first_name
        self.last_name =last_name
        self.age = age

    def to_json(self):
        """
        Returns a JSON-serializable representation of the Student object.
        :return: A dictionary containing the key-value pairs of the Student object's attributes
        """
        return self.__dict__

#!/usr/bin/python3

""" Module of a class Square,
inheritance of class Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Represent the Class Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes instances of the odjects"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the Square instance."""
        str_square = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return (str_square + str_id + str_xy + str_wh)

    @property
    def size(self):
        """ Get size value """
        return (self.width)

    @size.setter
    def size(self, value):
        """ Set size value """
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation of the Square object."""
        str_rectangle = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.size)

        return (str_rectangle + str_id + str_xy + str_size)

    def update(self, *args, **kwargs):
        """Update the attributes of the Square object.

        Args:
          *args: Variable length arg list representing the attrs to be updated.
          **kwargs: Keyword arg representing the attributes to be updated.

        Notes:
          If both *args and **kwargs are provided, *args takes precedence.
          The 'size' attribute can be updated through either 'size' or 'width'
          and 'height' attributes.

        """

        if args is not None and len(args) != 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a dictionary with attributes """
        list_atr = ['id', 'size', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            if key == 'size':
                dict_res[key] = getattr(self, 'width')
            else:
                dict_res[key] = getattr(self, key)

        return (dict_res)

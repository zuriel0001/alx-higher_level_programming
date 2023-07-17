#!/usr/bin/python3
""" Class Rectangle inheritance of class Base
"""

from models.base import Base


class Rectangle(Base):
    """ Represent Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize instances of the Class

        Args:
          width (int): The width of the object.
          height (int): The height of the object.
          x (int, optional): The x-coordinate of the object's position.
          y (int, optional): The y-coordinate of the object's position.
          id (int, optional): The ID of the object. If not provided,
                              a unique ID will be assigned automatically.

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Get height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Get x value """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the value of x.

        Args:
          value (int): The new value for x.

        Raises:
          TypeError: If the value is not an integer.
          ValueError: If the value is less than 0.

        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get y value """
        return self.__y

    @y.setter
    def y(self, value):
        """Set y value """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Method that returns the area of the rectangle object """
        return (self.width * self.height)

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end='')

    def __str__(self):
        """ Method that return str special """
        str_rectangle = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return (str_rectangle + str_id + str_xy + str_wh)

    def update(self, *args, **kwargs):
        """Update the attributes of the Rectangle instance.

        Args:
          *args: Variable length argument list representing the attributes
          in the order:  id, width, height, x, y.

        **kwargs: Arbitrary keyword arguments representing the attributes as
        key-value pairs.

        Returns:
          None

        """
        if args is not None and len(args) != 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ method that returs a dictionary with properties """
        list_atr = ['id', 'width', 'height', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            dict_res[key] = getattr(self, key)

        return (dict_res)

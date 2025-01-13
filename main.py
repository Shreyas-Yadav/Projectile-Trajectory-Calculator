import math
"""
Projectile Trajectory Calculator
This module provides classes to calculate and visualize the trajectory of a projectile.
Classes:
    Projectile: Represents a projectile with a given speed, height, and angle.
    Graph: Represents a graphical representation of the projectile's trajectory.
Constants:
    GRAVITATIONAL_ACCELERATION: The gravitational acceleration constant (9.81 m/s^2).
    PROJECTILE: The symbol used to represent the projectile in the graph.
    x_axis_tick: The symbol used to represent the x-axis tick in the graph.
    y_axis_tick: The symbol used to represent the y-axis tick in the graph.
Projectile Class:
    Attributes:
        speed (float): The speed of the projectile in m/s.
        height (float): The initial height of the projectile in meters.
        angle (float): The launch angle of the projectile in degrees.
    Methods:
        __init__(speed, height, angle): Initializes the projectile with speed, height, and angle.
        __str__(): Returns a string representation of the projectile details.
        __calculate_displacement(): Calculates the horizontal displacement of the projectile.
        __calculate_y_coordinate(x): Calculates the y-coordinate for a given x-coordinate.
        calculate_all_coordinates(): Calculates all coordinates of the projectile's trajectory.
        height: Property to get or set the height of the projectile.
        angle: Property to get or set the angle of the projectile.
        speed: Property to get or set the speed of the projectile.
        __repr__(): Returns a string representation of the projectile object.
Graph Class:
    Attributes:
        coord (list): A list of coordinates representing the projectile's trajectory.
    Methods:
        __init__(coord): Initializes the graph with the given coordinates.
        __repr__(): Returns a string representation of the graph object.
        create_coordinates_table(): Creates a table of x and y coordinates.
        create_trajectory(): Creates a graphical representation of the projectile's trajectory.
"""

GRAVITATIONAL_ACCELERATION = 9.81
PROJECTILE = "∙"
x_axis_tick = "T"
y_axis_tick = "⊣"

class Projectile:
    __slots__ = ('__speed', '__height', '__angle')

    def __init__(self, speed, height, angle):
        self.__speed = speed
        self.__height = height
        self.__angle = math.radians(angle)
        
    def __str__(self):
        return f'''
Projectile details:
speed: {self.speed} m/s
height: {self.height} m
angle: {self.angle}°
displacement: {round(self.__calculate_displacement(), 1)} m
'''

    def __calculate_displacement(self):
        horizontal_component = self.__speed * math.cos(self.__angle)
        vertical_component = self.__speed * math.sin(self.__angle)
        squared_component = vertical_component**2
        gh_component = 2 * GRAVITATIONAL_ACCELERATION * self.__height
        sqrt_component = math.sqrt(squared_component + gh_component)
        
        return horizontal_component * (vertical_component + sqrt_component) / GRAVITATIONAL_ACCELERATION
        
    def __calculate_y_coordinate(self, x):
        height_component = self.__height
        angle_component = math.tan(self.__angle) * x
        acceleration_component = GRAVITATIONAL_ACCELERATION * x ** 2 / (
                2 * self.__speed ** 2 * math.cos(self.__angle) ** 2)
        y_coordinate = height_component + angle_component - acceleration_component

        return y_coordinate
    
    def calculate_all_coordinates(self):
        return [
            (x, self.__calculate_y_coordinate(x))
            for x in range(math.ceil(self.__calculate_displacement()))
        ]

    @property
    def height(self):
        return self.__height

    @property
    def angle(self):
        return round(math.degrees(self.__angle))

    @property
    def speed(self):
        return self.__speed

    @height.setter
    def height(self, n):
        self.__height = n

    @angle.setter
    def angle(self, n):
        self.__angle = math.radians(n)

    @speed.setter
    def speed(self, s):
       self.__speed = s
    
    def __repr__(self):
        return f'{self.__class__}({self.speed}, {self.height}, {self.angle})'

class Graph:
    __slots__ = ('__coordinates')

    def __init__(self, coord):
        self.__coordinates = coord

    def __repr__(self):
        return f"Graph({self.__coordinates})"

    def create_coordinates_table(self):
        table = '\n  x      y\n'
        for x, y in self.__coordinates:
            table += f'{x:>3}{y:>7.2f}\n'

        return table

    def create_trajectory(self):

        rounded_coords = [(round(x), round(y)) for x, y in self.__coordinates]

        x_max = max(rounded_coords, key=lambda i: i[0])[0]
        y_max = max(rounded_coords, key=lambda j: j[1])[1]

        matrix_list = [[" " for _ in range(x_max + 1)] for _ in range(y_max + 1)]

        for x, y in rounded_coords:
            matrix_list[-1 - y][x] = PROJECTILE

        matrix = ["".join(line) for line in matrix_list]

        matrix_axes = [y_axis_tick + row for row in matrix]
        matrix_axes.append(" " + x_axis_tick * (len(matrix[0])))

        graph = "\n" + "\n".join(matrix_axes) + "\n"

        return graph

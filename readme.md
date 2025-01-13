## Projectile Trajectory Calculator
This project provides classes to calculate and visualize the trajectory of a projectile.

### Classes

#### Projectile
Represents a projectile with a given speed, height, and angle.

**Attributes:**
- `speed (float)`: The speed of the projectile in m/s.
- `height (float)`: The initial height of the projectile in meters.
- `angle (float)`: The launch angle of the projectile in degrees.

**Methods:**
- `__init__(speed, height, angle)`: Initializes the projectile with speed, height, and angle.
- `__str__()`: Returns a string representation of the projectile details.
- `__calculate_displacement()`: Calculates the horizontal displacement of the projectile.
- `__calculate_y_coordinate(x)`: Calculates the y-coordinate for a given x-coordinate.
- `calculate_all_coordinates()`: Calculates all coordinates of the projectile's trajectory.
- `height`: Property to get or set the height of the projectile.
- `angle`: Property to get or set the angle of the projectile.
- `speed`: Property to get or set the speed of the projectile.
- `__repr__()`: Returns a string representation of the projectile object.

#### Graph
Represents a graphical representation of the projectile's trajectory.

**Attributes:**
- `coord (list)`: A list of coordinates representing the projectile's trajectory.

**Methods:**
- `__init__(coord)`: Initializes the graph with the given coordinates.
- `__repr__()`: Returns a string representation of the graph object.
- `create_coordinates_table()`: Creates a table of x and y coordinates.
- `create_trajectory()`: Creates a graphical representation of the projectile's trajectory.

### Constants
- `GRAVITATIONAL_ACCELERATION`: The gravitational acceleration constant (9.81 m/s^2).
- `PROJECTILE`: The symbol used to represent the projectile in the graph.
- `x_axis_tick`: The symbol used to represent the x-axis tick in the graph.
- `y_axis_tick`: The symbol used to represent the y-axis tick in the graph.



### Usage

To use the Projectile Trajectory Calculator, you can create instances of the `Projectile` and `Graph` classes and call their methods as needed. Below is an example:

```python
from projectile import Projectile
from graph import Graph

# Create a projectile instance
projectile = Projectile(speed=50, height=1.5, angle=45)

# Calculate the trajectory coordinates
coordinates = projectile.calculate_all_coordinates()

# Create a graph instance
graph = Graph(coordinates)

# Generate the trajectory graph
graph.create_trajectory()
```

### Contributing

If you would like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.



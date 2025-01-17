# 🎯 Projectile Trajectory Calculator

A Python module for calculating and visualizing projectile motion trajectories with ASCII graphics.

## ✨ Features

- Calculate projectile motion with given speed, height, and angle
- Generate coordinate tables for trajectory points
- Visualize trajectory using ASCII graphics
- Real-time property updates for projectile parameters
- Physics-based calculations using standard gravitational acceleration

## 📦 Installation

1. Ensure Python 3.6+ is installed
2. Clone the repository:

```sh
git clone https://github.com/yourusername/projectile-trajectory-calculator.git
cd projectile-trajectory-calculator

🚀 Usage
Basic example:

from main import projectile_helper
# Parameters: speed (m/s), height (m), angle (degrees)
projectile_helper(10, 3, 45)

Output:
Projectile details:
speed: 10 m/s
height: 3 m
angle: 45°
displacement: 10.2 m

  x      y
  0   3.00
  1   4.39
  2   5.57
  3   6.54
  4   7.29
  5   7.84
  6   8.17
  7   8.29
  8   8.20
  9   7.90
 10   7.39

⊣     ∙
⊣  ∙∙∙ ∙∙∙
⊣ ∙       ∙
⊣∙         ∙
⊣           ∙
⊣            ∙
⊣
 TTTTTTTTTTTTT


 📚 API Reference
Projectile Class
Properties
speed: Initial velocity (m/s)
height: Initial height (m)
angle: Launch angle (degrees)
Methods
calculate_all_coordinates(): Returns list of (x,y) trajectory points
Other methods documented in source code




Graph Class
Methods
create_coordinates_table(): Generates coordinate table
create_trajectory(): Creates ASCII visualization
```

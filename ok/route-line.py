import matplotlib.pyplot as plt
import numpy as np

def rotate_line(x1, y1, x2, y2, angle):
    x2 -= x1
    y2 -= y1
    angle_rad = np.radians(angle)

    cos_theta = np.cos(angle_rad)
    sin_theta = np.sin(angle_rad)

    new_x2 = x2 * cos_theta - y2 * sin_theta
    new_y2 = x2 * sin_theta + y2 * cos_theta


    new_x2 += x1
    new_y2 += y1

    plt.plot([x1, x2], [y1, y2], 'b', label='Original Line')
    plt.plot([x1, new_x2], [y1, new_y2], 'r', label='Rotated Line')
    plt.scatter(x1, y1, color='g', label='Starting Point')
  
    plt.xlim(min(x1, x2, new_x2) - 1, max(x1, x2, new_x2) + 1)
    plt.ylim(min(y1, y2, new_y2) - 1, max(y1, y2, new_y2) + 1)

    plt.legend()
    plt.axis('on')
    plt.grid(True)
    plt.show()

x1 = 1
y1 = 1
x2 = 3
y2 = 3
angle = 90
rotate_line(x1, y1, x2, y2, angle)

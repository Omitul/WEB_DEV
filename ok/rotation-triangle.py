import matplotlib.pyplot as plt
import numpy as np

# Triangle vertices
triangle = np.array([[1, 1], [2, 1], [1.5, 2]])

# Center of rotation
center = np.array([1.5, 1.5])

# Rotation angle in degrees
rotation_angle = 45

# Convert the rotation angle to radians
rotation_angle_rad = np.radians(rotation_angle)

# Create a rotation matrix
rotation_matrix = np.array([[np.cos(rotation_angle_rad), -np.sin(rotation_angle_rad)],
                            [np.sin(rotation_angle_rad), np.cos(rotation_angle_rad)]])

# Apply rotation to each vertex
rotated_triangle = np.dot(triangle - center, rotation_matrix) + center

# Plot the original and rotated triangles
plt.figure()
plt.plot(triangle[:, 0], triangle[:, 1], 'b-', label='Original Triangle')
plt.plot(rotated_triangle[:, 0], rotated_triangle[:, 1], 'r-', label='Rotated Triangle')
plt.axis('equal')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Triangle Rotation')
plt.grid(True)
plt.show()

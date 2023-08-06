import matplotlib.pyplot as plt

def scale_triangle(x1, y1, x2, y2, x3, y3, scale_factor):
    new_x1 = x1 * scale_factor
    new_y1 = y1 * scale_factor
    new_x2 = x2 * scale_factor
    new_y2 = y2 * scale_factor
    new_x3 = x3 * scale_factor
    new_y3 = y3 * scale_factor

    plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], 'b', label='Original Triangle')
    plt.plot([new_x1, new_x2, new_x3, new_x1], [new_y1, new_y2, new_y3, new_y1], 'r', label='Scaled Triangle')

    plt.xlim(min(x1, x2, x3, new_x1, new_x2, new_x3) - 1, max(x1, x2, x3, new_x1, new_x2, new_x3) + 1)
    plt.ylim(min(y1, y2, y3, new_y1, new_y2, new_y3) - 1, max(y1, y2, y3, new_y1, new_y2, new_y3) + 1)

    plt.legend()
    plt.axis('on')
    plt.grid(True)
    plt.show()
    
x1 = 1
y1 = 2
x2 = 5
y2 = 5
x3 = 6
y3 = 3
scale_factor = 2

scale_triangle(x1, y1, x2, y2, x3, y3, scale_factor)

import matplotlib.pyplot as plt
def translate_line(x1, y1, x2, y2, tx,ty):

    new_x1 = x1 + tx
    new_y1 = y1 + ty
    new_x2 = x2 + tx
    new_y2 = y2 + ty
    
    plt.plot([x1, x2], [y1, y2], 'b', label='Original Line')
    plt.plot([new_x1,new_x2], [new_y1, new_y2], 'r', label='Translated Line')

    plt.xlim(min(x1, x2, new_x1, new_x2) - 1, max(x1, x2, new_x1, new_x2) + 1)
    plt.ylim(min(y1, y2, new_y1, new_y2) - 1, max(y1, y2, new_y1, new_y2) + 1)

    plt.legend()
    plt.axis('on')
    plt.grid(True)
    plt.show()

x1 = 1
y1 = 1
x2 = 3
y2 = 3
tx = 1
ty = 2

translate_line(x1, y1, x2, y2, tx, ty)

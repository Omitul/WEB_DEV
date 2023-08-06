import matplotlib.pyplot as plt
def round(a):
    a1 = int(a)
    a2 = a1+1
    if a-a1>=a2-a:
        return a2
    return a1

def DDA(x1,y1,x2,y2):
    if x1>x2 or y1>y2:
        x1,x2=x2,x1
        y1,y2=y2,y1
        
    dx = x2 - x1
    dy = y2 - y1
    m = dy/dx
    if m<0:
        print("Slope is negative")
        return
    step = max(abs(dx),abs(dy))
    xinc = dx / step
    yinc = dy / step
    
    # Set initial point
    x = x1
    y = y1

    X = [x]
    Y = [y]
    # Draw line
    for i in range(step):
        X.append(round(x+xinc))
        Y.append(round(y+yinc))
        x += xinc
        y += yinc
    print(X)
    print(Y)
    # Plot the points
    plt.scatter(X,Y)
    for i in range(len(X)):
        plt.annotate(f'({X[i]}, {Y[i]})', (X[i], Y[i]), textcoords="offset points", xytext=(0,10), ha='center')

    plt.show()

DDA(0,0,5,10)
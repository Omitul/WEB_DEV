import matplotlib.pyplot as plt

def bresenham_line(x1,y1,x2,y2):
    if (x1>x2 or y1>y2):
        x1,x2=x2,x1
        y1,y2=y2,y1
    dx = x2-x1
    dy = y2-y1
    m = dy/dx
    if m>=1:
        c1 = 2*dx
        c2 = 2*(dx-dy)
        p = c1-dy
    else:
        c1 = 2*dy
        c2 = 2*(dy-dx)
        p = c1-dx
        
    X=[x1]
    Y=[y1]
    got=0
    while got<2:
        if p > 0:
            p += c1
            if m >= 1:
                y1 += 1
            else:
                x1 += 1
        else:
            p += c2
            y1+=1
            x1+=1
        
        if got>0:
            got+=1
        if(x1==x2 and y1==y2):
            got=1
        if x1-2>x2 and y1-2>y2:
            break
        if(x1<=x2 and y1<=y2):
            X.append(x1)
            Y.append(y1)

    # Plot the points
    plt.scatter(X,Y)
    for i in range(len(X)):
        plt.annotate(f'({X[i]}, {Y[i]})', (X[i], Y[i]), textcoords="offset points", xytext=(0,10), ha='center')

    plt.show()

bresenham_line(1,2,7,11)
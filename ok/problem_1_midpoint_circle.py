import matplotlib.pyplot as PLOT

def mid_point_circle(h,k,r):
    x, y = 0,r 
    p = 1 - r
    X = []
    Y = []
    while(x <= y):
        X.append(x + h)
        Y.append(y + k)
        X.append(y + k)
        Y.append(x + h)
        X.append(-x + h)
        Y.append(y + k)
        X.append(y + k)
        Y.append(-x + h)
        X.append(-x + h)
        Y.append(-y + k)
        X.append(-y + k)
        Y.append(-x + h)
        X.append(x + h)
        Y.append(-y + k)
        X.append(-y + k)
        Y.append(x + h)

        if(p < 0):
            p = p + 2 * x + 3
        else:
            p = p + 2 * ( x-y ) + 5
            y-=1
        x+=1
    PLOT.scatter(X,Y)
    for i in range(len(X)):
        PLOT.annotate(f'({X[i]}, {Y[i]})', (X[i], Y[i]), textcoords="offset points", xytext=(0,10), ha='center')
    PLOT.show()
    

mid_point_circle(0,0,5)
import matplotlib.pyplot as plt

def midpoint_circle(h,k,r):
    x, y = 0,r
    p = 1-r
    X = []
    Y = []
    while(x<=y):
        X.append(x+h)
        Y.append(y+k)
        X.append(y+k)
        Y.append(x+h)
        X.append(-x+h)
        Y.append(y+k)
        X.append(y+k)
        Y.append(-x+h)
        X.append(-x+h)
        Y.append(-y+k)
        X.append(-y+k)
        Y.append(-x+h)
        X.append(x+h)
        Y.append(-y+k)
        X.append(-y+k)
        Y.append(x+h)
        
        if p<0:
            p = p+2*x+3
        else:
            p = p+2*(x-y)+5
            y-=1
        x+=1
        # Plot the points
    plt.scatter(X,Y)
    for i in range(len(X)):
        plt.annotate(f'({X[i]}, {Y[i]})', (X[i], Y[i]), textcoords="offset points", xytext=(0,10), ha='center')

    plt.show()

midpoint_circle(0,0,5)

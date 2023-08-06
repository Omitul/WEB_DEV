import matplotlib.pyplot as plt

def round(a):
    a1 = int(a)
    a2 = a1+1
    if a-a1>=a2-a:
        return a2
    return a1

def direct_line(x1,y1,x2,y2):
    if x1>x2:
        x1,x2=x2,x1 
        y1,y2=y2,y1
        
    m = abs(y1-y2)/abs(x1-x2)
    if m<0:
        print("Invalid input")
        return
    b = y1-m*x1
    X = []
    Y = []
    while x1<=x2 or y1<=y2:
        X.append(round(x1))
        Y.append(round(y1))
        if m<=1:
            x1 +=1
            y1 = m*x1+b
        else:
            y1+=1
            x1 = (y1-b)/m
    # Plot the points
    plt.plot(X,Y,marker='o')
    for i in range(len(X)):
        plt.annotate(f'({X[i]}, {Y[i]})', (X[i], Y[i]), textcoords="offset points", xytext=(0,5), ha='center')

    plt.show()
 
direct_line(-2,-2,7,10)
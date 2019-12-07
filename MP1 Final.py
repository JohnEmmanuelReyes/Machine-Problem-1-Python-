#Use np.linspace(0,99,100) as n
def f(n):
    import matplotlib.pyplot as plt
    import numpy as np
    
    y = np.copy(n)
    #Numpy version of conditional statements
    y[y < 10] = y[y < 10]**2 - 7
    #for the value of n from 10 to 99
    #It will loop the function until it reaches n less than 10.
    for x in range(10, n.size):
        y[x] = y[x - 10]
    
    #Plotting Specifications    
    plt.figure(figsize=(10,7))    
    plt.suptitle('Piecewise of f(n)')
    plt.xlabel('n in range of (0,99)')
    plt.ylabel('f (n)')
    plt.stem(n,y, linefmt='-.', markerfmt='bo', basefmt= 'r-')
    plt.show
    print(y)
    return 
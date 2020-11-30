
from math import fabs 
import matplotlib.pyplot as plt


def centroide(xs,ys):
    num = 0
    dem = 0
    for i in range(0,len(xs)):
        num += xs[i] * ys[i]
        dem += ys[i] 
    
    return num/dem
 
def bisectriz(xs,ys):
    izq = 0
    medio = 0
    derecha = len(xs)

    for _ in range(100):
        medio = int((izq + derecha)/2)
        area1 = 0
        area2 = 0
        for i in range(0,medio):
            area1 += ys[i]
        for i in range(medio,len(xs)):
            area2 += ys[i]
        
        if fabs( area1 - area2 ) <  10**-6:
            return medio
        if area1 > area2 :
            derecha = medio
        else:
            izq = medio
    return xs[medio]

def maxmo(xs,ys):
    xs.reverse()
    ys.reverse()
    return minmo(xs,ys)

def minmo(xs,ys):
    
    return xs[ys.index(max(ys))]

def middlemo(xs,ys):

    plt.plot(xs,ys)
    plt.show()

    maximo = max(ys)
    l = []
    for i in range(0,len(ys)):
        if ys[i] == maximo:
            l.append(xs[i])
    return sum(l)/len(l)

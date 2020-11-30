def trifm (a , m , b , mmin , mmax ,x) :
    if x < mmin or x > mmax:
        raise 'argumento fuera de rango'
    if x <= a or x >= b :
        return 0
    elif a < x <= m :
        return (x - a)/(m - a)
    else:
        return (b - x)/(b - m)
    

def trapfm (a , b , c , d, mmin , mmax ,x ) :
    if x < mmin or x > mmax:
        raise 'argumento fuera de rango'
    if x <= a or x >= d:
        return 0
    if a < x <= b :
        return (x - a)/(b - a)
    if b < x <= c :
        return 1
    else :
        return (d - x)/(d - c)

        


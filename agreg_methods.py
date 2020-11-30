
from rules import * 
import numpy as np

def Metodo_Agregacion( reglas,valores,funcs,dom,metodo) :
    resultado = []
    
    resultado_Reglas = []
    for item in reglas:
        regla = Regla(item)
        r = regla.evaluar(funcs,valores)
        
        if metodo == "Mamdani":
            resultado_Reglas.append(Mamdani((r[0],regla.consecuencia),funcs,dom))
        else:
            resultado_Reglas.append(Larsen((r[0],regla.consecuencia),funcs,dom))

    xs , ys = resultado_Reglas[0]
    for j in range(1,len(resultado_Reglas)):
        _ , ysi = resultado_Reglas[j]
        for i in range(len(ysi)):
            if ysi[i] > ys[i]:
                ys[i] = ysi[i]

    return xs ,ys

def Mamdani(item,funcs,dom):
    xs = []
    ys = []
    r,consecuencia = item
    func,param = funcs[consecuencia[0]][consecuencia[1]]

    
    for x in np.arange(dom[consecuencia[0]][0], dom[consecuencia[0]][1], 0.025):
    #for x in np.arange(dom[consecuencia[0]][0], dom[consecuencia[0]][1], 0.5):
    #for x in range(dom[consecuencia[0]][0],dom[consecuencia[0]][1] + 1) :   
        valor = func(*param,x)
        
        if valor > r:
            valor = r
        
        
        xs.append(x)
        
        ys.append(valor)
        
    return xs,ys

def Larsen(item,funcs,dom):
    xs = []
    ys = []
    r,consecuencia = item
    func,param = funcs[consecuencia[0]][consecuencia[1]]

    
    for x in np.arange(dom[consecuencia[0]][0], dom[consecuencia[0]][1], 0.025):
    #for x in np.arange(dom[consecuencia[0]][0], dom[consecuencia[0]][1], 0.5):
    #for x in range(dom[consecuencia[0]][0],dom[consecuencia[0]][1] + 1) :   
        valor = func(*param,x)
        
        valor = valor * r
        
        xs.append(x)
        ys.append(valor)
        
    return xs,ys


def TSK(reglas,valores,funcs,dom,metodo):
    resultado = []
    numerador = 0
    denominador = 0

    for item in reglas:
        regla = Regla(item)
        r = regla.evaluar(funcs,valores)
        resultado.append((r[1],regla.consecuencia))
    
    for item in resultado:
        r,consecuencia = item
        valores = tuple(r.values())
        funcion = funcs[consecuencia[0]]
        valor = funcion(*valores)
        numerador += min(valores) * valor
        denominador += min(valores)
    
    return numerador/denominador


from agreg_methods import * 
from defuzzy import *

class Sistema():
    def __init__(self,metodo,defusificacion,rules,funcs,variables):
        if metodo == "Mamdani":
            self.metodo = Metodo_Agregacion
        elif metodo == "Larsen":
            self.metodo = Metodo_Agregacion
        else:
            self.metodo = TSK
        
        self.nombre_metodo = metodo
        if defusificacion == "centroide":
            self.defusificacion = centroide
        elif defusificacion == "bisectriz":
            self.defusificacion = bisectriz
        elif defusificacion == "maxmo":
            self.defusificacion = maxmo
        elif defusificacion == "minmo":
            self.defusificacion = minmo
        else:
            self.defusificacion = middlemo
        
        self.rules = self.procesar(rules)
        

        self.funcs = funcs
        self.dominio_variables = variables
    
    def procesar(self,rules):
        misReglas = []
        for x in rules:

            ant ,con = x.split('entonces')
            con = con.split(',')
            if len(con) == 1:
                misReglas.append(x)
            else:
                for item in con: 
                    regla   = ant + "entonces " + item
                    misReglas.append(regla)

        return misReglas

    def solve(self,valores):
        resultado = self.metodo(self.rules,valores,self.funcs,self.dominio_variables,self.nombre_metodo)

        if self.nombre_metodo == "Mamdani" or self.nombre_metodo == "Larsen":
            return self.defusificacion(resultado[0],resultado[1])    
        return resultado
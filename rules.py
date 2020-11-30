
class Regla() : 

    def  __init__(self, regla ): 
        r = regla.split( 'entonces')
        self.antecedente = r[0].split()
        self.antecedente = self.antecedente[ 1: ]
        self.removeall( self.antecedente )
        self.consecuencia = r[1].split()
        self.removeall( self.consecuencia )

    def evaluar( self , funcs , valores ) :
        r = {}
        resultado = 0
        termino = []
        op = None
        neg = False
        for i in self.antecedente:
            if i == 'no':
                neg = True
                continue
            if i == 'y' or i == 'o':
                op = i
                continue
            termino.append(i)
            if len(termino) == 2:
                func,param = funcs[termino[0]][termino[1]]
                valor = func(*param,valores[termino[0]])
                variable = termino[0]
                termino = []
                if neg:
                    valor = 1 - valor
                    neg = False
                if op is None :
                    resultado = valor
                if variable not in r:
                    r[variable] = valor
                
                if op == 'y':
                    r[variable] = min(r[variable], valor)
                    resultado = min(resultado,valor)
                elif op == 'o':
                    r[variable] = max(r[variable], valor)
                    resultado= max(resultado,valor)
        return resultado,r

    def removeall ( self, l) :
        while True :
            try :
                l.remove('es')
            except :
                break


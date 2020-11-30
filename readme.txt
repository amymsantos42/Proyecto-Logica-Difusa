
Para correr el sistema  :
    python main.py

1 : Si se desea correr el problema propuesto con otros valores de entrada, cambiar las siguientes varibales
    valores_entrada["TC"] = x , donde x pertenece al intervalo de [0,30]
    valores_entrada["LLC"] = y, donde y pertenece al intervalo de [0,100]

2 : Si se desea cambiar el problema se necesita redefinir lo siguiete:
    -reglas , una lista de reglas que cumpla con las descritas en el informe
    -dominio_variables , donde para cada varibale que aparezca en alguna regla se le asigne su dominio_variables
    -funciones_variables , diccionario de funciones donde para cada una de las variables y sus definiciones exista una funcion de membresia asociada(triangular o trapezoidal)
    -valores_entrada , diccionario donde para cada varible que aparezca en el antecedente de alguna regla tenga un valor que pertezca a su dominio

3 : Definir el sistema , el sistema se crea con la instruccion :
    sistema = Sistema(metodo_de_agregcion,metodo_de_defuzzificacion,reglas,funciones_variables,dominio_variables) 
    Posibles valores para metodo_de_agregcion:
    - "Mamdani"
    - "Larsen"
    Posibles valores para metodo_de_defuzzificacion:
    - "centroide"
    - "bisectriz"
    - "middlemo"
    - "maxmo"
    - "minmo"

    

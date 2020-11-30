
from memb_func import *  
from sistem import *
import matplotlib.pyplot as plt
import numpy as np

#Variables:
#Tamanno de la cola (TC)
#Probabilidad de llegada del camion en % (LLC)
#Probabilidad de compra exitosa en % (PC)


reglas = [
    "Si TC es Pequenna y LLC es Baja entonces PC es Media",
    "Si TC es Pequenna o LLC es Alta entonces PC es Alta",
    "Si TC es Mediana y LLC es Alta entonces PC es Media",
    "Si TC es Mediana o LLC es Media entonces PC es Baja",
    "Si TC es Grande entonces PC es Baja"
    
    
]



dominio_variables = {}
dominio_variables["TC"] = (0,30)
dominio_variables["LLC"] = (0,100)
dominio_variables["PC"] = (0,100)

funciones_variables = {}
funciones_variables["TC"] = {}
funciones_variables["LLC"] = {}
funciones_variables["PC"] = {}
funciones_variables["TC"]["Pequenna"] = (trapfm,(0,0,5,11,0,30))
funciones_variables["TC"]["Mediana"] = (trapfm,(10,12,18,20,0,30))
funciones_variables["TC"]["Grande"] = (trapfm,(18,25,30,30,0,30))
funciones_variables["LLC"]["Baja"] = (trapfm,(0,0,30,45,0,100))
funciones_variables["LLC"]["Media"] = (trapfm,(30,45,65,80,0,100))
funciones_variables["LLC"]["Alta"] = (trapfm,(65,80,100,100,0,100))
funciones_variables["PC"]["Baja"] = (trifm,(0,0,30,0,100))
funciones_variables["PC"]["Media"] = (trifm,(20,50,80,0,100))
funciones_variables["PC"]["Alta"] = (trifm,(75,100,100,0,100))




valores_entrada = {}
valores_entrada["TC"] = 11
valores_entrada["LLC"] = 76


#Crear el Sistema
sistema = Sistema("Mamdani","bisectriz",reglas,funciones_variables,dominio_variables)
#sistema = Sistema("Larsen","middlemo",reglas,funciones_variables,dominio_variables)


print(f'Para una cola de tamanno {valores_entrada["TC"]} y una probabilidad de llegada del camion de {valores_entrada["LLC"]} % , se tiene una probabilidad de compra exitosa de {sistema.solve(valores_entrada)} %' )





def my_plot(fig,line,label,func,param):
    x = []
    y = []
    for i in line:
        x.append(i)
        y.append(func(*param,i))
   
    fig.plot(x,y,label = label)[0]

#Exportar la foto de las funciones de Membresia
#f,ax = plt.subplots(3,1)
# ax[0].set_title("Tamanno de la Cola",fontsize = 15) 


# line = np.arange(0, 30, 0.025)
# my_plot(ax[0],line,"Pequenna",trapfm,(0,0,5,11,0,30))
# my_plot(ax[0],line,"Mediana",trapfm,(10,12,18,20,0,30))
# my_plot(ax[0],line,"Grande",trapfm,(18,25,30,30,0,30))


# line = np.arange(0, 100, 0.025)
# ax[1].set_title("Probabilidad de llegada del camion",fontsize = 15) 
# my_plot(ax[1],line,"Baja",trapfm,(0,0,30,45,0,100))
# my_plot(ax[1],line,"Media",trifm,(30,55,80,0,100))
# my_plot(ax[1],line,"Alta",trapfm,(65,80,100,100,0,100))


# ax[2].set_title("Probabilidad de compra exitosa",fontsize = 15) 
# my_plot(ax[2],line,"Baja",trapfm,(0,0,30,45,0,100))
# my_plot(ax[2],line,"Media",trifm,(30,55,80,0,100))
# my_plot(ax[2],line,"Alta",trapfm,(65,80,100,100,0,100))


# l = ax[0].legend(loc = 'rigth', bbox_to_anchor=(1,0.5))
# l1 = ax[1].legend(loc = 'rigth', bbox_to_anchor=(1,0.5))
# l2 = ax[2].legend(loc = 'rigth' , bbox_to_anchor=(1,0.5))

# plt.subplots_adjust(right = 0.85)
# plt.tight_layout()

# plt.savefig('mf.png',dpi = 300,format = 'png',bbox_extra_artists = (l,l1,l2,),bbox_inches = 'tight')
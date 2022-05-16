import os
import numpy as np
import cv2
from matplotlib import pyplot as plt

#color=np.uint8([[[255,0,191]]]) #purpura
#color=np.uint8([[[255,0,128]]]) #violeta
#color=np.uint8([[[255,0,64]]])  #morado
#color=np.uint8([[[0,200,255]]])
'''
color=np.uint8([[[0,190,255]]])
hsv_color = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
print('HSV: ',hsv_color)
'''
'''
h=int(input('Introduce el valor de H: '))
s=int(input('Introduce el valor de S: '))
v=int(input('Introduce el valor de V: '))
color=np.uint8([[[h,s,v]]])

#color=np.uint8([[[180,255,255]]])#upper_red
#color=np.uint8([[[150,150,150]]])
bgr_color=cv2.cvtColor(color,cv2.COLOR_HSV2BGR)
#color1=np.uint8([[[0,0,255]]])#upper_Red
#color1=np.uint8([[[150,62,150]]])
#yuv_color1=cv2.cvtColor(color1,cv2.COLOR_BGR2YUV)
yuv_color=cv2.cvtColor(bgr_color,cv2.COLOR_BGR2YUV)

#color3=(0.299*255)+(0.587*150)+(0.114*180)

print('HSV: ',color,' a BGR: ',bgr_color,' a YUV: ',yuv_color)
#print('BGR: ',color1,' a YUV: ',yuv_color1)
#print('Y: ',color3)
'''

def h2y(l,m,n):
    l=int(input('Introduce el valor de H: '))
    m=int(input('Introduce el valor de S: '))
    n=int(input('Introduce el valor de V: '))
    color=np.uint8([[[l,m,n]]])
    bgr_color=cv2.cvtColor(color,cv2.COLOR_HSV2BGR)
    yuv_color=cv2.cvtColor(bgr_color,cv2.COLOR_BGR2YUV)
    print('HSV: ',color,' a BGR: ',bgr_color,' a YUV: ',yuv_color)

def f_SDTV(l,m,n):
    l=int(input('Introduce el valor de R: '))
    l=l/255
    m=int(input('Introduce el valor de G: '))
    m=m/255
    n=int(input('Introduce el valor de B: '))
    n=n/255

    V_M=[l,m,n]
    mat=[[0.299,0.587,0.114],[-0.14713,-0.28886,0.436],[0.615,-0.51499,-0.10001]]
    Y=(mat[0][0]*V_M[0])+(mat[0][1]*V_M[1])+(mat[0][2]*V_M[2])
    U=(mat[1][0]*V_M[0])+(mat[1][1]*V_M[1])+(mat[1][2]*V_M[2])
    V=(mat[2][0]*V_M[0])+(mat[2][1]*V_M[1])+(mat[2][2]*V_M[2])
    print('Y: ',Y)
    print('U: ',U)
    print('V: ',V)

def f_HDTV(l,m,n):
    l=int(input('Introduce el valor de R: '))
    l=l/255
    m=int(input('Introduce el valor de G: '))
    m=m/255
    n=int(input('Introduce el valor de B: '))
    n=n/255

    V_M=[l,m,n]
    mat=[[0.2126,0.7152,0.0722],[-0.09991,-0.33609,0.436],[0.615,-0.55861,-0.05639]]
    Y=(mat[0][0]*V_M[0])+(mat[0][1]*V_M[1])+(mat[0][2]*V_M[2])
    U=(mat[1][0]*V_M[0])+(mat[1][1]*V_M[1])+(mat[1][2]*V_M[2])
    V=(mat[2][0]*V_M[0])+(mat[2][1]*V_M[1])+(mat[2][2]*V_M[2])
    print('Y: ',Y)
    print('U: ',U)
    print('V: ',V)

def f_hsv(l,m,n):
    l=int(input('Introduce el valor de B: '))
    m=int(input('Introduce el valor de G: '))
    n=int(input('Introduce el valor de R: '))
    color=np.uint8([[[l,m,n]]])
    bgr_color=cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
    print('BGR: ',color,' a HSV: ',bgr_color)

r=1
while r==1:
    a=b=c=0
    print('_______________________________________________________________________________________________________________________\n')
    print('|Instrucciones de uso del programa:                                                                                    |\n')
    print('|1) Sacar color hex de https://en.wikipedia.org/wiki/Hue#24_hues_of_HSL/HSV para una guía rápida o de alguna otra forma|\n')
    print('|2) Convertir de hex a RGB                                                                                             |\n')
    print('|3) Introducir valor de RGB como un BGR al programa para obtener los rangos en numeros enteros                         |\n')
    print('------------------------------------------------------------------------------------------------------------------------\n')
    print('')
    metodo=int(input('Selecciona el metodo para obtener el color:\n 1)Con las funciones de opencv(HSV-YUV)\n 2) Con fórmula SDTV BT.470(RGB-YUV)\n 3) Con fórmula HDTV BT.709(RGB-YUV)\n 4) BGR-HSV\n'))
    if metodo==1:
        h2y(a,b,c)
    elif metodo==2:
        f_SDTV(a,b,c)
    elif metodo==3:
        f_HDTV(a,b,c)
    else:
        f_hsv(a,b,c)
    print('')
    r=int(input('Presione 1 para calcular otro color.\nPresione un numero diferente de 1 para finalizar\n'))
    if r==1:
        #os.system('cls')
        print('')
        print('______________________________________________________________________________________')
    else:
        break

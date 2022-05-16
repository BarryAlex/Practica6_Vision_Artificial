#Edwing Alexis Casillas Valencia.   19110113.   7E1.    Práctica 6 visión artificial
import os
import numpy as np
import cv2
from matplotlib import pyplot as plt

r=1
cap = cv2.VideoCapture(0)

def hsv_red():
    while(1):
        _, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #hue saturation value
        lower_red = np.array([150,150,150])
        upper_red = np.array([180,255,255])
        #lower_red = np.array([0,0,0])
        #upper_red = np.array([10,255,255])

        mask = cv2.inRange(hsv, lower_red, upper_red)
        res = cv2.bitwise_and(frame,frame, mask= mask)

        #mask = cv2.inRange(hsv, lower_red, upper_red)
        #res = cv2.bitwise_and(frame,frame, mask= mask)

        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)

        #k = cv2.waitKey(5) & 0xFF
        #if k == 27:
        if cv2.waitKey(1) & 0xFF == ord('0'):
            break

    cv2.destroyAllWindows()
    cap.release()

def hsv_green():
    while(1):
        _, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #hue saturation value
        lower_green = np.array([40,120,120])
        upper_green = np.array([90,255,255])

        mask_g = cv2.inRange(hsv, lower_green, upper_green)
        res = cv2.bitwise_and(frame,frame, mask= mask_g)

        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask_g)
        cv2.imshow('res',res)

        if cv2.waitKey(1) & 0xFF == ord('0'):
            break

def hsv_blue():
    while(1):
        _, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #hue saturation value
        lower_blue = np.array([90,150,100])
        upper_blue = np.array([120,255,255])

        mask_b = cv2.inRange(hsv, lower_blue, upper_blue)
        res = cv2.bitwise_and(frame,frame, mask= mask_b)

        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask_b)
        cv2.imshow('res',res)

        if cv2.waitKey(1) & 0xFF == ord('0'):
            break

def hsv_yellow():
    #print('Amarillo')
    while(1):
        _, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #hue saturation value
        lower_yellow = np.array([20,100,100])
        upper_yellow = np.array([60,255,255])

        mask_y = cv2.inRange(hsv, lower_yellow, upper_yellow)
        res = cv2.bitwise_and(frame,frame, mask= mask_y)

        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask_y)
        cv2.imshow('res',res)

        if cv2.waitKey(1) & 0xFF == ord('0'):
            break

def hsv_plp():
    #print('')
    while(1):
        _,frame=cap.read()
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        #hue saturation value
        lower_plp=np.array([120,80,90])
        upper_plp=np.array([150,255,255])

        mask_p=cv2.inRange(hsv,lower_plp,upper_plp)
        res=cv2.bitwise_and(frame,frame,mask=mask_p)

        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask_p)
        cv2.imshow('res',res)

        if cv2.waitKey(1) & 0xFF == ord('0'):
            break

def rgb_red():
    while(1):
        _, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        #hue saturation value
        lower_red = np.array([180,0,0])
        upper_red = np.array([255,100,100])

        mask = cv2.inRange(rgb, lower_red, upper_red)
        res = cv2.bitwise_and(frame,frame, mask= mask)

        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)

        if cv2.waitKey(1) & 0xFF == ord('0'):
            break

def rgb_yellow():
    while(1):
        _, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        #hue saturation value
        lower_yellow = np.array([150,150,0])
        upper_yellow = np.array([255,255,100])

        mask_y = cv2.inRange(rgb, lower_yellow, upper_yellow)
        res = cv2.bitwise_and(frame,frame, mask= mask_y)

        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask_y)
        cv2.imshow('res',res)

        if cv2.waitKey(1) & 0xFF == ord('0'):
            break

def rgb_green():
    while(1):
        _, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        #hue saturation value
        lower_green = np.array([0,150,0])
        upper_green = np.array([140,255,140])

        mask_g = cv2.inRange(rgb, lower_green, upper_green)
        res = cv2.bitwise_and(frame,frame, mask= mask_g)

        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask_g)
        cv2.imshow('res',res)

        if cv2.waitKey(1) & 0xFF == ord('0'):
            break

def rgb_blue():
    while(1):
        _, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        #hue saturation value
        lower_blue = np.array([0,0,130])
        upper_blue = np.array([180,180,255])

        mask_b = cv2.inRange(rgb, lower_blue, upper_blue)
        res = cv2.bitwise_and(frame,frame, mask= mask_b)

        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask_b)
        cv2.imshow('res',res)

        if cv2.waitKey(1) & 0xFF == ord('0'):
            break

def rgb_plp():
    while(1):
        _, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        #hue saturation value
        lower_plp = np.array([110,0,110])
        upper_plp = np.array([255,100,255])

        mask_p = cv2.inRange(rgb, lower_plp, upper_plp)
        res = cv2.bitwise_and(frame,frame, mask= mask_p)

        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask_p)
        cv2.imshow('res',res)

        if cv2.waitKey(1) & 0xFF == ord('0'):
            break

def yuv_red():
    while(1):
        _, frame = cap.read()
        yuv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)

        #Intencity, Hue, Value
        #Valores basados en la conversión de HSV a YUV
        lower_red = np.array([0.385662745098039,0.099690901960784,0.177722039215686])
        upper_red = np.array([0.299,-0.14713,0.615])

        mask = cv2.inRange(yuv, lower_red, upper_red)
        res = cv2.bitwise_and(frame,frame, mask= mask)

        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)

        if cv2.waitKey(1) & 0xFF == ord('0'):
            break

def yuv_yellow():
    print('Hola amarillo')

def yuv_plp():
    print('Hola morado')

def yuv_green():
    print('Hola verde')

def yuv_blue():
    print('Hola azul')
#__________________________________________________________________________ Main

print('Seleccione el modelo de colores deseado:')
modelo=int(input(' 1) HSV\n 2) RGB\n 3) YUV\n'))

if(modelo==1):
    print('Seleccione el color que quiera resaltar:')
    color=int(input(' 1) Rojo\n 2) Amarillo\n 3) Purpura\n 4) Verde\n 5) Azul\n'))
    if(color==1):
        hsv_red()
    elif(color==2):
        hsv_yellow()
    elif color==3:
        hsv_plp()
    elif color==4:
        hsv_green()
    else:
        hsv_blue()
elif(modelo==2):
    print('Seleccione el color que quiera resaltar:')
    color=int(input(' 1) Rojo\n 2) Amarillo\n 3) Purpura\n 4) Verde\n 5) Azul\n'))
    if(color==1):
        rgb_red()
    elif(color==2):
        rgb_yellow()
    elif color==3:
        rgb_plp()
    elif color==4:
        rgb_green()
    else:
        rgb_blue()
else:
    print('Seleccione el color que quiera resaltar:')
    color=int(input(' 1) Rojo\n 2) Amarillo\n 3) Purpura\n 4) Verde\n 5) Azul\n'))
    if(color==1):
        yuv_red()
    elif(color==2):
        yuv_yellow()
    elif color==3:
        yuv_plp()
    elif color==4:
        yuv_green()
    else:
        yuv_blue()

#yuv_red()
#hsv_blue()
#rgb_blue()

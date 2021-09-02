import requests
import re
import sys
import time
from decimal import Decimal
from datetime import date, datetime, timedelta
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import urllib.request
from PyQt5 import *

url = 'https://www.multiplay.com.pe/consultas/consulta-prueba.php'

#-------------------------------- Funciones Generales ----------------------------------

def ejecutarSql(sql):
    datos = {'accion':'ejecutar','sql': sql}
    x = requests.post(url, data = datos)
    if x.text!="":
        respuesta=x.json()
        if respuesta!=[]:
            print(respuesta)
    else:
        print("respuesta vacía")
    return respuesta

def consultarSql(sql):
    datos = {'accion':'leer','sql': sql}
    x = requests.post(url, data=datos)
    respuesta=x.json()
    myresult=[]
    if respuesta!=[]:
        for datos in respuesta:
            contenido=[]
            for k,dato in datos.items():
                contenido.append(dato)
            myresult.append(contenido)
    return myresult

def cargarLogo(lb, codSoc):
    try:
        if codSoc == 'multiplay':
            codSoc = 'Mp_st'
        folderLogo = '''Logos/Logo'''+ codSoc +'.png'
        logoSoc = QPixmap(folderLogo)
        ratio = QtCore.Qt.KeepAspectRatio
        logoSoc = logoSoc.scaled(250, 35, ratio)
        lb.setPixmap(logoSoc)
    except:
        ""

def cargarIcono(obj, tipoIcono):
    try:
        iconos = {
        'erp': "organization",
        'grabar': "diskette",
        'salir': "logout"}
        icono = iconos[tipoIcono]
        folderIcono = '''IconosLocales/'''+ icono +'.png'
        icon = QPixmap(folderIcono)
        if tipoIcono != 'erp':
            obj.setIcon(QIcon(icon))
        else:
            obj.setWindowIcon(QIcon(icon))
    except:
        ""

def mensajeDialogo(tipo, titulo, mensaje):
    try:
        msg = QMessageBox()
        cargarIcono(msg, 'erp')
        if tipo == 'error':
            msg.setIcon(QMessageBox.Critical)
        elif tipo == 'informacion':
            msg.setIcon(QMessageBox.Information)
        elif tipo == 'advertencia':
            msg.setIcon(QMessageBox.Warning)
        elif tipo == 'pregunta':
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setWindowTitle(titulo)
        msg.setText(mensaje)
        msg.setStyleSheet('''QMessageBox {background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(160, 160, 160, 255), stop:1 rgba(255, 255, 255, 255));} ''')
        valor = msg.exec_()
        if valor == 1024:
            valor = 'Ok'
        if valor == 16384:
            valor = 'Yes'
        if valor == 65536:
            valor = 'No'
        return valor
    except:
        ""

#--------------------------------PROGRAMA N° 1 - ERP_DATA_REF_P002----------------------------------

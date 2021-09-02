import sys
from datetime import datetime
from Funciones04 import *
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import urllib.request

sqlCod_Interlocutor = "SELECT Cod_tipo_inter FROM TAB_SOC_014_Tipo_de_Interlocutor"
sqlDescripción_Interlocutor = "SELECT Descrip_inter FROM TAB_SOC_014_Tipo_de_Interlocutor"

sqlCod_Documentos = "SELECT Tipo_Doc FROM TAB_SOC_012_Tipos_de_Documentos"
sqlDescripción_Documentos = "SELECT Descrip_Doc FROM TAB_SOC_012_Tipos_de_Documentos"

sqlCod_Productos = "SELECT Cod_Marca FROM TAB_MAT_010_Marca_de_Producto"
sqlDescripción_Productos = "SELECT Descrip_Marca FROM TAB_MAT_010_Marca_de_Producto"

sqlCod_Pedido = "SELECT Cod_Doc FROM TAB_SOC_015_Tipo_de_Documentos"
sqlDescripción_Pedido = "SELECT Descrip_Doc FROM TAB_SOC_015_Tipo_de_Documentos"

sqlCod_Stock = "SELECT Tipo_stock FROM TAB_SOC_013_Tipos_de_Stock"
sqlDescripción_Stock = "SELECT Descrip_Stock FROM TAB_SOC_013_Tipos_de_Stockde Stock"

sqlCod_Area = "SELECT Cod_Area FROM TAB_SOC_010_Áreas_de_la_empresa"
sqlDescripción_Area = "SELECT Descripción_Area FROM TAB_SOC_010_Áreas_de_la_empresa"

sqlCod_Cargo = "SELECT Cod_Cargo FROM TAB_SOC_011_Cargo_en_la_empresa"
sqlDescripción_Cargo = "SELECT Descripción_Cargo FROM TAB_SOC_011_Cargo_en_la_empresa"

sqlCod_Bancos = "SELECT Cod_Banco FROM TAB_SOC_016_Tipo_de_Bancos"
sqlDescripción_Bancos = "SELECT Descrip_Banco FROM TAB_SOC_016_Tipo_de_Bancos"

sqlForma_Envio = "SELECT Forma_Envio FROM `TAB_SOC_025: Forma de Envío`"
sqlDescripción_Envio = "SELECT Descrip_Envio FROM `TAB_SOC_025: Forma de Envío`"

class ERP_DATA_REF_P002(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("ERP_PAUX_002.ui",self)

        self.leTipo_Marca.setReadOnly(True)
        self.leDescripcion.setReadOnly(True)
        self.pbGrabar.setEnabled(False)

        self.rbTipo_Interlocutor.clicked.connect(self.Habilitado)
        self.rbTipo_Documentos.clicked.connect(self.Habilitado)
        self.rbMarca_Productos.clicked.connect(self.Habilitado)
        self.rbTipo_Pedido.clicked.connect(self.Habilitado)
        self.rbTipo_Stock.clicked.connect(self.Habilitado)
        self.rbArea.clicked.connect(self.Habilitado)
        self.rbCargo.clicked.connect(self.Habilitado)
        self.rbBancos.clicked.connect(self.Habilitado)
        self.rbForma_Envio.clicked.connect(self.Habilitado)
        self.leTipo_Marca.editingFinished.connect(self.Codigo)
        self.leDescripcion.editingFinished.connect(self.Descripcion)
        self.pbGrabar.clicked.connect(self.Grabar)
        self.pbSalir.clicked.connect(self.Salir)

    def datosGenerales(self, codSoc, empresa, usuario):
        global Cod_Soc, Nom_Soc, Cod_Usuario
        Cod_Soc = codSoc
        Nom_Soc = empresa
        Cod_Usuario = usuario

        cargarLogo(self.lbLogo_Mp,'multiplay')
        cargarLogo(self.lbLogo_Soc, Cod_Soc)
        cargarIcono(self, 'erp')
        cargarIcono(self.pbSalir, 'salir')
        cargarIcono(self.pbGrabar, 'grabar')

    def Habilitado(self):
        self.leTipo_Marca.setReadOnly(False)
        self.leDescripcion.setReadOnly(False)
        self.pbGrabar.setEnabled(True)

    def Codigo (self):
        if self.btgTablas.checkedButton()==self.rbTipo_Interlocutor:
            self.CodigoInterlocutor()
        if self.btgTablas.checkedButton()==self.rbTipo_Documentos:
            self.CodigoDocumentos()
        if self.btgTablas.checkedButton()==self.rbMarca_Productos:
            self.CodigoProductos()
        if self.btgTablas.checkedButton()==self.rbTipo_Pedido:
            self.CodigoPedido()
        if self.btgTablas.checkedButton()==self.rbTipo_Stock:
            self.CodigoStock()
        if self.btgTablas.checkedButton()==self.rbArea:
            self.CodigoArea()
        if self.btgTablas.checkedButton()==self.rbCargo:
            self.CodigoCargo()
        if self.btgTablas.checkedButton()==self.rbBancos:
            self.CodigoBancos()
        if self.btgTablas.checkedButton()==self.rbForma_Envio:
            self.CodigoForma_Envio()

    def Descripcion (self):
        if self.btgTablas.checkedButton()==self.rbTipo_Interlocutor:
            self.DescripcionInterlocutor()
        if self.btgTablas.checkedButton()==self.rbTipo_Documentos:
            self.DescripcionDocumentos()
        if self.btgTablas.checkedButton()==self.rbMarca_Productos:
            self.DescripcionProductos()
        if self.btgTablas.checkedButton()==self.rbTipo_Pedido:
            self.DescripcionPedido()
        if self.btgTablas.checkedButton()==self.rbTipo_Stock:
            self.DescripcionStock()
        if self.btgTablas.checkedButton()==self.rbArea:
            self.DescripcionArea()
        if self.btgTablas.checkedButton()==self.rbCargo:
            self.DescripcionCargo()
        if self.btgTablas.checkedButton()==self.rbBancos:
            self.DescripcionBancos()
        if self.btgTablas.checkedButton()==self.rbForma_Envio:
            self.DescripcionForma_Envio()

    def Grabar (self):
        if self.btgTablas.checkedButton()==self.rbTipo_Interlocutor:
            self.GrabarInterlocutor()
        if self.btgTablas.checkedButton()==self.rbTipo_Documentos:
            self.GrabarDocumentos()
        if self.btgTablas.checkedButton()==self.rbMarca_Productos:
            self.GrabarProductos()
        if self.btgTablas.checkedButton()==self.rbTipo_Pedido:
            self.GrabarPedido()
        if self.btgTablas.checkedButton()==self.rbTipo_Stock:
            self.GrabarStock()
        if self.btgTablas.checkedButton()==self.rbArea:
            self.GrabarArea()
        if self.btgTablas.checkedButton()==self.rbCargo:
            self.GrabarCargo()
        if self.btgTablas.checkedButton()==self.rbBancos:
            self.GrabarBancos()
        if self.btgTablas.checkedButton()==self.rbForma_Envio:
            self.GrabarForma_Envio()

    def Salir (self):
        self.close()

#--------------------------------------Interlocutor----------------------------------------------

    def CodigoInterlocutor(self):
        Tipo_Marca=self.leTipo_Marca.text()
        if len(Tipo_Marca) !=0:
            informacion=consultarSql(sqlCod_Interlocutor)
            lista = []
            for info in informacion:
                for elemento in info:
                    lista.append(elemento)
            if Tipo_Marca in lista:
                mensajeDialogo("advertencia", "Advertencia","Código Tipo Interlocutor ya existe")
                self.leTipo_Marca.clear()
                self.leDescripcion.setEnabled(False)
                self.leDescripcion.setEnabled(True)

    def DescripcionInterlocutor(self):
        Descripcion=self.leDescripcion.text()
        if len(Descripcion) !=0:
            informacion=consultarSql(sqlDescripción_Interlocutor)
            lista = []
            for info in informacion:
                for elemento in info:
                    lista.append(elemento)
            if Descripcion in lista:
                mensajeDialogo("advertencia", "Advertencia", "Descripción de Interlocutor ya existe")
        else:
            mensajeDialogo("advertencia", "Advertencia", "Campo Descripción vacío")

    def GrabarInterlocutor(self):
        Tipo_Marca=self.leTipo_Marca.text()
        Descripcion=self.leDescripcion.text()
        Fecha=datetime.now().strftime("%Y-%m-%d")
        Hora=datetime.now().strftime("%H:%M:%S.%f")
        if len(Tipo_Marca) and len(Descripcion)!=0:
            sql ="INSERT INTO TAB_SOC_014_Tipo_de_Interlocutor(Cod_tipo_inter,Descrip_inter,Usuario_Reg,Fecha_Reg,Hora_Reg) VALUES ('%s', '%s','%s','%s', '%s')" % (Tipo_Marca,Descripcion,Cod_Usuario,Fecha,Hora)
            respuesta=ejecutarSql(sql)
            if respuesta["respuesta"]=="correcto":
                mensajeDialogo("informacion", "Información", "Registro Grabado")
            if respuesta["respuesta"]=="incorrecto":
                mensajeDialogo("error", "Error", "Datos inválidos, verifique")
            self.leTipo_Marca.clear()
            self.leDescripcion.clear()
        else:
            mensajeDialogo("error", "Error", "Uno o más campos vacios, verifique")

#--------------------------------------Documentos----------------------------------------------

    def CodigoDocumentos(self):
        Tipo_Marca=self.leTipo_Marca.text()
        if len(Tipo_Marca) !=0:
            informacion=consultarSql(sqlCod_Documentos)
            lista = []
            for info in informacion:
                for elemento in info:
                    lista.append(elemento)
            if Tipo_Marca in lista:
                mensajeDialogo("advertencia", "Advertencia","Código Tipo Documento ya existe")
                self.leTipo_Marca.clear()
                self.leDescripcion.setEnabled(False)
                self.leDescripcion.setEnabled(True)

    def DescripcionDocumentos(self):
        Descripcion=self.leDescripcion.text()
        if len(Descripcion) !=0:
            informacion=consultarSql(sqlDescripción_Documentos)
            lista = []
            for info in informacion:
                for elemento in info:
                    lista.append(elemento)
            if Descripcion in lista:
                mensajeDialogo("advertencia", "Advertencia", "Descripción de Documentos ya existe")
        else:
            mensajeDialogo("advertencia", "Advertencia", "Campo Descripción vacío")

    def GrabarDocumentos(self):
        Tipo_Marca=self.leTipo_Marca.text()
        Descripcion=self.leDescripcion.text()
        Fecha=datetime.now().strftime("%Y-%m-%d")
        Hora=datetime.now().strftime("%H:%M:%S.%f")
        if len(Tipo_Marca) and len(Descripcion)!=0:
            sql ="INSERT INTO TAB_SOC_012_Tipos_de_Documentos (Tipo_Doc,Descrip_Doc,Usuario_Reg,Fecha_Reg,Hora_Reg) VALUES ('%s','%s','%s','%s','%s')" % (Tipo_Marca,Descripcion,Cod_Usuario,Fecha,Hora)
            respuesta=ejecutarSql(sql)
            if respuesta["respuesta"]=="correcto":
                mensajeDialogo("informacion", "Información", "Registro Grabado")
            if respuesta["respuesta"]=="incorrecto":
                mensajeDialogo("error", "Error", "Datos inválidos, verifique")
            self.leTipo_Marca.clear()
            self.leDescripcion.clear()
        else:
            mensajeDialogo("error", "Error", "Uno o más campos vacios, verifique")

#--------------------------------------Productos----------------------------------------------

    def CodigoProductos(self):
        Tipo_Marca=self.leTipo_Marca.text()
        if len(Tipo_Marca) !=0:
            informacion=consultarSql(sqlCod_Productos)
            lista = []
            for info in informacion:
                for elemento in info:
                    lista.append(elemento)
            if Tipo_Marca in lista:
                mensajeDialogo("advertencia", "Advertencia","Código Marca Producto ya existe")
                self.leTipo_Marca.clear()
                self.leDescripcion.setEnabled(False)
                self.leDescripcion.setEnabled(True)

    def DescripcionProductos(self):
        Descripcion=self.leDescripcion.text()
        if len(Descripcion) !=0:
            informacion=consultarSql(sqlDescripción_Productos)
            lista = []
            for info in informacion:
                for elemento in info:
                    lista.append(elemento)
            if Descripcion in lista:
                mensajeDialogo("advertencia", "Advertencia", "Descripción de Productos ya existe")
        else:
            mensajeDialogo("advertencia", "Advertencia", "Campo Descripción vacío")

    def GrabarProductos(self):
        Tipo_Marca=self.leTipo_Marca.text()
        Descripcion=self.leDescripcion.text()
        Fecha=datetime.now().strftime("%Y-%m-%d")
        Hora=datetime.now().strftime("%H:%M:%S.%f")
        if len(Tipo_Marca) and len(Descripcion)!=0:
            sql ="INSERT INTO TAB_MAT_010_Marca_de_Producto (Cod_Marca,Descrip_Marca,Usuario_Reg,Fecha_Reg,Hora_Reg) VALUES ('%s', '%s','%s','%s', '%s')" % (Tipo_Marca,Descripcion,Cod_Usuario,Fecha,Hora)
            respuesta=ejecutarSql(sql)
            if respuesta["respuesta"]=="correcto":
                mensajeDialogo("informacion", "Información", "Registro Grabado")
            if respuesta["respuesta"]=="incorrecto":
                mensajeDialogo("error", "Error", "Datos inválidos, verifique")
            self.leTipo_Marca.clear()
            self.leDescripcion.clear()
        else:
            mensajeDialogo("error", "Error", "Uno o más campos vacios, verifique")

#--------------------------------------Pedido----------------------------------------------

    def CodigoPedido(self):
        Tipo_Marca=self.leTipo_Marca.text()
        if len(Tipo_Marca) !=0:
            informacion=consultarSql(sqlCod_Pedido)
            lista = []
            for info in informacion:
                for elemento in info:
                    lista.append(elemento)
            if Tipo_Marca in lista:
                mensajeDialogo("advertencia", "Advertencia","Código Tipo Pedido ya existe")
                self.leTipo_Marca.clear()
                self.leDescripcion.setEnabled(False)
                self.leDescripcion.setEnabled(True)

    def DescripcionPedido(self):
        Descripcion=self.leDescripcion.text()
        if len(Descripcion) !=0:
            informacion=consultarSql(sqlDescripción_Pedido)
            lista = []
            for info in informacion:
                for elemento in info:
                    lista.append(elemento)
            if Descripcion in lista:
                mensajeDialogo("advertencia", "Advertencia", "Descripción de Pedido ya existe")
        else:
            mensajeDialogo("advertencia", "Advertencia", "Campo Descripción vacío")

    def GrabarPedido(self):
        Tipo_Marca=self.leTipo_Marca.text()
        Descripcion=self.leDescripcion.text()
        Fecha=datetime.now().strftime("%Y-%m-%d")
        Hora=datetime.now().strftime("%H:%M:%S.%f")
        if len(Tipo_Marca) and len(Descripcion)!=0:
            sql ="INSERT INTO TAB_SOC_015_Tipo_de_Documentos (Cod_Doc,Descrip_Doc,Usuario_Reg,Fecha_Reg,Hora_Reg) VALUES ('%s', '%s','%s','%s', '%s')" % (Tipo_Marca,Descripcion,Cod_Usuario,Fecha,Hora)
            respuesta=ejecutarSql(sql)
            if respuesta["respuesta"]=="correcto":
                mensajeDialogo("informacion", "Información", "Registro Grabado")
            if respuesta["respuesta"]=="incorrecto":
                mensajeDialogo("error", "Error", "Datos inválidos, verifique")
            self.leTipo_Marca.clear()
            self.leDescripcion.clear()
        else:
            mensajeDialogo("error", "Error", "Uno o más campos vacios, verifique")

#--------------------------------------Stock----------------------------------------------

    def CodigoStock(self):
        Tipo_Marca=self.leTipo_Marca.text()
        if len(Tipo_Marca) !=0:
            informacion=consultarSql(sqlCod_Stock)
            lista = []
            for info in informacion:
                for elemento in info:
                    lista.append(elemento)
            if Tipo_Marca in lista:
                mensajeDialogo("advertencia", "Advertencia","Código Tipo Stock ya existe")
                self.leTipo_Marca.clear()
                self.leDescripcion.setEnabled(False)
                self.leDescripcion.setEnabled(True)

    def DescripcionStock(self):
        Descripcion=self.leDescripcion.text()
        if len(Descripcion) !=0:
            informacion=consultarSql(sqlDescripción_Stock)
            lista = []
            for info in informacion:
                for elemento in info:
                    lista.append(elemento)
            if Descripcion in lista:
                mensajeDialogo("advertencia", "Advertencia", "Descripción de Stock ya existe")
        else:
            mensajeDialogo("advertencia", "Advertencia", "Campo Descripción vacío")

    def GrabarStock(self):
        Tipo_Marca=self.leTipo_Marca.text()
        Descripcion=self.leDescripcion.text()
        Fecha=datetime.now().strftime("%Y-%m-%d")
        Hora=datetime.now().strftime("%H:%M:%S.%f")
        if len(Tipo_Marca) and len(Descripcion)!=0:
            sql ="INSERT INTO TAB_SOC_013_Tipos_de_Stock (Tipo_stock,Descrip_Stock,Usuario_Reg,Fecha_Reg,Hora_Reg) VALUES ('%s', '%s','%s','%s', '%s')" % (Tipo_Marca,Descripcion,Cod_Usuario,Fecha,Hora)
            respuesta=ejecutarSql(sql)
            if respuesta["respuesta"]=="correcto":
                mensajeDialogo("informacion", "Información", "Registro Grabado")
            if respuesta["respuesta"]=="incorrecto":
                mensajeDialogo("error", "Error", "Datos inválidos, verifique")
            self.leTipo_Marca.clear()
            self.leDescripcion.clear()
        else:
            mensajeDialogo("error", "Error", "Uno o más campos vacios, verifique")

#--------------------------------------Area----------------------------------------------

    def CodigoArea(self):
        Tipo_Marca=self.leTipo_Marca.text()
        if len(Tipo_Marca) !=0:
            informacion=consultarSql(sqlCod_Area)
            lista = []
            for info in informacion:
                for elemento in info:
                    lista.append(elemento)
            if Tipo_Marca in lista:
                mensajeDialogo("advertencia", "Advertencia","Código Tipo Área ya existe")
                self.leTipo_Marca.clear()
                self.leDescripcion.setEnabled(False)
                self.leDescripcion.setEnabled(True)

    def DescripcionArea(self):
        Descripcion=self.leDescripcion.text()
        if len(Descripcion) !=0:
            informacion=consultarSql(sqlDescripción_Area)
            lista = []
            for info in informacion:
                for elemento in info:
                    lista.append(elemento)
            if Descripcion in lista:
                mensajeDialogo("advertencia", "Advertencia", "Descripción de Área ya existe")
        else:
            mensajeDialogo("advertencia", "Advertencia", "Campo Descripción vacío")

    def GrabarArea(self):
        Tipo_Marca=self.leTipo_Marca.text()
        Descripcion=self.leDescripcion.text()
        Fecha=datetime.now().strftime("%Y-%m-%d")
        Hora=datetime.now().strftime("%H:%M:%S.%f")
        if len(Tipo_Marca) and len(Descripcion)!=0:
            sql ="INSERT INTO TAB_SOC_010_Áreas_de_la_empresa (Cod_Área,Descripción_Área,Usuario_Reg,Fecha_Reg,Hora_Reg) VALUES ('%s', '%s','%s','%s', '%s')" % (Tipo_Marca,Descripcion,Cod_Usuario,Fecha,Hora)
            respuesta=ejecutarSql(sql)
            if respuesta["respuesta"]=="correcto":
                mensajeDialogo("informacion", "Información", "Registro Grabado")
            if respuesta["respuesta"]=="incorrecto":
                mensajeDialogo("error", "Error", "Datos inválidos, verifique")
            self.leTipo_Marca.clear()
            self.leDescripcion.clear()
        else:
            mensajeDialogo("error", "Error", "Uno o más campos vacios, verifique")

#--------------------------------------Cargo----------------------------------------------

    def CodigoCargo(self):
        Tipo_Marca=self.leTipo_Marca.text()
        if len(Tipo_Marca) !=0:
            informacion=consultarSql(sqlCod_Cargo)
            lista = []
            for info in informacion:
                for elemento in info:
                    lista.append(elemento)
            if Tipo_Marca in lista:
                mensajeDialogo("advertencia", "Advertencia","Código Tipo Cargo ya existe")
                self.leTipo_Marca.clear()
                self.leDescripcion.setEnabled(False)
                self.leDescripcion.setEnabled(True)

    def DescripcionCargo(self):
        Descripcion=self.leDescripcion.text()
        if len(Descripcion) !=0:
            informacion=consultarSql(sqlDescripción_Cargo)
            lista = []
            for info in informacion:
                for elemento in info:
                    lista.append(elemento)
            if Descripcion in lista:
                mensajeDialogo("advertencia", "Advertencia", "Descripción de Cargo ya existe")
        else:
            mensajeDialogo("advertencia", "Advertencia", "Campo Descripción vacío")

    def GrabarCargo(self):
        Tipo_Marca=self.leTipo_Marca.text()
        Descripcion=self.leDescripcion.text()
        Fecha=datetime.now().strftime("%Y-%m-%d")
        Hora=datetime.now().strftime("%H:%M:%S.%f")
        if len(Tipo_Marca) and len(Descripcion)!=0:
            sql ="INSERT INTO TAB_SOC_011_Cargo_en_la_empresa (Cod_Cargo,Descripción_Cargo,Usuario_Reg,Fecha_Reg,Hora_Reg) VALUES ('%s', '%s','%s','%s', '%s')" % (Tipo_Marca,Descripcion,Cod_Usuario,Fecha,Hora)
            respuesta=ejecutarSql(sql)
            if respuesta["respuesta"]=="correcto":
                mensajeDialogo("informacion", "Información", "Registro Grabado")
            if respuesta["respuesta"]=="incorrecto":
                mensajeDialogo("error", "Error", "Datos inválidos, verifique")
            self.leTipo_Marca.clear()
            self.leDescripcion.clear()
        else:
            mensajeDialogo("error", "Error", "Uno o más campos vacios, verifique")

#--------------------------------------Bancos----------------------------------------------

    def CodigoBancos(self):
        Tipo_Marca=self.leTipo_Marca.text()
        if len(Tipo_Marca) !=0:
            informacion=consultarSql(sqlCod_Bancos)
            lista = []
            for info in informacion:
                for elemento in info:
                    lista.append(elemento)
            if Tipo_Marca in lista:
                mensajeDialogo("advertencia", "Advertencia","Código Tipo Banco ya existe")
                self.leTipo_Marca.clear()
                self.leDescripcion.setEnabled(False)
                self.leDescripcion.setEnabled(True)

    def DescripcionBancos(self):
        Descripcion=self.leDescripcion.text()
        if len(Descripcion) !=0:
            informacion=consultarSql(sqlDescripción_Bancos)
            lista = []
            for info in informacion:
                for elemento in info:
                    lista.append(elemento)
            if Descripcion in lista:
                mensajeDialogo("advertencia", "Advertencia", "Descripción de Bancos ya existe")
        else:
            mensajeDialogo("advertencia", "Advertencia", "Campo Descripción vacío")

    def GrabarBancos(self):
        Tipo_Marca=self.leTipo_Marca.text()
        Descripcion=self.leDescripcion.text()
        Fecha=datetime.now().strftime("%Y-%m-%d")
        Hora=datetime.now().strftime("%H:%M:%S.%f")
        if len(Tipo_Marca) and len(Descripcion)!=0:
            sql ="INSERT INTO TAB_SOC_016_Tipo_de_Bancos(Cod_Banco,Descrip_Banco,Usuario_Reg,Fecha_Reg,Hora_Reg) VALUES ('%s', '%s','%s','%s', '%s')" % (Tipo_Marca,Descripcion,Cod_Usuario,Fecha,Hora)
            respuesta=ejecutarSql(sql)
            if respuesta["respuesta"]=="correcto":
                mensajeDialogo("informacion", "Información", "Registro Grabado")
            if respuesta["respuesta"]=="incorrecto":
                mensajeDialogo("error", "Error", "Datos inválidos, verifique")
            self.leTipo_Marca.clear()
            self.leDescripcion.clear()
        else:
            mensajeDialogo("error", "Error", "Uno o más campos vacios, verifique")

#--------------------------------------Forma Envio----------------------------------------------

    def CodigoForma_Envio(self):
        Tipo_Marca=self.leTipo_Marca.text()
        if len(Tipo_Marca) !=0:
            informacion=consultarSql(sqlForma_Envio)
            lista = []
            for info in informacion:
                for elemento in info:
                    lista.append(elemento)
            if Tipo_Marca in lista:
                mensajeDialogo("advertencia", "Advertencia","Código Forma de Envio ya existe")
                self.leTipo_Marca.clear()
                self.leDescripcion.setEnabled(False)
                self.leDescripcion.setEnabled(True)


    def DescripcionForma_Envio(self):
        Descripcion=self.leDescripcion.text()
        if len(Descripcion) !=0:
            informacion=consultarSql(sqlDescripción_Envio)
            lista = []
            for info in informacion:
                for elemento in info:
                    lista.append(elemento)
            if Descripcion in lista:
                mensajeDialogo("advertencia", "Advertencia", "Descripción de Forma de Envio ya existe")
        else:
            mensajeDialogo("advertencia", "Advertencia", "Campo Descripción vacío")

    def GrabarForma_Envio(self):
        Tipo_Marca=self.leTipo_Marca.text()
        Descripcion=self.leDescripcion.text()
        Fecha=datetime.now().strftime("%Y-%m-%d")
        Hora=datetime.now().strftime("%H:%M:%S.%f")
        if len(Tipo_Marca) and len(Descripcion)!=0:
            sql ="INSERT INTO `TAB_SOC_025: Forma de Envío`(Forma_Envio,Descrip_Envio,Usuario_Reg,Fecha_Reg,Hora_Reg) VALUES ('%s', '%s','%s','%s', '%s')" % (Tipo_Marca,Descripcion,Cod_Usuario,Fecha,Hora)
            respuesta=ejecutarSql(sql)
            if respuesta["respuesta"]=="correcto":
                mensajeDialogo("informacion", "Información", "Registro Grabado")
            if respuesta["respuesta"]=="incorrecto":
                mensajeDialogo("error", "Error", "Datos inválidos, verifique")
            self.leTipo_Marca.clear()
            self.leDescripcion.clear()
        else:
            mensajeDialogo("error", "Error", "Uno o más campos vacios, verifique")

if __name__ == '__main__':
    app=QApplication(sys.argv)
    _main=ERP_DATA_REF_P002()
    _main.showMaximized()
    app.exec_()

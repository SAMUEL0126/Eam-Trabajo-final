# -*- coding: 850-*-
# -*- coding: utf-8-*-

import socket
import time
import datetime
import pyodbc
import pickle
import Tkinter
import threading
import signal
import os
import signal
import sys

#============================================================================================#

class Comunicaciones():
    def __init__(self):
        self.s=0
        self.Cnxn=0
        self.Cursor=0
        self.IP_Cliente=0
        self.Conex_Cliente=0
        self.Dato_Tx = 0
        self.Dato_Rx = 0
        self.Indicad_Error = 0

#============================================================================================#

    def Open_Socket(self):
        while 1:
            try:
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.bind(('', 23))
                self.s.listen(30)
                break                
            except:
                pass           
        return
    
    def Open_Cliente(self):
        while 1:
            try:
                self.Conex_Cliente, self.IP_Cliente = self.s.accept()
                list(self.IP_Cliente)
                break                              
            except:
                pass
        return     
    
    def Rx_Dato_Socket(self):
        self.Conex_Cliente.settimeout(3)
        self.Indicad_Error = 0
        try:            
            LongBuffer = 1024
            self.Dato_Rx = self.Conex_Cliente.recv(LongBuffer)
            Texto = str(self.IP_Cliente[0]+" - "+datetime.datetime.now().strftime("%Y-%m-%d")+".txt")
            Log = open(Texto,"a")
            Log.write('RX: ')
            Texto = self.Dato_Rx
            Cadena=str(Texto)
            Log.write (Cadena)
            Log.write(' - ')
            Texto = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            Cadena=str(Texto)
            Log.write (Cadena)
            Log.write('\n')
            Log.close()
            return
        except:
            self.Dato_Rx = "ERROR"
            self.Indicad_Error = "ERROR_CNXN"
            return

    def Tx_Dato_Socket(self):
        self.Indicad_Error = 0
        try:
            self.Conex_Cliente.send(self.Dato_Tx)
            Texto = str(self.IP_Cliente[0]+" - "+datetime.datetime.now().strftime("%Y-%m-%d")+".txt")
            Log = open(Texto,"a")
            Log.write('TX: ')
            Texto = pickle.loads(self.Dato_Tx)
            Cadena=str(Texto)
            Log.write (Cadena)            
            Log.write(' - ')
            Texto = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            Cadena=str(Texto)
            Log.write (Cadena)
            Log.write(' - Tiempo_Respuesta: ')
            CNXNS.Timer_Conex_tout = time.time() - CNXNS.Timer_Conex_tout
            Texto = CNXNS.Timer_Conex_tout
            Cadena=str(Texto)
            Log.write (Cadena)            
            Log.write('\n')
            Log.close()
            return
        except:
            self.Indicad_Error = "ERROR_CNXN"
            print 'Error TX Socket'
            return
    
    def close_socket(self):
        self.Conex_Cliente.close
        return      

    def Open_Conex_Sql(self):
        self.Indicad_Error = 0
        try:
            
            #self.Cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=P1MARPTA0J8A8V\SQLEXPRESS;DATABASE=dbEmpaque_Raspi;UID=sa;PWD=sa')
            self.Cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.106.110.16\SQLEXPRESS;DATABASE=dbEmpaque_Raspi;UID=plc;PWD=plc')
            self.Cursor = self.Cnxn.cursor()
            return
        except:
            self.Indicad_Error = "ERROR_CNXN"
            print 'Error conex SQL'            
            return

    def Lectura_IP(self):
        try:
            COM.Cursor.execute("SELECT Codigo_Raspi FROM RaspberryPi WHERE IP_Raspi = (?)", self.IP_Cliente[0])
            CNXNS.Codigo_Mesa = self.Cursor.fetchone()
            if CNXNS.Codigo_Mesa != None:
                CNXNS.Codigo_Mesa = CNXNS.Codigo_Mesa[0]
            else:
                CNXNS.Codigo_Mesa = None
            return
        except:
            self.Indicad_Error = "ERROR_CNXN"
            print 'Error conex IP'            
            return
            

#============================================================================================#

class Hilo_Conexiones(threading.Thread, Comunicaciones):
    def __init__(self):
        threading.Thread.__init__(self)

        self.Row_Verif_Logueo = 0
        self.Row_Verif_Producc = 0
        self.Row_Verif_Paro_Maq = 0
        self.Row_Evento_Produccion = 0
        self.Row_Info_Empl = 0
        self.Row_Info_Lote = 0
        self.Row_Efici_Oper = 0
        self.Trama = 0
        self.Hora_Server = 0
        self.Codigo_Turno = 0
        self.Codigo_Mesa = 0
        self.Est_Maquina = 0
        self.Row_Cant_Event = 0
        self.Cantid_Operario = 0
        self.Turno_Marc_Empl = 0
        self.Estand = "0"
        self.Operac = "0"
        self.Eficiencia = 0
        self.Unidades_Oper = 0
        self.Anterior = 0
        self.Actual = 0
        self.Fecha_Inic = 0
        self.Fecha_Final = 0
        self.Tiemp_Paro_Alim = 0
        self.Verif_Paro_Aliment = 0
        self.Timer_Conex_tout = 0
        self.Indic_Error_Efic = 0
        self.Cantid_Acumulada=0
        self.Dia_Anterior = 0
        self.Dia_Actual = 0
        self.Fecha_Query = 0
        self.Row_Verif_Prod_Inic = 0
        self.Row_MSTR_Paros = 0
        self.Tiempo_Tot_Turno = 0
        self.Tiempo_Alimen_Dia = 0
        self.Minutos_Presencia = 0
        self.Unidades_x_Stdr = 0
        self.Reg_Paros_Afect_efic = 0
        self.Contador_Paros_Alim = 0
        self.Unidades_Turno = 0
        self.Eficiencia_Turno = 0
        self.Tiempo_Par_Afect_efic = 0
        self.Tiemp_Tot_Par_Sin_Efic = 0
        self.Copy_Turno = 0
        self.Registr_Min_Pres = 0
        
#============================================================================================#

    def run(self):
        while 1:
            COM.Open_Cliente()
            if CLSTURNO.Indicad_Cnxn != 0:
                COM.Dato_Tx = pickle.dumps("ERROR_CNXN*")
                COM.Tx_Dato_Socket()
                COM.Conex_Cliente.close
            else:
                self.Timer_Conex_tout = time.time()                
                CLSTURNO.Indicad_Cnxn = 2
                COM.Open_Conex_Sql()
                COM.Lectura_IP()
                COM.Cnxn.close
                if COM.Indicad_Error == "ERROR_CNXN":
                    COM.Dato_Tx = pickle.dumps("ERROR_CNXN*")
                    COM.Tx_Dato_Socket()
                    COM.Conex_Cliente.close
                    COM.Cnxn.close
                else:
                    if self.Codigo_Mesa != None:
                        COM.Rx_Dato_Socket()
                        if 'EG' in COM.Dato_Rx:
                            CNXNS.Sol_Est_Gral()                        
                            self.Timer_Conex_tout = time.time() - self.Timer_Conex_tout   
                            CLSTURNO.Indicad_Cnxn = 0
                        elif 'STB' in COM.Dato_Rx:
                            CNXNS.Est_Standby()
                            self.Timer_Conex_tout = time.time() - self.Timer_Conex_tout                            
                            CLSTURNO.Indicad_Cnxn = 0
                        elif 'LOG' in COM.Dato_Rx:
                            CNXNS.Est_Logueado()
                            self.Timer_Conex_tout = time.time() - self.Timer_Conex_tout
                            CLSTURNO.Indicad_Cnxn = 0                                                   
                        elif "ADMLGT" in COM.Dato_Rx:
                            CNXNS.Deslog_Usuario()
                            self.Timer_Conex_tout = time.time() - self.Timer_Conex_tout
                            CLSTURNO.Indicad_Cnxn = 0
                        else:
                            COM.Conex_Cliente.close
                            CLSTURNO.Indicad_Cnxn = 0
                    else:
                        COM.Conex_Cliente.close
                        CLSTURNO.Indicad_Cnxn = 0

#============================================================================================#
                    
    def Calcula_Eficienc(self):
        self.Indic_Error_Efic = 0
        try:
            self.Anterior = datetime.datetime.now()- datetime.timedelta(days=1)
            self.Actual = datetime.datetime.now()
            if self.Anterior.month <= 9 and self.Anterior.day <= 9:
                self.Fecha_Inic = ("0"+str(self.Anterior.day)+"/0"+str(self.Anterior.month)+"/"+str(self.Anterior.year)+" "+"22:00:00")
            elif self.Anterior.month <= 9:
                self.Fecha_Inic = (str(self.Anterior.day)+"/0"+str(self.Anterior.month)+"/"+str(self.Anterior.year)+" "+"22:00:00")
            elif self.Anterior.day <= 9:
                self.Fecha_Inic = ("0"+str(self.Anterior.day)+"/"+str(self.Anterior.month)+"/"+str(self.Anterior.year)+" "+"22:00:00")
            else:
                self.Fecha_Inic = (str(self.Anterior.day)+"/"+str(self.Anterior.month)+"/"+str(self.Anterior.year)+" "+"22:00:00")
                
            if self.Actual.month <= 9 and self.Actual.day <= 9:
                self.Fecha_Final = ("0"+str(self.Actual.day)+"/0"+str(self.Actual.month)+"/"+str(self.Actual.year)+" "+"22:00:59")
            elif self.Actual.month <= 9:
                self.Fecha_Final = (str(self.Actual.day)+"/0"+str(self.Actual.month)+"/"+str(self.Actual.year)+" "+"22:00:59")
            elif self.Actual.day <= 9:
                self.Fecha_Final = ("0"+str(self.Actual.day)+"/"+str(self.Actual.month)+"/"+str(self.Actual.year)+" "+"22:00:59")
            else:
                self.Fecha_Final = (str(self.Actual.day)+"/"+str(self.Actual.month)+"/"+str(self.Actual.year)+" "+"22:00:59")

            self.Tiempo_Tot_Turno = 0
            self.Tiempo_Alimen_Dia = 0
            self.Minutos_Presencia = 0
            self.Unidades_x_Stdr = 0
            self.Unidades_Turno = 0
            self.Eficiencia_Turno = 0
            self.Tiempo_Par_Afect_efic = 0
            self.Tiemp_Tot_Par_Sin_Efic = 0
            self.Registr_Min_Pres = 0
            COM.Cursor.execute("WITH C AS(SELECT Event_Prod.Id_Lote, Event_Prod.Codigo_Turno AS Turno, Marc.Fecha_Ingreso AS Marc_Ingreso, Marc.Fecha_Salida AS Marc_Salida, DATEDIFF(ss,Marc.Fecha_Ingreso, ISNULL(Marc.Fecha_Salida, GETDATE()))/60 AS 'Tiempo_Logueo', left(T_Empl.Hora_Inicio,8) AS Ini_Turno, left(T_Empl.Hora_Final,8) AS Fin_Turno, T_Empl.Tiempo_Turno_Minutos AS Minutos_Turno, CASE WHEN (Marc.Fecha_Salida IS NOT NULL) AND (T_Empl.Hora_Inicio != '00:00:00') AND ((DATEDIFF(ss,T_Empl.Hora_Inicio,CONVERT(varchar(25), GETDATE(), 108)))/60) >= T_Empl.Tiempo_Turno_Minutos THEN T_Empl.Tiempo_Turno_Minutos WHEN (Marc.Fecha_Salida IS NOT NULL ) AND (T_Empl.Hora_Inicio != '00:00:00') AND ((DATEDIFF(ss,T_Empl.Hora_Inicio,CONVERT(varchar(25), GETDATE(), 108)))/60) < T_Empl.Tiempo_Turno_Minutos THEN  ((DATEDIFF(ss,T_Empl.Hora_Inicio,CONVERT(varchar(25), GETDATE(), 108)))/60) WHEN (Marc.Fecha_Salida IS NOT NULL ) AND (T_Empl.Hora_Inicio = '00:00:00') AND ((DATEDIFF(ss,CONVERT(varchar(25), Marc.Fecha_Ingreso, 108),CONVERT(varchar(25), GETDATE(), 108)))/60) >= T_Empl.Tiempo_Turno_Minutos THEN  T_Empl.Tiempo_Turno_Minutos WHEN (Marc.Fecha_Salida IS NOT NULL ) AND (T_Empl.Hora_Inicio = '00:00:00') AND ((DATEDIFF(ss,CONVERT(varchar(25), Marc.Fecha_Ingreso, 108),CONVERT(varchar(25), GETDATE(), 108)))/60) < T_Empl.Tiempo_Turno_Minutos THEN ((DATEDIFF(ss,CONVERT(varchar(25), Marc.Fecha_Ingreso, 108),CONVERT(varchar(25), GETDATE(), 108)))/60) WHEN (T_Empl.Hora_Inicio != '00:00:00') AND((DATEDIFF(ss,T_Empl.Hora_Inicio,CONVERT(varchar(25), GETDATE(), 108)))/60) >= T_Empl.Tiempo_Turno_Minutos THEN T_Empl.Tiempo_Turno_Minutos WHEN (T_Empl.Hora_Inicio != '00:00:00') AND((DATEDIFF(ss,T_Empl.Hora_Inicio,CONVERT(varchar(25), GETDATE(), 108)))/60) < T_Empl.Tiempo_Turno_Minutos THEN ((DATEDIFF(ss,T_Empl.Hora_Inicio,CONVERT(varchar(25), GETDATE(), 108)))/60) WHEN (T_Empl.Hora_Inicio = '00:00:00') AND((DATEDIFF(ss,CONVERT(varchar(25), Marc.Fecha_Ingreso, 108),CONVERT(varchar(25), GETDATE(), 108)))/60) >= T_Empl.Tiempo_Turno_Minutos THEN T_Empl.Tiempo_Turno_Minutos ELSE ((DATEDIFF(ss,CONVERT(varchar(25), Marc.Fecha_Ingreso, 108),CONVERT(varchar(25), GETDATE(), 108)))/60) END AS Tiempo_Turno, 0 AS T_Alimentacion, Event_Prod.Identificacion, Event_Prod.Estandar, Lote.Unidades AS Unidades_Plega, (COUNT(Event_Prod.Id_Lote)) AS 'Contador', Lote.Unidades*(COUNT(Event_Prod.Id_Lote)) AS 'Tot_Unidades', (Event_Prod.Estandar*(Lote.Unidades*(COUNT(Event_Prod.Id_Lote)))) AS 'Minut_Produc' FROM Eventos_Produccion AS Event_Prod INNER JOIN Lote AS Lote ON Event_Prod.Id_Lote = Lote.Id_Lote INNER JOIN Turno_Empleado AS T_Empl ON Event_Prod.Codigo_Turno = T_Empl.Codigo_Turno INNER JOIN Marcaciones AS Marc ON (Event_Prod.Identificacion = Marc.Identificacion AND Event_Prod.Codigo_Turno = Marc.Codigo_Turno) WHERE Event_Prod.Ini_Event_Prod >= (?) AND Event_Prod.Ini_Event_Prod <= (?) AND Marc.Fecha_Ingreso >= (?) AND Marc.Fecha_Ingreso <= (?) AND Event_Prod.Identificacion = (?) AND Event_Prod.Fin_Event_Prod IS NOT NULL GROUP BY Event_Prod.Id_Lote, Event_Prod.Codigo_Turno, Marc.Fecha_Ingreso, Marc.Fecha_Salida, T_Empl.Hora_Inicio, T_Empl.Hora_Final, T_Empl.Tiempo_Turno_Minutos, T_Empl.Tiempo_Alimentacion, Event_Prod.Identificacion, Event_Prod.Estandar, Lote.Unidades) SELECT Identificacion, Turno, Ini_Turno, Fin_Turno, Minutos_Turno AS 'Tiempo_Turno (min)', (T_Alimentacion) AS 'Tiempo_Alim', (Marc_Ingreso) AS 'Fecha_Marc_Ingreso', (Marc_Salida) AS 'Fecha_Marc_Salida', (Tiempo_Logueo) AS 'Min_Presencia_Login', (Tiempo_Turno) AS 'Min_Presencia_Turno', SUM(CONVERT(Float,(Minut_Produc))) AS 'Unidades_x_std', SUM(Tot_Unidades) AS 'Unidades_x_Turno' FROM C GROUP BY Identificacion, Turno, Ini_Turno, Fin_Turno, Minutos_Turno, (T_Alimentacion), (Marc_Ingreso), (Marc_Salida), (Tiempo_Logueo), (Tiempo_Turno) ORDER BY Turno", self.Fecha_Inic, self.Fecha_Final, self.Fecha_Inic, self.Fecha_Final, self.Row_Verif_Logueo[1])
            self.Row_Event_P_Dia = COM.Cursor.fetchall()
            COM.Cursor.execute("SELECT Codigo_Mstr_Paro, Codigo_Turno, SUM(DATEDIFF(SS,Ini_Paro_Maq, ISNULL(Fin_Paro_Maq, GETDATE()))/60) AS Tiempo_Paro, COUNT (Codigo_Turno) AS Repeticiones FROM Paros_Maquina WHERE Identificacion = (?) AND Codigo_Mstr_Paro = (?) AND Ini_Paro_Maq >= (?) AND Ini_Paro_Maq <= (?) GROUP BY Codigo_Mstr_Paro, Codigo_Turno", self.Row_Verif_Logueo[1], '102', self.Fecha_Inic, self.Fecha_Final)
            self.Row_Par_Alim_Dia = COM.Cursor.fetchall()                         
            if self.Row_Event_P_Dia != None:
                self.Copy_Turno = 0                
                for self.Reg_Event_P_Dia in self.Row_Event_P_Dia:
                    if self.Reg_Event_P_Dia[1]!= self.Copy_Turno:
                        self.Unidades_x_Stdr = self.Unidades_x_Stdr + float(self.Reg_Event_P_Dia[10])                        
                        self.Unidades_Turno = self.Unidades_Turno + int(self.Reg_Event_P_Dia[11])                        
                        self.Tiempo_Tot_Turno = self.Tiempo_Tot_Turno + int(self.Reg_Event_P_Dia[4])
                        self.Minutos_Presencia = self.Minutos_Presencia + int(self.Reg_Event_P_Dia[9])
                        self.Registr_Min_Pres = self.Reg_Event_P_Dia[9]
                        self.Copy_Turno = self.Reg_Event_P_Dia[1]
                    else:
                        if int(self.Reg_Event_P_Dia[9]) > int(self.Registr_Min_Pres):
                            self.Minutos_Presencia = self.Minutos_Presencia - int(self.Registr_Min_Pres)
                            self.Minutos_Presencia = self.Minutos_Presencia + int(self.Reg_Event_P_Dia[9])
                            self.Registr_Min_Pres = int(self.Reg_Event_P_Dia[9])
                        else:
                            pass
                    
                if self.Row_Par_Alim_Dia != None:
                    self.Contador_Paros_Alim = 0
                    for self.Reg_Tiemp_Alim in self.Row_Par_Alim_Dia:
                        self.Tiempo_Alimen_Dia = self.Tiempo_Alimen_Dia + self.Reg_Tiemp_Alim[2]
                        self.Contador_Paros_Alim = self.Contador_Paros_Alim + 1
                else:
                    pass                    
            else:
                pass
            print ''
            print "Unid_X_STDR: ", self.Unidades_x_Stdr
            print "Tiempo_Turno: ", self.Tiempo_Tot_Turno
            print "Minut_Pesencia: ", self.Minutos_Presencia
            

        if self.Tiempo_Alimen_Dia != 0:
                if self.Tiempo_Tot_Turno >= 480 and self.Tiempo_Tot_Turno < 610:
                    if (self.Tiempo_Alimen_Dia >= 30) or (self.Tiempo_Alimen_Dia < 30 and self.Contador_Paros_Alim > 1):
                        self.Minutos_Presencia = self.Minutos_Presencia - 30                        
                    else:
                        self.Minutos_Presencia = self.Minutos_Presencia - self.Tiempo_Alimen_Dia
                elif self.Tiempo_Tot_Turno >= 610 and self.Tiempo_Tot_Turno < 720:
                    if (self.Tiempo_Alimen_Dia >= 45) or (self.Tiempo_Alimen_Dia < 45 and self.Contador_Paros_Alim > 2):
                        self.Minutos_Presencia = self.Minutos_Presencia - 45
                    else:
                        self.Minutos_Presencia = self.Minutos_Presencia - self.Tiempo_Alimen_Dia
                elif self.Tiempo_Tot_Turno >= 720:
                    if (self.Tiempo_Alimen_Dia >= 60) or (self.Tiempo_Alimen_Dia < 60 and self.Contador_Paros_Alim > 2):
                        self.Minutos_Presencia = self.Minutos_Presencia - 60
                    else:
                        self.Minutos_Presencia = self.Minutos_Presencia - self.Tiempo_Alimen_Dia
                else:
                    pass
        else:
            pass
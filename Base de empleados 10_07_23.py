# Estructura del diccionario y bibliotecas [T]

from datetime import date, time, datetime
import os
import time
import math
BaseD= {}
leg=0

def saf(fecha): #funcion para convertir str a fecha
   FD= datetime.strptime(fecha, '%d/%m/%Y') 
   return FD

def sd(legg): # funcion para sacar cantidad de dias desde el ingreso
    dif1=saf(BaseD[legg][4])
    dif2=(datetime.now()-dif1)
    dif3= (dif2.days)
    return dif3


def sdv(leggg): # funcion para sacar dias de vacaciones
    dif4=sd(leggg)
    dif5=0
    if dif4 < 182:
        op5=(dif4/24)
        dif5=math.floor(op5)
        return dif5
    elif dif4 < 1825:
        dif5=(14)
        return dif5
    elif dif4 < 3650:
        dif5=(21)
        return dif5
    elif dif4 < 7300:
        dif5=(28)
        return dif5
    elif dif4 > 7300:
        dif5=(35)
        return dif5
    
def sa(leg4): # funcion para sacar antiguedad
    dif6= sd(leg4)
    dif7= 0
    if dif6 < 365:
        dif7=0
        return dif7
    else:
        op2= (dif6/365)
        dif7= math.floor(op2)
        return dif7


os.system("cls")

# Estructura de introducion [T]------------------------------------------------------------------

bienv= str("   Buenos dias, bienvenido a su base de datos del personal!")
print(bienv.upper())



# Estructura While [P]-----------------------------------------------------------------------

while 0==0:
    print(
        ''' 
        POR FAVOR SELECCIONE LO QUE DESEA HACER:
        
        [1] MOSTRAR PLANTILLA DEL PERSONAL
        [2] BUSCAR UN EMPLEADO EN PARTICULAR
        [3] LIQUIDACIÓN DE SUELDO
        [4] MOSTRAR DÍAS DE VACACIONES CORRESPONDIENTES AL PERSONAL 
        [5] MOSTRAR EL PERSONAL EN PERIODO DE PRUEBA
        [6] MODIFICAR DATOS DE EMPLEADO
        [7] INGRESAR UN NUEVO EMPLEADO
        
        [0] FINALIZAR PROGRAMA

    ''')
    
    opcion=int(input("   OPCIÓN:"))
   
    
    os.system("cls")
    

# Estructura opcion 1 (mostrar todos los empleados) [T]-------------------------------------------------------------

    if opcion == 1:
        print(" ")
        print('''

        Si desea mostrar la lista de empleados de alta marque [1]
        
        Si desea mostrar la lista historica marque [2]
        
        ''')
        alba=int(input("Opcion: "))
        os.system("cls")
        print(" ")
        
        if alba== 2:
            for clave, valor in BaseD.items():
                print(clave,"-->", valor)
                print(" ")
        elif alba== 1:
            for clave, valor in BaseD.items():
                if BaseD[clave][5] == "ALTA":
                    print(clave,"-->", valor)
                    print(" ")
        else:
            print("LA OPCION INGRESADA NO ES VALIDA")

        print(" ")
        input("INGRESE ENTER PARA CONTINUAR...")
        os.system("cls")

# Estructura opcion 2 (buscar empleado en particular) [T]--------------------------------------------------------

    elif opcion == 2:
        
        busc=int(input("Marque el numero de legajo que desea buscar : "))
        try:
            op1=(sdv(busc))
            print(" ")
            print(f'''
                Empleado: {BaseD[busc][0]}
                N de DNI: {BaseD[busc][1]}
                Estado: {BaseD[busc][5]}
                Sueldo Bruto: ${BaseD[busc][2]}
                Sueldo Neto: ${BaseD[busc][3]} + presentismo (${BaseD[busc][2]*0.1})
                Fecha de ingreso: {BaseD[busc][4]}
                Tiempo en la empresa: {sa(busc)} año(s)
                Dias de vacaciones correspondientes: {math.floor(op1)} día(s)
            ''')
            print(" ")
        except:
            print("Legajo no encontrado o inexistente")      

        print(" ")
        input("INGRESE ENTER PARA CONTINUAR...")
        os.system("cls")
        

# Estructura opcion 3 (liquidacion) [T]-----------------------------------------------------------------

    elif opcion == 3:
        xliq=int(input("Seleccione el legajo del empleado a liquidar el mes: "))
        print(" ")
        try:
            tprest=int(input(f"El empleado {BaseD[xliq][0]} mantuvo el presentismo? SI [1] // NO [2] : "))
            print(" ")
            print("Calculando...")
            time.sleep(2)
            os.system("cls")
            ant1= sa(xliq)
            ant2= (BaseD[xliq][2]*0.03)*ant1
            if tprest==1:
                prest= int(BaseD[xliq][2]*0.1)
            else:
                prest= 0

            
            print(" ")
            print(f'''
            ____________________________________________________________________________________________
            |  Empleado {BaseD[xliq][0]}, numero de DNI: {BaseD[xliq][1]}:              Legajo: {xliq}   
            |____________________________________________________________________________________________
            |  Fecha de ingreso: {BaseD[xliq][4]}                                  Antiguedad: {ant1} Año(s)                 
            |____________________________________________________________________________________________
            |  Concepto:           |  Porcentaje: | Remunerativo:  | No remunerativo:  | Descuentos:     
            |______________________|______________|________________|___________________|_________________
            |  
            |  Sueldo basico:               100%            {BaseD[xliq][2]}
            |  Presentismo:                  10%            {prest}
            |  Antiguedad:              (x/a) 3%            {ant2}
            |  Jubilacion:                  -11%                                                {int(BaseD[xliq][2]*0.11)}
            |  Sindicato:                    -2%                                                {int(BaseD[xliq][2]*0.02)}
            |  INSSJP:                       -3%                                                {int(BaseD[xliq][2]*0.03)}
            |  O.S.:                         -3%                                                {int(BaseD[xliq][2]*0.03)}
            |_____________________________________________________________________________________________
            |  Sub total:                                   {BaseD[xliq][2]+prest+ant2}                              {int(BaseD[xliq][2]*0.19)}
            |  Total:                                                                           {(BaseD[xliq][2]*0.81)+prest+ant2}
            |_____________________________________________________________________________________________


            ''')
        except:
            print("Legajo no encontrado o inexistente")  

        print(" ")
        input("INGRESE ENTER PARA CONTINUAR...")
        os.system("cls")




# Estructura opcion 4 (mostrar dias de vacaciones) [T]-------------------------------------------------------------
    elif opcion == 4:
        for clave in BaseD.keys():
            if BaseD[clave][5] == "ALTA":
                print(f" Leg: {clave} - {BaseD[clave][0]:30} corresponden {sdv(clave):2} día(s)")
                print(" ")


        print(" ")
        input("INGRESE ENTER PARA CONTINUAR...")
        os.system("cls")


# Estructura opcion 5 (empleado en pp) [I]------------------------------------------------------

    elif opcion == 5:
     
        print(" ")
        for clave in BaseD.keys():
            op3= sd(clave)
            if op3 < 91 and BaseD[clave][5] == "ALTA":
                dr=90-op3
                print(f" Leg: {clave} - {BaseD[clave][0]:30}  DNI: {BaseD[clave][1]:9}, se encuentra en periodo de prueba por {dr} día(s) mas")
                print(" ")


        print(" ")
        input("INGRESE ENTER PARA CONTINUAR...")
        os.system("cls")
               

# Estructura opcion 6 (modificar datos) [T]--------------------------------------------------------

    elif opcion == 6:
        
        busc=int(input("Marque el numero de legajo que desea modificar : "))
        try:    
            op1=(sdv(busc))
            print(" ")
            print(f'''
                [1] Empleado: {BaseD[busc][0]}
                [2] N de DNI: {BaseD[busc][1]}
                [3] Sueldo Bruto: ${BaseD[busc][2]}
                [4] Fecha de ingreso: {BaseD[busc][4]}
                [5] Estado: {BaseD[busc][5]}
                [0] Cancelar operacion
            ''')
            print(" ")      

            opmod=int(input("Marque el dato que desea modificar: "))

            if opmod == 1:
                print(f"Empleado: {BaseD[busc][0]}")
                nomtemp= str(input("Ingrese nuevamente el nombre: "))
                BaseD[busc][0]= nomtemp.title()
                print(" ")
                print("Cambio realizado exitosamente!!")
                print(" ")
            elif opmod == 2: 
                print(f"N de DNI: {BaseD[busc][1]}")
                BaseD[busc][1]= int(input("Ingrese nuevamente el DNI: "))
                print(" ")
                print("Cambio realizado exitosamente!!")
                print(" ")
            
            elif opmod == 3:
                print(f"Sueldo Bruto: ${BaseD[busc][2]}")
                BaseD[busc][2]= int(input("Ingrese nuevamente el sueldo bruto: "))
                print(" ")
                print("Cambio realizado exitosamente!!")
                print(" ")


            elif opmod == 4:
                print(f"Fecha de ingreso: {BaseD[busc][4]}")
                BaseD[busc][4]= str(input("Ingrese nuevamente la fecha de ingreso: "))
                print(" ")
                print("Cambio realizado exitosamente!!")
                print(" ")


            elif opmod == 5:
                print(" ")
                print(f"El empleado {BaseD[busc][0]} ha sido dado de baja exitosamente!")
                BaseD[busc][5]= str("BAJA")
                print(" ")

            elif opmod == 0:
                print("")

            else:
                print("LA OPCION INGRESADA NO ES CORRECTA")
        except:
            print("Legajo no encontrado o inexistente") 

        print(" ")
        input("INGRESE ENTER PARA CONTINUAR...")
        os.system("cls")

# Estructura opcion 7 (nuevo empleado) [T] !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    elif opcion == 7:
        
        print(" ")
        leg+=1
        print("El numero de legajo correspondiente al nuevo empleado es: ", leg)
        print(" ")
        name= str(input("Apellido y Nombre: "))
        
        dni= int(input("DNI: "))
        
        salb= int(input("Sueldo bruto: "))
        
        saln= int(salb *0.81)
        
        fis= str(input("Ingresar fecha de ingreso de la siguiente manera (DD/MM/YYYY): "))
        est= str("ALTA")

        BaseD.update({leg:[name.title(), dni, salb, saln, fis, est]})
        print("Los datos ingresados son los siguientes: ", "N° de legajo: ", leg, BaseD[leg])
        print(" ")
        print("Considerando que el sueldo neto s/presentismo ni antiguedad es :", BaseD[leg][3])
        
        print(" ")
        input("INGRESE ENTER PARA CONTINUAR...")
        os.system("cls")


# Estructura opcion 0 [T]-----------------------------------------------------------------------------------------


    elif opcion == 0:
        break

# Estructura opcion invalida [T]--------------------------------------------------------------------------------
    else:
        print(" ")
        print("     LA OPCION INGRESADA NO ES VÁLIDA")
        print(" ")
        input("INGRESE ENTER PARA CONTINUAR...")
        os.system("cls")


print(
    '''
         FINALIZANDO PROGRAMA...
             QUE TENGA BUENOS DÍAS!!
    ''' 
    )

input("INGRESE ENTER PARA SALIR...")
os.system("cls")



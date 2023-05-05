from class_viajero_frec import Viajero
import csv

if __name__=='__main__':
       
        DatosViajeros= []  #inicializar lista vacia
        with open("datos_de_viajeros.csv") as archivo:
                reader = csv.reader(archivo, delimiter=',')
                for fila in reader:
                        unViajero= Viajero(fila[0], fila[1], fila[2], fila[3], int(fila[4]))
                        DatosViajeros.append(unViajero)
        
        #millasRecorridas= input('Ingrese cantidad de millas recorridas: ')
        #unViajero.acumularMillas(millasRecorridas)
        #acumuladas= int(unViajero.acumularMillas(millasRecorridas))
        #millasACanjear= int(input('Ingrese la cantidad de millas que desea canjear: '))
        #print(f'{millasACanjear} millas a canjear')
        #print(f'{acumuladas} millas a acumuladas')
        #unViajero.canjearMillas__le__(millasACanjear, acumuladas)

        print(f"--- MENU: ---")
        print(f"[1]. Consultar cantidad de millas")
        print(f"[2]. Acumluar millas")
        print(f"[3]. Canjear millas")
        print(f"[0]. Salir")
        opcion= int(input("Ingrese el numero de opción que desea: "))
        
        while opcion != 0:
                if opcion == 1:
                        for i in range(len(DatosViajeros)):   #PARA ITERAR TODOS LOS ELEMENTOS DE LA LISTA
                         print(f'La cantidad de millas son: {DatosViajeros[i].getMillas}')
                elif opcion == 2: 
                        millasRecorridas= int (input('Ingrese cantidad de millas recorridas: '))
                        DatosViajeros[i].acumularMillas(millasRecorridas)
                        acumuladas= int(DatosViajeros[i].acumularMillas(millasRecorridas))
                elif opcion == 3: 
                        millasACanjear= int(input('Ingrese la cantidad de millas que desea canjear: '))
                        DatosViajeros[i].canjearMillas__le__(millasACanjear, acumuladas)
                opcion= int(input("Ingrese el numero de opción que desea: "))

        
         
        


             
       




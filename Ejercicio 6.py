import csv
class ViajeroFrecuente:
    __Numero = 0
    __DNI = 0
    __Nombre = ''
    __Apellido = ''
    __MillasAcum = 0.0
    
    def __init__(self,num,dni,nom,apell,millas):
        self.__Numero = num
        self.__DNI = dni
        self.__Nombre = nom 
        self.__Apellido = apell 
        self.__MillasAcum = millas
    
    
    def __gt__(self,otro):
        return self.__MillasAcum > otro.__MillasAcum
        
    
    def __add__(self,millas):
        return self.__MillasAcum + millas
    
    def __sub__(self,canje):
        return self.__MillasAcum - canje
    
    def __str__(self):
        return 'Nombre:{}\nApelido:{}\nMillas: {}'.format(self.__Nombre,self.__Apellido,self.__MillasAcum)
    
    
    def totalMillas(self):
        return self.__MillasAcum
    
    def numero(self):
        return self.__Numero
    


if __name__ == '__main__':
    
    viajeros = None
    archivo = open('ViajeroFracuente')
    reader = csv.reaer(archivo,delimiter =';')
    
    for fila in reader:
        unViajero = ViajeroFrecuente(fila[0], fila[1], fila[2], fila[3], fila[4])
        viajeros.append(unViajero)
        
    
    archivo.close()
    
    
    print('--------Viajeros con mas millas---------')
    
    for i in range(len(viajeros)):       
        if viajeros[i] > viajeros[i+1]:
            mill = viajeros[i].totalMillas()
            
    for i in range(len(viajeros)):
        if mill == viajeros[i].totalMillas():
            print(viajeros[i])
    
    
    print('--------Acumular millas------------------')
    
    num = int(input('Ingrese el numero del viajero'))
    ban = False
    i=0
    while ban == False:
        if num == viajeros[i].numero():
            ban = True 
        else:
            i=i+1
    
    millas = float(input('Ingrese la nueva cantidad de millas: '))
    viajeros[i] = viajeros[i] + millas
    
    
    print('--------Canjear millas------------------')
    
    num = int(input('Ingrese el numero del viajero'))
    ban = False
    i=0
    while ban == False:
        if num == viajeros[i].numero():
            ban = True 
        else:
            i=i+1
   
    canjear = float(input('Ingrese la nueva cantidad de millas a canjear: '))
    if viajeros[i].totalMillas() >= canjear:
        viajeros[i] = viajeros[i] - canjear
        print('Canje realizado. Nuevas millas: {}'.format(viajeros[i].totalMillas()))
    else:
        print('No se puede canjear')
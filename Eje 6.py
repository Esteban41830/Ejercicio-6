import  csv
class ViajeroFrecuente:
    __NumeroViajero = 0
    __DNI = 0
    __Nombre = ''
    __Apellido = ''
    __MillasAcum = 0.0
    
    def __init__(self, NumeroViajero, DNI, Nombre, Apellido, MillasAcum):
      self.__NumeroViajero = NumeroViajero
      self.__DNI = DNI
      self.__Nombre = Nombre
      self.__Apellido = Apellido
      self.__MillasAcum = float(MillasAcum)

    def cantidadTotalMillas(self):
        return "Millas acumuladas: {}".format(self.__MillasAcum)
    
    def __gt__(self,otro):
        return self.__MillasAcum > otro.MillasAcum
    
    def Mostrar(self):
        return "El viajero N°{}, Nombre: {}, Apellido: {}, acumulo mas millas".format(self.NumeroViajero,
                             self.__Nombre,self.__Apellido)
    
    def __add__(self,millas):
        return self.__MillasAcum + millas

    def __sub__(self,canje):
        return self.__MillasAcum - canje
        
    def canjearMillas(self,canje):
        if self.__MillasAcum < canje:
            print("Error, no se puede canjear")
        else:
            self.__MillasAcum = self.__MillasAcum - canje
            print("Se puede canjear\n\nMillas acumuladas: {}".format(self.__MillasAcum))
        
    

if __name__ == '__main__':

    viajeros = []
    archivo = open("viajerofrecuente.csv")
    reader = csv.reader(archivo,delimiter=",")
    
    for fila in reader:
        viajero = ViajeroFrecuente(fila[0],fila[1],fila[2],fila[3],fila[4])
        viajeros.append(viajero)

    archivo.close()
        
    num = int(input("Ingrese numero del viajero: \n"))
    print("------Cantidad de millas Para un viajero----------\n\n\n")
    
    print(viajeros[num-1].cantidadTotalMillas())
   
    print("------Acumular Millas--------------\n\n\n")
    millas = int(input("Ingrese millas recorridas: "))
    viajeros[num-1] = viajeros[num-1] + millas
 
    print("------Canjear Millas---------------\n\n\n")
    canje = float(input("Ingrese millas a canjear: "))
    viajeros[num-1].CanjearMillas(canje)
            
    print("------El viajero con mas Millas------\n\n\n")
    mayor = 0
    for i in range(len(viajeros)):
        if viajeros[i] > viajeros[i+1]:
            mayor = i
            
    print(viajeros[mayor].Mostrar)
      
        

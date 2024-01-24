class Maquina_expendedora:   #Definimos la clase "Maquina_expendedora".
    def __init__(self):#Definimos las variables de instancia.
        self._Moneda_existente = ["100", "200", "500", "1000"] #Lista que contiene las monedas validas para la maquina.
        self._Dinero_total = 0 #Cuenta del usuario.
        self._Dinero_ingresado = ""#Este es el dinero que sera ingresado y posteriormente pasado a entero (int) para calculos.

        #Diccionario que contiene los productos de la maquina con sus respectivos precios, cantidad, nombre y posicion.
        self._Productos = {"1":{"precio":300,"nombre":"galleta","cantidad":1}, "2":{"precio":1500,"nombre":"papas","cantidad":0},
                           "3":{"precio":1000,"nombre":"gaseosa","cantidad":5},"4":{"precio":500,"nombre":"chocolate","cantidad":10},
                           "5":{"precio":5000,"nombre":"chocorramo","cantidad":10},"6":{"precio":100,"nombre":"mani","cantidad":20}}
        self._Producto_elegido = ""#Producto que eligira el usuario.
        self._Dinero_falta = 0 #Cuenta para operar y conocer el dinero faltante de ser el caso.

    def ingreso_de_dinero(self):  # Aqui el usuario ingresa el dinero
        print("===============================================================================================")
        for key in self._Productos: #Ciclo para recorrer el diccionario y mostrarlos al usuario con sus respectivas caracteristicas.
            print(self._Productos[key]["nombre"],"__","| posicion:",key,"| precio: $", self._Productos[key]["precio"],"| cantidad:",self._Productos[key]["cantidad"],"|")
        print("===============================================================================================")
        #En este punto se le pide al usuario que ingrese las monedas.
        self._Dinero_ingresado = input("Ingrese monedas, solo puede ingresar monedas de 100, 200, 500, 1000, presione F para finalizar:")
        while self._Dinero_ingresado != "F": #Ciclo para que mientras no se presione F se realice la funcion a continuacion.
            #Condicional para saber si la moneda ingresada esta en la lista de monedas.
            if self._Dinero_ingresado in self._Moneda_existente:
                self._Dinero_total += int(self._Dinero_ingresado)#Aqui suma el dinero ingresado por el usuario.
                print("Total ingresado:",self._Dinero_total)#Muestr cuanto lleva a medida que ingresa.
                self._Dinero_ingresado = input("Ingrese monedas, solo puede ingresar monedas de 100, 200, 500, 1000, presione F para finalizar:")#Vuelve y pide mas monedas.
            else:
                print("Valor ingresado incorrecto, se le devolvera el mismo.")#Si la moneda no existe pasara esto.
                self._Dinero_ingresado = input("Ingrese monedas, solo puede ingresar monedas de 100, 200, 500, 1000, presione F para finalizar:")#Pide de nuevo la moneda.
        print("El dinero total ingresado es:", self._Dinero_total)#Muestra la cuenta.

    def producto(self):  # Aqui el usuario dice el producto que desea y el programa le dice si esta disponible y cuantas unidades del mismo quedan
        self._Producto_elegido = input("Ingrese la posicion del producto que desea o presione R para que se le regrese su dinero:")#Pide la posicion del producto que desea al usuario
        #Condicional con el que si se presiona R al elegir el producto entonces se devolvera el dinero.
        if self._Producto_elegido == "R":
            print("Se le devuelven", self._Dinero_total, "pesos")
            self._Dinero_total = 0

        else:

            while self._Producto_elegido not in self._Productos:#Mientras el producto no se encuentre en el diccionario.

                print("El producto ingresado no esta disponible o ha sido escrito de manera erronea.")
                v = input("Ingrese F para escribir nuevamente el producto o Ingrese R para recibir de vuelta su dinero:")
                while (v != "F") and (v != "R"):#Mientras que el valor ingresado sea distinto de "F" o "R".
                    print("Incorrecto")
                    v = input("Ingrese F, para escribir nuevamente el producto. Ingrese R para recibir de vuelta su dinero:")
                if v == "R":#Si el valor ingresado es R se le devuelve el dinero.
                    print("Se le han devuelto", self._Dinero_total,"pesos.")
                    self._Dinero_total = 0
                    break
                self._Producto_elegido = input("Ingrese el producto que desea(todo en minusculas):")

    def compra(self):
        while self._Producto_elegido in self._Productos:#Cuando el producto seleccionado si se encuentra en el diccionario.
            if self._Productos[self._Producto_elegido]["precio"] <= self._Dinero_total:#Condicional: Si el precio del producto elegido es menor o igual al dinero ingresado.
                #Condicional por si el producto esta agotado.
                if self._Productos[self._Producto_elegido]["cantidad"] <= 0:
                    print("El producto se ha agotado")
                    print("se le regresan",self._Dinero_total,"pesos")
                    self._Dinero_total = 0

                else:
                    self._Productos[self._Producto_elegido]["cantidad"] = self._Productos[self._Producto_elegido]["cantidad"] - 1 #Resta 1 la cantidad del producto seleccionado.
                    self._Dinero_total = self._Dinero_total - self._Productos[self._Producto_elegido]["precio"]#Resta a la cuenta del usuario el valor del producto que selecciona.
                    print("Producto entregado","quedan",self._Productos[self._Producto_elegido]["cantidad"],"unidades de",self._Productos[self._Producto_elegido]["nombre"])#Muestra la cantidad de producto que quedo.
                    print("Se han devuelto $",self._Dinero_total)
                    self._Dinero_total = 0
                    #Si se le agota el dinero.
                    if self._Dinero_total == 0:
                        print("Gracias por su compra")
                        break
            #Si el dinero no alcanza entonces...
            else:
                self._Dinero_falta = self._Productos[self._Producto_elegido]["precio"] - self._Dinero_total#Calcula cuanto dinero falta.
                print("Dinero insuficiente, le falta:",self._Dinero_falta,"para",self._Productos[self._Producto_elegido]["nombre"])#Muestra cuanto dinero falta.
                x = input("Ingrese F para ingresar dinero o R para que se le regrese el dinero:")
                while (x!="F") and (x !="R"):#Mientras que no se presione ni "R" o "F"
                    print("Error, ha presionado una tecla incorrecta.")
                    x = input("Ingrese F para ingresar el dinero o R para que se le regrese el dinero:")
                if x == "F":# Si presiona F entonces le volvera a pedir que ingrese dinero
                    self._Dinero_ingresado = ""
                    self._Dinero_ingresado = input("Ingrese monedas, solo puede ingresar monedas de 100, 200, 500, 1000, o presione R para que se le regrese el dinero:")
                    #Cuando el dinero en cuenta es menor que el valor del producto.
                    while self._Dinero_total < self._Productos[self._Producto_elegido]["precio"]:
                        #Empieza a sumar el dinero ingresado si es que se encuentra dentro de la lista.
                        if self._Dinero_ingresado in self._Moneda_existente:
                            self._Dinero_total += int(self._Dinero_ingresado)
                            print("Dinero total:", self._Dinero_total)
                            #Si el valor del producto es menor a la cuenta del usuario.
                            if self._Dinero_total >= self._Productos[self._Producto_elegido]["precio"]:
                                self._Dinero_total = self._Dinero_total - self._Productos[self._Producto_elegido]["precio"]#Resta el valor del producto a la cuenta del usuario.
                                self._Productos[self._Producto_elegido]["cantidad"] = self._Productos[self._Producto_elegido]["cantidad"] - 1#Resta una unidad al producto seleccionado.
                                if self._Dinero_total == 0:# Si no hay mas dinero entonces termina el proceso.
                                    print("Producto entregado","quedan",self._Productos[self._Producto_elegido]["cantidad"],"unidades de",self._Productos[self._Producto_elegido]["nombre"])
                                    print("Gracias por su compra")
                                    break
                                if self._Dinero_total > 0:#Si hay dinero entonces se le devuelve el valor en la cuenta.
                                    print("Se le han regresado", self._Dinero_total,"de devuelta y se ha entregado:", self._Productos[self._Producto_elegido]["nombre"])
                                    print("Gracias por su compra")
                                    self._Dinero_total = 0
                                    break
                            else:
                                self._Dinero_ingresado = input("Ingrese monedas, solo puede ingresar monedas de 100, 200, 500, 1000, o presione R para que se le regrese el dinero:")
                        elif self._Dinero_ingresado == "R":#Si presiona R se le devolvera el dinero que le resta.
                            print("Se le devuelven",self._Dinero_total,"pesos")
                            self._Dinero_total = 0
                            break
                        else:#Si ingresa un valor erroneo entonces se le devuelve el dinero y pedira de nuevo que ingrese mas dinero.
                            print("Valor ingresado incorrecto, se le devolvera el mismo.")
                            self._Dinero_ingresado = input("Ingrese monedas, solo puede ingresar monedas de 100, 200, 500, 1000, o presione R para que se le regrese el dinero:")
                if x == "R":
                    print("Se han devuelto los $", self._Dinero_total, "ingresados")#Devuelve el dinero de la cuenta.

            break



if __name__ == '__main__':
    me = Maquina_expendedora()
    while True:
        me.ingreso_de_dinero()
        me.producto()
        me.compra()
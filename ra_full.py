class Nodo:
    def __init__(self, item: int):
        self.item = item
        self.siguiente = None
        self.anterior = None


class doubleList:
    def __init__(self):
        self.root = None

    def insertar_lista_vacia(self, data: int):
        if self.root is None:
            nuevo_nodo = Nodo(data)
            self.root = nuevo_nodo
        else:
            print("La lista no esta vacia")

    def insertar_inicio(self, data: int):
        if self.root is None:
            self.insertar_lista_vacia(data)
            return
        else:
            nuevo_nodo = Nodo(data)
            nuevo_nodo.siguiente = self.root
            self.root.anterior = nuevo_nodo
            self.root = nuevo_nodo

    def insetar_final(self, data: int):
        if self.root is None:
            nuevo_nodo = Nodo(data)
            self.root = nuevo_nodo
            return
        apuntador = self.root
        while apuntador.siguiente is not None:
            apuntador = apuntador.siguiente
        nuevo_nodo = Nodo(data)
        apuntador.siguiente = nuevo_nodo
        nuevo_nodo.anterior = apuntador

    def insertar_despues_elemento(self, x, data):
        if self.root is None:
            print("La lista esta vacia")
        else:
            apuntador = self.root
            while apuntador is not None:
                if apuntador.item == x:
                    break
                apuntador = apuntador.siguiente
            if apuntador is None:
                print("El elemento no se encuentra en la lista")
            else:
                nuevo_nodo = Nodo(data)
                nuevo_nodo.anterior = apuntador
                nuevo_nodo.siguiente = apuntador.siguiente
                if apuntador.siguiente is not None:
                    apuntador.siguiente.anterior = nuevo_nodo
                apuntador.siguiente = nuevo_nodo

    def insertar_antes_elemento(self, x, data):
        if self.root is None:
            print("La lista esta vacia")
        else:
            apuntador = self.root
            while apuntador is not None:
                if apuntador.item == x:
                    break
                apuntador = apuntador.siguiente
            if apuntador is None:
                print("El elemento no se encuentra en la lista")
            else:
                nuevo_nodo = Nodo(data)
                nuevo_nodo.siguiente = apuntador
                nuevo_nodo.anterior = apuntador.anterior
                if apuntador.anterior is not None:
                    apuntador.anterior.siguiente = nuevo_nodo
                apuntador.anterior = nuevo_nodo

    def buscar_elemento(self, x):
        if self.root is None:
            print("La lista está vacía")
            return
        apuntador = self.root
        encontrado = False
        while apuntador is not None:
            if apuntador.item == x:
                encontrado = True
                break
            apuntador = apuntador.siguiente
        if encontrado:
            print(f"El elemento {x} se encuentra en la lista.")
        else:
            print(f"El elemento {x} no se encuentra en la lista.")

    def navegar_lista(self):
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            apuntador = self.root
            while apuntador is not None:
                print(apuntador.item, " ")
                apuntador = apuntador.siguiente

    def eliminar_inicio(self):
        if self.root is None:
            print("La lista no contiene Nodos para eliminar")
            return
        if self.root.siguiente is None:
            self.root = None
        self.root = self.root.siguiente
        self.root.anterior = None

    def eliminar_final(self):
        if self.root is None:
            print("La lista no contiene Nodos para eliminar")
            return
        if self.root.siguiente is None:
            self.root = None
            return
        apuntador = self.root
        while apuntador.siguiente is not None:
            apuntador = apuntador.siguiente
        apuntador.anterior.siguiente = None

    def eliminar_elemento(self, x):
        if self.root is None:
            print("La lista esta vacia")
            return
        if self.root.siguiente is None:
            if self.root.item == x:
                self.root = None
            else:
                print("Elemento no encontrado")
        if self.root.item == x:
            self.eliminar_inicio()
            return
        apuntador = self.root
        while apuntador.siguiente is not None:
            if apuntador.item == x:
                break
            apuntador = apuntador.siguiente
        if apuntador.siguiente is not None:
            apuntador.anterior.siguiente = apuntador.siguiente
            apuntador.siguiente.anterior = apuntador.anterior
        else:
            if apuntador.item == x:
                self.eliminar_final()
            else:
                return print("Elemento no encontrado")


MSG: str = """
1. Lista Simple
2. Lista Doblemente Ligada
0. Salir
¿Qué opción desea?
"""
MSG_LIST = """
1. Inserción
2. Búsqueda
3. Eliminación
4. Consultar
5. Regresar al menú principal.
¿Qué opción desea?
"""
MSG_LIST_DOUBLE = """
1. insertar al inicio
2. insertar al final
3. insertar despues de un elemento
4. insertar antes de un elemento
"""
MSG_LIST_DOUBLE_DEL = """
1. eliminar al inicio
2. eliminar al final
3. eliminar elemento
"""

print("MENU PRINCIPAL".center(30, "="))
print(MSG)
opcion: int = int(input())
while opcion != 0:
    if opcion == 1:
        print("Has elegido la opción 1. Listas Simple".center(60, ":"))
        print(MSG_LIST)
        opc_list = int(input("Ingresa la opción: "))
        lista1 = []  # LISTA PARA INSERCION NO BORRAR
        while opc_list != 5:
            if opc_list == 1:
                dat1 = int(input("Ingrese un dato entero a la lista: "))
                lista1.append(dat1)
                print("\nDato '{}' insertado en la lista.".format(dat1))
            elif opc_list == 2:
                print("En lista simple opc2")
                buscar1=int(input("Ingresa un número entero que desees buscar:"))
                BUS=(buscar1 in lista1)
                if BUS == True:
                    print(f"El número {buscar1} está en la lista." )
                else:
                    print(f"El número {buscar1} no está en la lista.")
            elif opc_list == 3:
                while True:
                    print("Eliminar un dato (A)")
                    print("Eliminar el ultimo dato (B)")
                    op = input("Eliga una opcion: \n")
                    if op.lower() == "a":
                        bdt = int(
                            input("Que dato desea eliminar de la lista: "))
                        print(f"Dato {bdt} eliminado de la lista \n")
                        lista1.remove(bdt)
                        break
                    elif op.lower() == "b":
                        lista1.pop()
                        break
                    else:
                        print("Solo puede ingresar (A/B)")
            elif opc_list == 4:
                print("En lista simple opc4")
            print("Has elegido la opción 1. Listas Simple".center(60, ":"))
            print(MSG_LIST)
            opc_list = int(input("Ingresa la opción: "))
    elif opcion == 2:
        print("Has elegido la opción 2. Lista Doblemente Ligada".center(70, ":"))
        print(MSG_LIST)
        opc_list = int(input("Ingresa la opción: "))
        nueva_listd = doubleList()
        while opc_list != 5:
            if opc_list == 1:
                if nueva_listd.root is None:
                    valor_in = int(input("Ingresa un valor: "))
                    nueva_listd.insertar_lista_vacia(valor_in)
                else:
                    print(MSG_LIST_DOUBLE)
                    opc_in_list = int(input("Ingres la opcion: "))
                    if opc_in_list == 1:
                        valor_in = int(input("Ingresa un valor: "))
                        nueva_listd.insertar_inicio(valor_in)
                    elif opc_in_list == 2:
                        valor_in = int(input("Ingresa un valor: "))
                        nueva_listd.insetar_final(valor_in)
                    elif opc_in_list == 3:
                        valor_desp = int(
                            input("Ingresa el elemento de la lista: "))
                        valor_in = int(input("Ingresa un valor: "))
                        nueva_listd.insertar_despues_elemento(
                            valor_desp, valor_in)
                    elif opc_in_list == 4:
                        valor_antes = int(
                            input("Ingresa el elemento de la lista: "))
                        valor_in = int(input("Ingresa un valor: "))
                        nueva_listd.insertar_antes_elemento(
                            valor_antes, valor_in)
            elif opc_list == 2:
                valor_buscar = int(input("Ingresa el elemento a buscar: "))
                nueva_listd.buscar_elemento(valor_buscar)
            elif opc_list == 3:
                print(MSG_LIST_DOUBLE_DEL)
                opc_del_list = int(input("Ingres la opcion: "))
                if opc_del_list == 1:
                    nueva_listd.eliminar_inicio()
                elif opc_del_list == 2:
                    nueva_listd.eliminar_final()
                elif opc_del_list == 3:
                    item_del = int(input("Ingresa el elemento a eliminar: "))
                    nueva_listd.eliminar_elemento(item_del)
            elif opc_list == 4:
                nueva_listd.navegar_lista()
            print("Has elegido la opción 2. Lista Doblemente Ligada".center(70, ":"))
            print(MSG_LIST)
            opc_list = int(input("Ingresa la opción: "))
    print("MENU PRINCIPAL".center(30, "="))
    print(MSG)
    opcion: int = int(input())

class Proyecto:
    def __init__(self,SD,DL,user,desc):
        self.StartDate = SD
        self.Deadline = DL
        self.name= user
        self.description = desc
        self.siguiente = None


class User:
        def __init__(self,nam,passw,mail,proAso,cod):
            self.name=nam
            self.password=passw
            self.email=mail
            self.proyectosAsociados= proAso
            self.codigo = cod
            self.izquierda = None
            self.derecha = None


class ListaSE:
    def __init__(self):
        self.cabeza = None
        
    def IndicarVacia(self):
        if self.cabeza is None:
            return True
        else:
            return False
        
    def ContarElementos(self):
        actualNodo = self.cabeza
        contador = 0
        while actualNodo != None:
            contador +=1
            actualNodo = actualNodo.siguiente
        return contador
    
    def ImprimirElementos(self):
        pass
        
    def BuscarNombre(self,nomb):
        nActual = self.cabeza #valor observado
        buscando = True
        while buscando:
            if nActual.name == nomb: #si el nodo observado tiene valor igual al vab
                buscando = False
                return True
            else:
                if nActual.siguiente is None: #si el valor no es igual, se revisa si el nodo apunt a un nodo distinto
                    buscando = False
                    return False
                else:
                    nActual = nActual.siguiente # si sí tiene nodo siguiente, se observa el próximo nodo
                    
                    
class ListaProyectos(ListaSE):
    def AgregarInicio(self, proyect):
        nProyecto = proyect
        
        if self.cabeza is None:
            self.cabeza = nProyecto
            return
        else:
            nProyecto.siguiente = self.cabeza
            self.cabeza = nProyecto
            
    def ImprimirElementos(self):
        actualProyecto = self.cabeza
        while(actualProyecto):
            print(actualProyecto.StartDate)
            print(actualProyecto.Deadline)
            print(actualProyecto.name)
            print(actualProyecto.description)
            actualProyecto = actualProyecto.siguiente

class Arbol:
    # Funciones privadas
     
    def __init__(self, usuario):
        self.raiz = usuario

    def __agregar_recursivo(self, nodo, usuario):
        if usuario.codigo < nodo.codigo:
            if nodo.izquierda is None:
                nodo.izquierda = usuario
            else:
                self.__agregar_recursivo(nodo.izquierda, usuario)
        else:
            if nodo.derecha is None:
                nodo.derecha = usuario
            else:
                self.__agregar_recursivo(nodo.derecha, usuario)

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print(nodo.name, "/" , nodo.password, "/", nodo.email)
            if nodo.proyectosAsociados != None:
                nodo.proyectosAsociados.ImprimirElementos()
            self.__inorden_recursivo(nodo.derecha)

    def __preorden_recursivo(self, nodo):
        if nodo is not None:

            print(nodo.name)
            print(nodo.password)
            print(nodo.email)
            nodo.proyectosAsociados.ImprimirElementos()
            self.__preorden_recursivo(nodo.izquierda)
            self.__preorden_recursivo(nodo.derecha)

    def __postorden_recursivo(self, nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierda)
        
            self.__postorden_recursivo(nodo.derecha)
            print(nodo.dato, end=", ")

    def __buscar(self, nodo, codigo):
        if nodo is None:
            return None
        if nodo.codigo == codigo:
            return nodo
        if codigo < nodo.codigo:
            return self.__buscar(nodo.izquierda, codigo)
        else:
            return self.__buscar(nodo.derecha, codigo)
        
    def eliminarInorden(self, nodo, codigo):
        
        nodoPorEliminar = self.__buscar(self.raiz, codigo)
        
        if nodoPorEliminar.izquierda is None and nodoPorEliminar.derecha is None:
             nodoPorEliminar = None
        
        elif nodoPorEliminar.izquierda is not None and nodoPorEliminar.derecha is None:
            nodoPorEliminar = nodoPorEliminar.izquierda
            
        elif nodoPorEliminar.izquierda is  None and nodoPorEliminar.derecha is not  None:
            print("") 
        elif nodoPorEliminar.izquierda is not None and nodoPorEliminar.derecha is not  None:
            print("")
        if nodo is None:
            return nodo

        # Recorrer el subárbol izquierdo
        nodo.left = self.EliminarInorden(nodo.left, nomb)

        # Si el nombre coincide con el nombre del nodo actual, eliminarlo
        if nodo.name == nomb:
        # Caso 1: Nodo sin hijos o con un solo hijo
            if nodo.left is None:
             temp = nodo.right
             nodo = None
             return temp
            elif nodo.right is None:
                temp = nodo.left
                nodo = None
                return temp

        # Caso 2: Nodo con dos hijos
        # Encontrar el sucesor inmediato (el nodo más pequeño en el subárbol derecho)
        temp = self.EncontrarMinimo(nodo.right)

        # Copiar el valor del sucesor inmediato al nodo que se eliminará
        nodo.name = temp.name

        # Eliminar el sucesor inmediato
        nodo.right = self.EliminarInorden(nodo.right, temp.name)

        # Recorrer el subárbol derecho
        nodo.right = self.EliminarInorden(nodo.right, nomb)

        return nodo

    def EncontrarMinimo(self, nodo):
        current = nodo
        while current.left is not None:
            current = current.left
        return current

    # Funciones públicas

    def agregar(self, usuario):
        self.__agregar_recursivo(self.raiz, usuario)

    def inorden(self):
        print("Imprimiendo lista de usuarios en inorden: ")
        self.__inorden_recursivo(self.raiz)
        print("")

    def preorden(self):
        print("Imprimiendo árbol preorden: ")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol postorden: ")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, codigo):
        return self.__buscar(self.raiz, codigo)
    
    


##Zona de Pruebas
usuario1 = User("Juan", "k123", "asomfo@gmail.com", None, 3 )
usuario2 = User("Paolo", "k123", "asomfo@gmail.com", None, 1 )
usuario3 = User("Manuel", "k123", "asomfo@gmail.com", None, 7 )

arbolPrueba = Arbol(usuario1)
arbolPrueba.agregar(usuario2)
arbolPrueba.agregar(usuario3)
arbolPrueba.inorden()

print(arbolPrueba.buscar(7).name)
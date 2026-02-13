# servicios/inventario.py

from modelos.producto import Producto

class Inventario:
    """
    Clase encargada de gestionar los productos.
    Utiliza una lista como estructura principal de almacenamiento.
    """

    def __init__(self):
        # Lista donde se almacenarán los objetos Producto
        self.productos = []

    # ==============================
    # Añadir producto
    # ==============================
    def agregar_producto(self, id_producto, nombre, cantidad, precio):

        # Validamos que el ID no esté repetido
        for producto in self.productos:
            if producto.get_id() == id_producto:
                print("Error: Ya existe un producto con ese ID.")
                return

        # Si no existe, se crea y se agrega
        nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        print("Producto agregado correctamente.")

    # ==============================
    # Eliminar producto por ID
    # ==============================
    def eliminar_producto(self, id_producto):

        for producto in self.productos:
            if producto.get_id() == id_producto:
                self.productos.remove(producto)
                print("Producto eliminado correctamente.")
                return

        print("Producto no encontrado.")

    # ==============================
    # Actualizar producto
    # ==============================
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):

        for producto in self.productos:
            if producto.get_id() == id_producto:

                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)

                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)

                print("Producto actualizado correctamente.")
                return

        print("Producto no encontrado.")

    # ==============================
    # Buscar por nombre (coincidencia parcial)
    # ==============================
    def buscar_producto(self, nombre):

        encontrados = []

        for producto in self.productos:
            # lower() permite búsqueda sin importar mayúsculas
            if nombre.lower() in producto.get_nombre().lower():
                encontrados.append(producto)

        return encontrados

    # ==============================
    # Mostrar todos los productos
    # ==============================
    def mostrar_inventario(self):

        if not self.productos:
            print("El inventario está vacío.")
            return

        for producto in self.productos:
            print(producto)

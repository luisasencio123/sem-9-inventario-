class Producto:
    """
    Clase Producto

    Esta clase representa la entidad principal del sistema de inventarios.
    Cada objeto de esta clase corresponde a un producto almacenado en la tienda.

    Se aplica el principio de ENCAPSULAMIENTO, ya que los atributos se
    declaran como privados (usando doble guion bajo __) para evitar que
    sean modificados directamente desde fuera de la clase.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor de la clase.

        Se ejecuta automáticamente cuando se crea un nuevo objeto Producto.
        Inicializa los atributos del producto con los valores recibidos.
        """

        # Atributos privados
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # ==============================
    # MÉTODOS GETTERS
    # Permiten acceder a los atributos privados
    # ==============================

    def get_id(self):
        """Devuelve el ID del producto."""
        return self.__id

    def get_nombre(self):
        """Devuelve el nombre del producto."""
        return self.__nombre

    def get_cantidad(self):
        """Devuelve la cantidad disponible del producto."""
        return self.__cantidad

    def get_precio(self):
        """Devuelve el precio del producto."""
        return self.__precio

    # ==============================
    # MÉTODOS SETTERS
    # Permiten modificar atributos de forma controlada
    # ==============================

    def set_cantidad(self, cantidad):
        """
        Actualiza la cantidad del producto.
        Se podría añadir validación para evitar valores negativos.
        """
        self.__cantidad = cantidad

    def set_precio(self, precio):
        """
        Actualiza el precio del producto.
        Se podría añadir validación para evitar valores negativos.
        """
        self.__precio = precio

    # ==============================
    # MÉTODO ESPECIAL
    # ==============================

    def __str__(self):
        """
        Método especial que define cómo se mostrará el objeto
        cuando se imprima en pantalla con print().
        """
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"

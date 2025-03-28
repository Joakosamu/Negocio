class Almacenista():
    def __init__(self):
        pass

    def print_inventory(self):
        data = pandas.read_csv("./inventario.csv")
        print("Aquí está el inventario actual.")
        print(data)
        print("\n\n")


    def add_item(self):
        codigo = input("¿Cuál es el código del producto?\n")
        descripcion = input("Escribe una descripcion corta del producto:\n")
        precio = input("¿Cuál es el precio unitario del producto?\n")
        maximo = input("¿Cuál es el máximo número de piezas que tendrías?\n")
        minimo = input("¿Cuál es el mínimo? Cuando el producto alcance el mínimo se generará una orden de compra.\n")
        clasificacion = input("¿Qué clasificación tendrá? P. ej. cuchillos, refrigeracion, coccion, etc.\n")
        proveedor = input("¿Quién es el proveedor? P. ej. Importadora Raza, Torrey, Victorinox, etc.\n")

        with open("inventario.csv", mode="a") as file:
            file.write(f"\n{codigo},{descripcion},{precio},{maximo},{minimo},{clasificacion},{proveedor},0")

        print("El artículo ha sido registrado en el inventario.\n\n")


    def enter_merchandise(self):
        print("Ingreso de mercancía")
        add_to_codigo = input("Ingresa el código del producto:\n")
        quantity = int(input("Ingresa el número de piezas a añadir:\n"))
        data = pandas.read_csv("./inventario.csv")
        cantidad_actual = (data.loc[data["codigo"] == add_to_codigo, "existencias"].iloc[0])
        nueva_cantidad = cantidad_actual + quantity
        data.loc[data["codigo"] == add_to_codigo, "existencias"] = nueva_cantidad
        data.to_csv("./inventario.csv", index=False)
        print("La mercancía ha entrado al inventario.\n\n")


    def release_merchandise(self):
        print("Salida de mercancía")
        substract_to_codigo = input("Ingresa el código del producto:\n")
        minus_quantity = int(input("Ingresa el número de piezas que saldrán:\n"))
        data = pandas.read_csv("./inventario.csv")
        cantidad_actual = (data.loc[data["codigo"] == substract_to_codigo, "existencias"].iloc[0])
        nueva_cantidad = cantidad_actual - minus_quantity
        data.loc[data["codigo"] == substract_to_codigo, "existencias"] = nueva_cantidad
        data.to_csv("./inventario.csv", index=False)
        print("La mercancía ha salido del inventario.\n\n")
        self.check_minimum(substract_to_codigo, data, nueva_cantidad)

    def check_minimum(self, code, data, new_quantity):
        minimo = int(data.loc[data["codigo"] == code, "minimo"].iloc[0])
        if new_quantity <= minimo:
            print("Es hora de pedir más de este producto\n\n")
            description = data.loc[data["codigo"] == code, "descripcion"].iloc[0]
            maximo = int(data.loc[data["codigo"] == code, "maximo"].iloc[0])
            pedido = maximo - new_quantity

            with open("./ordendecompra.csv", mode="a") as file:
                file.write(f"\n{code},{description},{pedido}")

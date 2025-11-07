# --- Subsistemas ---
class Inventario:
    def __init__(self):
        # Simulamos un inventario de productos
        self.productos = {
            "A123": {"nombre": "Laptop", "precio": 1200, "stock": 5},
            "B456": {"nombre": "Mouse", "precio": 25, "stock": 20},
            "C789": {"nombre": "Teclado", "precio": 45, "stock": 10}
        }

    def mostrar_productos(self):
        print("\nProductos disponibles:")
        for pid, info in self.productos.items():
            print(f"  {pid}: {info['nombre']} - ${info['precio']} (Stock: {info['stock']})")

    def verificar_stock(self, producto_id, cantidad):
        producto = self.productos.get(producto_id)
        if not producto:
            print("Producto no encontrado.")
            return False
        if producto["stock"] < cantidad:
            print("No hay suficiente stock disponible.")
            return False
        return True

    def reducir_stock(self, producto_id, cantidad):
        self.productos[producto_id]["stock"] -= cantidad
        print(f"Stock actualizado: {self.productos[producto_id]['stock']} unidades restantes.")

class Pagos:
    def procesar_pago(self, metodo, monto):
        print(f"\nProcesando pago de ${monto:.2f} usando {metodo}...")
        if metodo.lower() not in ["tarjeta", "paypal"]:
            print("Método de pago no aceptado.")
            return False
        print("Pago aprobado.")
        return True

class Envio:
    def calcular_envio(self, direccion):
        print(f"\nCalculando envío para {direccion}...")
        return 15.0  # costo fijo de envío

    def generar_guia(self, direccion):
        print(f"Generando guía de envío para {direccion}...")
        return "GUIA-" + str(hash(direccion))[-6:]

# --- Facade ---
class EcommerceFacade:
    def __init__(self):
        self.inventario = Inventario()
        self.pagos = Pagos()
        self.envio = Envio()

    def realizar_compra(self):
        print("\n=== 🛍 Bienvenido al sistema de compras ===")
        self.inventario.mostrar_productos()

        producto_id = input("\nIngrese el ID del producto que desea comprar: ").strip().upper()
        cantidad = int(input("Cantidad: "))

        if not self.inventario.verificar_stock(producto_id, cantidad):
            return

        metodo_pago = input("Método de pago (Tarjeta/PayPal): ").strip()
        direccion = input("Dirección de envío: ").strip()

        # Calcular total
        producto = self.inventario.productos[producto_id]
        costo_envio = self.envio.calcular_envio(direccion)
        total = producto["precio"] * cantidad + costo_envio
        print(f"\nTotal a pagar: ${total:.2f} (Producto + Envío)")

        # Procesar pago
        if not self.pagos.procesar_pago(metodo_pago, total):
            print("Compra cancelada por error de pago.")
            return

        # Confirmar compra
        self.inventario.reducir_stock(producto_id, cantidad)
        guia = self.envio.generar_guia(direccion)
        print(f"\n¡Compra completada con éxito!")
        print(f"📄 Guía de envío: {guia}")
        print("=========================================\n")

# --- Ejecución ---
if __name__ == "__main__":
    sistema = EcommerceFacade()
    while True:
        sistema.realizar_compra()
        otra = input("¿Desea realizar otra compra? (s/n): ").strip().lower()
        if otra != "s":
            print("\nGracias por usar el sistema de compras. ¡Hasta luego!")
            break

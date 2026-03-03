from cons import Cons
from cuenta_bancaria import CuentaBancaria


class Dawbank:
    iban: str = ""
    titular: str = ""
    cuenta: CuentaBancaria = CuentaBancaria(iban, titular)

    def imprimir_menu(self) -> None:
        print("." * Cons.ESTRELLAS_NUM)
        print(f"{Cons.OPCION_DATOS}- Mostrar datos de la cuenta.")
        print(f"{Cons.OPCION_IBAN}- Mostrar IBAN.")
        print(f"{Cons.OPCION_TITULAR}- Mostrar titular.")
        print(f"{Cons.OPCION_SALDO}- Mostrar saldo.")
        print(f"{Cons.OPCION_INGRE}- Ingreso.")
        print(f"{Cons.OPCION_RETI}- Retirada.")
        print(f"{Cons.OPCION_MOVI}- Mostrar movimientos.")
        print(f"{Cons.OPCION_SALIR}- SALIR.")
        print("." * Cons.ESTRELLAS_NUM)

    def pedir_opcion(self) -> int:
        opcion: int = -1
        opcion = int(input("Introducir el número de la transacción a realizar: "))
        return opcion

    def ingresar_dinero(self, cantidad: float):
        if cantidad > Cons.MOVIMIENTO_MAX:
            print("Notificar a Hacienda del movimiento.")
        saldo = round(self.cuenta.saldo + cantidad, 2)
        self.cuenta.saldo = saldo
        self.cuenta.movimientos.append(f"INGR. +{cantidad}")
        print(f"Se introdujeron {cantidad}€ exitosamente. Nuevo balance: {self.cuenta.saldo}€.")

    def retirar_dinero(self, cantidad: float):
        if self.cuenta.saldo - cantidad < Cons.MINIMO_SALDO:
            print(f"No es posible llegar a {Cons.MINIMO_SALDO}€. Saldo actual: {self.cuenta.saldo}€.")
        else:
            if cantidad > Cons.MOVIMIENTO_MAX:
                print("Notificar a Hacienda del movimiento.")
            saldo = round(self.cuenta.saldo - cantidad, 2)
            self.cuenta.saldo = saldo
            self.cuenta.movimientos.append(f"RETIR. -{cantidad}")
            print(f"Se retiraron {cantidad}€ exitosamente. Nuevo balance: {self.cuenta.saldo}€.")
            self.avisar_saldo_negativo(self.cuenta.saldo)

    def imprimir_mov(self):
        print("-- LISTA DE MOVIMIENTOS --")
        for i in range(len(self.cuenta.movimientos)):
            if i < Cons.MAX_MOVS:
                print(f"- {self.cuenta.movimientos[i]}€")

    def avisar_saldo_negativo(self, saldo):
        if saldo < 0:
            print("AVISO: Saldo negativo.")

    def run(self):
        opcion: int = -1
        saldo: float = 0.0
        cant: float = 0.0
        iban_manual: str = ""

        iban_manual = input("Introducir IBAN bancario: ")
        while not self.cuenta.comprobar_iban(iban_manual):
            iban_manual = input("IBAN incorrecto, introducir de nuevo: ")
        else:
            self.iban = iban_manual

        self.titular = input("Introducir titular de la cuenta: ")

        self.cuenta = CuentaBancaria(self.iban, self.titular)

        while opcion != Cons.OPCION_SALIR:
            self.imprimir_menu()
            opcion = self.pedir_opcion()
            if opcion == Cons.OPCION_DATOS:
                print(self.cuenta)
            elif opcion == Cons.OPCION_IBAN:
                print(f"IBAN: {self.cuenta.iban}")
            elif opcion == Cons.OPCION_TITULAR:
                print(f"Titular de la cuenta: {self.cuenta.titular}")
            elif opcion == Cons.OPCION_SALDO:
                print(f"Saldo disponible: {self.cuenta.saldo}")
            elif opcion == Cons.OPCION_INGRE:
                cant = float(input("Cantidad a introducir: "))
                self.ingresar_dinero(cant)
            elif opcion == Cons.OPCION_RETI:
                cant = float(input("Cantidad a retirar: "))
                self.retirar_dinero(cant)
            elif opcion == Cons.OPCION_MOVI:
                self.imprimir_mov()
            elif opcion == Cons.OPCION_SALIR:
                print("-- Finalizando proceso --")
            else:
                print("--- ERROR --- Opción no reflejada. Introducir de nuevo.")


Dawbank().run()

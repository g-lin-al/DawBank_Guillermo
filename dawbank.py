from cons import Cons
from cuenta_bancaria import CuentaBancaria


class Dawbank: # Contiene función main
    cuenta: CuentaBancaria = CuentaBancaria
    iban: str = ""
    titular: str = ""

    def imprimir_menu(self) -> None: # Cambiar los números de las opciones a una constante
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

    def imprimir_mov(self):
        print("-- LISTA DE MOVIMIENTOS --")
        for i in self.cuenta.movimientos:
            print(f"- {i}")

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
                continue
            if opcion == Cons.OPCION_IBAN:
                print(f"IBAN: {self.cuenta.iban}")
                continue
            if opcion == Cons.OPCION_TITULAR:
                print(f"Titular de la cuenta: {self.cuenta.titular}")
                continue
            if opcion == Cons.OPCION_SALDO:
                print(f"Saldo disponible: {self.cuenta.saldo}")
                continue
            if opcion == Cons.OPCION_INGRE:
                cant = float(input("Cantidad a introducir: "))
                saldo = self.cuenta.saldo + cant
                self.cuenta.saldo = saldo
                self.cuenta.movimientos.append(f"INGR. +{cant}")
                print(f"Se introdujeron {cant}€ exitosamente. Nuevo balance: {self.cuenta.saldo}")
                continue
            if opcion == Cons.OPCION_RETI:
                cant = float(input("Cantidad a retirar: "))
                saldo = self.cuenta.saldo - cant
                self.cuenta.saldo = saldo
                self.cuenta.movimientos.append(f"RETIR. -{cant}")
                print(f"Se retiraron {cant}€ exitosamente. Nuevo balance: {self.cuenta.saldo}")
                continue
            if opcion == Cons.OPCION_MOVI:
                self.imprimir_mov()
                continue
            if opcion == Cons.OPCION_SALIR:
                break
            else:
                print("--- ERROR --- Opción no reflejada. Introducir de nuevo.")
                continue


Dawbank().run()

from cons import Cons
from cuenta_bancaria import CuentaBancaria


class Dawbank: # Contiene función main
    cuenta: CuentaBancaria = CuentaBancaria
    iban: str = ""
    titular: str = ""

    def imprimir_menu(self) -> None:
        print("1- Mostrar datos de la cuenta.")
        print("2- Mostrar IBAN.")
        print("3- Mostrar titular.")
        print("4- Mostrar saldo.")
        print("5- Ingreso.")
        print("6- Retirada.")
        print("7- Mostrar movimientos.")
        print("8- SALIR.")
        print("." * 25)

    def pedir_opcion(self) -> int:
        opcion: int = -1
        opcion = int(input("Introducir el número de la transacción a realizar: "))
        return opcion

    def run(self):
        opcion: int = -1
        saldo: int = 0
        cant: int = 0

        self.iban = input("Introducir IBAN bancario: ")
        self.titular = input("Introducir titular de la cuenta: ")
        self.cuenta = CuentaBancaria(self.iban, self.titular)

        while opcion != Cons.OPCION_SALIR:
            self.imprimir_menu()
            opcion = self.pedir_opcion()
            if opcion == Cons.OPCION_DATOS:
                print(self.cuenta)
                continue
            if opcion == Cons.OPCION_IBAN:
                print(self.cuenta.get_iban())
                continue
            if opcion == Cons.OPCION_TITULAR:
                print(self.cuenta.get_titular())
                continue
            if opcion == Cons.OPCION_SALDO:
                print(self.cuenta.get_saldo())
                continue
            if opcion == Cons.OPCION_INGRE:
                cant = int(input("Cantidad a introducir: "))
                saldo = self.cuenta.get_saldo() + cant
                self.cuenta.set_saldo(saldo)
                self.cuenta.set_movimientos(f"INGR. +{cant}")
                print(f"Se introdujeron {cant}€ exitosamente. Nuevo balance: {self.cuenta.get_saldo()}")
                continue
            if opcion == Cons.OPCION_RETI:
                cant = int(input("Cantidad a retirar: "))
                saldo = self.cuenta.get_saldo() - cant
                self.cuenta.set_saldo(saldo)
                self.cuenta.set_movimientos(f"RETIR. -{cant}")
                print(f"Se retiraron {cant}€ exitosamente. Nuevo balance: {self.cuenta.get_saldo()}")
                continue
            if opcion == Cons.OPCION_MOVI:
                print(self.cuenta.get_movimientos())
                continue
            if opcion == Cons.OPCION_SALIR:
                break
            else:
                print("--- ERROR --- Opción no reflejada. Introducir de nuevo.")
                continue

Dawbank().run()

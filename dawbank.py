from cons import Cons
from cuenta_bancaria import CuentaBancaria


class Dawbank: # Contiene función main
    cuenta: CuentaBancaria = CuentaBancaria

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



        while opcion != Cons.OPCION_SALIR:
            self.imprimir_menu()
            opcion = self.pedir_opcion()
            if opcion == Cons.OPCION_DATOS:
                print(self.cuenta)
            if opcion == Cons.OPCION_IBAN:
                pass
            if opcion == Cons.OPCION_TITULAR:
                pass
            if opcion == Cons.OPCION_SALDO:
                pass
            if opcion == Cons.OPCION_INGRE:
                pass
            if opcion == Cons.OPCION_RETI:
                pass
            if opcion == Cons.OPCION_MOVI:
                pass
            else:
                print("--- ERROR --- Opción no reflejada. Introducir de nuevo.")
                self.imprimir_menu()
                self.pedir_opcion()


            # mientras la opcion no sea salir:
            #     imprimes menu
            #     pides opcion
            #     segun la opcion:
            #         realizas opcion
            #         imprimes menu
            #         pides opcion


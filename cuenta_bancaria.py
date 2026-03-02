from cons import Cons


class CuentaBancaria:
    IBAN: str = ""
    TITULAR: str = ""
    saldo: float = 0.0
    movimientos: list[str] = []

    def __init__(self, iban: str, titular: str):
        self.IBAN = self.comprobar_iban(iban)
        self.TITULAR = titular
        self.saldo = Cons.SALDO_DEF
        self.movimientos = []

    def comprobar_iban(self, valor):
        return valor

    def __str__(self):
        return f"IBAN: {self.IBAN} - Titular: {self.TITULAR} - Saldo: {self.saldo}"

    def get_iban(self):
        return self.IBAN

    def set_iban(self, valor: str):
        self.IBAN = valor

    def get_titular(self):
        return self.TITULAR

    def set_titular(self, valor: str):
        self.TITULAR = valor

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, valor: float):
        self.saldo = valor

    def get_movimientos(self):
        return self.movimientos

    def set_movimientos(self, valor: str):

        self.movimientos.append(valor)


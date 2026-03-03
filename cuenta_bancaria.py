from cons import Cons
import re


class CuentaBancaria:
    IBAN: str = ""
    TITULAR: str = ""
    _saldo: float = 0.0
    _movimientos: list[str] = []


    def __init__(self, iban: str, titular: str):
        self.IBAN = iban
        self.TITULAR = titular
        self._saldo = Cons.SALDO_DEF
        self._movimientos = []

    def __str__(self):
        return f"IBAN: {self.IBAN} - Titular: {self.TITULAR} - Saldo: {self.saldo}"

    def comprobar_iban(self, valor: str):
        patron = re.compile(r'[A-Z]{2}\d{22}')
        if patron.match(valor):
            return True
        else:
            return False

    @property
    def iban(self):
        return self.IBAN

    @iban.setter
    def iban(self, nuevo_iban: str):
        self.IBAN = nuevo_iban

    @property
    def titular(self):
        return self.TITULAR

    @titular.setter
    def titular(self, nuevo_titular):
        self.titular = nuevo_titular

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        self._saldo = nuevo_saldo

    @property
    def movimientos(self):
        return self._movimientos

    @movimientos.setter
    def movimientos(self, nuevo_movimiento: str):
        self._movimientos.append(nuevo_movimiento)


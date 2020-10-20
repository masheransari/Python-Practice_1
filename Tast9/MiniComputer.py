from Computer import Computer


class MiniComputer(Computer):
    _company: str

    def set_company(self, cmpy):
        self._company = cmpy

    def billing(self):
        return "Billing method calling from MiniComputer Class"

from CompanyClass import CompanyClass


class CeoClass(CompanyClass):
    ceoName = ""

    def showCEOName(self):
        print(self.ceoName)

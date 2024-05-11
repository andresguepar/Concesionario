import IFactoryAbstract,KiaSedan,KiaSuv,KiaHatchBack

class KiaFactory(IFactoryAbstract):
    def createSedan(self):
        return KiaSedan()
    def createSuv(self):
        return KiaSuv()
    def createHactchback(self):
        return KiaHatchBack()
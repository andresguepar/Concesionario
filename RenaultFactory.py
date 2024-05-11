import IFactoryAbstract, RenaultHatchBack,RenaultSuv,RenaultSedan

class RenaultFactory(IFactoryAbstract):
    def createSedan(self):
        return RenaultSedan()
    def createSuv(self):
        return RenaultSuv()
    def createHactchback(self):
        return RenaultHatchBack()
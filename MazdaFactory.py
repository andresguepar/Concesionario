import IFactoryAbstract,MazdaHatchBack,MazdaSedan,MazdaSuv

class MazdaFactory(IFactoryAbstract):
    def createSedan(self):
        return MazdaSedan()
    def createSuv(self):
        return MazdaSuv()
    def createHactchback(self):
        return MazdaHatchBack()
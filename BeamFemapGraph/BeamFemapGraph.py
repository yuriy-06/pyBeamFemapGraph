import re
import matplotlib.pyplot as plt
class FemapRsuBeam:
    def __init__(self, seysmik, wind_y, wind_x):
        self.seysmik = seysmik
        self.wind_y = wind_y
        self.wind_x = wind_x
        SmFile = open(self.seysmik, "r")
        self.mLinesSm = SmFile.readlines()
        SmFile.close()
        WyFile = open(self.wind_y, "r")
        self.mLinesWy = WyFile.readlines()
        WyFile.close()
        WxFile = open(self.wind_x, "r")
        self.mLinesWx = WxFile.readlines()
        WxFile.close()
    def numbers(self, mArg):
        pat = "(\d\.\d+E[-+]\d+)\s+"
        self.mnSm = []; self.mnWx = []; self.mnWy = []
        for item in mArg:
            pass
            searchPat = "\s+" + item + "\s+\d+\s+\d\s+" + pat + pat + pat + pat + pat + pat
            fPat = re.compile(searchPat)
            self.mnSm.append(self.eachFileN(self.mLinesSm, fPat))
            self.mnWy.append(self.eachFileN(self.mLinesWy, fPat))
            self.mnWx.append(self.eachFileN(self.mLinesWx, fPat))
        self.plotMy(self.mnSm, 'seysmik_My')
        self.plotQz(self.mnSm, 'seysmik_Qz')
        self.plotMy(self.mnWy, "Wy_My")
        self.plotQz(self.mnWy, "Wy_Qz")
        self.plotMy(self.mnWx, "Wx_My")
        self.plotQz(self.mnWx, "Wx_Qz")

        plt.show()

    def eachFileN(self, LinesInFile, fPat):
        m = []
        for i in LinesInFile:
            f = re.search(fPat, i)
            if f != None:
                n1 = f.group(1)
                n2 = f.group(2)
                n3 = f.group(3)
                n4 = f.group(4)
                n5 = f.group(5)
                n6 = f.group(6)
                m.append([n1,n2,n3,n4,n5,n6])
        return m
    def plotMy(self, m, title):
        self.plot(m, title, 4)
    def plotMz(self, m, title):
        self.plot(m, title, 5)
    def plotQz(self, m, title):
        self.plot(m, title, 2)
    def plot(self, m, title, n):
        i = 0
        plt.title(title)
        for item in m:
            plt.plot([i, i + 1],[item[0][n], item[1][n]])
            i=+1
        plt.show()
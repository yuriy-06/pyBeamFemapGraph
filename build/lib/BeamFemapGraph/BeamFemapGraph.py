import re
import matplotlib.pyplot as plt


class FemapRsuBeam:
    def __init__(self, seysmik, wind_y, wind_x):
        self.seysmik = seysmik  # для отладочных целей
        self.wind_y = wind_y
        self.wind_x = wind_x

        self.mLinesSm = self.openReadClose(seysmik)  # записали из файлов массивы строк
        self.mLinesWy = self.openReadClose(wind_y)
        self.mLinesWx = self.openReadClose(wind_x)

        self.mnSm = []  # массивы усилий
        self.mnWx = []
        self.mnWy = []

    @staticmethod
    def openReadClose(name):
        f = open(name, "r")
        m = f.readlines()
        f.close()
        return m

    def numbers(self, mArg):
        pat = "(\d\.\d+E[-+]\d+)\s+"

        for item in mArg:
            pass
            searchPat = "\s+" + str(item) + "\s+\d+\s+\d\s+" + pat + pat + pat + pat + pat + pat
            fPat = re.compile(searchPat)
            self.mnSm.append(self.eachFileN(self.mLinesSm, fPat, item))
            self.mnWy.append(self.eachFileN(self.mLinesWy, fPat, item))
            self.mnWx.append(self.eachFileN(self.mLinesWx, fPat, item))
        self.plotMy(self.mnSm, 'seysmik_My')
        self.plotQz(self.mnSm, 'seysmik_Qz')
        self.plotMy(self.mnWy, "Wy_My")
        self.plotQz(self.mnWy, "Wy_Qz")
        self.plotMy(self.mnWx, "Wx_My")
        self.plotQz(self.mnWx, "Wx_Qz")

        plt.show()

    def eachFileN(self, linesInFile, fPat, item):
        m = []
        for i in linesInFile:
            f = re.search(fPat, i)
            if f is not None:  # срабатывает только раз, т.к в файле только один такой КЕ с таким fPat
                n1 = f.group(1)
                n2 = f.group(2)
                n3 = f.group(3)
                n4 = f.group(4)
                n5 = f.group(5)
                n6 = f.group(6)
                m.append([n1, n2, n3, n4, n5, n6])
            if m == []:
                print("\nнет такого КЕ -- ", item)
        return m

    def plotMy(self, m, title):
        self.plot(m, title, 4)

    def plotMz(self, m, title):
        self.plot(m, title, 5)

    def plotQz(self, m, title):
        self.plot(m, title, 2)

    def plot(self, m, title, n):  # n - это вид усилий
        i = 0
        plt.title(title)
        for item in m:
            plt.plot([i, i + 1], [item[0][n], item[1][n]])
            i = i + 1
        plt.show()

import re
import matplotlib.pyplot as plt

'''
from BeamFemapGraph.BeamFemapGraph import FemapRsuBeamGraph as fg
test = fg(seysmik="G:/temp/analiz/seysmik", wind_x="G:/temp/analiz/wind_x", wind_y="G:/temp/analiz/wind_y")
fg.numbers(["2125","2126"])
'''


class FemapRsuBeamGraph:
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
                
        self.plotCount = 1 # счетчик окон печати

    @staticmethod
    def openReadClose(name):
        f = open(name, "r")
        m = f.readlines()
        f.close()
        return m

    def numbers(self, mArg):
        pat = "(\d\.\d+E[-+]\d+)\s+"
        self.last = mArg[-1]
        if (self.last == "0") or (self.last == "1"):
            self.head = mArg[0:-1]
        else:
            self.head = mArg
        for ke in self.head:
            pass
            searchPat = "\s+" + str(ke) + "\s+\d+\s+\d\s+" + pat + pat + pat + pat + pat + pat
            fPat = re.compile(searchPat)
            self.mnSm.append(self.eachFileN(self.mLinesSm, fPat, str(ke)))  # append дополнительно оборачиваеи
            # выводимое значение в массив, поэтому массивы усилий для каждого КЕ оборачиваются своим массивом
            # массив усилий -> массив сечений -> массив КЕ
            self.mnWy.append(self.eachFileN(self.mLinesWy, fPat, str(ke)))
            self.mnWx.append(self.eachFileN(self.mLinesWx, fPat, str(ke)))
        self.plotMy(self.mnSm, 'seismic_My on ' + str(self.head))
        self.plotQz(self.mnSm, 'seismic_Qz on ' + str (self.head))
        self.plotMy(self.mnWy, "Wy_My on " + str(self.head))
        self.plotQz(self.mnWy, "Wy_Qz on " + str(self.head))
        self.plotMy(self.mnWx, "Wx_My on " + str(self.head))
        self.plotQz(self.mnWx, "Wx_Qz on " + str(self.head))
        plt.show()

    def eachFileN(self, linesInFile, fPat, item):
        m = []
        for string in linesInFile:
            f = re.search(fPat, string)
            if f is not None:  # срабатывает несколько раз для данного КЕ (несколько сечений)
                n1 = float(f.group(1))/10000
                n2 = float(f.group(2))/10000
                n3 = float(f.group(3))/10000
                n4 = float(f.group(4))/10000
                n5 = float(f.group(5))/10000
                n6 = float(f.group(6))/10000
                m.append([n1, n2, n3, n4, n5, n6])  # выводится массив массивов
            if m == []:
                pass
                # print("\n нет такого КЕ -- ", item)
        return m

    def plotMy(self, m, title):
        self.plot(m, title, 4)

    def plotMz(self, m, title):
        self.plot(m, title, 5)

    def plotQz(self, m, title):
        self.plot(m, title, 2)

    def plot(self, m, title, forceCase):  # forceCase - это вид усилий
        mx = []; my = []
        plt.subplot(3, 2, self.plotCount)
        self.plotCount += 1
        x = 0
        plt.title(title)
        for ke in m:
            # массив ke -> массив сечений -> массив усилий
            if self.last == "0":
                mx.append(x); mx.append(x+1)
                my.append(ke[1][forceCase]); my.append(ke[0][forceCase])
                plt.xlabel('Sections; direction 0; for help only')
            else:
                mx.append(x); mx.append(x+1)
                my.append(ke[0][forceCase]); my.append(ke[1][forceCase])
                plt.xlabel('Sections; directions 1; for help only')
            x = x + 1
        plt.plot([0, x],[0,0]) # так просто горизонтальную линию печатаем
        plt.plot(mx,my)

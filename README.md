Этот пакет предназначен для рисования упрощенных эпюр (графиков усилий) для серии КЕ балок и колонн.
Усилия используются из расчетной программы  femap.
Пример использования:
```
from BeamFemapGraph.BeamFemapGraph import FemapRsuBeam as fm
test = fm(seysmik="G:/temp/analiz/seysmik", wind_x="G:/temp/analiz/wind_x", wind_y="G:/temp/analiz/wind_y")
test.numbers(["1908", "1907"]) # здесь слева направо КЕ балки
test.numbers([1908, 1907])
```
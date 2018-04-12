from BeamFemapGraph.BeamFemapGraph import FemapRsuBeam as fm
test = fm(seysmik="G:/temp/analiz/seysmik", wind_x="G:/temp/analiz/wind_x", wind_y="G:/temp/analiz/wind_y")
test.numbers([35667, 2144, 35668]) # or
test.numbers(['35667', '2144', '35668'])
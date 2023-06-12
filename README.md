# Projekt_informatik
Program jest napisany w języku python i umożliwia konwersje współrzędnych. Skrypt działa na elipsoidachgrs80 i wgs84.Zastosowane są transformacje:

XYZ -> BLH                                                                                                                                        
BLH -> XYZ                                                                                                                                          
XYZ -> NEU                                                                                                                                          
BL -> XY2000                                                                                                                                            
BL -> XY1992                                                                                                                                                    
XYZ -> XY1992                                                                                                                                               
XYZ -> XY2000                                                                                                                                                       

Wymagania:                                                                                                                                                   
-Program stworzony dla Windowsa 10 i 11                                                                                                                          
-System operacyjny python 3.7                                                                                                                                   
-math                                                                                                                                                          
-numpy                                                                                                                                                          
-biblioteka argparse                                                                                                                                            
-Wywołania z pliku main.py                                                                          

Program obsługuje pliki txt, gdzie kolejna linia współrzędnych oddzielona jest przecinkiem. Przykład:

52.0972722,21.0315333,   141.399,947413.418,-1352137.431,6140234.316,481634032430.556,15027939082.113,437788127780.763,13935385475.422
52.0972722,21.0315331,   141.400,947412.960,-1352137.320,6140234.411,481633670612.755,15027908118.825,437787798717.301,13935356874.680
52.0972721,21.0315330,   141.403,947412.561,-1352137.293,6140234.482,481633405928.928,15027885921.696,437787557891.252,13935336368.116
52.0972721,21.0315328,   141.408,947412.181,-1352137.295,6140234.544,481633173623.022,15027866646.614,437787346477.610,13935318559.605
52.0972721,21.0315332,   141.410,947412.808,-1352136.863,6140234.545,481633241783.705,15027868666.475,437787409336.033,13935320451.482

Wywołania zwracją pliki w takim samym formacie. Przykładowe wywołanie:

 wczyt_plik.py -i wsp_inp.txt -o wsp_out.txt -el GRS80 -t xyz_to_blh

Wady programu:                                                            
Dane są z minimalnym, ale niezauważalnym błędem



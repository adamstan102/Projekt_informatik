# Projekt_informatik
Program jest napisany w języku python i umożliwia konwersje współrzędnych. Skrypt działa na elipsoidachgrs80 i wgs84.Zastosowane są transformacje:

XYZ -> BLH
BLH -> XYZ
XYZ -> NEUp
BL -> XY2000
BL -> XY1992
XYZ -> XY1992
XYZ -> XY2000
Wymagania:
-System operacyjny python 3.7
-math
-numpy
-biblioteka argparse
-Wywołania z pliku main.py

Program obsługuje pliki txt, gdzie kolejna linia współrzędnych oddzielona jest przecinkiem. Przykład

5773723.182,7502160.783
5773723.175,7502160.77
5773723.171,7502160.757
5773723.167,7502160.744

Wywołania zwracją pliki w takim samym formacie. Przykładowe wywołanie:

wczyt_plik.py -i wsp_inp.txt -o wyniki.txt -t xyz_to_blh

Wady programu
Dane są z minimalnym, ale niezauważalnym błędem



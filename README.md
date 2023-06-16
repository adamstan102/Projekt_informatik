# Projekt_informatik
Program jest napisany w języku python i umożliwia konwersje współrzędnych. Skrypt działa na elipsoidachgrs80 i wgs84.Zastosowane są transformacje:

- XYZ -> BLH                                                                                                                                        
- BLH -> XYZ                                                                                                                                          
- XYZ -> NEU                                                                                                                                          
- BL -> XY2000                                                                                                                                            
- BL -> XY1992                                                                                                                                                
- XYZ -> XY1992                                                                                                                                               
- XYZ -> XY2000                                                                                                                                                       

# Wymagania:                                                                                                                                                   
- Program stworzony dla Windowsa 10 i 11                                                                                                                          
- System operacyjny python 3.7                                                                                                                                   
- math                                                                                                                                                          
- numpy                                                                                                                                                          
- biblioteka argparse                                                                                                                                            

# Instrukcja po plikach

- Plik "Projekt_z_informatyki.py" jest biblioteką funkcji transformacji.
- Plik wczyt_plik.py służy do obliczania transformacji.
- wsp_inp.txt to przykładowe dane z Obserwatorium Astronomiczno-Geodezyjne w Józefosławiu
- wsp_out.txt to plik, w którym zapisują się wyniki.




# Program obsługuje pliki txt, gdzie kolejna linia współrzędnych oddzielona jest przecinkiem. Przykład:


Nazwy wartości w "wsp_inp.txt" jedna po drugiej:
- Pierwsza kolumna: X
- Druga kolumna: Y
- Trzecia kolumna: Z

3664940.500,1409153.590,5009571.170
3664940.510,1409153.580,5009571.167
3664940.520,1409153.570,5009571.167
3664940.530,1409153.560,5009571.168
3664940.520,1409153.590,5009571.170
3664940.514,1409153.584,5009571.166
3664940.525,1409153.575,5009571.166
3664940.533,1409153.564,5009571.169
3664940.515,1409153.590,5009571.170
3664940.514,1409153.584,5009571.169
3664940.515,1409153.595,5009571.169
3664940.513,1409153.584,5009571.171



Nazwy wyników w "wsp_out.txt" jedna po drugiej:
- Kolumna 1: Phi (B)
- Kolumna 2:Lambda (L)
- Kolumna 3: Wysokość (H)
- Kolumna 4: Wartość X z obliczonych BLH
- Kolumna 5: Wartość Y z obliczonych BLH
- Kolumna 6: Wartość Z z obliczonych BLH
- Kolumna 7: Wartość X2000 z obliczonych BLH
- Kolumna 8: Wartość Y2000 z obliczonych BLH
- Kolumna 9: Wartość X1992 z obliczonych BLH
- Kolumna 10: Wartość Y1992 z obliczonych BLH

52.0972721,21.0315332,   141.410,3664940.520,1409153.590,5009571.170,481633241783.705,15027868666.475,437787409336.033,13935320451.482
52.0972721,21.0315332,   141.402,3664940.514,1409153.584,5009571.166,481633427849.633,15027885909.378,437787578257.429,13935336369.679
52.0972721,21.0315330,   141.406,3664940.525,1409153.575,5009571.166,481633110569.583,15027858890.410,437787289669.585,13935311411.388
52.0972721,21.0315328,   141.411,3664940.533,1409153.564,5009571.169,481633035148.251,15027853802.057,437787220764.940,13935306701.922
52.0972721,21.0315333,   141.407,3664940.515,1409153.590,5009571.170,481633439445.405,15027886270.381,437787588947.203,13935336707.463
52.0972721,21.0315332,   141.405,3664940.514,1409153.584,5009571.169,481633524983.483,15027894675.521,437787666494.729,13935344463.842
52.0972721,21.0315333,   141.408,3664940.515,1409153.595,5009571.169,481633341747.679,15027876842.992,437787500336.633,13935328006.710
52.0972722,21.0315332,   141.406,3664940.513,1409153.584,5009571.171,481633629271.735,15027904040.399,437787761241.841,13935353111.149

Wywołania zwracją pliki w takim samym formacie. Przykładowe wywołanie:

python wczyt_plik.py -i wsp_inp.txt -o wsp_out.txt -el grs80 -t xyz_to_blh


Wady programu:                                                            
Nie wiem czemu, ale dane z BLH na XYZ są źle obliczane przez program. Reszta wyników jest oparta na tych wynikach XYZ przez co dalsze wyniki także są nieprawidłowe, jednak gdyby funkcje nie brały złych wartości, tylko na przykład takie jakie poda użytkowanik to reszta funkcji oblicza poprawnie.
Podczas wykorzystywania wywoływania transformacji "xyz_to_blh", plik tekstowy wypisuje także inne transformacje: "blh_to_xyz", "BL_to_XY2000", "BL_to_XY1992". 


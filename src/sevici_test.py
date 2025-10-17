from sevici import *
def main():
    ruta = "./data/estaciones.csv"
    datos =lee_estaciones(ruta)
    #test_lee_estaciones(ruta)
    #test_estaciones_bicis_libres(datos)
    #print(estaciones_bicis_libres(datos,1))
    test_estaciones_cercanas(datos)


def test_lee_estaciones(ruta):
    print("Las tres primeras son...")
    print(lee_estaciones(ruta)[:5])
    print("Y las tres ultimas...")
    print(lee_estaciones(ruta)[-5:])

def  test_estaciones_bicis_libres(datos):
    print("Primeras 5 libres...",estaciones_bicis_libres(datos)[:5])
    print("Últimas 5 libres...",estaciones_bicis_libres(datos)[-5:])

def test_estaciones_cercanas(datos):
    print(estaciones_cercanas(datos,(37.357659, -5.9863),7))





if __name__ == '__main__':
    main()
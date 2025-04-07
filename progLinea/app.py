''' Calculo de coordenadas de lineas '''
import argparse
import funciones

def main(m:float,b:float):
    '''
        Funcion principal
        Recibe m y b en la ejecucion del programa
    '''
    X = [x/10.0 for x in range(10,110,5)]
    Y = [funciones.calcular_y(x,m,b) for x in X]
    coordenadas = list(zip(X,Y))
    print(coordenadas)
    funciones.grafica_linea(X,Y,m,b)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calcula las coordenadas de una linea recta')
    parser.add_argument('-m',type=float,help='Pendiende de la linea',default=2.0) # Si no se especifica el valor se le da un valor de 2.0
    parser.add_argument('-b',type=float,help='Inteseccion en y', default=3.0) # Si no se especifica el valor se le da un valor de 3.0
    args = parser.parse_args()
    main(args.m,args.b)

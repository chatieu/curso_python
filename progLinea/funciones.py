'''Funciones para progLinea.'''
import matplotlib.pyplot as plt

def calcular_y(x:float,m:float,b:float)->float:
    ''' 
        y = mx + b
        m : pendiente
        b : interseccion en y
    '''
    return (m*x)+b

def grafica_linea(X:list,Y:list,m:float,b:float):
    '''
        X : lista con valores de x
        Y : lista con valores de y
        m : pendiente
        b : interseccion en y
    '''

    plt.plot(X,Y)
    plt.title(f'Linea recta con pendiente m={m} e interseccion en y={b}')
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.grid()
    plt.show()

def test_linea():
    '''
        Comprobamos calcular_y()
    '''

    y = calcular_y(0.0,2.0,3.0)
    return y

if __name__ == '__main__': 
    if test_linea() == 3.0: 
        print('ta bn')
    else: 
        print('todo mal w')
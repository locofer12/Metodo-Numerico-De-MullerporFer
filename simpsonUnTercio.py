import math
#n se va iterando

Ni =[]
def numerosN(n):
    for i in range(0, n):
        Ni.append(i + 1)
    print(f"valorss de N son {Ni}")


n = 4
numerosN(n)

#a es el limite inferior de la integral
a=0
#b es el limite superior de la integral
b=3



deltaX =(b - a)/n
print( "es el valor de deltax ", deltaX ,"\n")
x0 = a
valor = []
#formulas
def formula(x):
    f = 5+(3*math.cos(x))
    return f
xIterada = [x0]
def equis(n):

    xx=0
    for i in range(0, n+1):
        xx+= deltaX
        xIterada.append((x0+xx).__round__(4))
        print("valor de x" , i  ," = ",xIterada[i])

equis(n)
fxN = []
def eseFormula():

    for i in range (0,n+1):
        fxN.append(formula(xIterada[i]).__round__(4))
        print("respuesta fx",i," es ",fxN[i])
print("\n")
eseFormula()
def resolucion(n):
    suma = 0
    for i in range (1,n):
        if(i%2==0):
            RESULT = 2*fxN[i]
            print("resultado 2x",fxN[i], " es ", RESULT)
        else:
            RESULT = 4*fxN[i]
            print("resultado 4x", fxN[i], " es ", RESULT)
        suma+=RESULT
    print ("\n valor deltax / 3 = ", (deltaX/3).__round__(4))
    print("valor solo de fx0 +4fx1 + 2fx2... fxn = ", (fxN[0] + suma+ fxN[-1]).__round__(4) )
    print("solo sumas sin extremos", suma.__round__(4))
    print("solucion de S = ",((deltaX/3)*(fxN[0] + suma+ fxN[-1])).__round__(4))

resolucion(n)



#valores
# lineal o base 2 hay que cambiar n
n = 2
print("base : ", n)
x0 = 1
x1=4
x2 = 6 #cambiar si existe

#funciones
fx0 =0
fx1 = 1.386394
fx2 = 1.791760 #cambiar si existe
#incognita
x = 2
if (n == 1):
    fx = ((x-x1)/(x0-x1))*fx0+((x-x0)/(x1-x0))*fx1
    print("f1x es ",fx)
elif(n==2):

    fx= (((x-x1)*(x-x2))/((x0-x1)*(x0-x2)))*fx0 + (((x-x0)*(x-x2))/((x1-x0)*(x1-x2)))*fx1 +(((x-x0)*(x-x1))/((x2-x0)*(x2-x1)))*fx2
    print("f2x = ", fx)

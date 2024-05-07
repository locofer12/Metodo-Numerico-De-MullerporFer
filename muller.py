import math

def ecuacion1(lista):
    resultados = []
    for x in lista:
        #la ecuacion cambia segun necesidad
        form = 1/(x**2) -math.tan(x)
        resultados.append(form)

    return resultados
#aca se cambian los valores segun cada iteracion
lista = [0.5, 1,1.5]
resultados = ecuacion1(lista)

#valores iniciales de x
x0 =lista[0]
x1 = lista[1]
x2 = lista[2]

print(resultados[:])
#resultados
res1= resultados[0]
res2= resultados[1]
res3= resultados[2]
#calculamos valoers h y s
h0= x1-x0
h1= x2-x1
print("valores h1 y h0 respectivos son: h1:",h1,", h0:", h0)
#valores S

s0 = (res2-res1)/(h0)
s1 = (res3-res2)/(h1)
print("valores s1 y s0 respectivos son: s1:",s1,", s0:",s0)
#coeficiente de la parabola
a=(s1-s0)/(h1+h0)

b=a*h1+s1

c= res3
print("valores a, b y c respectivos son:  ",a, " ", b,", ", c)
#calulamos discriminante positivo y negativo
discriminantePositivo = math.fabs((b+math.sqrt(b**2-4*a*c)))
discriminanteNegativo = math.fabs((b-math.sqrt(b**2-4*a*c)))
#raiz discriminante
raizDiscriminante = math.sqrt(b**2-4*a*c)
print("raiz discriminante es: ",raizDiscriminante)
#sumaabsoluta con positivo

#vemos el signo
if(discriminantePositivo>discriminanteNegativo):
    print("valor positivo ")
else:
    print("valor negativo ")

#cambiamos el valor segun salga arriba negativo o positivo en el DENOMMINADOR
x3 = x2 + (-2*c)/(b-raizDiscriminante)
print("valor de x final")
print(x3)

error = math.fabs(((x3-x2)/x3)*100)
#use round para  que solo salgan 4 decimales
print("el error es ", round(error,4), "%")

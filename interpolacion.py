#interpolacion lineal


x0 = 2
x1 =4
X = 3
fx0 =0.693147
fx1=1.3862

fxdesconocida = fx0 + ((fx1-fx0)/(x1-x0))*(X-x0)

print(fxdesconocida)
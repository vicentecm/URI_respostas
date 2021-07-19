#uri 1012

dados = input().split(" ")
A = float(dados[0])
B = float(dados[1])
C = float(dados[2])
pi = 3.14159

area_triangulo = (A*C)/2
area_circulo = pi*(C**2)
area_trapezio = ((A+B)*C)/2
area_quadrado = B**2
area_retangulo = A*B

print(f"TRIANGULO: {area_triangulo:.3f}")
print(f"CIRCULO: {area_circulo:.3f}")
print(f"TRAPEZIO: {area_trapezio:.3f}")
print(f"QUADRADO: {area_quadrado:.3f}")
print(f"RETANGULO: {area_retangulo:.3f}")





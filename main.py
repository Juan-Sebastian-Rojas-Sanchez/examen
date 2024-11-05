import math

def area_triangulo_equilatero(lado):
    return (math.sqrt(3) / 4) * lado ** 2

# Ejemplo de uso
lado = float(input("Ingrese el lado triangulo: "))
area = area_triangulo_equilatero(lado)
if area < 1000:
  print(f"El area del triangulo equilatero es: {area}")
else:
    print(f"datos no validos: {area}")


#promedio
# Ask the user to enter the grades
v1 = float(input("Ingrese el primer voltaje: "))
v2 = float(input("Ingese el segundo voltaje: "))
v3 = float(input("Ingese el tercer voltaje:"))
v4 = float(input("Ingrese el cuarto voltaje: "))
v5 = float(input("Ingrese el quinto voltaje: "))
# Calculate the average
average = (v1 + v2 + v3 + v4+ v5) / 5
if average > 220:
  print(f"El voltaje es alto ya que su promedio es: {average}")
else:
    print(f"El voltaje es correcto ya que su promedio es: {average}")
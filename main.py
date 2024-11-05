# Ask the user to enter the grades
v1 = float(input("Ingrese el primer voltaje: "))
v2 = float(input("Ingese el segundo voltaje: "))
v3 = float(input("Ingese el tercer voltaje:"))

# Calculate the average
average = (v1 + v2 + v3) / 3

if average < 115:
  print(f"El voltaje es correcto ya que su promedio es: {average}")
elif average >115 and average<220:
    print(f"El voltaje es alto ya que su promedio es: {average}")
elif average > 220:
    print(f"Peligro ya que su promedio es: {average}")

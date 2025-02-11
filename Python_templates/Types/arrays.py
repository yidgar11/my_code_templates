# https://www.w3schools.com/python/python_arrays.asp

cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
l = len(cars)

cars.append("Honda")


for x in cars:
  print(x)

# Remove
cars.pop(1)
cars.remove("Volvo")

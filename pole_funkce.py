cars = ["ford", "volvo", "bmw", "audi"]

print(cars)
for i in range( len(cars) ):
    print(f"{i}: {cars[i - 1]}")
    print(f"auto s čislem {i+1}: {cars[i]}")
          
prvek_plus = input("zadejte auto")

print(" ")
cars.append(prvek_plus)

for x in range(len(cars)):
    print(f"auto s čislem {x+1}: {cars[x]}")
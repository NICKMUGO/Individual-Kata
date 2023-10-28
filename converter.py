name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
weight_pounds = float(input("Please enter your weight in pounds: "))
weight_kilograms = weight_pounds * 0.453592
print(f"Name: {name}")
print(f"Age: {age} years")
print(f"Weight (in pounds): {weight_pounds} lbs")
print(f"Weight (in kilograms): {weight_kilograms:.2f} kg")

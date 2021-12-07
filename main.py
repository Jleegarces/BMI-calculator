weight = input("enter your weight in kg: ")
height = input("enter your height in m: ")

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)

print(bmi_as_int)
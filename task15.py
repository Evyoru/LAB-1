feet = int(input("Feet: "))
inches = int(input("Inches: "))

height_cm = feet * 30.48 + inches * 2.54

print(f"Your height is: {round(height_cm)} cm.")
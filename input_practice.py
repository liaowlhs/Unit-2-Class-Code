"""
Name: Guoming Liao
Date: 10-1-24
Description: Salad ingredient amount generator
"""

print("Enter an ingredient for a salad and the amount of ounces for one serving.")
ingredient_one = input("First ingredient: ")
ounces_one = float(input(f"Ounces of {ingredient_one}: "))
ingredient_two = input("Second ingredient: ")
ounces_two = float(input(f"Ounces of {ingredient_two}: "))
ingredient_three = input("Third ingredient: ")
ounces_three = float(input(f"Ounces of {ingredient_three}: "))


servings = float(input("Now, how many servings do you want: "))
print(f"This is how many ounces for all three ingredients for {servings} servings.")
serving_one = ounces_one*servings
serving_two = ounces_two*servings
serving_three = ounces_three*servings

print(f"{ingredient_one}: {serving_one:.1f} ounces.")
print(f"{ingredient_two}: {serving_two:.1f} ounces.")
print(f"{ingredient_three}: {serving_three:.1f} ounces.")

#why is not not commiting
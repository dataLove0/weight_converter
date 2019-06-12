print("Weight converter!")
print("Default: Kilo")
print("\nType: kg to convert from kg")
print("\nType: lbs to convert from lbs")

while True:
    weight_type = input("LBS or KG? ")

    if weight_type.lower() == "kg":

        while True:
            kg = float(input("Kilos: "))

            print(f"{int(kg)} kilo grams is: {int(kg) * 1000} grams")
            print(f"{int(kg)} kilo grams is: {int(kg) * 2.20462262} pounds/LBS")
            print(f"{int(kg)} kilo grams is: {int(kg) * 0.00110231131} tons")
            print(f"{int(kg)} kilo grams is: {int(kg) * 35.2739619} ounces")

    elif weight_type.lower() == "lbs":

        while True:
            lbs = float(input("Lbs: "))

            print(f"{int(lbs)} pounds is: {int(lbs) * 453.59237} grams")
            print(f"{int(lbs)} pounds is: {int(lbs) * 0.45359237} kilo grams")
            print(f"{int(lbs)} pounds is: {int(lbs) * 0.0005} tons")
            print(f"{int(lbs)} pounds is: {int(lbs) * 16} ounces")

    print("Invalid value")


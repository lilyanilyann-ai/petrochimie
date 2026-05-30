# Petroleum Unit Converter
# No external libraries needed!

def barrel_to_liter(barrels):
    return barrels * 158.987

def liter_to_barrel(liters):
    return liters / 158.987

def barrel_to_gallon(barrels):
    return barrels * 42

def gallon_to_barrel(gallons):
    return gallons / 42

def calc_api(specific_gravity):
    return (141.5 / specific_gravity) - 131.5

def classify_oil(api):
    if api > 45:
        return "Extra Light"
    elif api > 31.1:
        return "Light"
    elif api > 22.3:
        return "Medium"
    elif api > 10:
        return "Heavy"
    else:
        return "Extra Heavy"

def save_results(results):
    with open("results.txt", "w") as f:
        f.write("=" * 40 + "\n")
        f.write("  Petroleum Converter Results\n")
        f.write("=" * 40 + "\n")
        for line in results:
            f.write(line + "\n")
    print("Results saved to results.txt")

def run():
    print("=" * 40)
    print("  Petroleum Unit Converter")
    print("=" * 40)
    results = []

    while True:
        print("\n1. Barrel to Liter")
        print("2. Liter to Barrel")
        print("3. Barrel to Gallon")
        print("4. Gallon to Barrel")
        print("5. Calculate API Gravity")
        print("6. Save and Exit")

        choice = input("\nChoose (1-6): ")

        if choice == "1":
            val = float(input("Enter barrels: "))
            res = barrel_to_liter(val)
            line = f"{val} BBL = {res:.2f} Liters"
            print(line)
            results.append(line)

        elif choice == "2":
            val = float(input("Enter liters: "))
            res = liter_to_barrel(val)
            line = f"{val} Liters = {res:.4f} BBL"
            print(line)
            results.append(line)

        elif choice == "3":
            val = float(input("Enter barrels: "))
            res = barrel_to_gallon(val)
            line = f"{val} BBL = {res:.2f} Gallons"
            print(line)
            results.append(line)

        elif choice == "4":
            val = float(input("Enter gallons: "))
            res = gallon_to_barrel(val)
            line = f"{val} Gallons = {res:.4f} BBL"
            print(line)
            results.append(line)

        elif choice == "5":
            sg = float(input("Enter Specific Gravity: "))
            api = calc_api(sg)
            oil_type = classify_oil(api)
            line = f"SG={sg} -> API={api:.2f} -> {oil_type}"
            print(line)
            results.append(line)

        elif choice == "6":
            if results:
                save_results(results)
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    run()
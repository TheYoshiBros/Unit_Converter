flag = True

history = {
    "Temperature": [],
    "Distance": [],
    "Weight": [],
    "Volume": []
}

def main():
    global flag
    while flag:
        print("""\n UNIT CONVERTER:
  1. Convert Temperature
  2. Convert Distance
  3. Convert Weight
  4. Convert Liquid-Volume
  5. View History
  6. Exit""")
        choice = input("\nSelect option (1-6): ")

        match choice:
            case "1":
                print("""\n TEMPERATURE UNITS:
  1. Celsius
  2. Fahrenheit
  3. Kelvin""")

                from_unit = input("\nSelect starting unit (1-3): ")
                to_unit = input("Select destination unit (1-3): ")

                num = input("Enter number to convert: ")

                try:
                    value = float(num)
                except ValueError:
                    print("Invalid number. Please try again.")
                    continue

                message = None

                if from_unit == "1" and to_unit == "2":
                    message = f'{num} degrees Celsius is {float(num) * 9/5 + 32:.4f} degrees Fahrenheit.'

                elif from_unit == "1" and to_unit == "3":
                    message = f'{num} degrees Celsius is {float(num) + 273.15:.4f} Kelvin.'

                elif from_unit == "2" and to_unit == "1":
                    message = f'{num} degrees Fahrenheit is {(float(num) - 32) * 5/9:.4f} degrees Celsius.'

                elif from_unit == "2" and to_unit == "3":
                    celsius = (float(num) - 32) * 5/9
                    message = f'{num} degrees Fahrenheit is {celsius + 273.15:.4f} Kelvin.'

                elif from_unit == "3" and to_unit == "1":
                    message = f'{num} Kelvin is {float(num) - 273.15:.4f} degrees Celsius.'

                elif from_unit == "3" and to_unit == "2":
                    celsius = float(num) - 273.15
                    message = f'{num} Kelvin is {celsius * 9/5 + 32:.4f} degrees Fahrenheit.'

                elif from_unit == to_unit:
                    if from_unit == "1":
                        message = f'{num} degrees Celsius is {float(num):.4f} degrees Celsius.'
                    elif from_unit == "2":
                        message = f'{num} degrees Fahrenheit is {float(num):.4f} degrees Fahrenheit.'
                    elif from_unit == "3":
                        message = f'{num} Kelvin is {float(num):.4f} Kelvin.'
                    else:
                        print("Invalid temperature unit.")

                else:
                    print("Invalid temperature unit.")

                if message is not None:
                    print(message)
                    history["Temperature"].append(message)

                pass

            case "2":
                print("""\n DISTANCE UNITS:
    1. Millimeters
    2. Centimeters
    3. Meters
    4. Kilometers
    5. Inches
    6. Feet
    7. Yards
    8. Miles
    9. Micrometers
    10. Nanometers
    11. Picometers
    12. Femtometers
    13. Angstroms
    14. Nautical Miles""")
                start_unit = input("\nSelect starting unit (1-14): ")
                end_unit = input("\nSelect destination unit (1-14): ")

                if start_unit not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"):
                    print("Invalid starting unit.")
                    continue

                if end_unit not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"):
                    print("Invalid destination unit.")
                    continue

                try:
                    num = float(input("Enter the number to convert: "))
                except ValueError:
                    print("Invalid number. Please try again.")
                    continue

                match (start_unit):
                    case "1":
                        start_unit_name = "Millimeters"
                        start_unit_value = 0.001
                    case "2":
                        start_unit_name = "Centimeters"
                        start_unit_value = 0.01
                    case "3":
                        start_unit_name = "Meters"
                        start_unit_value = 1
                    case "4":
                        start_unit_name = "Kilometers"
                        start_unit_value = 1000
                    case "5":
                        start_unit_name = "Inches"
                        start_unit_value = 0.0254
                    case "6":
                        start_unit_name = "Feet"
                        start_unit_value = 0.3048
                    case "7":
                        start_unit_name = "Yards"
                        start_unit_value = 0.9144
                    case "8":
                        start_unit_name = "Miles"
                        start_unit_value = 1609.344
                    case "9":
                        start_unit_name = "Micrometers"
                        start_unit_value = 1e-6
                    case "10":
                        start_unit_name = "Nanometers"
                        start_unit_value = 1e-9
                    case "11":
                        start_unit_name = "Picometers"
                        start_unit_value = 1e-12
                    case "12":
                        start_unit_name = "Femtometers"
                        start_unit_value = 1e-15
                    case "13":
                        start_unit_name = "Angstroms"
                        start_unit_value = 1e-10
                    case "14":
                        start_unit_name = "Nautical Miles"
                        start_unit_value = 1852.0
                    case _:
                        print("Invalid starting unit.")
                
                match (end_unit):
                    case "1":
                        end_unit_name = "Millimeters"
                        end_unit_value = 0.001
                    case "2":
                        end_unit_name = "Centimeters"
                        end_unit_value = 0.01
                    case "3":
                        end_unit_name = "Meters"
                        end_unit_value = 1
                    case "4":
                        end_unit_name = "Kilometers"
                        end_unit_value = 1000
                    case "5":
                        end_unit_name = "Inches"
                        end_unit_value = 0.0254
                    case "6":
                        end_unit_name = "Feet"
                        end_unit_value = 0.3048
                    case "7":
                        end_unit_name = "Yards"
                        end_unit_value = 0.9144
                    case "8":
                        end_unit_name = "Miles"
                        end_unit_value = 1609.344
                    case "9":
                        end_unit_name = "Micrometers"
                        end_unit_value = 1e-6
                    case "10":
                        end_unit_name = "Nanometers"
                        end_unit_value = 1e-9
                    case "11":
                        end_unit_name = "Picometers"
                        end_unit_value = 1e-12
                    case "12":
                        end_unit_name = "Femtometers"
                        end_unit_value = 1e-15
                    case "13":
                        end_unit_name = "Angstroms"
                        end_unit_value = 1e-10
                    case "14":
                        end_unit_name = "Nautical Miles"
                        end_unit_value = 1852.0
                    case _:
                        print("Invalid destination unit.")
                result = num * start_unit_value / end_unit_value

                if result != 0 and abs(result) < 0.0001:
                    formatted_result = f"{result:.15g}"
                else:
                    formatted_result = f"{result:.4f}"

                message = (
                    f"{num:g} {start_unit_name} is "
                    f"{formatted_result} {end_unit_name}."
                )
                print(message)
                history["Distance"].append(message)

                pass

            case "3":
                print("""\n WEIGHT AND MASS UNITS:
    1. Grams
    2. Kilograms
    3. Milligrams
    4. Ounces
    5. Pounds
    6. Micrograms
    7. Metric Tons
    8. Stones
    9. US Tons""")
                start_unit = input("\nSelect Starting unit (1-9): ")
                end_unit = input("\nSelect destination unit (1-9): ")
                num = input("Enter the number to convert: ")

                try:
                    value = float(num)
                except ValueError:
                    print("Invalid number. Please try again.")
                    continue

                match (start_unit):
                    case "1":
                        start_unit_name = "Grams"
                        start_unit = 1

                    case "2":
                        start_unit_name = "Kilograms"
                        start_unit = 1000

                    case "3":
                        start_unit_name = "Milligrams"
                        start_unit = 0.001

                    case "4":
                        start_unit_name = "Ounces"
                        start_unit = 28.349523125

                    case "5":
                        start_unit_name = "Pounds"
                        start_unit = 453.59237
                    case "6":
                        start_unit_name = "Micrograms"
                        start_unit = 0.000001
                    case "7":
                        start_unit_name = "Metric Tons"
                        start_unit = 1000000
                    case "8":
                        start_unit_name = "Stones"
                        start_unit = 6350.29318
                    case "9":
                        start_unit_name = "US Tons"
                        start_unit = 907184.74

                    case _:
                        print("Invalid starting unit.")
                        continue

                match (end_unit):
                    case "1":
                        end_unit_name = "Grams"
                        end_unit_value = 1

                    case "2":
                        end_unit_name = "Kilograms"
                        end_unit_value = 1000

                    case "3":
                        end_unit_name = "Milligrams"
                        end_unit_value = 0.001

                    case "4":
                        end_unit_name = "Ounces"
                        end_unit_value = 28.349523125

                    case "5":
                        end_unit_name = "Pounds"
                        end_unit_value = 453.59237
                    case "6":
                        end_unit_name = "Micrograms"
                        end_unit_value = 0.000001
                    case "7":
                        end_unit_name = "Metric Tons"
                        end_unit_value = 1000000
                    case "8":
                        end_unit_name = "Stones"
                        end_unit_value = 6350.29318
                    case "9":
                        end_unit_name = "US Tons"
                        end_unit_value = 907184.74

                    case _:
                        print("Invalid destination unit.")
                        continue
                
                message = f'{num} {start_unit_name} is {value * start_unit / end_unit_value:.4f} {end_unit_name}.'
                print(message)
                history["Weight"].append(message)
                pass

            case "4":
                print("""\n LIQUID-VOLUME UNITS:
    1. Liters
    2. Milliliters
    3. Cups
    4. Fluid Ounces
    5. Gallons
    6. Teaspoons
    7. Tablespoons
    8. Pints
    9. Quarts""")
                start_unit = input("\nSelect starting unit (1-9): ")
                end_unit = input("Select destination unit (1-9): ")
                num = input("Enter the number to convert: ")

                try:
                    value = float(num)
                except ValueError:
                    print("Invalid number. Please try again.")
                    continue

                match (start_unit):
                    case "1":
                        start_unit_name = "Liters"
                        start_unit_value = 1
                    case "2":
                        start_unit_name = "Milliliters"
                        start_unit_value = 0.001
                    case "3":
                        start_unit_name = "Cups"
                        start_unit_value = 0.236588
                    case "4":
                        start_unit_name = "Fluid Ounces"
                        start_unit_value = 0.0295735
                    case "5":
                        start_unit_name = "Gallons"
                        start_unit_value = 3.78541
                    case "6":
                        start_unit_name = "Teaspoons"
                        start_unit_value = 0.00492892
                    case "7":
                        start_unit_name = "Tablespoons"
                        start_unit_value = 0.0147868
                    case "8":
                        start_unit_name = "Pints"
                        start_unit_value = 0.473176
                    case "9":
                        start_unit_name = "Quarts"
                        start_unit_value = 0.946353
                    case _:
                        print("Invalid starting unit.")
                        continue

                match (end_unit):
                    case "1":
                        end_unit_name = "Liters"
                        end_unit_value = 1
                    case "2":
                        end_unit_name = "Milliliters"
                        end_unit_value = 0.001
                    case "3":
                        end_unit_name = "Cups"
                        end_unit_value = 0.236588
                    case "4":
                        end_unit_name = "Fluid Ounces"
                        end_unit_value = 0.0295735
                    case "5":
                        end_unit_name = "Gallons"
                        end_unit_value = 3.78541
                    case "6":
                        end_unit_name = "Teaspoons"
                        end_unit_value = 0.00492892
                    case "7":
                        end_unit_name = "Tablespoons"
                        end_unit_value = 0.0147868
                    case "8":
                        end_unit_name = "Pints"
                        end_unit_value = 0.473176
                    case "9":
                        end_unit_name = "Quarts"
                        end_unit_value = 0.946353
                    case _:
                        print("Invalid destination unit.")
                        continue

                message = f'{num} {start_unit_name} is {value * start_unit_value / end_unit_value:.4f} {end_unit_name}.'
                print(message)
                history["Volume"].append(message)
                pass

            case "5":
                while True:
                    print("""\n CONVERSION HISTORY:
  1. Temperature
  2. Distance
  3. Weight
  4. Volume
  5. All Calculations
  6. Back to Main Menu""")

                    history_choice = input("\nSelect option (1-6): ")

                    categories = {
                        "1": "Temperature",
                        "2": "Distance",
                        "3": "Weight",
                        "4": "Volume"
                    }

                    if history_choice in categories:
                        category = categories[history_choice]
                        print(f"\n {category.upper()} HISTORY:")

                        if history[category]:
                            for index, calculation in enumerate(history[category], 1):
                                print(f"  {index}. {calculation}")
                        else:
                            print("No calculations found.")

                    elif history_choice == "5":
                        print("\n ALL CALCULATIONS:")
                        for category, calculations in history.items():
                            print(f"\n {category} History:")
                            if calculations:
                                for index, calculation in enumerate(calculations, 1):
                                    print(f"  {index}. {calculation}")
                            else:
                                print("  No calculations found.")

                    elif history_choice == "6":
                        break

                    else:
                        print("Invalid choice. Please try again.")

            case "6":
                print("Exiting...")
                flag = False
                break

            case _:
                print("Invalid choice. Please try again.")

        pass

main()

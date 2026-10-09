flag = True

def main():
    global flag
    while flag:
        print("""\n UNIT CONVERTER:
  1. Convert Temperature
  2. Convert Distance
  3. Convert Weight
  4. Convert Liquid-Volume
  5. Exit""")
        choice = input("\nSelect option (1-5): ")

        match choice:
            case "1":
                print("""\n TEMPERATURE UNITS:
  1. Celsius
  2. Fahrenheit
  3. Kelvin""")

                from_unit = input("\nSelect starting unit (1-3): ")
                to_unit = input("Select destination unit (1-3): ")

                num = input("Enter number to convert: ")

                if from_unit == "1" and to_unit == "2":
                    print(f'{num} degrees Celsius is {float(num) * 9/5 + 32:.4f} degrees Fahrenheit.')

                elif from_unit == "1" and to_unit == "3":
                    print(f'{num} degrees Celsius is {float(num) + 273.15:.4f} Kelvin.')

                elif from_unit == "2" and to_unit == "1":
                    print(f'{num} degrees Fahrenheit is {(float(num) - 32) * 5/9:.4f} degrees Celsius.')

                elif from_unit == "2" and to_unit == "3":
                    celsius = (float(num) - 32) * 5/9
                    print(f'{num} degrees Fahrenheit is {celsius + 273.15:.4f} Kelvin.')

                elif from_unit == "3" and to_unit == "1":
                    print(f'{num} Kelvin is {float(num) - 273.15:.4f} degrees Celsius.')

                elif from_unit == "3" and to_unit == "2":
                    celsius = float(num) - 273.15
                    print(f'{num} Kelvin is {celsius * 9/5 + 32:.4f} degrees Fahrenheit.')

                elif from_unit == to_unit:
                    if from_unit == "1":
                        print(f'{num} degrees Celsius is {float(num):.4f} degrees Celsius.')
                    elif from_unit == "2":
                        print(f'{num} degrees Fahrenheit is {float(num):.4f} degrees Fahrenheit.')
                    elif from_unit == "3":
                        print(f'{num} Kelvin is {float(num):.4f} Kelvin.')
                    else:
                        print("Invalid temperature unit.")

                else:
                    print("Invalid temperature unit.")

                pass

            case "2":
                print("""\n DISTANCE UNITS:
    1. Milimeters
    2. Centimeters
    3. Meters
    4. Kilometers
    5. Inches
    6. Feet
    7. Yards
    8. Miles""")
                start_unit = input("\nSelect starting unit (1-8): ")
                end_unit = input("\nSelect destination unit (1-8): ")

                #print("Starting unit selected:", start_unit)
                #print("Destination unit selected:", end_unit)
                
                #print(f'{num} meters is {float(num) * 3.28084} feet.')

                if start_unit not in ("1", "2", "3", "4", "5", "6", "7", "8"):
                    print("Invalid starting unit.")
                    continue

                if end_unit not in ("1", "2", "3", "4", "5", "6", "7", "8"):
                    print("Invalid destination unit.")
                    continue

                num = input("Enter the number to convert: ")

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
                    case _:
                        print("Invalid destination unit.")
                print(f'{num} {start_unit_name} is {float(num) * start_unit_value / end_unit_value:.4f} {end_unit_name}.')

                pass

            case "3":
                print("""\n Wight and mass units:
    1. Grams
    2. Kilograms
    3. Milligrams
    4. Ounces
    5. Pounds""")
                start_units = input("\nSelect Starting unit (1-5):")
                end_unit = input("\nSelect destination unit (1-5)")
                num = input("Enter the number to convert: ")

                 match (start_unit):
                    case "1":
                        start_unit_name = "Grams"
                        start_unit_value = 1

                    case "2":
                        start_unit_name = "Kilograms"
                        start_unit_value = 1000

                    case "3":
                        start_unit_name = "Milligrams"
                        start_unit_value = 0.001

                    case "4":
                        start_unit_name = "Ounces"
                        start_unit_value = 28.349523125

                    case "5":
                        start_unit_name = "Pounds"
                        start_unit_value = 453.59237

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

                    case _:
                        print("Invalid destination unit.")
                        continue
                
                print(f'{num} {start_unit_name} is {float(num) * start_unit_value / end_unit_value:.4f} {end_unit_name}.')
                pass

            case "4":
                print("""\n LIQUID-VOLUME UNITS:
    1. Liters
    2. Milliliters
    3. Cups
    4. Fluid Ounces
    5. Gallons""")
                start_unit = input("\nSelect starting unit (1-5): ")
                end_unit = input("\nSelect destination unit (1-5): ")
                num = input("Enter the number to convert: ")

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
                    case _:
                        print("Invalid starting unit.")

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
                    case _:
                        print("Invalid destination unit.")
                print(f'{num} {start_unit_name} is {float(num) * start_unit_value / end_unit_value:.4f} {end_unit_name}.')
                pass

            case "5":
                print("Exiting...")
                flag = False
                break

            case _:
                print("Invalid choice. Please try again.")

        pass

main()

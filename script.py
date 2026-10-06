flag = True


def main():
    global flag

    while flag:
        print("""
 UNIT CONVERTER:
  1. Convert Temperature
  2. Convert Distance
  3. Convert Weight
  4. Convert Volume
  5. Exit""")

        choice = input("\nSelect option (1-5): ")

        match choice:
            case "1":
                print("""
 Temperature Units:
  1. Celsius
  2. Fahrenheit
  3. Kelvin""")

                from_unit = input("\nSelect starting unit (1-3): ")
                to_unit = input("Select destination unit (1-3): ")
                num = float(input("Enter number to convert: "))

                # Convert starting temperature to Celsius
                match from_unit:
                    case "1":
                        celsius = num
                        from_name = "Celsius"

                    case "2":
                        celsius = (num - 32) * 5 / 9
                        from_name = "Fahrenheit"

                    case "3":
                        celsius = num - 273.15
                        from_name = "Kelvin"

                    case _:
                        print("Invalid temperature unit.")
                        continue

                # Convert Celsius to destination unit
                match to_unit:
                    case "1":
                        result = celsius
                        to_name = "Celsius"

                    case "2":
                        result = (celsius * 9 / 5) + 32
                        to_name = "Fahrenheit"

                    case "3":
                        result = celsius + 273.15
                        to_name = "Kelvin"

                    case _:
                        print("Invalid temperature unit.")
                        continue

                print(
                    f"{num:.4f} degrees {from_name} is "
                    f"{result:.4f} degrees {to_name}."
                )

            case "2":
                num = input("Enter number: ")
                print(
                    f'{num} meters is '
                    f'{float(num) * 3.28084:.4f} feet.'
                )

            case "3":
                num = input("Enter the number to convert: ")
                print(
                    f'{num} kilograms is '
                    f'{float(num) * 2.20462:.4f} pounds.'
                )

            case "4":
                num = input("Enter the number to convert: ")
                print(
                    f'{num} liters is '
                    f'{float(num) * 0.264172:.4f} gallons.'
                )

            case "5":
                print("Exiting...")
                flag = False
                break

            case _:
                print("Invalid choice. Please try again.")


main()
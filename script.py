

flag = True

def main():
  global flag
  while flag: 
    print("""\n UNIT CONVERTER:
  1. Convert Temperature
  2. Convert Distance
  3. Convert Weight
  4. Convert Volume
  5. Exit""")
    choice = input("\nSelect option (1-5): ")
    match choice:
      case "1":
        num = input("Enter number to convert: ")
        print(f'{num} degrees Celsius is {float(num) * 9/5 + 32} degrees Fahrenheit.')
        ### Finish Code of all permutations
        pass
      case "2":
        num = input("Enter number: ")
        print(f'{num} meters is {float(num) * 3.28084} feet.')
        pass
      case "3":
        num = input("Enter the number to convert: ")
        print(f'{num} kilograms is {float(num) * 2.20462} pounds.')
        pass
      case "4":
        num = input("Enter the number to convert: ")
        print(f'{num} liters is {float(num) * 0.264172} gallons.')
        pass
      case "5":
        print("Exiting...")
        flag = False
        break
      case _:
        print("Invalid choice. Please try again.")
    pass

main()
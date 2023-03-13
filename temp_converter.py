import temp_conversions

celsius = ['c',' c', 'celsius']
fahrenheit = ['f',' f', 'fahrenheit']
kelvin = ['k', ' k', 'kelvin']
while(1):
    try:
        prompt = input("Enter Temperature to be Converted with its unit: ")

        unit = prompt[-1:]
        num = float(prompt[:-1])

    except ValueError:
        print("Invalid Input. Please Try Again.")

    if unit.lower() in celsius:
        conv = input("Convert it into? [F, K]: ")
        if conv.lower() in fahrenheit:
            num = temp_conversions.celsius_to_fahrenheit(num)
            print("The conversion is: ", round(num, 2), " F")
        elif conv.lower() in kelvin:
            num = temp_conversions.celsius_to_kelvin(num)
            print("The conversion is: ", round(num, 2), " K")
        elif conv.lower() in celsius:
            print("Cannot convert Celsius to Celsius. Please Try Again.")
        else:
            print("Invalid Unit. Please Try Again.")
    elif unit.lower() in fahrenheit:
            conv = input("Convert it into? [C, K]: ")
            if conv.lower() in celsius:
                num = temp_conversions.fahrenheit_to_celsius(num)
                print("The conversion is: ", round(num, 2), " C")
            elif conv.lower() in kelvin:
                num = temp_conversions.fahrenheit_to_kelvin(num)
                print("The conversion is: ", round(num, 2), " K")
            elif conv.lower() in fahrenheit:
                print("Cannot convert Fahrenheit to Fahrenheit. Please Try Again.")
            else:
                print("Invalid Unit. Please Try Again.")
    elif unit.lower() in kelvin:
            conv = input("Convert it into? [C, F]: ")
            if conv.lower() in celsius:
                num = temp_conversions.kelvin_to_celsius(num)
                print("The conversion is: ", round(num, 2), " C")
            elif conv.lower() in fahrenheit:
                num = temp_conversions.kelvin_to_fahrenheit(num)
                print("The conversion is: ", round(num, 2), " F")
            elif conv.lower() in kelvin:
                print("Cannot convert Kelvin to Kelvin. Please Try Again.")
            else:
                print("Invalid Unit. Please Try Again.")
    else:
         print("Invalid Input. Please Try Again.")

    user_input = input("Would you like to convert again? (yes/no): ")
    yes_choices = ['yes', 'y', 'ye']
    no_choices = ['no', 'n', 'on']
    if user_input.lower() in yes_choices:
        continue
    elif user_input.lower() in no_choices:
        print("Thank you!")
        break
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    if from_unit == 'C':
        return value + 273.15 if to_unit == 'K' else (value * 9/5) + 32
    elif from_unit == 'F':
        return (value - 32) * 5/9 if to_unit == 'C' else (value - 32) * 5/9 + 273.15
    elif from_unit == 'K':
        return value - 273.15 if to_unit == 'C' else (value - 273.15) * 9/5 + 32
    else:
        raise ValueError("Invalid temperature unit. Please enter C, F, or K.")

def main():
    print("Temperature Unit Converter")

    # Get user input
    temperature = float(input("Enter temperature value: "))
    original_unit = input("Enter original temperature unit (C, F, K): ").upper()
    target_units = ['C', 'F', 'K']

    # Display the results
    for target_unit in target_units:
        converted_value = convert_temperature(temperature, original_unit, target_unit)
        print(f"{temperature} {original_unit} is equal to {converted_value:.2f} {target_unit}")

if __name__ == "__main__":
    main()
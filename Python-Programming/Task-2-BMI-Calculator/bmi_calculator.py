def calculate_bmi(weight, height):
    """
    Calculate BMI using weight in kilograms
    and height in meters.
    """
    bmi = weight / (height ** 2)
    return round(bmi, 2)


def get_bmi_category(bmi):
    """Return the BMI category."""

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal Weight"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"


def main():

    print("=" * 50)
    print("           OIBSIP BMI CALCULATOR")
    print("=" * 50)

    try:
        weight = float(input("\nEnter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("\nError: Weight and height must be greater than zero.")
            return

        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        print("\n" + "-" * 50)
        print(f"Weight       : {weight} kg")
        print(f"Height       : {height} m")
        print(f"BMI          : {bmi}")
        print(f"Category     : {category}")
        print("-" * 50)

    except ValueError:
        print("\nError: Please enter valid numeric values.")


if __name__ == "__main__":
    main()
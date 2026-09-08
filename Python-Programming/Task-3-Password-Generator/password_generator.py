import string
import secrets


def generate_password(length):
    """Generate a secure random password."""

    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = "".join(
        secrets.choice(characters)
        for _ in range(length)
    )

    return password


def main():

    print("=" * 55)
    print("        OIBSIP RANDOM PASSWORD GENERATOR")
    print("=" * 55)

    try:
        length = int(input("\nEnter password length: "))

        if length < 4:
            print("\nPassword length must be at least 4 characters.")
            return

        password = generate_password(length)

        print("\n" + "-" * 55)
        print(f"Generated Password : {password}")
        print(f"Password Length    : {length}")
        print("-" * 55)

    except ValueError:
        print("\nError: Please enter a valid number.")


if __name__ == "__main__":
    main()
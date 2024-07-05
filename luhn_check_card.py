def luhn_check(card_number):
    """
    Checks if a credit card number is valid using the Luhn algorithm.

    Parameters:
    card_number (str): The credit card number as a string of digits.

    Returns:
    bool: True if the credit card number is valid, False otherwise.
    """
    def digits_of(number):
        """Converts the number into a list of digits."""
        return [int(digit) for digit in str(number)]

    # Check that the input is a string of digits
    if not card_number.isdigit():
        raise ValueError("The card number should contain only digits.")

    # Get all digits of the card number
    digits = digits_of(card_number)

    # Get digits at odd positions from the end
    odd_digits = digits[-1::-2]

    # Get digits at even positions from the end
    even_digits = digits[-2::-2]

    # Initialize checksum with the sum of odd digits
    checksum = sum(odd_digits)

    # Double each even digit and sum the digits of the result
    checksum += sum(sum(digits_of(digit * 2)) for digit in even_digits)

    # The card is valid if the checksum is divisible by 10
    return checksum % 10 == 0

# Example usage
card_number = "4871450093666910"
if luhn_check(card_number):
    print("The card number is valid.")
else:
    print("The card number is not valid.")

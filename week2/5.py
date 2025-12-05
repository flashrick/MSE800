"""Week2 - Activity5 Simple OOP temperature converter."""
"""
Author: Wade Wang
Date: 05/12/2025
"""

"""Convert temperatures based on the prefix."""
class TemperatureConverter:
    def __init__(self, raw_value: str):
        # keep the original input for output reuse
        self.raw_value = raw_value.strip()
        # split into prefix and numeric part
        self.prefix = self.raw_value[:1]
        self.numeric_part = self.raw_value[1:]

    def is_valid(self) -> bool:
        # basic validation for length and numeric part
        if len(self.raw_value) < 2:
            return False
        try:
            float(self.numeric_part)
        except ValueError:
            return False
        return self.prefix in ("C", "F")

    def convert(self) -> str:
        # convert based on prefix
        value = float(self.numeric_part)
        if self.prefix == "F":
            converted = (value - 32) * 5 / 9
            return (
                f"{self.raw_value} degrees Fahrenheit is converted to "
                f"{converted:.2f} degrees Celsius"
            )
        converted = (value * 9 / 5) + 32
        return (
            f"{self.raw_value} degrees Celsius is converted to "
            f"{converted:.2f} degrees Fahrenheit"
        )


def main():
    is_valid = False
    while not is_valid:
        user_input = input("Enter the temperature (e.g., F51 or C11): ")
        converter = TemperatureConverter(user_input)
        is_valid = converter.is_valid()
        print("Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix.")
    print(converter.convert())
        


if __name__ == "__main__":
    main()

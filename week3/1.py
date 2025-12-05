"""
Author: Wade Wang
Date: 06/12/2025
Description: Week3 - Activity1 Develop an OOP code that reads the file and prints the output. Then, add functionality to count the number of * characters in the file.
"""

from pathlib import Path


class FileReader:
    def __init__(self, filename: str):
        # Always load the file next to this script so cwd does not matter
        self.file_path = Path(__file__).with_name(filename)
        self.content = self.file_path.read_text(encoding="utf-8")

    def print_content(self) -> None:
        # Output the file text
        print(self.content)

    def count_stars(self) -> None:
        # Print how many '*' characters
        print(f"Number of '*' characters: {self.content.count('*')}")

def main():
    file_reader = FileReader("demo_file.txt")
    file_reader.print_content()
    file_reader.count_stars()

        
if __name__ == "__main__":
    main()

# pylint: disable=C0103
"""
Number Conversion Program
This script reads numbers from a file and converts them to binary and
hexadecimal bases using basic algorithms.
"""

import sys
import time


def to_binary(n):
    """Converts an integer to binary string using basic algorithm."""
    if n == 0:
        return "0"
    is_negative = n < 0
    n = abs(int(n))
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return ("-" if is_negative else "") + binary


def to_hexadecimal(n):
    """Converts an integer to hexadecimal string using basic algorithm."""
    if n == 0:
        return "0"
    hex_chars = "01234567839ABCDEF"
    # Wait, hex_chars should be 16 chars: 0123456789ABCDEF
    hex_chars = "0123456789ABCDEF"
    is_negative = n < 0
    n = abs(int(n))
    hexa = ""
    while n > 0:
        hexa = hex_chars[n % 16] + hexa
        n //= 16
    return ("-" if is_negative else "") + hexa


def get_numbers_from_file(file_path):
    """Reads a file and extracts numbers, handling errors."""
    numbers = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    # Requirements say base base algorithms, usually means int
                    # conversions for bin/hex.
                    num = float(line)
                    # Convert to int for bitwise-like conversion if it's whole
                    numbers.append(int(num))
                except ValueError:
                    print(f"Error: Invalid data found: '{line}'")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    return numbers


def main():
    """Main function to execute the number conversion."""
    if len(sys.argv) < 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    start_time = time.time()

    data = get_numbers_from_file(file_path)

    if not data:
        print("No valid numbers found in the file.")
        elapsed_time = time.time() - start_time
        print(f"Execution Time: {elapsed_time:.4f} seconds")
        sys.exit(0)

    results = [
        "--- Conversion Results ---",
        f"File: {file_path}",
        f"{'Decimal':<15} {'Binary':<20} {'Hexadecimal':<15}",
        "-" * 52
    ]

    for num in data:
        bin_val = to_binary(num)
        hex_val = to_hexadecimal(num)
        results.append(f"{num:<15} {bin_val:<20} {hex_val:<15}")

    elapsed_time = time.time() - start_time
    results.append("-" * 52)
    results.append(f"Execution Time: {elapsed_time:.4f} seconds")

    # Print to screen
    for line in results:
        print(line)

    # Write to file, if exists it will be appended
    try:
        with open("ConvertionResults.txt", "a", encoding="utf-8") as out_file:
            for line in results:
                out_file.write(line + "\n")
    except IOError as e:
        print(f"Error writing to file: {e}")


if __name__ == "__main__":
    main()

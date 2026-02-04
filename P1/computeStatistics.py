# pylint: disable=C0103
"""
Compute Statistics Program
This script reads numbers from a file and computes descriptive statistics:
mean, median, mode, standard deviation, and variance.
"""

import sys
import time


def get_numbers_from_file(file_path):
    """Reads a file and extracts numbers, handling errors."""
    numbers = []
    errors = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    numbers.append(float(line))
                except ValueError:
                    errors.append(line)
                    print(f"Error: Invalid data found: '{line}'")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    return numbers, errors


def compute_mean(data):
    """Calculates the mean of a list of numbers."""
    if not data:
        return 0
    total = 0.0
    for x in data:
        total += x
    return total / len(data)


def compute_median(data):
    """Calculates the median of a list of numbers."""
    if not data:
        return 0
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]


def compute_mode(data):
    """Calculates the mode(s) of a list of numbers."""
    if not data:
        return 0
    counts = {}
    for x in data:
        counts[x] = counts.get(x, 0) + 1

    max_count = 0
    for count in counts.values():
        max_count = max(max_count, count)

    modes = [val for val, count in counts.items() if count == max_count]

    if len(modes) == len(data) and len(data) > 1:
        return "No unique mode"
    return modes[0] if len(modes) == 1 else modes


def compute_variance(data, mean):
    """Calculates the population variance."""
    if not data:
        return 0
    sum_sq_diff = 0.0
    for x in data:
        sum_sq_diff += (x - mean) ** 2
    return sum_sq_diff / len(data)


def compute_std_dev(variance):
    """Calculates the standard deviation."""
    return variance ** 0.5


def main():
    """Main function to execute the statistics computation."""
    if len(sys.argv) < 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    start_time = time.time()

    data, errors = get_numbers_from_file(file_path)

    if not data:
        print("No valid numbers found in the file.")
        elapsed_time = time.time() - start_time
        print(f"Execution Time: {elapsed_time:.4f} seconds")
        sys.exit(0)

    mean = compute_mean(data)
    median = compute_median(data)
    mode = compute_mode(data)
    variance = compute_variance(data, mean)
    std_dev = compute_std_dev(variance)

    elapsed_time = time.time() - start_time

    results = [
        "--- Statistics Results ---",
        f"File: {file_path}",
        f"Count: {len(data)}",
        f"Mean: {mean:.4f}",
        f"Median: {median:.4f}",
        f"Mode: {mode}",
        f"Standard Deviation: {std_dev:.4f}",
        f"Variance: {variance:.4f}",
        f"Errors: {errors}",
        f"Execution Time: {elapsed_time:.4f} seconds"
    ]

    # Print to screen
    for line in results:
        print(line)

    # Write to file, if exists it will be appended
    try:
        with open("StatisticsResults.txt", "a", encoding="utf-8") as out_file:
            for line in results:
                out_file.write(line + "\n")
    except IOError as e:
        print(f"Error writing to file: {e}")


if __name__ == "__main__":
    main()

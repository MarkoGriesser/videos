import sys

def is_binary_divisible_by_3(binary_str):
    odd_count = 0
    even_count = 0

    for index, bit in enumerate(reversed(binary_str)):
        if bit == '1':
            if index % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    difference = abs(odd_count - even_count)

    return difference % 3 == 0

if __name__ == "__main__":
    binary_number = sys.argv[1]

    if is_binary_divisible_by_3(binary_number):
        print(f"The binary number {binary_number} is divisible by 3.")
    else:
        print(f"The binary number {binary_number} is not divisible by 3.")


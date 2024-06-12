import sys

def is_binary_divisible_by_3(binary_str):
    decimal_number = int(binary_str, 2)
    
    return decimal_number % 3 == 0

if __name__ == "__main__":
    binary_number = sys.argv[1]

    if is_binary_divisible_by_3(binary_number):
        print(f"The binary number {binary_number} is divisible by 3.")
    else:
        print(f"The binary number {binary_number} is not divisible by 3.")


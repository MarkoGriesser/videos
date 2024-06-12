import sys

def is_binary_divisible_by_3(binary_str):
    state = 0

    for bit in binary_str:
        if bit == '0':
            if state == 0:
                state = 0
            elif state == 1:
                state = 2
            elif state == 2:
                state = 1
        elif bit == '1':
            if state == 0:
                state = 1
            elif state == 1:
                state = 0
            elif state == 2:
                state = 2

    return state == 0

if __name__ == "__main__":
    binary_number = sys.argv[1]

    if is_binary_divisible_by_3(binary_number):
        print(f"The binary number {binary_number} is divisible by 3.")
    else:
        print(f"The binary number {binary_number} is not divisible by 3.")


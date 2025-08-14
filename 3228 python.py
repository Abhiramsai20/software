import math

def solve_quadratic(a, b, c):
    """Solves the quadratic equation ax^2 + bx + c = 0 and returns the roots."""
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    else:
        return None

def stage_1_hardcoded():
    print("\n--- Stage 1: Hardcoded Variables ---")
    a, b, c = 1, -3, 2  # You can change these values
    print(f"Using a={a}, b={b}, c={c}")
    result = solve_quadratic(a, b, c)
    if result:
        print(f"Roots: {result[0]}, {result[1]}")
    else:
        print("No real roots.")

def stage_2_keyboard_input():
    print("\n--- Stage 2: Keyboard Input ---")
    try:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        result = solve_quadratic(a, b, c)
        if result:
            print(f"Roots: {result[0]}, {result[1]}")
        else:
            print("No real roots.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

def stage_3_file_single():
    print("\n--- Stage 3: File Input (Single Set) ---")
    try:
        with open('input_single.txt', 'r') as file:
            line = file.readline()
            a, b, c = map(float, line.strip().split())
            print(f"Read from file: a={a}, b={b}, c={c}")
            result = solve_quadratic(a, b, c)
            if result:
                print(f"Roots: {result[0]}, {result[1]}")
            else:
                print("No real roots.")
    except FileNotFoundError:
        print("File 'input_single.txt' not found.")
    except ValueError:
        print("Invalid data format in file.")

def stage_4_file_multiple():
    print("\n--- Stage 4: File Input (Multiple Sets) ---")
    try:
        with open('input_multiple.txt', 'r') as file:
            for idx, line in enumerate(file, 1):
                try:
                    a, b, c = map(float, line.strip().split())
                    print(f"\nEquation {idx}: a={a}, b={b}, c={c}")
                    result = solve_quadratic(a, b, c)
                    if result:
                        print(f"  Roots: {result[0]}, {result[1]}")
                    else:
                        print("  No real roots.")
                except ValueError:
                    print(f"  Invalid data format on line {idx}.")
    except FileNotFoundError:
        print("File 'input_multiple.txt' not found.")

# -------------------------------
# Run all stages
# -------------------------------
if __name__ == "__main__":
    stage_1_hardcoded()
    stage_2_keyboard_input()
    stage_3_file_single()
    stage_4_file_multiple()

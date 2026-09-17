#!/usr/bin/env python3

def main() -> None:
    print("=== Garden Error Types Demo ===")
    print("Testing operation 0...")
    test_error_types(0)
    print("Testing operation 1...")
    test_error_types(1)
    print("Testing operation 2...")
    test_error_types(2)
    print("Testing operation 3...")
    test_error_types(3)
    print("Testing operation 4...")
    test_error_types(4)
    print()
    print("All error types tested successfully!")


def test_error_types(operation_number: int) -> None:
    try:
        garden_operations(operation_number)
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        if isinstance(e, ValueError):
            print(f"Caught ValueError: {e}")
        elif isinstance(e, ZeroDivisionError):
            print(f"Caught ZeroDivisionError: {e}")
        elif isinstance(e, FileNotFoundError):
            print(f"Caught FileNotFoundError: {e}")
        elif isinstance(e, TypeError):
            print(f"Caught TypeError: {e}")


def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        42 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "abc" + 42
    else:
        print("Operation completed succesfully")


if __name__ == "__main__":
    main()

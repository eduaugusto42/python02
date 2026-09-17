#!/usr/bin/env python3

def main() -> None:
    print("=== Garden Temperature ===")
    print()
    print("Input data is '25'")
    test_temperature("25")
    print()
    print("Input data is 'abc'")
    test_temperature("abc")
    print()
    print("All tests completed - program didn't crash!")


def test_temperature(temp_str: str) -> None:
    try:
        i = input_temperature(temp_str)
        print(f"Temperature is now {i}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


def input_temperature(temp_str: str) -> int:
    return int(temp_str)


if __name__ == "__main__":
    main()

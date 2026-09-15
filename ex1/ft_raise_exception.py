#!/usr/bin/env python3 

def test_temperature(temp_str: str) -> None:
    try:
        i = input_temperature(temp_str)
        print(f"Temperature is now {i}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

def input_temperature(temp_str: str) -> int:
    i = int(temp_str)
    if i > 40:
        raise Exception(f"{i} is too hot for plants (max 40°C)")
    elif i < 0:
        raise Exception(f"{i} is too cold for plants (min 0°C)")
    return i

def main():
    print("=== Garden Temperature Checker ===")
    print()
    print("Input data is '25'")
    test_temperature("25")
    print()
    print("Input data is 'abc'")
    test_temperature("abc")
    print()
    print("Input data is '100'")
    test_temperature("100")
    print()
    print("Input data is '-50'")
    test_temperature("-50")
    print()
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    main()



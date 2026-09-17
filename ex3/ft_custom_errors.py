#!/usr/bin/env python3

def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    test_plant_error("The tomato plant is wilting!")
    print()
    print("Testing WaterError...")
    test_water_error("Not enough water in the tank!")
    print()
    print("Testing catching all garden errors...")
    test_garden_error(0, "The tomato plant is wilting!")
    test_garden_error(1, "Not enough water in the tank!")
    print()
    print("All custom error types work correctly!")


class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)


def test_plant_error(s: str) -> None:
    try:
        raise PlantError(s)
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def test_water_error(s: str) -> None:
    try:
        raise WaterError(s)
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def test_garden_error(op: int, s: str) -> None:
    if op == 0:
        try:
            raise PlantError(s)
        except GardenError as e:
            print(f"Caught GardenError: {e}")
    elif op == 1:
        try:
            raise WaterError(s)
        except GardenError as e:
            print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    main()

def get_car_positions(car_type, direction):
    """Get positions for cars or trucks based on user input."""
    cars = {}
    print(f"Enter {car_type} {direction} (type '-1' to stop):")
    while True:
        name = input(f"Enter the name of the {car_type} (e.g., 'orange-car'): ")
        if name == "-1":
            break
        try:
            x = int(input(f"Enter the starting x-coordinate for {name} (e.g., 0): "))
            y = int(input(f"Enter the starting y-coordinate for {name} (e.g., 0): "))
            if direction == "vertical":
                cars[name] = (f"cube-x{x}-y{y}", f"cube-x{x}-y{y+1}")
            elif direction == "horizontal":
                cars[name] = (f"cube-x{x}-y{y}", f"cube-x{x+1}-y{y}")
            elif car_type == "truck" and direction == "vertical":
                cars[name] = [f"cube-x{x}-y{y}", f"cube-x{x}-y{y+1}", f"cube-x{x}-y{y+2}"]
            elif car_type == "truck" and direction == "horizontal":
                cars[name] = [f"cube-x{x}-y{y}", f"cube-x{x+1}-y{y}", f"cube-x{x+2}-y{y}"]
        except ValueError:
            print("Invalid input, please enter integers for coordinates.")
            continue
    return cars

def main():
    print("Welcome to the Red Car Problem Generator!")
    name = input("Enter the name of the problem: ")

    print("\n-- Vertical Cars --")
    cars_vertical = get_car_positions("car", "vertical")

    print("\n-- Horizontal Cars --")
    cars_horizontal = get_car_positions("car", "horizontal")

    print("\n-- Vertical Trucks --")
    trucks_vertical = get_car_positions("truck", "vertical")

    print("\n-- Horizontal Trucks --")
    trucks_horizontal = get_car_positions("truck", "horizontal")

    problem = {
        "name": name,
        "cars_vertical": cars_vertical,
        "cars_horizontal": cars_horizontal,
        "trucks_vertical": trucks_vertical,
        "trucks_horizontal": trucks_horizontal,
    }

    print("\nGenerated Problem:")
    import json
    print(json.dumps(problem, indent=4))

if __name__ == "__main__":
    main()

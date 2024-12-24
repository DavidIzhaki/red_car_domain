def get_vehicle_positions(vehicle_type, direction, grid_rows, grid_cols):
    """Get positions for vehicles based on user input."""
    vehicles = {}
    print(f"Enter {vehicle_type} {direction} (type '-1' to stop):")
    while True:
        name = input(f"Enter the name of the {vehicle_type} (e.g., 'red-car'): ")
        if name == "-1":
            break
        try:
            x = int(input(f"Enter the starting x-coordinate for {name} (e.g., 0): "))
            y = int(input(f"Enter the starting y-coordinate for {name} (e.g., 0): "))
            if direction == "vertical":
                if x + 1 >= grid_rows:
                    print(f"{name} cannot fit vertically within the grid.")
                    continue
                vehicles[name] = [(x, y), (x + 1, y)]
            elif direction == "horizontal":
                if y + 1 >= grid_cols:
                    print(f"{name} cannot fit horizontally within the grid.")
                    continue
                vehicles[name] = [(x, y), (x, y + 1)]
            elif vehicle_type == "truck" and direction == "vertical":
                if x + 2 >= grid_rows:
                    print(f"{name} cannot fit vertically within the grid.")
                    continue
                vehicles[name] = [(x, y), (x + 1, y), (x + 2, y)]
            elif vehicle_type == "truck" and direction == "horizontal":
                if y + 2 >= grid_cols:
                    print(f"{name} cannot fit horizontally within the grid.")
                    continue
                vehicles[name] = [(x, y), (x, y + 1), (x, y + 2)]
        except ValueError:
            print("Invalid input, please enter integers for coordinates.")
            continue
    return vehicles

def main():
    print("Welcome to the Rust Problem Generator!")
    rows = int(input("Enter the number of rows for the grid (e.g., 6): "))
    cols = int(input("Enter the number of columns for the grid (e.g., 6): "))

    print("\n-- Vertical Cars --")
    cars_vertical = get_vehicle_positions("car", "vertical", rows, cols)

    print("\n-- Horizontal Cars --")
    cars_horizontal = get_vehicle_positions("car", "horizontal", rows, cols)

    print("\n-- Vertical Trucks --")
    trucks_vertical = get_vehicle_positions("truck", "vertical", rows, cols)

    print("\n-- Horizontal Trucks --")
    trucks_horizontal = get_vehicle_positions("truck", "horizontal", rows, cols)

    goal = f"red-car at (2, {cols - 2}), red-car at (2, {cols - 1})"

    rust_code = [
        "use red_car_domain::*;",  # Adjust based on your Rust project module setup
        "",
        f"fn main() {{",
        f"    let mut grid = Grid::new({rows}, {cols});",
        "",
    ]

    for name, positions in cars_vertical.items():
        x, y = positions[0]
        rust_code.append(f"    let {name} = Vehicle::new(VehicleKind::VerticalCar, [{x}, {y}], \"{name}\".to_string());")
        rust_code.append(f"    grid.place_object(&{name}).unwrap();")
        rust_code.append(f"    grid.add_vehicle({name});")
        rust_code.append("")

    for name, positions in cars_horizontal.items():
        x, y = positions[0]
        rust_code.append(f"    let {name} = Vehicle::new(VehicleKind::HorizontalCar, [{x}, {y}], \"{name}\".to_string());")
        rust_code.append(f"    grid.place_object(&{name}).unwrap();")
        rust_code.append(f"    grid.add_vehicle({name});")
        rust_code.append("")

    for name, positions in trucks_vertical.items():
        x, y = positions[0]
        rust_code.append(f"    let {name} = Vehicle::new(VehicleKind::VerticalTruck, [{x}, {y}], \"{name}\".to_string());")
        rust_code.append(f"    grid.place_object(&{name}).unwrap();")
        rust_code.append(f"    grid.add_vehicle({name});")
        rust_code.append("")

    for name, positions in trucks_horizontal.items():
        x, y = positions[0]
        rust_code.append(f"    let {name} = Vehicle::new(VehicleKind::HorizontalTruck, [{x}, {y}], \"{name}\".to_string());")
        rust_code.append(f"    grid.place_object(&{name}).unwrap();")
        rust_code.append(f"    grid.add_vehicle({name});")
        rust_code.append("")

    rust_code.append(f"    // Define the goal: {goal}")
    rust_code.append("    grid.display();")
    rust_code.append("}")

    rust_code_output = "\n".join(rust_code)
    
    save_path = input("Enter the file name to save the Rust code (e.g., 'problem.rs'): ")
    if not save_path.endswith(".rs"):
        save_path += ".rs"
    with open(save_path, "w") as f:
        f.write(rust_code_output)
    print(f"Rust problem file saved to {save_path}.")

if __name__ == "__main__":
    main()

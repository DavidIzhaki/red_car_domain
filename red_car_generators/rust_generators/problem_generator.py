def generate_problem_file(problem_name, rows, cols, cars_vertical, cars_horizontal, trucks_vertical, trucks_horizontal):
    """Generate a Rust problem file."""
    goal = f"red-car at (2, {cols - 2}), red-car at (2, {cols - 1})"

    rust_code = [
        "use red_car_domain::*;",  # Adjust based on your Rust project module setup
        "",
        f"fn main() {{",
        f"    let mut grid = Grid::new({rows}, {cols});",
        "",
    ]

    # Handle vertical cars
    for name, position in cars_vertical.items():
        x, y = position
        rust_code.append(f"    let {name} = Vehicle::new(VehicleKind::VerticalCar, [{x}, {y}], \"{name}\".to_string());")
        rust_code.append(f"    grid.place_object(&{name}).unwrap();")
        rust_code.append(f"    grid.add_vehicle({name});")
        rust_code.append("")

    # Handle horizontal cars
    for name, position in cars_horizontal.items():
        x, y = position
        rust_code.append(f"    let {name} = Vehicle::new(VehicleKind::HorizontalCar, [{x}, {y}], \"{name}\".to_string());")
        rust_code.append(f"    grid.place_object(&{name}).unwrap();")
        rust_code.append(f"    grid.add_vehicle({name});")
        rust_code.append("")

    # Handle vertical trucks
    for name, position in trucks_vertical.items():
        x, y = position
        rust_code.append(f"    let {name} = Vehicle::new(VehicleKind::VerticalTruck, [{x}, {y}], \"{name}\".to_string());")
        rust_code.append(f"    grid.place_object(&{name}).unwrap();")
        rust_code.append(f"    grid.add_vehicle({name});")
        rust_code.append("")

    # Handle horizontal trucks
    for name, position in trucks_horizontal.items():
        x, y = position
        rust_code.append(f"    let {name} = Vehicle::new(VehicleKind::HorizontalTruck, [{x}, {y}], \"{name}\".to_string());")
        rust_code.append(f"    grid.place_object(&{name}).unwrap();")
        rust_code.append(f"    grid.add_vehicle({name});")
        rust_code.append("")

    rust_code.append(f"    // Define the goal: {goal}")
    rust_code.append("    grid.display();")
    rust_code.append("}")

    rust_code_output = "\n".join(rust_code)

    save_path = problem_name
    if not save_path.endswith(".rs"):
        save_path += ".rs"
    with open(save_path, "w") as f:
        f.write(rust_code_output)
    print(f"Rust problem file saved to {save_path}.")

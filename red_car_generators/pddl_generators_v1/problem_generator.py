def generate_problem_file(problem_name, grid_size, cars_vertical, cars_horizontal, trucks_vertical, trucks_horizontal):
    """Generate a PDDL problem file."""
    # Generate grid objects
    # Generate cube objects in rows
    cube_rows = [
        " ".join(
            [f"cube-x{col}-y{row}" for col in range(grid_size)]
        ) + " - cube ;; row " + str(row + 1)
        for row in range(grid_size)
    ]
    objects = ";;Cubes: Represent the individual grid cells in the 6x6 grid.\nEach cube has a unique identifier based on its coordinates (e.g., cube-x0-y0 for the cell at column 0, row 0).\n"
    objects += "\n".join(cube_rows) + "\n"

    cars = ";;Cars: Represents cars in the grid, identified by their names (e.g., red-car).\n"
    # Define cars and trucks
    cars += (
        " ".join(list(cars_vertical.keys()) + list(cars_horizontal.keys()))
        + " - car"
        if cars_vertical or cars_horizontal
        else ""
    )
    trucks = ";;Trucks:  Represents trucks in the grid, identified by their names (e.g., green-truck).\n"
    trucks += (
        " ".join(list(trucks_vertical.keys()) + list(trucks_horizontal.keys()))
        + " - truck"
        if trucks_vertical or trucks_horizontal
        else ""
    )

    # Add adjacency rules for cars (horizontal and vertical)

    car_adjacency = ("\n;;Car Adjacency: Defines the relationships between adjacent grid cells that cars can occupy.(Only 2 cubes)\n"
                     ";;Horizontal adjacency: Specifies which cells are next to each other horizontally in the same row.\n"
                     ";;Example: (adjacent-horizontal-car cube-x0-y0 cube-x1-y0)\n"
                     ";;Vertical adjacency: Specifies which cells are next to each other vertically in the same column.\n"
                     ";;Example: (adjacent-vertical-car cube-x0-y0 cube-x0-y1)\n\n"
                     ";; Horizontal Car Adjacency\n")
    car_adjacency += "\n".join(
        f"(adjacent-horizontal-car cube-x{col}-y{row} cube-x{col + 1}-y{row})"
        for row in range(grid_size) for col in range(grid_size - 1)
    )
    car_adjacency += "\n\n;; Vertical Car Adjacency\n" + "\n".join(
        f"(adjacent-vertical-car cube-x{col}-y{row} cube-x{col}-y{row + 1})"
        for col in range(grid_size) for row in range(grid_size - 1)
    )

    # Add adjacency rules for trucks (horizontal and vertical)

    truck_adjacency = ("\n\n;;Truck Adjacency: Defines the relationships between groups of grid cells that trucks can occupy.\n"
                       ";;Horizontal adjacency: Specifies groups of three consecutive cells in the same row that trucks can occupy.\n"
                       ";;Example: (adjacent-horizontal-truck cube-x0-y0 cube-x1-y0 cube-x2-y0)\n"
                       ";;Vertical adjacency: Specifies groups of three consecutive cells in the same column that trucks can occupy.\n"
                       ";;Example: (adjacent - vertical - truck cube-x0-y0 cube-x0-y1 cube-x0-y2)\n\n"
                       ";; Horizontal Truck Adjacency\n")

    truck_adjacency += "\n".join(
        f"(adjacent-horizontal-truck cube-x{col}-y{row} cube-x{col + 1}-y{row} cube-x{col + 2}-y{row})"
        for row in range(grid_size) for col in range(grid_size - 2)
    )
    truck_adjacency += "\n\n;; Horizontal Truck Adjacency\n" + "\n".join(
        f"(adjacent-vertical-truck cube-x{col}-y{row} cube-x{col}-y{row + 1} cube-x{col}-y{row + 2})"
        for col in range(grid_size) for row in range(grid_size - 2)
    )

    # Combine all adjacency rules
    adjacency = f"{car_adjacency}\n{truck_adjacency}"



    # Initial state for clear cells
    occupied_positions = set()
    init = "\n;;Car&Trucks Initial Position: \n"

    # Add positions for horizontal cars
    for car, (start, end) in cars_horizontal.items():
        init += f"\n(at-car-horizontal {car} {start} {end})"
        init += f"\n(not (clear {start}))\n(not (clear {end}))"
        occupied_positions.update([start, end])

    # Add positions for vertical cars
    for car, (start, end) in cars_vertical.items():
        init += f"\n(at-car-vertical {car} {start} {end})"
        init += f"\n(not (clear {start}))\n(not (clear {end}))"
        occupied_positions.update([start, end])

    # Add positions for horizontal trucks
    for truck, cubes in trucks_horizontal.items():
        init += f"\n(at-truck-horizontal {truck} {' '.join(cubes)})"
        for cube in cubes:
            init += f"\n(not (clear {cube}))"
            occupied_positions.add(cube)

    # Add positions for vertical trucks
    for truck, cubes in trucks_vertical.items():
        init += f"\n(at-truck-vertical {truck} {' '.join(cubes)})"
        for cube in cubes:
            init += f"\n(not (clear {cube}))"
            occupied_positions.add(cube)

    # Add remaining clear positions
    all_positions = {f"cube-x{col}-y{row}" for row in range(grid_size) for col in range(grid_size)}
    clear_positions = all_positions - occupied_positions
    for pos in clear_positions:
        init += f"\n(clear {pos})"



    # Add goal (always the same for all problems)
    goal = "(at-car-horizontal red-car cube-x4-y2 cube-x5-y2)"

    # Combine everything into the problem file
    problem_content = f"""(define (problem {problem_name})
(:domain RedCar)
(:objects
{objects}
{cars}
{trucks}
)
(:init
{adjacency}
{init}

)
(:goal
    {goal}
))
"""

    # Save the file
    file_path = f"{problem_name}.pddl"
    with open(file_path, "w") as f:
        f.write(problem_content)
    print(f"PDDL problem file '{file_path}' generated successfully!")

mod red_car_domain;
use red_car_domain::*;
mod search;
use search::a_star;

fn main() {
    // Load the problem definition from the `problems` directory
    include!("./problems/Red_Car_Problem1_Beginner.rs");

    // Ensure the problem grid is initialized properly
    let problem_grid = problem();

    // Display the initial grid
    println!("Initial Grid:");
    problem_grid.display();

    // Solve the problem using A* search
    match a_star(problem_grid) {
        Some(path) => {
            println!("Solution Found:");
            for (i, step) in path.iter().enumerate() {
                println!("Step {}:", i + 1);
                step.display();
            }
        }
        None => {
            println!("No solution found.");
        }
    }
}

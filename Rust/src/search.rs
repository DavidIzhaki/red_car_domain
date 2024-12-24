use crate::red_car_domain::Grid; // Import Grid from red_car_domain.rs
use crate::red_car_domain::HorizontalCar;
use crate::red_car_domain::Vehicle; // Import the Vehicle trait
use std::cmp::Ordering;
use std::collections::{BinaryHeap, HashMap}; // Import HorizontalCar

#[derive(Clone, Debug)]
pub struct AStarNode {
    pub grid: Grid,
    pub cost: usize,                    // g: Cost to reach this grid
    pub heuristic: usize,               // h: Heuristic to goal
    pub parent: Option<Box<AStarNode>>, // To reconstruct the path later
    pub move_description: String,       // Store the move description to track the path
}

impl AStarNode {
    pub fn new(
        grid: Grid,
        cost: usize,
        heuristic: usize,
        parent: Option<Box<AStarNode>>,
        move_description: String,
    ) -> Self {
        AStarNode {
            grid,
            cost,
            heuristic,
            parent,
            move_description,
        }
    }

    pub fn total_cost(&self) -> usize {
        self.cost + self.heuristic
    }
}

impl PartialEq for AStarNode {
    fn eq(&self, other: &Self) -> bool {
        // Compare `AStarNode` based on the grid and move description
        self.grid == other.grid && self.move_description == other.move_description
    }
}

impl Eq for AStarNode {}

// Implementing `Ord` and `PartialOrd` for AStarNode to use BinaryHeap for the priority queue
impl Ord for AStarNode {
    fn cmp(&self, other: &Self) -> Ordering {
        other.total_cost().cmp(&self.total_cost()) // Reverse to get a min-heap
    }
}

impl PartialOrd for AStarNode {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

// Heuristic function (you can adjust it based on your problem)
fn heuristic(grid: &Grid) -> usize {
    0 // Placeholder, adjust as needed
}

fn is_goal_reached(grid: &Grid) -> bool {
    // Check if the red car is at the goal position (2, m-2) and (2, m-1)
    for object in &grid.objects {
        if let Some(car) = object.as_any().downcast_ref::<HorizontalCar>() {
            if car.name() == "Red Car" {
                let positions = car.positions();
                if positions.contains(&(2, grid.col_size - 2))
                    && positions.contains(&(2, grid.col_size - 1))
                {
                    return true; // Goal reached
                }
            }
        }
    }
    false // Goal not reached
}

// The main A* function
pub fn a_star(start: Grid) -> Option<Vec<Grid>> {
    let mut open_list = BinaryHeap::new();
    let mut closed_list = HashMap::new();

    let start_node = AStarNode::new(start.clone(), 0, heuristic(&start), None, String::new());
    open_list.push(start_node);

    while let Some(current_node) = open_list.pop() {
        // Check if we've reached the goal
        if is_goal_reached(&current_node.grid) {
            let mut path = Vec::new();
            let mut node = Some(current_node);

            // Reconstruct the path from goal to start
            while let Some(n) = node {
                path.push(n.grid);
                node = n.parent;
            }

            path.reverse(); // Reverse to get path from start to goal
            return Some(path); // Return the reconstructed path
        }

        // Add current node to closed list
        closed_list.insert(current_node.grid.clone(), current_node.cost);

        // Generate successors (using the existing Grid methods)
        let successors = current_node.grid.generate_moves(); // This method generates valid moves

        for (new_grid, move_description) in successors {
            let cost = current_node.cost + 1; // Assume each move has a cost of 1
            let heuristic_value = heuristic(&new_grid);
            let total_cost = cost + heuristic_value;

            if !closed_list.contains_key(&new_grid) || cost < *closed_list.get(&new_grid).unwrap() {
                let successor_node = AStarNode::new(
                    new_grid,
                    cost,
                    heuristic_value,
                    Some(Box::new(current_node.clone())),
                    move_description,
                );
                open_list.push(successor_node);
            }
        }
    }

    None // No path found
}

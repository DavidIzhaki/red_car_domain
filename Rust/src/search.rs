use std::collections::{BinaryHeap, HashMap};
use std::cmp::Ordering;
use crate::red_car_domain::{Grid, VehicleKind, Vehicle};

#[derive(Clone, Debug)]
struct AStarNode {
    grid: Grid,
    cost: usize,                    // g(n): Cost to reach this grid
    heuristic: usize,               // h(n): Estimated cost to goal
    parent: Option<Box<AStarNode>>, // Pointer to parent node for path reconstruction
    move_description: String,       // Description of the move leading to this state
}

impl AStarNode {
    fn new(
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

    fn total_cost(&self) -> usize {
        self.cost + self.heuristic
    }
}

impl PartialEq for AStarNode {
    fn eq(&self, other: &Self) -> bool {
        self.grid == other.grid
    }
}

impl Eq for AStarNode {}

impl PartialOrd for AStarNode {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for AStarNode {
    fn cmp(&self, other: &Self) -> Ordering {
        other.total_cost().cmp(&self.total_cost()) // Reverse to create a min-heap
    }
}

fn heuristic(grid: &Grid) -> usize {
    // for object in &grid.objects {
    //     if object.kind == VehicleKind::HorizontalCar && object.name == "RC" {
    //         let positions = object.positions();
    //         let rightmost_pos = positions.iter().map(|pos| pos[1]).max().unwrap_or(0);
    //         return grid.col_size - rightmost_pos - 1; // Distance to the right edge
    //     }
    // }
    0 // Default heuristic if red car not found
}

fn is_goal_reached(grid: &Grid) -> bool {
    for object in &grid.objects {
        if object.kind == VehicleKind::HorizontalCar && object.name == "RC" {
            let positions = object.positions();
            return positions.contains(&(2, grid.col_size - 2)) &&
                   positions.contains(&(2, grid.col_size - 1));
        }
    }
    false
}

pub fn a_star(start: Grid) -> Option<Vec<Grid>> {
    let mut open_list = BinaryHeap::new();
    let mut closed_list = HashMap::new();

    let start_node = AStarNode::new(start.clone(), 0, heuristic(&start), None, String::new());
    open_list.push(start_node);

    while let Some(current_node) = open_list.pop() {
        // Check if the goal is reached
        if is_goal_reached(&current_node.grid) {
            let mut path = Vec::new();
            let mut node = Some(current_node);

            while let Some(n) = node {
                path.push(n.grid);
                node = n.parent.map(|p| *p);
            }

            path.reverse();
            return Some(path);
        }

        closed_list.insert(current_node.grid.clone(), current_node.cost);

        // Generate successors
        let successors = current_node.grid.generate_moves();

        for (new_grid, move_description) in successors {
            let new_cost = current_node.cost + 1;

            if let Some(&existing_cost) = closed_list.get(&new_grid) {
                if new_cost >= existing_cost {
                    continue;
                }
            }

            let successor_node = AStarNode::new(
                new_grid,
                new_cost,
                heuristic(&new_grid),
                Some(Box::new(current_node.clone())),
                move_description,
            );

            open_list.push(successor_node);
        }
    }

    None // No path found
}

use std::fmt;
#[derive(Clone)] 
pub struct Grid {
    pub row_size: usize,
    pub col_size: usize,                 // Size of the grid (n x n)
    pub cells: Vec<Vec<Option<String>>>, // 2D grid holding objects like "BC" or "RT"
    pub objects: Vec<Box<dyn Vehicle>>,
}

impl fmt::Debug for Grid {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(
            f,
            "Grid {{ row_size: {}, col_size: {}, objects: {:?} }}",
            self.row_size, self.col_size, self.objects
        )
    }
}

impl fmt::Debug for Box<dyn Vehicle> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Downcast the `Box<dyn Vehicle>` to a concrete type (e.g., HorizontalCar)
        if let Some(car) = self.as_any().downcast_ref::<HorizontalCar>() {
            write!(
                f,
                "HorizontalCar {{ name: {}, fixed_x: {}, start_y: {} }}",
                car.name, car.fixed_x, car.start_y
            )
        } else if let Some(car) = self.as_any().downcast_ref::<VerticalCar>() {
            write!(
                f,
                "VerticalCar {{ name: {}, start_x: {}, fixed_y: {} }}",
                car.name, car.start_x, car.fixed_y
            )
        } else if let Some(truck) = self.as_any().downcast_ref::<HorizontalTruck>() {
            write!(
                f,
                "HorizontalTruck {{ name: {}, fixed_x: {}, start_y: {} }}",
                truck.name, truck.fixed_x, truck.start_y
            )
        } else if let Some(truck) = self.as_any().downcast_ref::<VerticalTruck>() {
            write!(
                f,
                "VerticalTruck {{ name: {}, start_x: {}, fixed_y: {} }}",
                truck.name, truck.start_x, truck.fixed_y
            )
        } else {
            write!(f, "Unknown Vehicle")
        }
    }
}

impl Grid {
// Constructor to create a new grid
pub fn new(row_size: usize, col_size: usize) -> Self {
    Self {
        row_size,
        col_size,
        cells: vec![vec![None; col_size]; row_size], // Initialize with None
        objects: vec![],
    }
}

// Display the grid
pub fn display(&self) {
    for row in &self.cells {
        for cell in row {
            match cell {
                Some(obj) => print!("{} ", obj), // Print object
                None => print!(". "),            // E`mpty cell
            }
        }
        println!(); // Newline for each row
    }
}

    pub fn place_object<T>(&mut self, object: &T) -> Result<String, String>
    where
        T: Vehicle, // Require the object to implement the Vehicle trait
    {
        // Check if all positions are free and within bounds
        for &(x, y) in &object.positions() {
            if x >= self.row_size || y >= self.col_size {
                return Err("Object is out of bounds.".to_string());
            }
            if self.cells[x][y].is_some() {
                return Err(format!("Cell ({}, {}) is already occupied.", x, y));
            }
        }

        // Place the object in the grid
        for &(x, y) in &object.positions() {
            self.cells[x][y] = Some(object.name().to_string());
        }

        let positions = object
            .positions()
            .iter()
            .map(|(x, y)| format!("[{}, {}]", x, y))
            .collect::<Vec<_>>() // Collect formatted strings into a vector
            .join(", "); // Join them with ", "

        Ok(format!("{} placed in {}", object.name(), positions))
    }

    pub fn generate_moves(&self) -> Vec<(Grid, String)> {
        let mut moves = Vec::new();

        // Iterate over all objects in the grid
        for boxi in &self.objects {
            let object = &**boxi;
            // Check all possible moves for the object
            for (new_grid, move_description) in self.get_object_moves(object) {
                moves.push((new_grid, move_description)); // Only return the new grid and description
            }
        }
        moves
    }

    pub fn get_object_moves(&self, object: &dyn Vehicle) -> Vec<(Grid, String)> {
        let mut possible_moves = Vec::new();

        // Check if the object is a HorizontalVehicle
        if let Some(horizontal) = object.as_any().downcast_ref::<HorizontalCar>() {
            // Now you can call the move_left and move_right methods for HorizontalCar
            if let Some(new_grid) = self.try_move(horizontal, "left") {
                possible_moves.push((new_grid, format!("{} moved left", horizontal.name())));
            }
            if let Some(new_grid) = self.try_move(horizontal, "right") {
                possible_moves.push((new_grid, format!("{} moved right", horizontal.name())));
            }
        }
        // Check if the object is a HorizontalTruck
        else if let Some(horizontal) = object.as_any().downcast_ref::<HorizontalTruck>() {
            if let Some(new_grid) = self.try_move(horizontal, "left") {
                possible_moves.push((new_grid, format!("{} moved left", horizontal.name())));
            }
            if let Some(new_grid) = self.try_move(horizontal, "right") {
                possible_moves.push((new_grid, format!("{} moved right", horizontal.name())));
            }
        }
        // Check if the object is a VerticalVehicle
        else if let Some(vertical) = object.as_any().downcast_ref::<VerticalCar>() {
            if let Some(new_grid) = self.try_move(vertical, "up") {
                possible_moves.push((new_grid, format!("{} moved up", vertical.name())));
            }
            if let Some(new_grid) = self.try_move(vertical, "down") {
                possible_moves.push((new_grid, format!("{} moved down", vertical.name())));
            }
        }
        // Check if the object is a VerticalTruck
        else if let Some(vertical) = object.as_any().downcast_ref::<VerticalTruck>() {
            if let Some(new_grid) = self.try_move(vertical, "up") {
                possible_moves.push((new_grid, format!("{} moved up", vertical.name())));
            }
            if let Some(new_grid) = self.try_move(vertical, "down") {
                possible_moves.push((new_grid, format!("{} moved down", vertical.name())));
            }
        }

        possible_moves
    }

    pub fn try_move<T>(&self, object: &T, direction: &str) -> Option<Grid>
    where
        T: Vehicle + ?Sized, // Object must implement the Vehicle trait
    {
        // Create a mutable clone of the grid
        let mut new_grid = self.clone();

        // Find the object in the cloned grid by its name
        if let Some(obj) = new_grid
            .objects
            .iter_mut()
            .find(|o| o.name() == object.name())
        {
            // Try to downcast the object to a concrete type (HorizontalCar, HorizontalTruck, etc.)
            if let Some(horizontal) = obj.as_any().downcast_ref::<HorizontalCar>() {
                match direction {
                    "left" => {
                        if horizontal.move_left(&mut new_grid).is_ok() {
                            return Some(new_grid); // Return the updated grid if the move is valid
                        }
                    }
                    "right" => {
                        if horizontal.move_right(&mut new_grid).is_ok() {
                            return Some(new_grid);
                        }
                    }
                    _ => {}
                }
            } else if let Some(horizontal_truck) = obj.as_any().downcast_ref::<HorizontalTruck>() {
                // Check if the object is a HorizontalTruck
                match direction {
                    "left" => {
                        if horizontal_truck.move_left(&mut new_grid).is_ok() {
                            return Some(new_grid);
                        }
                    }
                    "right" => {
                        if horizontal_truck.move_right(&mut new_grid).is_ok() {
                            return Some(new_grid);
                        }
                    }
                    _ => {}
                }
            } else if let Some(vertical) = obj.as_any().downcast_ref::<VerticalCar>() {
                match direction {
                    "up" => {
                        if vertical.move_up(&mut new_grid).is_ok() {
                            return Some(new_grid);
                        }
                    }
                    "down" => {
                        if vertical.move_down(&mut new_grid).is_ok() {
                            return Some(new_grid);
                        }
                    }
                    _ => {}
                }
            } else if let Some(vertical_truck) = obj.as_any().downcast_ref::<VerticalTruck>() {
                // Check if the object is a VerticalTruck
                match direction {
                    "up" => {
                        if vertical_truck.move_up(&mut new_grid).is_ok() {
                            return Some(new_grid);
                        }
                    }
                    "down" => {
                        if vertical_truck.move_down(&mut new_grid).is_ok() {
                            return Some(new_grid);
                        }
                    }
                    _ => {}
                }
            }
        }

        None // If no valid move is found, return None
    }

}
use std::any::Any;
pub trait Vehicle {
    fn positions(&self) -> Vec<(usize, usize)>; // Get occupied positions
    fn name(&self) -> &str; // Get the object's name
    fn as_any(&self) -> &dyn Any; // Enables downcasting
}


pub trait HorizontalVehicle: Vehicle {
    fn move_left(&mut self, grid: &mut Grid) -> Result<String, String>;
    fn move_right(&mut self, grid: &mut Grid) -> Result<String, String>;
}

pub trait VerticalVehicle: Vehicle {
    fn move_up(&mut self, grid: &mut Grid) -> Result<String, String>;
    fn move_down(&mut self, grid: &mut Grid) -> Result<String, String>;
}


pub struct HorizontalCar {
    pub name: String,
    pub fixed_x: usize, // The fixed row coordinate
    pub start_y: usize, // The starting column coordinate
}



impl fmt::Debug for HorizontalCar {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(
            f,
            "HorizontalCar {{ name: {}, fixed_x: {}, start_y: {} }}",
            self.name, self.fixed_x, self.start_y
        )
    }
}

impl HorizontalCar {
    // Constructor for HorizontalCar
    pub fn new(fixed_x: usize, start_y: usize, name: String) -> Self {
        Self {
            name,
            fixed_x,
            start_y,
        }
    }
}

impl Vehicle for HorizontalCar {
    fn positions(&self) -> Vec<(usize, usize)> {
        vec![
            (self.fixed_x, self.start_y),
            (self.fixed_x, self.start_y + 1),
        ]
    }

    fn name(&self) -> &str {
        &self.name
    }

    fn as_any(&self) -> &dyn Any {
        self
    }
}

impl HorizontalVehicle for HorizontalCar {
    fn move_left(&mut self, grid: &mut Grid) -> Result<String, String> {
        if self.start_y == 0 || grid.cells[self.fixed_x][self.start_y - 1].is_some() {
            return Err("Cannot move left: Cell is occupied or out of bounds.".to_string());
        }

        // Clear the rightmost cell
        grid.cells[self.fixed_x][self.start_y + 1] = None;

        // Update state
        self.start_y -= 1;

        // Occupy the new leftmost cell
        grid.cells[self.fixed_x][self.start_y] = Some(self.name.clone());

        Ok(format!("{} moved left", self.name))
    }

    fn move_right(&mut self, grid: &mut Grid) -> Result<String, String> {
        // Check if the rightmost cell will go out of bounds or if it's occupied
        if self.start_y + 2 == grid.col_size || grid.cells[self.fixed_x][self.start_y + 2].is_some()
        {
            return Err("Cannot move right: Cell is occupied or out of bounds.".to_string());
        }

        // Clear the leftmost cell
        grid.cells[self.fixed_x][self.start_y] = None;

        // Update state
        self.start_y += 1;

        // Occupy the new rightmost cell
        grid.cells[self.fixed_x][self.start_y + 1] = Some(self.name.clone());

        Ok(format!("{} moved right", self.name))
    }
}

pub struct VerticalCar {
    pub name: String,
    pub start_x: usize, // The starting x-coordinate (row index)
    pub fixed_y: usize, // The fixed y-coordinate (column index)
}

impl VerticalCar {
    pub fn new(start_x: usize, fixed_y: usize, name: String) -> Self {
        Self {
            name,
            start_x,
            fixed_y,
        }
    }
}

impl fmt::Debug for VerticalCar {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(
            f,
            "VerticalCar {{ name: {}, start_x: {}, fixed_y: {} }}",
            self.name, self.start_x, self.fixed_y
        )
    }
}

impl Vehicle for VerticalCar {
    fn positions(&self) -> Vec<(usize, usize)> {
        vec![
            (self.start_x, self.fixed_y),
            (self.start_x + 1, self.fixed_y),
        ]
    }

    fn name(&self) -> &str {
        &self.name
    }
    fn as_any(&self) -> &dyn Any {
        self
    }
}

impl VerticalVehicle for VerticalCar {
    fn move_up(&mut self, grid: &mut Grid) -> Result<String, String> {
        // Check if the move is valid
        if self.start_x == 0 || grid.cells[self.start_x - 1][self.fixed_y].is_some() {
            return Err("Cannot move up: Cell is occupied or out of bounds.".to_string());
        }

        // Clear the bottom-most cell
        let bottom_x = self.start_x + 1;
        grid.cells[bottom_x][self.fixed_y] = None;

        // Update state
        self.start_x -= 1;

        // Occupy the new top-most cell
        grid.cells[self.start_x][self.fixed_y] = Some(self.name.clone());

        Ok(format!("{} moved up", self.name))
    }

    fn move_down(&mut self, grid: &mut Grid) -> Result<String, String> {
        // Check if the move is valid
        if self.start_x + 2 >= grid.row_size || grid.cells[self.start_x + 2][self.fixed_y].is_some()
        {
            return Err("Cannot move down: Cell is occupied or out of bounds.".to_string());
        }

        // Clear the top-most cell
        grid.cells[self.start_x][self.fixed_y] = None;

        // Update state
        self.start_x += 1;

        // Occupy the new bottom-most cell
        let bottom_x = self.start_x + 1;
        grid.cells[bottom_x][self.fixed_y] = Some(self.name.clone());

        Ok(format!("{} moved down", self.name))
    }
}

pub struct HorizontalTruck {
    pub name: String,
    pub fixed_x: usize, // The fixed row coordinate
    pub start_y: usize, // The starting column coordinate
}

impl Clone for HorizontalTruck {
    fn clone(&self) -> Self {
        HorizontalTruck {
            name: self.name.clone(),
            fixed_x: self.fixed_x,
            start_y: self.start_y,
        }
    }
}


impl HorizontalTruck {
    pub fn new(fixed_x: usize, start_y: usize, name: String) -> Self {
        Self {
            name,
            fixed_x,
            start_y,
        }
    }
}
impl fmt::Debug for HorizontalTruck {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(
            f,
            "HorizontalTruck {{ name: {}, fixed_x: {}, start_y: {} }}",
            self.name, self.fixed_x, self.start_y
        )
    }
}

impl Vehicle for HorizontalTruck {
    fn positions(&self) -> Vec<(usize, usize)> {
        vec![
            (self.fixed_x, self.start_y),
            (self.fixed_x, self.start_y + 1),
            (self.fixed_x, self.start_y + 2),
        ]
    }

    fn name(&self) -> &str {
        &self.name
    }
    fn as_any(&self) -> &dyn Any {
        self
    }
}

impl HorizontalVehicle for HorizontalTruck {
    fn move_left(&mut self, grid: &mut Grid) -> Result<String, String> {
        // Check if the move is valid
        if self.start_y == 0 || grid.cells[self.fixed_x][self.start_y - 1].is_some() {
            return Err("Cannot move left: Cell is occupied or out of bounds.".to_string());
        }

        // Clear the rightmost cell
        let right_y = self.start_y + 2;
        grid.cells[self.fixed_x][right_y] = None;

        // Update state
        self.start_y -= 1;

        // Occupy the new leftmost cell
        grid.cells[self.fixed_x][self.start_y] = Some(self.name.clone());

        Ok(format!("{} moved left", self.name))
    }

    fn move_right(&mut self, grid: &mut Grid) -> Result<String, String> {
        // Check if the move is valid
        if self.start_y + 3 == grid.col_size || grid.cells[self.fixed_x][self.start_y + 3].is_some()
        {
            return Err("Cannot move right: Cell is occupied or out of bounds.".to_string());
        }

        // Clear the leftmost cell
        grid.cells[self.fixed_x][self.start_y] = None;

        // Update state
        self.start_y += 1;

        // Occupy the new rightmost cell
        let right_y = self.start_y + 2;
        grid.cells[self.fixed_x][right_y] = Some(self.name.clone());

        Ok(format!("{} moved right", self.name))
    }
}

pub struct VerticalTruck {
    pub name: String,
    pub start_x: usize, // The starting row coordinate
    pub fixed_y: usize, // The fixed column coordinate
}
impl Clone for VerticalTruck {
    fn clone(&self) -> Self {
        VerticalTruck {
            name: self.name.clone(),
            start_x: self.start_x,
            fixed_y: self.fixed_y,
        }
    }
}

impl fmt::Debug for VerticalTruck {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(
            f,
            "VerticalTruck {{ name: {}, start_x: {}, fixed_y: {} }}",
            self.name, self.start_x, self.fixed_y
        )
    }
}
impl VerticalTruck {
    pub fn new(start_x: usize, fixed_y: usize, name: String) -> Self {
        Self {
            name,
            start_x,
            fixed_y,
        }
    }
}

impl Vehicle for VerticalTruck {
    fn positions(&self) -> Vec<(usize, usize)> {
        vec![
            (self.start_x, self.fixed_y),
            (self.start_x + 1, self.fixed_y),
            (self.start_x + 2, self.fixed_y),
        ]
    }

    fn name(&self) -> &str {
        &self.name
    }
    fn as_any(&self) -> &dyn Any {
        self
    }
}

impl VerticalVehicle for VerticalTruck {
    fn move_up(&mut self, grid: &mut Grid) -> Result<String, String> {
        // Check if the move is valid
        if self.start_x == 0 || grid.cells[self.start_x - 1][self.fixed_y].is_some() {
            return Err("Cannot move up: Cell is occupied or out of bounds.".to_string());
        }

        // Clear the bottom-most cell
        let bottom_x = self.start_x + 2;
        grid.cells[bottom_x][self.fixed_y] = None;

        // Update state
        self.start_x -= 1;

        // Occupy the new top-most cell
        grid.cells[self.start_x][self.fixed_y] = Some(self.name.clone());

        Ok(format!("{} moved up", self.name))
    }

    fn move_down(&mut self, grid: &mut Grid) -> Result<String, String> {
        // Check if the move is valid
        if self.start_x + 3 >= grid.row_size || grid.cells[self.start_x + 3][self.fixed_y].is_some()
        {
            return Err("Cannot move down: Cell is occupied or out of bounds.".to_string());
        }

        // Clear the top-most cell
        grid.cells[self.start_x][self.fixed_y] = None;

        // Update state
        self.start_x += 1;

        // Occupy the new bottom-most cell
        let bottom_x = self.start_x + 2;
        grid.cells[bottom_x][self.fixed_y] = Some(self.name.clone());

        Ok(format!("{} moved down", self.name))
    }
}

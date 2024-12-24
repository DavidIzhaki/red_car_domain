#[derive(Clone,Debug)]
pub struct Grid {
    pub row_size: usize,
    pub col_size: usize,                 // Size of the grid (n x m)
    pub cells: Vec<Vec<Option<String>>>, // 2D grid holding objects like "BC" or "RT"
   pub objects: Vec<Vehicle>,
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
    pub fn display(&self) {
        for row in &self.cells {
            for cell in row {
                match cell {
                    Some(obj) => print!("{} ", obj), // Print object
                    None => print!(".. "),           // E`mpty cell
                }
            }
            println!(); // Newline for each row
        }
    }

    fn update(
        &mut self,
        old_positions: Vec<[usize; 2]>,
        new_positions: Vec<[usize; 2]>,
        name: String,
    ) {
        // Remove vehicle from old position
        for pos in old_positions {
            self.cells[pos[0]][pos[1]] = None;
        }
        for pos in new_positions {
            self.cells[pos[0]][pos[1]] = Some(name.to_string());
        }

        // Place the vehicle at the new position
    }

    fn add_vehicle(&mut self, vehicle: Vehicle) {
        self.objects.push(vehicle);
    }

    fn place_object(&mut self, object: &Vehicle) -> Result<String, String> {
        let positions = &object.positions();
        // Check if all positions are free and within bounds
        for &[x, y] in positions {
            if x >= self.row_size || y >= self.col_size {
                return Err("Object is out of bounds.".to_string());
            }
            if self.cells[x][y].is_some() {
                return Err(format!("Cell ({}, {}) is already occupied.", x, y));
            }
        }

        // Place the object in the grid
        for &[x, y] in positions {
            self.cells[x][y] = Some(object.name().to_string());
        }

        let positions = object
            .positions()
            .iter()
            .map(|[x, y]| format!("[{}, {}]", x, y))
            .collect::<Vec<_>>() // Collect formatted strings into a vector
            .join(", "); // Join them with ", "

        Ok(format!("{} placed in {}", object.name(), positions))
    }

    pub fn generate_moves(&self) -> Vec<(Grid, String)> {
        let mut new_grids = Vec::new();

        for object in &self.objects {
            let mut new_grid;

            match object.kind {
                VehicleKind::VerticalCar => {
                    // Check if the vehicle can move up
                    if object.can_move("up", &self) {
                        new_grid = self.clone();
                        if let Some(found_object) = new_grid
                            .objects
                            .iter_mut()
                            .find(|v| v.name() == object.name())
                        {
                            let _old_position = found_object.position;
                            let action = found_object.move_vehicle("up");
                            new_grid.cells[_old_position[0] + 1][_old_position[1]] = None;
                            new_grid.cells[_old_position[0] - 1][_old_position[1]] =
                                Some(found_object.name.clone());
                            new_grids.push((new_grid, action));
                        }
                    }

                    // Check if the vehicle can move down
                    if object.can_move("down", &self) {
                        new_grid = self.clone();
                        if let Some(found_object) = new_grid
                            .objects
                            .iter_mut()
                            .find(|v| v.name() == object.name())
                        {
                            let _old_position = found_object.position;
                            let action = found_object.move_vehicle("down");
                            new_grid.cells[_old_position[0]][_old_position[1]] = None;
                            new_grid.cells[_old_position[0] + 2][_old_position[1]] =
                                Some(found_object.name.clone());
                            new_grids.push((new_grid, action));
                        }
                    }
                }

                VehicleKind::VerticalTruck => {
                    // Check if the vehicle can move up
                    if object.can_move("up", &self) {
                        new_grid = self.clone();
                        if let Some(found_object) = new_grid
                            .objects
                            .iter_mut()
                            .find(|v| v.name() == object.name())
                        {
                            let _old_position = found_object.position;
                            let action = found_object.move_vehicle("up");
                            new_grid.cells[_old_position[0] + 2][_old_position[1]] = None;
                            new_grid.cells[_old_position[0] - 1][_old_position[1]] =
                                Some(found_object.name.clone());
                            new_grids.push((new_grid, action));
                        }
                    }

                    // Check if the vehicle can move down
                    if object.can_move("down", &self) {
                        new_grid = self.clone();
                        if let Some(found_object) = new_grid
                            .objects
                            .iter_mut()
                            .find(|v| v.name() == object.name())
                        {
                            let _old_position = found_object.position;
                            let action = found_object.move_vehicle("down");
                            new_grid.cells[_old_position[0]][_old_position[1]] = None;
                            new_grid.cells[_old_position[0] + 3][_old_position[1]] =
                                Some(found_object.name.clone());
                            new_grids.push((new_grid, action));
                        }
                    }
                }

                VehicleKind::HorizontalCar => {
                    // Check if the vehicle can move right
                    if object.can_move("right", &self) {
                        new_grid = self.clone();
                        if let Some(found_object) = new_grid
                            .objects
                            .iter_mut()
                            .find(|v| v.name() == object.name())
                        {
                            let _old_position = found_object.position;
                            let action = found_object.move_vehicle("right");
                            new_grid.cells[_old_position[0]][_old_position[1]] = None;
                            new_grid.cells[_old_position[0]][_old_position[1] + 2] =
                                Some(found_object.name.clone());
                            new_grids.push((new_grid, action));
                        }
                    }

                    // Check if the vehicle can move left
                    if object.can_move("left", &self) {
                        new_grid = self.clone();
                        if let Some(found_object) = new_grid
                            .objects
                            .iter_mut()
                            .find(|v| v.name() == object.name())
                        {
                            let _old_position = found_object.position;
                            let action = found_object.move_vehicle("left");
                            new_grid.cells[_old_position[0]][_old_position[1] + 1] = None;
                            new_grid.cells[_old_position[0]][_old_position[1] - 1] =
                                Some(found_object.name.clone());
                            new_grids.push((new_grid, action));
                        }
                    }
                }

                VehicleKind::HorizontalTruck => {
                    // Check if the vehicle can move right
                    if object.can_move("right", &self) {
                        new_grid = self.clone();
                        if let Some(found_object) = new_grid
                            .objects
                            .iter_mut()
                            .find(|v| v.name() == object.name())
                        {
                            let _old_position = found_object.position;
                            let action = found_object.move_vehicle("right");
                            new_grid.cells[_old_position[0]][_old_position[1]] = None;
                            new_grid.cells[_old_position[0]][_old_position[1] + 3] =
                                Some(found_object.name.clone());
                            new_grids.push((new_grid, action));
                        }
                    }
                    // Check if the vehicle can move left
                    if object.can_move("left", &self) {
                        new_grid = self.clone();
                        if let Some(found_object) = new_grid
                            .objects
                            .iter_mut()
                            .find(|v| v.name() == object.name())
                        {
                            let _old_position = found_object.position;
                            let action = found_object.move_vehicle("left");
                            new_grid.cells[_old_position[0]][_old_position[1] + 2] = None;
                            new_grid.cells[_old_position[0]][_old_position[1] - 1] =
                                Some(found_object.name.clone());
                            new_grids.push((new_grid, action));
                        }
                    }
                }
            }
        }

        new_grids // Return the vector of new grid configurations
    }
}

#[derive(Clone, Copy, Debug)]
pub enum VehicleKind {
    HorizontalCar,
    HorizontalTruck,
    VerticalCar,
    VerticalTruck,
}

#[derive(Clone, Copy, Debug)]
enum Direction {
    Horizontal,
    Vertical,
}
#[derive(Clone, Debug)]
pub struct Vehicle {
    pub kind: VehicleKind,
    pub position: [usize; 2],
    pub name: String,
}

impl VehicleKind {
    fn length(self) -> usize {
        match self {
            Self::HorizontalCar => 2,
            Self::VerticalCar => 2,
            Self::HorizontalTruck => 3,
            Self::VerticalTruck => 3,
        }
    }

    fn direction(self) -> Direction {
        match self {
            Self::HorizontalCar | Self::HorizontalTruck => Direction::Horizontal,
            Self::VerticalCar | Self::VerticalTruck => Direction::Vertical,
        }
    }
}
 
impl Vehicle {
    pub fn new(kind: VehicleKind, position: [usize; 2], name: String) -> Self {
        Self {
            kind,
            position,
            name,
        }
    }

    fn name(&self) -> &str {
        &self.name
    }

    pub fn positions(&self) -> Vec<[usize; 2]> {
        let mut points_positions = Vec::with_capacity(3);
        match self.kind {
            VehicleKind::VerticalCar => {
                let end_point = [self.position[0] + 1, self.position[1]];
                points_positions.push(self.position);
                points_positions.push(end_point);
            }
            VehicleKind::HorizontalCar => {
                let end_point = [self.position[0], self.position[1] + 1];
                points_positions.push(self.position);
                points_positions.push(end_point);
            }
            VehicleKind::VerticalTruck => {
                let middle_point = [self.position[0] + 1, self.position[1]];
                let end_point = [self.position[0] + 2, self.position[1]];
                points_positions.push(self.position);
                points_positions.push(middle_point);
                points_positions.push(end_point);
            }
            VehicleKind::HorizontalTruck => {
                let middle_point = [self.position[0], self.position[1] + 1];
                let end_point = [self.position[0], self.position[1] + 2];
                points_positions.push(self.position);
                points_positions.push(middle_point);
                points_positions.push(end_point);
            }
        }
        points_positions
    }

    fn can_move(&self, direction: &str, grid: &Grid) -> bool {
        match self.kind.direction() {
            Direction::Horizontal => match direction {
                "right" => {
                    let end_position = self.position[1] + self.kind.length(); // Rightmost position of the vehicle
                    end_position < grid.col_size
                        && grid.cells[self.position[0]][end_position].is_none()
                }
                "left" => {
                    self.position[1] > 0
                        && grid.cells[self.position[0]][self.position[1] - 1].is_none()
                }
                _ => false, // Invalid direction
            },
            Direction::Vertical => match direction {
                "up" => {
                    self.position[0] > 0
                        && grid.cells[self.position[0] - 1][self.position[1]].is_none()
                }
                "down" => {
                    let end_position = self.position[0] + self.kind.length(); // Bottommost position of the vehicle
                    end_position < grid.row_size
                        && grid.cells[end_position][self.position[1]].is_none()
                }
                _ => false, // Invalid direction
            },
        }
    }

    fn move_vehicle(&mut self, direction: &str) -> String {
        match direction {
            "up" => self.position[0] -= 1,
            "down" => self.position[0] += 1,
            "left" => self.position[1] -= 1,
            "right" => self.position[1] += 1,
            _ => return "Invalid move".to_string(),
        }
        format!("{} moved {}", self.name(), direction)
    }
}
fn main() {
    // Create a 6x6 grid
    let mut grid = Grid::new(6, 6);

    // Create a "Red Car" (HorizontalCar) with name "RC" and position at (2, 0)
    let red_car = Vehicle::new(VehicleKind::HorizontalCar, [2, 0], "RC".to_string());

    // Place the red car on the grid
    match grid.place_object(&red_car) {
        Ok(message) => println!("{}", message),
        Err(e) => println!("Error: {}", e),
    }
    grid.add_vehicle(red_car);
    grid.display();
    if grid.objects[0].can_move("right", &grid) {
        let old_positions = grid.objects[0].positions();
        grid.objects[0].move_vehicle("right");
        let new_positions = grid.objects[0].positions();
        let name = grid.objects[0].name.clone();
        grid.update(old_positions, new_positions, name);
    }

    grid.display();
}

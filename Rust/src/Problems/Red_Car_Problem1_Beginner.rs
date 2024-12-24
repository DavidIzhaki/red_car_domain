use red_car_domain::*;

fn main() {
    let mut grid = Grid::new(6, 6);

    let red_car = Vehicle::new(VehicleKind::HorizontalCar, [0, 2], "red_car".to_string());
    grid.place_object(&red_car).unwrap();
    grid.add_vehicle(red_car);

    // Define the goal: red-car at (2, 4), red-car at (2, 5)
    grid.display();
}
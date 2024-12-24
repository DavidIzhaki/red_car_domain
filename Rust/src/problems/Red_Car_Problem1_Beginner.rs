mod red_car_domain;
use red_car_domain::*;

pub fn problem() -> Grid {
    // Create a 6x6 grid
    let mut grid = Grid::new(6, 6);

    // Add the red car
    let red_car = Vehicle::new(VehicleKind::HorizontalCar, [0, 2], "red_car".to_string());
    grid.place_object(&red_car).unwrap();
    grid.add_vehicle(red_car);

    grid
}

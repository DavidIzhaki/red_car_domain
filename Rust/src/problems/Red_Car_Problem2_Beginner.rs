use red_car_domain::*;

fn main() {
    let mut grid = Grid::new(6, 6);

    let green_car = Vehicle::new(VehicleKind::VerticalCar, [0, 1], "green_car".to_string());
    grid.place_object(&green_car).unwrap();
    grid.add_vehicle(green_car);

    let orange_car = Vehicle::new(VehicleKind::VerticalCar, [1, 1], "orange_car".to_string());
    grid.place_object(&orange_car).unwrap();
    grid.add_vehicle(orange_car);

    let pink_car = Vehicle::new(VehicleKind::VerticalCar, [4, 1], "pink_car".to_string());
    grid.place_object(&pink_car).unwrap();
    grid.add_vehicle(pink_car);

    let green_over_car = Vehicle::new(VehicleKind::VerticalCar, [2, 2], "green_over_car".to_string());
    grid.place_object(&green_over_car).unwrap();
    grid.add_vehicle(green_over_car);

    let white_car = Vehicle::new(VehicleKind::VerticalCar, [2, 4], "white_car".to_string());
    grid.place_object(&white_car).unwrap();
    grid.add_vehicle(white_car);

    let gray_car = Vehicle::new(VehicleKind::VerticalCar, [4, 3], "gray_car".to_string());
    grid.place_object(&gray_car).unwrap();
    grid.add_vehicle(gray_car);

    let red_car = Vehicle::new(VehicleKind::HorizontalCar, [0, 2], "red_car".to_string());
    grid.place_object(&red_car).unwrap();
    grid.add_vehicle(red_car);

    let blue_car = Vehicle::new(VehicleKind::HorizontalCar, [2, 0], "blue_car".to_string());
    grid.place_object(&blue_car).unwrap();
    grid.add_vehicle(blue_car);

    let purple_car = Vehicle::new(VehicleKind::HorizontalCar, [2, 1], "purple_car".to_string());
    grid.place_object(&purple_car).unwrap();
    grid.add_vehicle(purple_car);

    let yellow_truck = Vehicle::new(VehicleKind::VerticalTruck, [3, 2], "yellow_truck".to_string());
    grid.place_object(&yellow_truck).unwrap();
    grid.add_vehicle(yellow_truck);

    // Define the goal: red-car at (2, 4), red-car at (2, 5)
    grid.display();
}
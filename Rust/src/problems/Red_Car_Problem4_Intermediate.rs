use red_car_domain::*;

fn main() {
    let mut grid = Grid::new(6, 6);

    let pink_car = Vehicle::new(VehicleKind::VerticalCar, [5, 1], "pink_car".to_string());
    grid.place_object(&pink_car).unwrap();
    grid.add_vehicle(pink_car);

    let blue_car = Vehicle::new(VehicleKind::VerticalCar, [4, 1], "blue_car".to_string());
    grid.place_object(&blue_car).unwrap();
    grid.add_vehicle(blue_car);

    let orange_car = Vehicle::new(VehicleKind::VerticalCar, [3, 1], "orange_car".to_string());
    grid.place_object(&orange_car).unwrap();
    grid.add_vehicle(orange_car);

    let purple_car = Vehicle::new(VehicleKind::VerticalCar, [2, 2], "purple_car".to_string());
    grid.place_object(&purple_car).unwrap();
    grid.add_vehicle(purple_car);

    let green_over_car = Vehicle::new(VehicleKind::VerticalCar, [0, 3], "green_over_car".to_string());
    grid.place_object(&green_over_car).unwrap();
    grid.add_vehicle(green_over_car);

    let red_car = Vehicle::new(VehicleKind::HorizontalCar, [0, 2], "red_car".to_string());
    grid.place_object(&red_car).unwrap();
    grid.add_vehicle(red_car);

    let yellow_car = Vehicle::new(VehicleKind::HorizontalCar, [0, 5], "yellow_car".to_string());
    grid.place_object(&yellow_car).unwrap();
    grid.add_vehicle(yellow_car);

    let yellow_special_car = Vehicle::new(VehicleKind::HorizontalCar, [1, 4], "yellow_special_car".to_string());
    grid.place_object(&yellow_special_car).unwrap();
    grid.add_vehicle(yellow_special_car);

    let gray_white_car = Vehicle::new(VehicleKind::HorizontalCar, [3, 3], "gray_white_car".to_string());
    grid.place_object(&gray_white_car).unwrap();
    grid.add_vehicle(gray_white_car);

    let green_car = Vehicle::new(VehicleKind::HorizontalCar, [1, 0], "green_car".to_string());
    grid.place_object(&green_car).unwrap();
    grid.add_vehicle(green_car);

    let blue_truck = Vehicle::new(VehicleKind::VerticalTruck, [5, 3], "blue_truck".to_string());
    grid.place_object(&blue_truck).unwrap();
    grid.add_vehicle(blue_truck);

    let purple_truck = Vehicle::new(VehicleKind::HorizontalTruck, [1, 5], "purple_truck".to_string());
    grid.place_object(&purple_truck).unwrap();
    grid.add_vehicle(purple_truck);

    let yellow_truck = Vehicle::new(VehicleKind::HorizontalTruck, [3, 0], "yellow_truck".to_string());
    grid.place_object(&yellow_truck).unwrap();
    grid.add_vehicle(yellow_truck);

    let green_truck = Vehicle::new(VehicleKind::HorizontalTruck, [2, 5], "green_truck".to_string());
    grid.place_object(&green_truck).unwrap();
    grid.add_vehicle(green_truck);

    // Define the goal: red-car at (2, 4), red-car at (2, 5)
    grid.display();
}
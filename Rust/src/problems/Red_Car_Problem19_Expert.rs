use red_car_domain::*;

fn main() {
    let mut grid = Grid::new(6, 6);

    let orange_car = Vehicle::new(VehicleKind::VerticalCar, [3, 1], "orange_car".to_string());
    grid.place_object(&orange_car).unwrap();
    grid.add_vehicle(orange_car);

    let pink_car = Vehicle::new(VehicleKind::VerticalCar, [0, 2], "pink_car".to_string());
    grid.place_object(&pink_car).unwrap();
    grid.add_vehicle(pink_car);

    let white_gray_car = Vehicle::new(VehicleKind::VerticalCar, [0, 4], "white_gray_car".to_string());
    grid.place_object(&white_gray_car).unwrap();
    grid.add_vehicle(white_gray_car);

    let purple_car = Vehicle::new(VehicleKind::VerticalCar, [5, 2], "purple_car".to_string());
    grid.place_object(&purple_car).unwrap();
    grid.add_vehicle(purple_car);

    let green_car = Vehicle::new(VehicleKind::VerticalCar, [2, 0], "green_car".to_string());
    grid.place_object(&green_car).unwrap();
    grid.add_vehicle(green_car);

    let green_hover_car = Vehicle::new(VehicleKind::VerticalCar, [1, 3], "green_hover_car".to_string());
    grid.place_object(&green_hover_car).unwrap();
    grid.add_vehicle(green_hover_car);

    let yellow_car = Vehicle::new(VehicleKind::VerticalCar, [5, 4], "yellow_car".to_string());
    grid.place_object(&yellow_car).unwrap();
    grid.add_vehicle(yellow_car);

    let blue_sky_car = Vehicle::new(VehicleKind::HorizontalCar, [4, 1], "blue_sky_car".to_string());
    grid.place_object(&blue_sky_car).unwrap();
    grid.add_vehicle(blue_sky_car);

    let red_car = Vehicle::new(VehicleKind::HorizontalCar, [1, 2], "red_car".to_string());
    grid.place_object(&red_car).unwrap();
    grid.add_vehicle(red_car);

    let brown_car = Vehicle::new(VehicleKind::HorizontalCar, [1, 5], "brown_car".to_string());
    grid.place_object(&brown_car).unwrap();
    grid.add_vehicle(brown_car);

    let yellow_hover_car = Vehicle::new(VehicleKind::HorizontalCar, [2, 4], "yellow_hover_car".to_string());
    grid.place_object(&yellow_hover_car).unwrap();
    grid.add_vehicle(yellow_hover_car);

    let yellow_special_car = Vehicle::new(VehicleKind::HorizontalCar, [3, 5], "yellow_special_car".to_string());
    grid.place_object(&yellow_special_car).unwrap();
    grid.add_vehicle(yellow_special_car);

    let purple_truck = Vehicle::new(VehicleKind::VerticalTruck, [4, 2], "purple_truck".to_string());
    grid.place_object(&purple_truck).unwrap();
    grid.add_vehicle(purple_truck);

    let yellow_truck = Vehicle::new(VehicleKind::HorizontalTruck, [3, 0], "yellow_truck".to_string());
    grid.place_object(&yellow_truck).unwrap();
    grid.add_vehicle(yellow_truck);

    // Define the goal: red-car at (2, 4), red-car at (2, 5)
    grid.display();
}
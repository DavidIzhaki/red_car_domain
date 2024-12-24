mod red_car_domain2;

use red_car_domain2::{Grid, HorizontalCar, HorizontalTruck, VerticalCar, VerticalTruck};

fn main() {
    // Create a 6x6 grid
    let mut grid = Grid::new(6, 6);

    // Create objects
    let horizontal_car = HorizontalCar::new(0, 0, "HC1".to_string());
    let vertical_car = VerticalCar::new(0, 5, "VC1".to_string());
    let horizontal_truck = HorizontalTruck::new(3, 0, "HT1".to_string());
    let vertical_truck = VerticalTruck::new(3, 5, "VT1".to_string());

    // Place objects on the grid
    grid.place_object(&horizontal_car)
        .expect("Failed to place HorizontalCar");
    grid.place_object(&vertical_car)
        .expect("Failed to place VerticalCar");
    grid.place_object(&horizontal_truck)
        .expect("Failed to place HorizontalTruck");
    grid.place_object(&vertical_truck)
        .expect("Failed to place VerticalTruck");

    // Display the grid
    println!("Initial Grid State:");
    grid.display();
}

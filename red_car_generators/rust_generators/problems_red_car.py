from problem_generator import generate_problem_file

problems = [
    {
        "name": "Red_Car_Problem1_Beginner",
        "cars_vertical": {},
        "cars_horizontal": {"red_car": [0, 2]},
        "trucks_vertical": {},
        "trucks_horizontal": {},
    },
    {
        "name": "Red_Car_Problem2_Beginner",
        "cars_vertical": {
            "green_car": [0, 1],
            "orange_car": [1, 1],
            "pink_car": [4, 1],
            "green_over_car": [2, 2],
            "white_car": [2, 4],
            "gray_car": [4, 3]
        },
        "cars_horizontal": {
            "red_car": [0, 2],
            "blue_car": [2, 0],
            "purple_car": [2, 1]
        },
        "trucks_vertical": {
            "yellow_truck": [3, 2]
        },
        "trucks_horizontal": {},
    },
    {
        "name": "Red_Car_Problem3_Beginner",
        "cars_vertical": {
            "green_car": [5, 1],
            "orange_car": [0, 3],
            "green_over_car": [4, 4],
            "purple_car": [3, 4]
        },
        "cars_horizontal": {
            "red_car": [0, 2],
            "pink_car": [1, 4],
            "blue_car": [3, 3]
        },
        "trucks_vertical": {
            "yellow_truck": [2, 1],
            "purple_truck": [5, 3]
        },
        "trucks_horizontal": {
            "blue_truck": [0, 5]
        },
    },
    {
        "name": "Red_Car_Problem4_Intermediate",
        "cars_vertical": {
            "pink_car": [5, 1],
            "blue_car": [4, 1],
            "orange_car": [3, 1],
            "purple_car": [2, 2],
            "green_over_car": [0, 3]
        },
        "cars_horizontal": {
            "red_car": [0, 2],
            "yellow_car": [0, 5],
            "yellow_special_car": [1, 4],
            "gray_white_car": [3, 3],
            "green_car": [1, 0]
        },
        "trucks_vertical": {
            "blue_truck": [5, 3]
        },
        "trucks_horizontal": {
            "purple_truck": [1, 5],
            "yellow_truck": [3, 0],
            "green_truck": [2, 5]
        },
    },
    {
        "name": "Red_Car_Problem5_Intermediate",
        "cars_vertical": {
            "pink_car": [4, 2],
            "blue_car": [0, 1],
            "orange_car": [2, 0],
            "green_over_car": [5, 4]
        },
        "cars_horizontal": {
            "red_car": [2, 2],
            "purple_car": [0, 4],
            "green_car": [0, 0]
        },
        "trucks_vertical": {},
        "trucks_horizontal": {
            "purple_truck": [2, 4],
            "yellow_truck": [3, 1]
        },
    },
    {
        "name": "Red_Car_Problem6_Intermediate",
        "cars_vertical": {
            "pink_car": [1, 2],
            "green_car": [1, 0],
            "yellow_car": [5, 4],
            "yellow_over_car": [4, 4],
            "purple_car": [5, 2],
            "green_over_car": [0, 3]
        },
        "cars_horizontal": {
            "red_car": [3, 2],
            "orange_car": [2, 0],
            "blue_sky_car": [4, 0],
            "gray_white_car": [3, 3]
        },
        "trucks_vertical": {
            "yellow_truck": [0, 1]
        },
        "trucks_horizontal": {
            "purple_truck": [3, 2],
            "blue_truck": [1, 4],
            "green_truck": [0, 5]
        },
    },
    {
        "name": "Red_Car_Problem7_Intermediate",
        "cars_vertical": {
            "pink_car": [2, 2],
            "purple_car": [3, 2],
            "green_car": [3, 0],
            "green_over_car": [4, 2],
            "white_gray_car": [5, 2],
            "yellow_car": [0, 4],
            "brown_car": [4, 4],
            "yellow_special_car": [5, 4]
        },
        "cars_horizontal": {
            "red_car": [0, 2],
            "brown_sky_car": [0, 3],
            "orange_car": [4, 0],
            "blue_sky_car": [4, 1]
        },
        "trucks_vertical": {},
        "trucks_horizontal": {
            "purple_truck": [1, 5],
            "yellow_truck": [1, 4]
        },
    },
    {
        "name": "Red_Car_Problem8_Intermediate",
        "cars_vertical": {
            "pink_car": [2, 1],
            "orange_car": [5, 0],
            "green_over_car": [5, 2],
            "yellow_special_car": [0, 4],
            "white_gray_car": [4, 3]
        },
        "cars_horizontal": {
            "red_car": [0, 2],
            "blue_sky_car": [0, 1],
            "green_car": [3, 0],
            "purple_car": [3, 1],
            "yellow_car": [1, 4],
            "brown_car": [4, 5]
        },
        "trucks_vertical": {
            "purple_truck": [3, 2]
        },
        "trucks_horizontal": {
            "blue_truck": [1, 5],
            "yellow_truck": [0, 0]
        },
    },
    {
        "name": "Red_Car_Problem9_Advanced",
        "cars_vertical": {
            "green_car": [1, 0],
            "purple_car": [2, 1],
            "green_over_car": [3, 1],
            "pink_car": [5, 0],
            "blue_sky_car": [4, 0],
            "white_gray_car": [4, 2],
            "yellow_special_car": [2, 3],
            "yellow_over_car": [3, 3]
        },
        "cars_horizontal": {
            "red_car": [0, 2],
            "orange_car": [2, 0],
            "brown_car": [4, 5]
        },
        "trucks_vertical": {
            "yellow_truck": [5, 2],
            "purple_truck": [0, 3]
        },
        "trucks_horizontal": {
            "blue_truck": [1, 5]
        },
    },
    {
        "name": "Red_Car_Problem10_Advanced",
        "cars_vertical": {
            "green_car": [0, 0],
            "orange_car": [2, 0],
            "green_over_car": [1, 3],
            "pink_car": [3, 2],
            "purple_car": [4, 2],
            "yellow_car": [5, 4],
            "yellow_over_car": [4, 4]
        },
        "cars_horizontal": {
            "red_car": [1, 2],
            "blue_sky_car": [4, 0],
            "brown_car": [0, 5],
            "yellow_special_car": [2, 5],
            "white_gray_car": [2, 4]
        },
        "trucks_vertical": {
            "purple_truck": [0, 2]
        },
        "trucks_horizontal": {
            "yellow_truck": [3, 1]
        },
    },
    {
        "name": "Red_Car_Problem11_Advanced",
        "cars_vertical": {
            "orange_car": [4, 0],
            "blue_sky_car": [5, 0],
            "pink_car": [0, 2]
        },
        "cars_horizontal": {
            "red_car": [1, 2],
            "green_car": [0, 0],
            "green_over_car": [0, 4],
            "purple_car": [3, 3],
            "white_gray_car": [0, 5]
        },
        "trucks_vertical": {
            "purple_truck": [5, 2],
            "blue_truck": [2, 3],
            "yellow_truck": [3, 0]
        },
        "trucks_horizontal": {},
    },
    {
        "name": "Red_Car_Problem12_Advanced",
        "cars_vertical": {
            "orange_car": [2, 0],
            "pink_car": [5, 3],
            "purple_car": [3, 4]
        },
        "cars_horizontal": {
            "red_car": [2, 2],
            "green_car": [0, 0],
            "green_over_car": [4, 5],
            "blue_sky_car": [4, 0]
        },
        "trucks_vertical": {
            "purple_truck": [4, 2],
            "yellow_truck": [0, 1]
        },
        "trucks_horizontal": {
            "blue_truck": [1, 3]
        },
    },
    {
        "name": "Red_Car_Problem13_Advanced",
        "cars_vertical": {
            "orange_car": [5, 0],
            "blue_sky_car": [0, 1],
            "yellow_car": [2, 4],
            "white_gray_car": [4, 3]
        },
        "cars_horizontal": {
            "red_car": [3, 2],
            "green_car": [0, 0],
            "green_over_car": [2, 3],
            "purple_car": [0, 3],
            "yellow_hover_car": [0, 4],
            "pink_car": [3, 1]
        },
        "trucks_vertical": {
            "purple_truck": [5, 2]
        },
        "trucks_horizontal": {
            "blue_truck": [3, 5],
            "yellow_truck": [2, 0]
        },
    },
    {
        "name": "Red_Car_Problem14_Advanced",
        "cars_vertical": {
            "orange_car": [2, 2],
            "blue_sky_car": [3, 2],
            "purple_car": [3, 4],
            "green_car": [0, 0]
        },
        "cars_horizontal": {
            "red_car": [0, 2],
            "green_hover_car": [4, 4],
            "pink_car": [0, 3],
            "white_gray_car": [1, 5]
        },
        "trucks_vertical": {
            "blue_truck": [4, 1],
            "green_truck": [5, 1]
        },
        "trucks_horizontal": {
            "yellow_truck": [2, 0],
            "purple_truck": [1, 1]
        },
    },
    {
        "name": "Red_Car_Problem15_Expert",
        "cars_vertical": {
            "orange_car": [1, 0],
            "pink_car": [4, 0],
            "green_car": [0, 0],
            "purple_car": [5, 0],
            "yellow_car": [2, 4],
            "green_hover_car": [3, 2],
            "white_gray_car": [5, 2]
        },
        "cars_horizontal": {
            "red_car": [1, 2],
            "yellow_hover_car": [1, 3],
            "brown_car": [0, 5]
        },
        "trucks_vertical": {
            "yellow_truck": [0, 2]
        },
        "trucks_horizontal": {
            "blue_truck": [3, 4],
            "purple_truck": [3, 5]
        },
    },
    {
        "name": "Red_Car_Problem16_Expert",
        "cars_vertical": {
            "orange_car": [5, 0],
            "purple_car": [4, 1],
            "blue_sky_car": [0, 1],
            "yellow_special_car": [4, 4],
            "yellow_hover_car": [3, 3],
            "green_hover_car": [5, 2]
        },
        "cars_horizontal": {
            "red_car": [2, 2],
            "yellow_car": [3, 3],
            "brown_car": [0, 4],
            "white_gray_car": [0, 3],
            "green_car": [0, 0],
            "pink_car": [2, 1]
        },
        "trucks_vertical": {},
        "trucks_horizontal": {
            "yellow_truck": [2, 0],
            "purple_truck": [0, 5]
        },
    },
    {
        "name": "Red_Car_Problem17_Expert",
        "cars_vertical": {
            "orange_car": [3, 0],
            "blue_sky_car": [5, 0],
            "pink_car": [0, 1],
            "purple_car": [1, 1],
            "yellow_car": [2, 4],
            "green_hover_car": [5, 2],
            "yellow_hover_car": [3, 3]
        },
        "cars_horizontal": {
            "red_car": [2, 2],
            "green_car": [0, 0],
            "brown_car": [3, 5],
            "white_gray_car": [1, 3]
        },
        "trucks_vertical": {
            "yellow_truck": [4, 2],
            "purple_truck": [0, 3]
        },
        "trucks_horizontal": {},
    },
    {
        "name": "Red_Car_Problem18_Expert",
        "cars_vertical": {
            "orange_car": [3, 0],
            "pink_car": [3, 2],
            "white_gray_car": [5, 4]
        },
        "cars_horizontal": {
            "blue_sky_car": [4, 1],
            "red_car": [1, 2],
            "green_car": [1, 0],
            "purple_car": [4, 3],
            "green_hover_car": [3, 4]
        },
        "trucks_vertical": {
            "yellow_truck": [0, 0],
            "purple_truck": [2, 3]
        },
        "trucks_horizontal": {},
    },
    {
        "name": "Red_Car_Problem19_Expert",
        "cars_vertical": {
            "orange_car": [3, 1],
            "pink_car": [0, 2],
            "white_gray_car": [0, 4],
            "purple_car": [5, 2],
            "green_car": [2, 0],
            "green_hover_car": [1, 3],
            "yellow_car": [5, 4]
        },
        "cars_horizontal": {
            "blue_sky_car": [4, 1],
            "red_car": [1, 2],
            "brown_car": [1, 5],
            "yellow_hover_car": [2, 4],
            "yellow_special_car": [3, 5]
        },
        "trucks_vertical": {
            "purple_truck": [4, 2]
        },
        "trucks_horizontal": {
            "yellow_truck": [3, 0]
        },
    },
    {
        "name": "Red_Car_Problem20_Expert",
        "cars_vertical": {
            "green_car": [0, 0],
            "pink_car": [4, 1],
            "yellow_car": [3, 4],
            "purple_car": [2, 2]
        },
        "cars_horizontal": {
            "blue_sky_car": [2, 1],
            "red_car": [0, 2],
            "green_hover_car": [0, 3],
            "yellow_hover_car": [1, 4],
            "orange_car": [1, 0],
            "white_gray_car": [3, 3]
        },
        "trucks_vertical": {
            "purple_truck": [5, 3]
        },
        "trucks_horizontal": {
            "yellow_truck": [3, 0],
            "blue_truck": [0, 5]
        },
    }
    # Continue with the rest of the problems
]
def generate_rust_files():
    print("Welcome to the Rust Problem Generator!")
    for problem in problems:
        generate_problem_file(
            problem_name=problem["name"],
            #rows = int(input("Enter the number of rows for the grid (e.g., 6): "))
            #cols = int(input("Enter the number of columns for the grid (e.g., 6): "))
            rows=6,
            cols =6,
            cars_vertical=problem["cars_vertical"],
            cars_horizontal=problem["cars_horizontal"],
            trucks_vertical=problem["trucks_vertical"],
            trucks_horizontal=problem["trucks_horizontal"],)

if __name__ == "__main__":
    generate_rust_files()
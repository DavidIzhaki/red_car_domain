from problem_generator import generate_problem_file

# Define the problems
problems = [
    {
        "name": "Red-Car-Problem1-Beginner",
        "cars_vertical": {},  # No vertical cars in this problem
        "cars_horizontal": {"red-car": ("cube-x0-y2", "cube-x1-y2")},
        "trucks_vertical": {},  # No vertical trucks in this problem
        "trucks_horizontal": {},  # No horizontal trucks in this problem
    },
    {
        "name": "Red-Car-Problem2-Beginner",
        "cars_vertical": {"green-car": ("cube-x0-y1", "cube-x0-y2"),
                          "orange-car": ("cube-x1-y1", "cube-x1-y2"),
                          "pink-car": ("cube-x4-y1", "cube-x4-y2"),
                          "green-over-car": ("cube-x2-y2", "cube-x2-y3"),
                          "white-car": ("cube-x2-y4", "cube-x2-y5"),
                          "gray-car": ("cube-x4-y3", "cube-x4-y4")},
        "cars_horizontal": {"red-car": ("cube-x0-y2", "cube-x1-y2"),
                            "blue-car": ("cube-x2-y0", "cube-x3-y0"),
                            "purple-car": ("cube-x2-y1", "cube-x3-y1")},
        "trucks_vertical": {"yellow-truck": ["cube-x3-y2", "cube-x3-y3", "cube-x3-y4"]},
        "trucks_horizontal": {},
    },
    {
        "name": "Red-Car-Problem3-Beginner",
        "cars_vertical": {"green-car": ("cube-x5-y1", "cube-x5-y2"),
                          "orange-car": ("cube-x0-y3", "cube-x0-y4"),
                          "green-over-car": ("cube-x4-y4", "cube-x4-y5"),
                          "purple-car": ("cube-x3-y4", "cube-x3-y5"),},
        "cars_horizontal": {"red-car": ("cube-x0-y2", "cube-x1-y2"),
                            "pink-car": ("cube-x1-y4", "cube-x2-y4"),
                            "blue-car": ("cube-x3-y3", "cube-x4-y3")},
        "trucks_vertical": {"yellow-truck": ["cube-x2-y1", "cube-x2-y2", "cube-x2-y3"],
                            "purple-truck": ["cube-x5-y3", "cube-x5-y4", "cube-x5-y5"]},
        "trucks_horizontal": {"blue-truck": ["cube-x0-y5", "cube-x1-y5", "cube-x2-y5"]},
    },
    {
        "name": "Red-Car-Problem3-Beginner",
        "cars_vertical": {
            "pink-car": ("cube-x1-y3", "cube-x1-y4"),
            "blue-car": ("cube-x5-y1", "cube-x5-y2"),
            "purple-car": ("cube-x3-y3", "cube-x3-y4"),
            "white-car": ("cube-x4-y4", "cube-x4-y5"),
            "yellow-car": ("cube-x5-y4", "cube-x5-y5"),
        },
        "cars_horizontal": {
            "red-car": ("cube-x3-y2", "cube-x4-y2"),
            "green-car": ("cube-x2-y0", "cube-x3-y0"),
            "orange-car": ("cube-x4-y0", "cube-x5-y0"),
            "green-over-car": ("cube-x4-y3", "cube-x5-y3"),
        },
        "trucks_vertical": {
            "yellow-truck": ["cube-x1-y0", "cube-x1-y1", "cube-x1-y2"],
        },
        "trucks_horizontal": {
            "purple-truck": ["cube-x1-y5", "cube-x2-y5", "cube-x3-y5"],
        },
    },
    {
        "name": "Red-Car-Problem4-Intermediate",
        "cars_vertical": {
            "pink-car": ("cube-x5-y1", "cube-x5-y2"),
            "blue-car": ("cube-x4-y1", "cube-x4-y2"),
            "orange-car": ("cube-x3-y1", "cube-x3-y2"),
            "purple-car": ("cube-x2-y2", "cube-x2-y3"),
            "green-over-car": ("cube-x0-y3", "cube-x0-y4"),
        },
        "cars_horizontal": {
            "red-car": ("cube-x0-y2", "cube-x1-y2"),
            "yellow-car": ("cube-x0-y5", "cube-x1-y5"),
            "yellow-special-car": ("cube-x1-y4", "cube-x2-y4"),
            "gray-white-car": ("cube-x3-y3", "cube-x4-y3"),
            "green-car": ("cube-x1-y0", "cube-x2-y0"),
        },
        "trucks_vertical": {
            "blue-truck": ["cube-x5-y3", "cube-x5-y4", "cube-x5-y5"],
        },
        "trucks_horizontal": {
            "purple-truck": ["cube-x1-y5", "cube-x2-y5", "cube-x3-y5"],
            "yellow-truck": ["cube-x3-y0", "cube-x4-y0", "cube-x5-y0"],
            "green-truck": ["cube-x2-y5", "cube-x3-y5", "cube-x4-y5"],
        },
    },
    {
        "name": "Red-Car-Problem5-Intermediate",
        "cars_vertical": {
            "pink-car": ("cube-x4-y2", "cube-x4-y3"),
            "blue-car": ("cube-x0-y1", "cube-x0-y2"),
            "orange-car": ("cube-x2-y0", "cube-x2-y1"),
            "green-over-car": ("cube-x5-y4", "cube-x5-y5"),
        },
        "cars_horizontal": {
            "red-car": ("cube-x2-y2", "cube-x3-y2"),
            "purple-car": ("cube-x0-y4", "cube-x1-y4"),
            "green-car": ("cube-x0-y0", "cube-x1-y0"),
        },
        "trucks_vertical": {
        },
        "trucks_horizontal": {
            "purple-truck": ["cube-x2-y4", "cube-x3-y4", "cube-x4-y4"],
            "yellow-truck": ["cube-x3-y1", "cube-x4-y1", "cube-x5-y1"],
        },
    },
    {
        "name": "Red-Car-Problem6-Intermediate",
        "cars_vertical": {
            "pink-car": ("cube-x1-y2", "cube-x1-y3"),
            "green-car": ("cube-x1-y0", "cube-x1-y1"),
            "yellow-car": ("cube-x5-y4", "cube-x5-y5"),
            "yellow-over-car": ("cube-x4-y4", "cube-x4-y5"),
            "purple-car": ("cube-x5-y2", "cube-x5-y3"),
            "green-over-car": ("cube-x0-y3", "cube-x0-y4"),
        },
        "cars_horizontal": {
            "red-car": ("cube-x3-y2", "cube-x4-y2"),
            "orange-car": ("cube-x2-y0", "cube-x3-y0"),
            "blue-sky-car": ("cube-x4-y0", "cube-x5-y0"),
            "gray-white-car": ("cube-x3-y3", "cube-x4-y3"),
        },
        "trucks_vertical": {
            "yellow-truck": ["cube-x0-y1", "cube-x0-y2", "cube-x0-y3"],
        },
        "trucks_horizontal": {
            "purple-truck": ["cube-x3-y2", "cube-x4-y2", "cube-x5-y2"],
            "blue-truck": ["cube-x1-y4", "cube-x2-y4", "cube-x3-y4"],
            "green-truck": ["cube-x0-y5", "cube-x1-y5", "cube-x2-y5"],
        },
    },
    {
        "name": "Red-Car-Problem7-Intermediate",
        "cars_vertical": {
            "pink-car": ("cube-x2-y2", "cube-x2-y3"),
            "purple-car": ("cube-x3-y2", "cube-x3-y3"),
            "green-car": ("cube-x3-y0", "cube-x3-y1"),
            "green-over-car": ("cube-x4-y2", "cube-x4-y3"),
            "white-gray-car": ("cube-x5-y2", "cube-x5-y3"),
            "yellow-car": ("cube-x0-y4", "cube-x0-y5"),
            "brown-car": ("cube-x4-y4", "cube-x4-y5"),
            "yellow-special-car": ("cube-x5-y4", "cube-x5-y5"),
            },
        "cars_horizontal": {
            "red-car": ("cube-x0-y2", "cube-x1-y2"),
            "brown-sky-car": ("cube-x0-y3", "cube-x1-y3"),
            "orange-car": ("cube-x4-y0", "cube-x5-y0"),
            "blue-sky-car": ("cube-x4-y1", "cube-x5-y1"),
        },
        "trucks_vertical": {

        },
        "trucks_horizontal": {
            "purple-truck": ["cube-x1-y5", "cube-x2-y5", "cube-x3-y5"],
            "yellow-truck": ["cube-x1-y4", "cube-x2-y4", "cube-x3-y4"],
        },
    },
    {
        "name": "Red-Car-Problem8-Intermediate",
        "cars_vertical": {
            "pink-car": ("cube-x2-y1", "cube-x2-y2"),
            "orange-car": ("cube-x5-y0", "cube-x5-y1"),
            "green-over-car": ("cube-x5-y2", "cube-x5-y3"),
            "yellow-special-car": ("cube-x0-y4", "cube-x0-y5"),
            "white-gray-car": ("cube-x4-y3", "cube-x4-y4"),
            },
        "cars_horizontal": {
            "red-car": ("cube-x0-y2", "cube-x1-y2"),
            "blue-sky-car": ("cube-x0-y1", "cube-x1-y1"),
            "green-car": ("cube-x3-y0", "cube-x4-y0"),
            "purple-car": ("cube-x3-y1", "cube-x4-y1"),
            "yellow-car": ("cube-x1-y4", "cube-x2-y4"),
            "brown-car": ("cube-x4-y5", "cube-x5-y5"),
        },
        "trucks_vertical": {
            "purple-truck": ["cube-x3-y2", "cube-x3-y3", "cube-x3-y4"],
        },
        "trucks_horizontal": {
            "blue-truck": ["cube-x1-y5", "cube-x2-y5", "cube-x3-y5"],
            "yellow-truck": ["cube-x0-y0", "cube-x1-y0", "cube-x2-y0"],
        },
    },
    {
        "name": "Red-Car-Problem9-Advanced",
        "cars_vertical": {
            "green-car": ("cube-x1-y0", "cube-x1-y1"),
            "purple-car": ("cube-x2-y1", "cube-x2-y2"),
            "green-over-car": ("cube-x3-y1", "cube-x3-y2"),
            "pink-car": ("cube-x5-y0", "cube-x5-y1"),
            "blue-sky-car": ("cube-x4-y0", "cube-x4-y1"),
            "white-gray-car": ("cube-x4-y2", "cube-x4-y3"),
            "yellow-special-car": ("cube-x2-y3", "cube-x2-y4"),
            "yellow-over-car": ("cube-x3-y3", "cube-x3-y4"),
        },
        "cars_horizontal": {
            "red-car": ("cube-x0-y2", "cube-x1-y2"),
            "orange-car": ("cube-x2-y0", "cube-x3-y0"),
            "brown-car": ("cube-x4-y5", "cube-x5-y5"),
        },
        "trucks_vertical": {
            "yellow-truck": ["cube-x5-y2", "cube-x5-y3", "cube-x5-y4"],
            "purple-truck": ["cube-x0-y3", "cube-x0-y4", "cube-x0-y5"],
        },
        "trucks_horizontal": {
            "blue-truck": ["cube-x1-y5", "cube-x2-y5", "cube-x3-y5"],
        },
    },
    {
        "name": "Red-Car-Problem10-Advanced",
        "cars_vertical": {
            "green-car": ("cube-x0-y0", "cube-x0-y1"),
            "orange-car": ("cube-x2-y0", "cube-x2-y1"),
            "green-over-car": ("cube-x1-y3", "cube-x1-y4"),
            "pink-car": ("cube-x3-y2", "cube-x3-y3"),
            "purple-car": ("cube-x4-y2", "cube-x4-y3"),
            "yellow-car": ("cube-x5-y4", "cube-x5-y5"),
            "yellow-over-car": ("cube-x4-y4", "cube-x4-y5"),

        },
        "cars_horizontal": {
            "red-car": ("cube-x1-y2", "cube-x2-y2"),
            "blue-sky-car": ("cube-x4-y0", "cube-x5-y0"),
            "brown-car": ("cube-x0-y5", "cube-x1-y5"),
            "yellow-special-car": ("cube-x2-y5", "cube-x3-y5"),
            "white-gray-car": ("cube-x2-y4", "cube-x3-y4"),
        },
        "trucks_vertical": {
            "purple-truck": ["cube-x0-y2", "cube-x0-y3", "cube-x0-y4"],
        },
        "trucks_horizontal": {
            "yellow-truck": ["cube-x3-y1", "cube-x4-y1", "cube-x5-y1"],
        },
    },
    {
        "name": "Red-Car-Problem11-Advanced",
        "cars_vertical": {
            "orange-car": ("cube-x4-y0", "cube-x4-y1"),
            "blue-sky-car": ("cube-x5-y0", "cube-x5-y1"),
            "pink-car": ("cube-x0-y2", "cube-x0-y3"),
        },
        "cars_horizontal": {
            "red-car": ("cube-x1-y2", "cube-x2-y2"),
            "green-car": ("cube-x0-y0", "cube-x1-y0"),
            "green-over-car": ("cube-x0-y4", "cube-x1-y4"),
            "purple-car": ("cube-x3-y3", "cube-x4-y3"),
            "white-gray-car": ("cube-x0-y5", "cube-x0-y5"),
        },
        "trucks_vertical": {
            "purple-truck": ["cube-x5-y2", "cube-x5-y3", "cube-x5-y4"],
            "blue-truck": ["cube-x2-y3", "cube-x2-y4", "cube-x2-y5"],
            "yellow-truck": ["cube-x3-y0", "cube-x3-y1", "cube-x3-y2"],
        },
        "trucks_horizontal": {

        },
    },
    {
        "name": "Red-Car-Problem12-Advanced",
        "cars_vertical": {
            "orange-car": ("cube-x2-y0", "cube-x2-y1"),
            "pink-car": ("cube-x5-y3", "cube-x5-y4"),
            "purple-car": ("cube-x3-y4", "cube-x3-y5"),
        },
        "cars_horizontal": {
            "red-car": ("cube-x2-y2", "cube-x3-y2"),
            "green-car": ("cube-x0-y0", "cube-x1-y0"),
            "green-over-car": ("cube-x4-y5", "cube-x5-y5"),
            "blue-sky-car": ("cube-x4-y0", "cube-x5-y0"),
        },
        "trucks_vertical": {
            "purple-truck": ["cube-x4-y2", "cube-x4-y3", "cube-x4-y4"],
            "yellow-truck": ["cube-x0-y1", "cube-x0-y2", "cube-x0-y3"],

        },
        "trucks_horizontal": {
           "blue-truck": ["cube-x1-y3", "cube-x2-y3", "cube-x3-y3"],
        },
    },
    {
        "name": "Red-Car-Problem13-Advanced",
        "cars_vertical": {
            "orange-car": ("cube-x5-y0", "cube-x5-y1"),
            "blue-sky-car": ("cube-x0-y1", "cube-x0-y2"),
            "yellow-car": ("cube-x2-y4", "cube-x2-y5"),
            "white-gray-car": ("cube-x4-y3", "cube-x4-y4"),
        },
        "cars_horizontal": {
            "red-car": ("cube-x3-y2", "cube-x4-y2"),
            "green-car": ("cube-x0-y0", "cube-x1-y0"),
            "green-over-car": ("cube-x2-y3", "cube-x3-y3"),
            "purple-car": ("cube-x0-y3", "cube-x1-y3"),
            "yellow-hover-car": ("cube-x0-y4", "cube-x1-y4"),
            "pink-car": ("cube-x3-y1", "cube-x4-y1"),
        },
        "trucks_vertical": {
            "purple-truck": ["cube-x5-y2", "cube-x5-y3", "cube-x5-y4"],

        },
        "trucks_horizontal": {
            "blue-truck": ["cube-x3-y5", "cube-x4-y5", "cube-x5-y5"],
            "yellow-truck": ["cube-x2-y0", "cube-x3-y0", "cube-x4-y0"],
        },
    },

    {
        "name": "Red-Car-Problem13-Advanced",
        "cars_vertical": {
            "orange-car": ("cube-x4-y0", "cube-x4-y1"),
            "pink-car": ("cube-x0-y4", "cube-x0-y5"),
        },
        "cars_horizontal": {
            "red-car": ("cube-x3-y2", "cube-x4-y2"),
            "green-car": ("cube-x0-y0", "cube-x1-y0"),
            "purple-car": ("cube-x1-y4", "cube-x2-y4"),
            "blue-sky-car": ("cube-x4-y3", "cube-x5-y3"),

        },
        "trucks_vertical": {
            "purple-truck": ["cube-x5-y0", "cube-x5-y1", "cube-x5-y2"],
            "yellow-truck": ["cube-x2-y0", "cube-x2-y1", "cube-x2-y2"],
            "blue-truck": ["cube-x3-y3", "cube-x3-y4", "cube-x3-y5"],

        },
        "trucks_horizontal": {
        },
    },
    {
        "name": "Red-Car-Problem14-Advanced",
        "cars_vertical": {
            "orange-car": ("cube-x2-y2", "cube-x2-y3"),
            "blue-sky-car": ("cube-x3-y2", "cube-x3-y3"),
            "purple-car": ("cube-x3-y4", "cube-x3-y5"),
            "green-car": ("cube-x0-y0", "cube-x0-y1"),
        },
        "cars_horizontal": {
            "red-car": ("cube-x0-y2", "cube-x1-y2"),
            "green-hover-car": ("cube-x4-y4", "cube-x4-y5"),
            "pink-car": ("cube-x0-y3", "cube-x1-y3"),
            "white-gray-car": ("cube-x1-y5", "cube-x2-y5"),

        },
        "trucks_vertical": {
            "blue-truck": ["cube-x4-y1", "cube-x4-y2", "cube-x4-y3"],
            "green-truck": ["cube-x5-y1", "cube-x5-y2", "cube-x5-y3"],        },
        "trucks_horizontal": {
            "yellow-truck": ["cube-x2-y0", "cube-x3-y0", "cube-x4-y0"],
            "purple-truck": ["cube-x1-y1", "cube-x2-y1", "cube-x3-y1"],
        },
    },
    {
        "name": "Red-Car-Problem15-Expert",
        "cars_vertical": {
            "orange-car": ("cube-x1-y0", "cube-x1-y1"),
            "pink-car": ("cube-x4-y0", "cube-x4-y1"),
            "green-car": ("cube-x0-y0", "cube-x0-y1"),
            "purple-car": ("cube-x5-y0", "cube-x5-y1"),
            "yellow-car": ("cube-x2-y4", "cube-x2-y5"),
            "green-hover-car": ("cube-x3-y2", "cube-x3-y3"),
            "white-gray-car": ("cube-x5-y2", "cube-x5-y3"),
        },
        "cars_horizontal": {
            "red-car": ("cube-x1-y2", "cube-x2-y2"),
            "yellow-hover-car": ("cube-x1-y3", "cube-x2-y3"),
            "brown-car": ("cube-x0-y5", "cube-x1-y5"),
                },
        "trucks_vertical": {
            "yellow-truck": ["cube-x0-y2", "cube-x0-y3", "cube-x0-y4"],
        },
        "trucks_horizontal": {
            "blue-truck": ["cube-x3-y4", "cube-x4-y4", "cube-x5-y4"],
            "purple-truck": ["cube-x3-y5", "cube-x4-y5", "cube-x5-y5"],
        },
    },
    {
        "name": "Red-Car-Problem16 Expert",
        "cars_vertical": {
            "orange-car": ("cube-x5-y0", "cube-x5-y1"),
            "purple-car": ("cube-x4-y1", "cube-x4-y2"),
            "blue-sky-car": ("cube-x0-y1", "cube-x0-y2"),
            "yellow-special-car": ("cube-x4-y4", "cube-x4-y5"),
            "yellow-hover-car": ("cube-x3-y3", "cube-x3-y4"),
            "green-hover-car": ("cube-x5-y2", "cube-x5-y3"),
        },
        "cars_horizontal": {
            "red-car": ("cube-x2-y2", "cube-x3-y2"),
            "yellow-car": ("cube-x3-y3", "cube-x4-y3"),
            "brown-car": ("cube-x0-y4", "cube-x1-y4"),
            "white-gray-car": ("cube-x0-y3", "cube-x1-y3"),
            "green-car": ("cube-x0-y0", "cube-x1-y0"),
            "pink-car": ("cube-x2-y1", "cube-x3-y1"),

        },
        "trucks_vertical": {

        },
        "trucks_horizontal": {
            "yellow-truck": ["cube-x2-y0", "cube-x3-y0", "cube-x4-y0"],
            "purple-truck": ["cube-x0-y5", "cube-x1-y5", "cube-x2-y5"],
        },
    },
    {
        "name": "Red-Car-Problem17 Expert",
        "cars_vertical": {
            "orange-car": ("cube-x3-y0", "cube-x3-y1"),
            "blue-sky-car": ("cube-x5-y0", "cube-x5-y1"),
            "pink-car": ("cube-x0-y1", "cube-x0-y2"),
            "purple-car": ("cube-x1-y1", "cube-x1-y2"),
            "yellow-car": ("cube-x2-y4", "cube-x2-y5"),
            "green-hover-car": ("cube-x5-y2", "cube-x5-y3"),
            "yellow-hover-car": ("cube-x3-y3", "cube-x3-y4"),
        },
        "cars_horizontal": {
            "red-car": ("cube-x2-y2", "cube-x3-y2"),
            "green-car": ("cube-x0-y0", "cube-x1-y0"),
            "brown-car": ("cube-x3-y5", "cube-x4-y5"),
            "white-gray-car": ("cube-x1-y3", "cube-x2-y3"),
        },
        "trucks_vertical": {
            "yellow-truck": ["cube-x4-y2", "cube-x4-y3", "cube-x4-y4"],
            "purple-truck": ["cube-x0-y3", "cube-x0-y4", "cube-x0-y5"],
        },
        "trucks_horizontal": {
        },
    },
    {
        "name": "Red-Car-Problem18 Expert",
        "cars_vertical": {
            "orange-car": ("cube-x3-y0", "cube-x3-y1"),
            "pink-car": ("cube-x3-y2", "cube-x3-y3"),
            "white-gray-car": ("cube-x5-y4", "cube-x5-y5"),
            },
        "cars_horizontal": {
            "blue-sky-car": ("cube-x4-y1", "cube-x5-y1"),
            "red-car": ("cube-x1-y2", "cube-x2-y2"),
            "green-car": ("cube-x1-y0", "cube-x2-y0"),
            "purple-car": ("cube-x4-y3", "cube-x5-y3"),
            "green-hover-car": ("cube-x3-y4", "cube-x4-y4"),
        },
        "trucks_vertical": {
            "yellow-truck": ["cube-x0-y0", "cube-x0-y1", "cube-x0-y2"],
            "purple-truck": ["cube-x2-y3", "cube-x2-y4", "cube-x2-y5"],
        },
        "trucks_horizontal": {
        },
    },
    {
        "name": "Red-Car-Problem19 Expert",
        "cars_vertical": {
            "orange-car": ("cube-x3-y1", "cube-x3-y2"),
            "pink-car": ("cube-x0-y2", "cube-x0-y3"),
            "white-gray-car": ("cube-x0-y4", "cube-x0-y5"),
            "purple-car": ("cube-x5-y2", "cube-x5-y3"),
            "green-car": ("cube-x2-y0", "cube-x2-y1"),
            "green-hover-car": ("cube-x1-y3", "cube-x1-y4"),
            "yellow-car": ("cube-x5-y4", "cube-x5-y5"),
            },
        "cars_horizontal": {
            "blue-sky-car": ("cube-x4-y1", "cube-x5-y1"),
            "red-car": ("cube-x1-y2", "cube-x2-y2"),
            "brown-car": ("cube-x1-y5", "cube-x2-y5"),
            "yellow-hover-car": ("cube-x2-y4", "cube-x3-y4"),
            "yellow-special-car": ("cube-x3-y5", "cube-x4-y5"),
        },
        "trucks_vertical": {

            "purple-truck": ["cube-x4-y2", "cube-x4-y3", "cube-x4-y4"],
        },
        "trucks_horizontal": {
            "yellow-truck": ["cube-x3-y0", "cube-x4-y0", "cube-x5-y0"],
        },
    },
    {
        "name": "Red-Car-Problem20 Expert",
        "cars_vertical": {
            "green-car": ("cube-x0-y0", "cube-x0-y1"),
            "pink-car": ("cube-x4-y1", "cube-x4-y2"),
            "yellow-car": ("cube-x3-y4", "cube-x3-y5"),
            "purple-car": ("cube-x2-y2", "cube-x2-y3"),
        },
        "cars_horizontal": {
            "blue-sky-car": ("cube-x2-y1", "cube-x3-y1"),
            "red-car": ("cube-x0-y2", "cube-x1-y2"),
            "green-hover-car": ("cube-x0-y3", "cube-x1-y3"),
            "yellow-hover-car": ("cube-x1-y4", "cube-x2-y4"),
            "orange-car": ("cube-x1-y0", "cube-x2-y0"),
            "white-gray-car": ("cube-x3-y3", "cube-x4-y3"),
        },
        "trucks_vertical": {

            "purple-truck": ["cube-x5-y3", "cube-x5-y4", "cube-x5-y5"],
        },
        "trucks_horizontal": {
            "yellow-truck": ["cube-x3-y0", "cube-x4-y0", "cube-x5-y0"],
            "blue-truck": ["cube-x0-y5", "cube-x1-y5", "cube-x2-y5"],
        },
    },
    # Add more problems here...
]

# Generate the files
grid_size = 6  # The grid size is consistent for all problems
for problem in problems:
    generate_problem_file(
        problem_name=problem["name"],
        grid_size=grid_size,
        cars_vertical=problem["cars_vertical"],
        cars_horizontal=problem["cars_horizontal"],
        trucks_vertical=problem["trucks_vertical"],
        trucks_horizontal=problem["trucks_horizontal"],
    )

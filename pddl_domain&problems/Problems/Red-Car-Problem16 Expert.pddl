(define (problem Red-Car-Problem16 Expert)
(:domain RedCar)
(:objects
;;Cubes: Represent the individual grid cells in the 6x6 grid.
Each cube has a unique identifier based on its coordinates (e.g., cube-x0-y0 for the cell at column 0, row 0).
cube-x0-y0 cube-x1-y0 cube-x2-y0 cube-x3-y0 cube-x4-y0 cube-x5-y0 - cube ;; row 1
cube-x0-y1 cube-x1-y1 cube-x2-y1 cube-x3-y1 cube-x4-y1 cube-x5-y1 - cube ;; row 2
cube-x0-y2 cube-x1-y2 cube-x2-y2 cube-x3-y2 cube-x4-y2 cube-x5-y2 - cube ;; row 3
cube-x0-y3 cube-x1-y3 cube-x2-y3 cube-x3-y3 cube-x4-y3 cube-x5-y3 - cube ;; row 4
cube-x0-y4 cube-x1-y4 cube-x2-y4 cube-x3-y4 cube-x4-y4 cube-x5-y4 - cube ;; row 5
cube-x0-y5 cube-x1-y5 cube-x2-y5 cube-x3-y5 cube-x4-y5 cube-x5-y5 - cube ;; row 6

;;Cars: Represents cars in the grid, identified by their names (e.g., red-car).
orange-car purple-car blue-sky-car yellow-special-car yellow-hover-car green-hover-car red-car yellow-car brown-car white-gray-car green-car pink-car - car
;;Trucks:  Represents trucks in the grid, identified by their names (e.g., green-truck).
yellow-truck purple-truck - truck
)
(:init

;;Car Adjacency: Defines the relationships between adjacent grid cells that cars can occupy.(Only 2 cubes)
;;Horizontal adjacency: Specifies which cells are next to each other horizontally in the same row.
;;Example: (adjacent-horizontal-car cube-x0-y0 cube-x1-y0)
;;Vertical adjacency: Specifies which cells are next to each other vertically in the same column.
;;Example: (adjacent-vertical-car cube-x0-y0 cube-x0-y1)

;; Horizontal Car Adjacency
(adjacent-horizontal-car cube-x0-y0 cube-x1-y0)
(adjacent-horizontal-car cube-x1-y0 cube-x2-y0)
(adjacent-horizontal-car cube-x2-y0 cube-x3-y0)
(adjacent-horizontal-car cube-x3-y0 cube-x4-y0)
(adjacent-horizontal-car cube-x4-y0 cube-x5-y0)
(adjacent-horizontal-car cube-x0-y1 cube-x1-y1)
(adjacent-horizontal-car cube-x1-y1 cube-x2-y1)
(adjacent-horizontal-car cube-x2-y1 cube-x3-y1)
(adjacent-horizontal-car cube-x3-y1 cube-x4-y1)
(adjacent-horizontal-car cube-x4-y1 cube-x5-y1)
(adjacent-horizontal-car cube-x0-y2 cube-x1-y2)
(adjacent-horizontal-car cube-x1-y2 cube-x2-y2)
(adjacent-horizontal-car cube-x2-y2 cube-x3-y2)
(adjacent-horizontal-car cube-x3-y2 cube-x4-y2)
(adjacent-horizontal-car cube-x4-y2 cube-x5-y2)
(adjacent-horizontal-car cube-x0-y3 cube-x1-y3)
(adjacent-horizontal-car cube-x1-y3 cube-x2-y3)
(adjacent-horizontal-car cube-x2-y3 cube-x3-y3)
(adjacent-horizontal-car cube-x3-y3 cube-x4-y3)
(adjacent-horizontal-car cube-x4-y3 cube-x5-y3)
(adjacent-horizontal-car cube-x0-y4 cube-x1-y4)
(adjacent-horizontal-car cube-x1-y4 cube-x2-y4)
(adjacent-horizontal-car cube-x2-y4 cube-x3-y4)
(adjacent-horizontal-car cube-x3-y4 cube-x4-y4)
(adjacent-horizontal-car cube-x4-y4 cube-x5-y4)
(adjacent-horizontal-car cube-x0-y5 cube-x1-y5)
(adjacent-horizontal-car cube-x1-y5 cube-x2-y5)
(adjacent-horizontal-car cube-x2-y5 cube-x3-y5)
(adjacent-horizontal-car cube-x3-y5 cube-x4-y5)
(adjacent-horizontal-car cube-x4-y5 cube-x5-y5)

;; Vertical Car Adjacency
(adjacent-vertical-car cube-x0-y0 cube-x0-y1)
(adjacent-vertical-car cube-x0-y1 cube-x0-y2)
(adjacent-vertical-car cube-x0-y2 cube-x0-y3)
(adjacent-vertical-car cube-x0-y3 cube-x0-y4)
(adjacent-vertical-car cube-x0-y4 cube-x0-y5)
(adjacent-vertical-car cube-x1-y0 cube-x1-y1)
(adjacent-vertical-car cube-x1-y1 cube-x1-y2)
(adjacent-vertical-car cube-x1-y2 cube-x1-y3)
(adjacent-vertical-car cube-x1-y3 cube-x1-y4)
(adjacent-vertical-car cube-x1-y4 cube-x1-y5)
(adjacent-vertical-car cube-x2-y0 cube-x2-y1)
(adjacent-vertical-car cube-x2-y1 cube-x2-y2)
(adjacent-vertical-car cube-x2-y2 cube-x2-y3)
(adjacent-vertical-car cube-x2-y3 cube-x2-y4)
(adjacent-vertical-car cube-x2-y4 cube-x2-y5)
(adjacent-vertical-car cube-x3-y0 cube-x3-y1)
(adjacent-vertical-car cube-x3-y1 cube-x3-y2)
(adjacent-vertical-car cube-x3-y2 cube-x3-y3)
(adjacent-vertical-car cube-x3-y3 cube-x3-y4)
(adjacent-vertical-car cube-x3-y4 cube-x3-y5)
(adjacent-vertical-car cube-x4-y0 cube-x4-y1)
(adjacent-vertical-car cube-x4-y1 cube-x4-y2)
(adjacent-vertical-car cube-x4-y2 cube-x4-y3)
(adjacent-vertical-car cube-x4-y3 cube-x4-y4)
(adjacent-vertical-car cube-x4-y4 cube-x4-y5)
(adjacent-vertical-car cube-x5-y0 cube-x5-y1)
(adjacent-vertical-car cube-x5-y1 cube-x5-y2)
(adjacent-vertical-car cube-x5-y2 cube-x5-y3)
(adjacent-vertical-car cube-x5-y3 cube-x5-y4)
(adjacent-vertical-car cube-x5-y4 cube-x5-y5)


;;Truck Adjacency: Defines the relationships between groups of grid cells that trucks can occupy.
;;Horizontal adjacency: Specifies groups of three consecutive cells in the same row that trucks can occupy.
;;Example: (adjacent-horizontal-truck cube-x0-y0 cube-x1-y0 cube-x2-y0)
;;Vertical adjacency: Specifies groups of three consecutive cells in the same column that trucks can occupy.
;;Example: (adjacent - vertical - truck cube-x0-y0 cube-x0-y1 cube-x0-y2)

;; Horizontal Truck Adjacency
(adjacent-horizontal-truck cube-x0-y0 cube-x1-y0 cube-x2-y0)
(adjacent-horizontal-truck cube-x1-y0 cube-x2-y0 cube-x3-y0)
(adjacent-horizontal-truck cube-x2-y0 cube-x3-y0 cube-x4-y0)
(adjacent-horizontal-truck cube-x3-y0 cube-x4-y0 cube-x5-y0)
(adjacent-horizontal-truck cube-x0-y1 cube-x1-y1 cube-x2-y1)
(adjacent-horizontal-truck cube-x1-y1 cube-x2-y1 cube-x3-y1)
(adjacent-horizontal-truck cube-x2-y1 cube-x3-y1 cube-x4-y1)
(adjacent-horizontal-truck cube-x3-y1 cube-x4-y1 cube-x5-y1)
(adjacent-horizontal-truck cube-x0-y2 cube-x1-y2 cube-x2-y2)
(adjacent-horizontal-truck cube-x1-y2 cube-x2-y2 cube-x3-y2)
(adjacent-horizontal-truck cube-x2-y2 cube-x3-y2 cube-x4-y2)
(adjacent-horizontal-truck cube-x3-y2 cube-x4-y2 cube-x5-y2)
(adjacent-horizontal-truck cube-x0-y3 cube-x1-y3 cube-x2-y3)
(adjacent-horizontal-truck cube-x1-y3 cube-x2-y3 cube-x3-y3)
(adjacent-horizontal-truck cube-x2-y3 cube-x3-y3 cube-x4-y3)
(adjacent-horizontal-truck cube-x3-y3 cube-x4-y3 cube-x5-y3)
(adjacent-horizontal-truck cube-x0-y4 cube-x1-y4 cube-x2-y4)
(adjacent-horizontal-truck cube-x1-y4 cube-x2-y4 cube-x3-y4)
(adjacent-horizontal-truck cube-x2-y4 cube-x3-y4 cube-x4-y4)
(adjacent-horizontal-truck cube-x3-y4 cube-x4-y4 cube-x5-y4)
(adjacent-horizontal-truck cube-x0-y5 cube-x1-y5 cube-x2-y5)
(adjacent-horizontal-truck cube-x1-y5 cube-x2-y5 cube-x3-y5)
(adjacent-horizontal-truck cube-x2-y5 cube-x3-y5 cube-x4-y5)
(adjacent-horizontal-truck cube-x3-y5 cube-x4-y5 cube-x5-y5)

;; Horizontal Truck Adjacency
(adjacent-vertical-truck cube-x0-y0 cube-x0-y1 cube-x0-y2)
(adjacent-vertical-truck cube-x0-y1 cube-x0-y2 cube-x0-y3)
(adjacent-vertical-truck cube-x0-y2 cube-x0-y3 cube-x0-y4)
(adjacent-vertical-truck cube-x0-y3 cube-x0-y4 cube-x0-y5)
(adjacent-vertical-truck cube-x1-y0 cube-x1-y1 cube-x1-y2)
(adjacent-vertical-truck cube-x1-y1 cube-x1-y2 cube-x1-y3)
(adjacent-vertical-truck cube-x1-y2 cube-x1-y3 cube-x1-y4)
(adjacent-vertical-truck cube-x1-y3 cube-x1-y4 cube-x1-y5)
(adjacent-vertical-truck cube-x2-y0 cube-x2-y1 cube-x2-y2)
(adjacent-vertical-truck cube-x2-y1 cube-x2-y2 cube-x2-y3)
(adjacent-vertical-truck cube-x2-y2 cube-x2-y3 cube-x2-y4)
(adjacent-vertical-truck cube-x2-y3 cube-x2-y4 cube-x2-y5)
(adjacent-vertical-truck cube-x3-y0 cube-x3-y1 cube-x3-y2)
(adjacent-vertical-truck cube-x3-y1 cube-x3-y2 cube-x3-y3)
(adjacent-vertical-truck cube-x3-y2 cube-x3-y3 cube-x3-y4)
(adjacent-vertical-truck cube-x3-y3 cube-x3-y4 cube-x3-y5)
(adjacent-vertical-truck cube-x4-y0 cube-x4-y1 cube-x4-y2)
(adjacent-vertical-truck cube-x4-y1 cube-x4-y2 cube-x4-y3)
(adjacent-vertical-truck cube-x4-y2 cube-x4-y3 cube-x4-y4)
(adjacent-vertical-truck cube-x4-y3 cube-x4-y4 cube-x4-y5)
(adjacent-vertical-truck cube-x5-y0 cube-x5-y1 cube-x5-y2)
(adjacent-vertical-truck cube-x5-y1 cube-x5-y2 cube-x5-y3)
(adjacent-vertical-truck cube-x5-y2 cube-x5-y3 cube-x5-y4)
(adjacent-vertical-truck cube-x5-y3 cube-x5-y4 cube-x5-y5)

;;Car&Trucks Initial Position: 

(at-car-horizontal red-car cube-x2-y2 cube-x3-y2)
(not (clear cube-x2-y2))
(not (clear cube-x3-y2))
(at-car-horizontal yellow-car cube-x3-y3 cube-x4-y3)
(not (clear cube-x3-y3))
(not (clear cube-x4-y3))
(at-car-horizontal brown-car cube-x0-y4 cube-x1-y4)
(not (clear cube-x0-y4))
(not (clear cube-x1-y4))
(at-car-horizontal white-gray-car cube-x0-y3 cube-x1-y3)
(not (clear cube-x0-y3))
(not (clear cube-x1-y3))
(at-car-horizontal green-car cube-x0-y0 cube-x1-y0)
(not (clear cube-x0-y0))
(not (clear cube-x1-y0))
(at-car-horizontal pink-car cube-x2-y1 cube-x3-y1)
(not (clear cube-x2-y1))
(not (clear cube-x3-y1))
(at-car-vertical orange-car cube-x5-y0 cube-x5-y1)
(not (clear cube-x5-y0))
(not (clear cube-x5-y1))
(at-car-vertical purple-car cube-x4-y1 cube-x4-y2)
(not (clear cube-x4-y1))
(not (clear cube-x4-y2))
(at-car-vertical blue-sky-car cube-x0-y1 cube-x0-y2)
(not (clear cube-x0-y1))
(not (clear cube-x0-y2))
(at-car-vertical yellow-special-car cube-x4-y4 cube-x4-y5)
(not (clear cube-x4-y4))
(not (clear cube-x4-y5))
(at-car-vertical yellow-hover-car cube-x3-y3 cube-x3-y4)
(not (clear cube-x3-y3))
(not (clear cube-x3-y4))
(at-car-vertical green-hover-car cube-x5-y2 cube-x5-y3)
(not (clear cube-x5-y2))
(not (clear cube-x5-y3))
(at-truck-horizontal yellow-truck cube-x2-y0 cube-x3-y0 cube-x4-y0)
(not (clear cube-x2-y0))
(not (clear cube-x3-y0))
(not (clear cube-x4-y0))
(at-truck-horizontal purple-truck cube-x0-y5 cube-x1-y5 cube-x2-y5)
(not (clear cube-x0-y5))
(not (clear cube-x1-y5))
(not (clear cube-x2-y5))
(clear cube-x2-y4)
(clear cube-x1-y2)
(clear cube-x2-y3)
(clear cube-x5-y5)
(clear cube-x5-y4)
(clear cube-x3-y5)
(clear cube-x1-y1)

)
(:goal
    (at-car-horizontal red-car cube-x4-y2 cube-x5-y2)
))

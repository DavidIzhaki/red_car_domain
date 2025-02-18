(define (domain RedCar)
  (:requirements :typing :action-costs)

  (:types
      vehicle - object
      car truck - vehicle
      horizontalCar verticalCar - car
      horizontalTruck verticalTruck - truck
  )

  (:functions
     (pos-x ?v - vehicle)   - number;; X coordinate
     (pos-y ?v - vehicle)  - number ;; Y coordinate
     (grid-width) - number           ;; Max X boundary
     (grid-height) - number         ;; Max Y boundary
     (clear ?x ?y) - number ;; 1 if cell is clear, 0 if occupied
     (total-cost) - number           ;; Sum of movement costs
  )

  ;; Move Horizontal Car Right
  (:action move-car-right
    :parameters (?c - horizontalCar)
    :precondition (and
        (< (+ (pos-x ?c) 2) grid-width) ;; Ensure within grid
        (= (clear (+ (pos-x ?c) 2) (pos-y ?c)) 1) ;; Ensure new cell is clear
    )
    :effect (and
        (increase (clear (pos-x ?c) (pos-y ?c)) 1) ;; Free current leftmost cell
        (decrease (clear (+ (pos-x ?c) 2) (pos-y ?c)) 1) ;; Occupy new rightmost cell
        (increase (pos-x ?c) 1) ;; Move car right
        (increase (total-cost) 1) ;; Track cost
    )
  )


  ;; Move Horizontal Car Left
  (:action move-car-left
    :parameters (?c - horizontalCar)
    :precondition (and
        (> (pos-x ?c) 0) ;; Ensure within grid
        (= (clear (- (pos-x ?c) 1) (pos-y ?c)) 1) ;; Ensure new cell is clear
    )
    :effect (and
        (decrease (clear (+ (pos-x ?c) 1) (pos-y ?c)) 1) ;; Free old cell (x+1, y)
        (increase (clear (- (pos-x ?c) 1) (pos-y ?c)) 1) ;; Occupy new cell (x-1, y)
        (decrease (pos-x ?c) 1) ;; Move car left
        (increase (total-cost) 1)
    )
  )


  ;; Move Vertical Car Up
  (:action move-car-up
    :parameters (?c - verticalCar)
    :precondition (and
        (> (pos-y ?c) 0) ;; Check within grid
        (= (clear (pos-x ?c) (- (pos-y ?c) 1)) 1) ;; Ensure new cell is clear
    )
    :effect (and
        (increase (clear (pos-x ?c) (+ (pos-y ?c) 1)) 1) ;; Free top cell (x, y+1)
        (decrease (clear (pos-x ?c) (- (pos-y ?c) 1)) 1) ;; Occupy new top cell (x, y-1)
        (decrease (pos-y ?c) 1) ;; Move car down
        (increase (total-cost) 1)
    )
  )


  ;; Move Vertical Car Down
  (:action move-car-down
    :parameters (?c - verticalCar)
    :precondition (and
        (< (+ (pos-y ?c) 2) grid-height) ;; Check within grid
        (= (clear (pos-x ?c) (+ (pos-y ?c) 2)) 1) ;; Ensure new cell is clear
    )
    :effect (and
        (increase (clear (pos-x ?c) (pos-y ?c)) 1) ;; Free bottom cell (x, y)
        (decrease (clear (pos-x ?c) (+ (pos-y ?c) 2)) 1) ;; Occupy new bottom cell (x, y+2)
        (increase (pos-y ?c) 1) ;; Move car up
        (increase (total-cost) 1)
    )
  )

  ;; Move Horizontal Truck Right
  (:action move-truck-right
    :parameters (?t - horizontalTruck)
    :precondition (and
        (< (+ (pos-x ?t) 3) grid-width) ;; Ensure within grid
        (= (clear (+ (pos-x ?t) 3) (pos-y ?t)) 1) ;; Ensure new cell is clear
    )
    :effect (and
        (decrease (clear (pos-x ?t) (pos-y ?t)) 1) ;; Free old cell (x, y)
        (increase (clear (+ (pos-x ?t) 3) (pos-y ?t)) 1) ;; Occupy new cell (x+3, y)
        (increase (pos-x ?t) 1) ;; Move truck right
        (increase (total-cost) 1)
    )
  )

  ;; Move Horizontal Truck Left
  (:action move-truck-left
    :parameters (?t - horizontalTruck)
    :precondition (and
        (> (pos-x ?t) 0) ;; Ensure within grid
        (= (clear (- (pos-x ?t) 1) (pos-y ?t)) 1) ;; Ensure new cell is clear
    )
    :effect (and
        (decrease (clear (+ (pos-x ?t) 2) (pos-y ?t)) 1) ;; Free old cell (x+2, y)
        (increase (clear (- (pos-x ?t) 1) (pos-y ?t)) 1) ;; Occupy new cell (x-1, y)
        (decrease (pos-x ?t) 1) ;; Move truck left
        (increase (total-cost) 1)
    )
  )

   ;; Move Vertical Truck Truck Down
  (:action move-truck-down
    :parameters (?t - verticalTruck)
    :precondition (and
        (< (+ (pos-y ?t) 3) grid-height) ;; Check within grid
        (= (clear (pos-x ?t) (+ (pos-y ?t) 3)) 1) ;; Ensure new top cell is clear
    )
    :effect (and
        (increase (clear (pos-x ?t) (pos-y ?t)) 1) ;; Free cell (x, y)
        (decrease (clear (pos-x ?t) (+ (pos-y ?t) 3)) 1) ;; Occupy new bottom cell (x, y+3)
        (increase (pos-y ?t) 1) ;; Move truck up
        (increase (total-cost) 1)
    )
  )

   ;; Move Vertical Truck Up
  (:action move-truck-up
    :parameters (?t - verticalTruck)
    :precondition (and
        (> (pos-y ?t) 0) ;; Check within grid
        (= (clear (pos-x ?t) (- (pos-y ?t) 1)) 1) ;; Ensure new bottom cell is clear
    )
    :effect (and
        (increase (clear (pos-x ?t) (+ (pos-y ?t) 2)) 1) ;; Free  cell (x, y+2)
        (decrease (clear (pos-x ?t) (- (pos-y ?t) 1)) 1) ;; Occupy new top cell (x, y-1)
        (decrease (pos-y ?t) 1) ;; Move truck down
        (increase (total-cost) 1)
    )
  )





)

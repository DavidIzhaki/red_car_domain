;; Transport sequential domain
(define (domain RedCar)
  (:requirements :typing)
  
  (:types
      object
      cube
      car truck - object
      horizontalCar verticalCar - car
      horizontalTruck verticalTruck - truck
  )

  (:predicates 
     (adjacent-horizontal-car ?c1 ?c2 - cube) 
     (adjacent-vertical-car ?c1 ?c2 - cube) 
     (adjacent-horizontal-truck ?c1 ?c2 ?c3 - cube) 
     (adjacent-vertical-truck ?c1 ?c2 ?c3 - cube)  
     (clear ?c1 - cube)
     (at-truck-horizontal ?t - horizontalTruck ?c1 ?c2 ?c3 - cube) 
     (at-truck-vertical ?t - verticalTruck ?c1 ?c2 ?c3 - cube)
     (at-car-horizontal ?c - horizontalCar ?c1 ?c2 - cube) 
     (at-car-vertical ?c - verticalCar ?c1 ?c2 - cube)
  )

  ;; Move Horizontal Car Right
  (:action move-car-horizontal-right
    :parameters (?c - horizontalCar ?c1 ?c2 ?c3 - cube)
    :precondition (and
        (at-car-horizontal ?c ?c1 ?c2)
        (adjacent-horizontal-car ?c2 ?c3)
        (clear ?c3)
    )
    :effect (and
        (not (at-car-horizontal ?c ?c1 ?c2))
        (at-car-horizontal ?c ?c2 ?c3)
        (not (clear ?c3))
        (clear ?c1)
    )
  )

  ;; Move Horizontal Car Left
  (:action move-car-horizontal-left
    :parameters (?c - horizontalCar ?c1 ?c2 ?c3 - cube)
    :precondition (and
        (at-car-horizontal ?c ?c2 ?c3)
        (adjacent-horizontal-car ?c1 ?c2)
        (clear ?c1)
    )
    :effect (and
        (not (at-car-horizontal ?c ?c2 ?c3))
        (at-car-horizontal ?c ?c1 ?c2)
        (not (clear ?c1))
        (clear ?c3)
    )
  )

  ;; Move Vertical Car Up
  (:action move-car-vertical-up
    :parameters (?c - verticalCar ?c1 ?c2 ?c3 - cube)
    :precondition (and
        (at-car-vertical ?c ?c1 ?c2)
        (adjacent-vertical-car ?c2 ?c3)
        (clear ?c3)
    )
    :effect (and
        (not (at-car-vertical ?c ?c1 ?c2))
        (at-car-vertical ?c ?c2 ?c3)
        (not (clear ?c3))
        (clear ?c1)
    )
  )

  ;; Move Vertical Car Down
  (:action move-car-vertical-down
    :parameters (?c - verticalCar ?c1 ?c2 ?c3 - cube)
    :precondition (and
        (at-car-vertical ?c ?c2 ?c3)
        (adjacent-vertical-car ?c1 ?c2)
        (clear ?c1)
    )
    :effect (and
        (not (at-car-vertical ?c ?c2 ?c3))
        (at-car-vertical ?c ?c1 ?c2)
        (not (clear ?c1))
        (clear ?c3)
    )
  )

  ;; Move Horizontal Truck Right
  (:action move-truck-horizontal-right
    :parameters (?t - horizontalTruck ?c1 ?c2 ?c3 ?c4 - cube)
    :precondition (and
        (at-truck-horizontal ?t ?c1 ?c2 ?c3)
        (adjacent-horizontal-truck ?c2 ?c3 ?c4)
        (clear ?c4)
    )
    :effect (and
        (not (at-truck-horizontal ?t ?c1 ?c2 ?c3))
        (at-truck-horizontal ?t ?c2 ?c3 ?c4)
        (not (clear ?c4))
        (clear ?c1)
    )
  )

  ;; Move Horizontal Truck Left
  (:action move-truck-horizontal-left
    :parameters (?t - horizontalTruck ?c1 ?c2 ?c3 ?c4 - cube)
    :precondition (and
        (at-truck-horizontal ?t ?c2 ?c3 ?c4)
        (adjacent-horizontal-truck ?c1 ?c2 ?c3)
        (clear ?c1)
    )
    :effect (and
        (not (at-truck-horizontal ?t ?c2 ?c3 ?c4))
        (at-truck-horizontal ?t ?c1 ?c2 ?c3)
        (not (clear ?c1))
        (clear ?c4)
    )
  )

  ;; Move Vertical Truck Up
  (:action move-truck-vertical-up
    :parameters (?t - verticalTruck ?c1 ?c2 ?c3 ?c4 - cube)
    :precondition (and
        (at-truck-vertical ?t ?c1 ?c2 ?c3)
        (adjacent-vertical-truck ?c2 ?c3 ?c4)
        (clear ?c4)
    )
    :effect (and
        (not (at-truck-vertical ?t ?c1 ?c2 ?c3))
        (at-truck-vertical ?t ?c2 ?c3 ?c4)
        (not (clear ?c4))
        (clear ?c1)
    )
  )

  ;; Move Vertical Truck Down
  (:action move-truck-vertical-down
    :parameters (?t - verticalTruck ?c1 ?c2 ?c3 ?c4 - cube)
    :precondition (and
        (at-truck-vertical ?t ?c2 ?c3 ?c4)
        (adjacent-vertical-truck ?c1 ?c2 ?c3)
        (clear ?c1)
    )
    :effect (and
        (not (at-truck-vertical ?t ?c2 ?c3 ?c4))
        (at-truck-vertical ?t ?c1 ?c2 ?c3)
        (not (clear ?c1))
        (clear ?c4)
    )
  )
)

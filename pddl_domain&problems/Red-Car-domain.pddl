;; Transport sequential
;;

(define (domain RedCar)
  (:requirements :typing)
  (:types
        cube car truck - object
  )

  (:predicates 
    
     (adjacent-horizontal-car ?c1 ?c2 - cube) 
     (adjacent-vertical-car ?c1 ?c2 - cube) 
     (adjacent-horizontal-truck ?c1 ?c2 ?c3 - cube) 
     (adjacent-vertical-truck ?c1 ?c2 ?c3 - cube)  
     (clear ?c1 - cube)
     (at-truck-horizontal ?t - truck ?c1 ?c2 ?c3 - cube) 
     (at-truck-vertical ?t - truck ?c1 ?c2 ?c3 - cube)
     (at-car-horizontal ?c - car ?c1 ?c2 - cube) 
     (at-car-vertical ?c - car ?c1 ?c2 - cube)

  )

 (:action move-car-horizontal-right
    :parameters (?c - car ?c1 ?c2 ?c3 - cube)
    :precondition (and
        (at-car-horizontal ?c ?c1 ?c2)  ;; Car is horizontal and occupies ?c1 and ?c2
        (adjacent-horizontal-car ?c2 ?c3)  ;; ?c3 is adjacent to the right of ?c2
        (clear ?c3)                    ;; ?c3 must be clear
    )
    :effect (and
        ;; Update the car's position
        (not (at-car-horizontal ?c ?c1 ?c2))
        (at-car-horizontal ?c ?c2 ?c3)
        
        ;; Update the grid
        (not (clear ?c3))  ;; ?c3 is now occupied
        (clear ?c1)        ;; ?c1 is now free
    )
 )
  (:action move-car-horizontal-left
    :parameters (?c - car ?c1 ?c2 ?c3 - cube)
    :precondition (and
        (at-car-horizontal ?c ?c2 ?c3)  ;; Car is horizontal and occupies ?c2 and ?c3
        (adjacent-horizontal-car ?c1 ?c2)  ;; ?c1 is adjacent to the left of ?c2
        (clear ?c1)                    ;; ?c1 must be clear
    )
    :effect (and
        ;; Update the car's position
        (not (at-car-horizontal ?c ?c2 ?c3))
        (at-car-horizontal ?c ?c1 ?c2)
        
        ;; Update the grid
        (not (clear ?c1))  ;; ?c1 is now occupied
        (clear ?c3)        ;; ?c3 is now free
    )
 )
 
 (:action move-car-vertical-up
    :parameters (?c - car ?c1 ?c2 ?c3 - cube)
    :precondition (and
        (at-car-vertical ?c ?c1 ?c2)  ;; Car is vertical and occupies ?c1 and ?c2
        (adjacent-vertical-car ?c2 ?c3)  ;; ?c3 is adjacent to the up of ?c2
        (clear ?c3)                    ;; ?c3 must be clear
    )
    :effect (and
        ;; Update the car's position
        (not (at-car-vertical ?c ?c1 ?c2))
        (at-car-vertical ?c ?c2 ?c3)
        
        ;; Update the grid
        (not (clear ?c3))  ;; ?c3 is now occupied
        (clear ?c1)        ;; ?c1 is now free
    )
 )
 (:action move-car-vertical-down
    :parameters (?c - car ?c1 ?c2 ?c3 - cube)
    :precondition (and
        (at-car-vertical ?c ?c2 ?c3)  ;; Car is vertical and occupies ?c2 and ?c3
        (adjacent-vertical-car ?c1 ?c2)  ;; ?c1 is adjacent to the down of ?c2
        (clear ?c1)                    ;; ?c must be clear
    )
    :effect (and
        ;; Update the car's position
        (not (at-car-vertical ?c ?c2 ?c3))
        (at-car-vertical ?c ?c1 ?c2)
        
        ;; Update the grid
        (not (clear ?c1))  ;; ?c3 is now occupied
        (clear ?c3)        ;; ?c1 is now free
    )
 )
 
 
 (:action move-truck-horizontal-right
    :parameters (?t - truck ?c1 ?c2 ?c3 ?c4 - cube)
    :precondition (and
        (at-truck-horizontal ?t ?c1 ?c2 ?c3)  ;; Truck is horizontal and occupies ?c1 and ?c2 and ?c3
        (adjacent-horizontal-truck ?c2 ?c3 ?c4)  ;; ?c2 ?c3 is adjacent to the right of ?c4
        (clear ?c4)                    ;; ?c4 must be clear
    )
    :effect (and
        ;; Update the truck's position
        (not (at-truck-horizontal ?t ?c1 ?c2 ?c3))
        (at-truck-horizontal ?t ?c2 ?c3 ?c4)
        
        ;; Update the grid
        (not (clear ?c4))  ;; ?c4 is now occupied
        (clear ?c1)        ;; ?c1 is now free
    )
 )
  (:action move-truck-horizontal-left
    :parameters (?t - truck ?c1 ?c2 ?c3 ?c4 - cube)
    :precondition (and
        (at-truck-horizontal ?t ?c2 ?c3 ?c4)  ;; Car is horizontal and occupies ?c2 and ?c3 and ?c4
        (adjacent-horizontal-truck ?c1 ?c2 ?c3)  ;; ?c1 is adjacent to the left of ?c2 and ?c3
        (clear ?c1)                    ;; ?c1 must be clear
    )
    :effect (and
        ;; Update the car's position
        (not (at-truck-horizontal ?t ?c2 ?c3 ?c4))
        (at-truck-horizontal ?t ?c1 ?c2 ?c3)
        
        ;; Update the grid
        (not (clear ?c1))  ;; ?c1 is now occupied
        (clear ?c4)        ;; ?c4 is now free
    )
 )
 
 (:action move-truck-vertical-up
    :parameters (?t - truck ?c1 ?c2 ?c3 ?c4 - cube)
    :precondition (and
        (at-truck-vertical ?t ?c1 ?c2 ?c3)  ;; Car is vertical and occupies ?c1 and ?c2 and ?c3
        (adjacent-vertical-truck ?c2 ?c3 ?c4)  ;; ?c4 is adjacent to the up of ?c2 and ?c3
        (clear ?c4)                    ;; ?c3 must be clear
    )
    :effect (and
        ;; Update the car's position
        (not (at-truck-vertical ?t ?c1 ?c2 ?c3))
        (at-truck-vertical ?t ?c2 ?c3 ?c4)
        
        ;; Update the grid
        (not (clear ?c4))  ;; ?c4 is now occupied
        (clear ?c1)        ;; ?c1 is now free
    )
 )
 (:action move-truck-vertical-down
    :parameters (?t - truck ?c1 ?c2 ?c3 ?c4 - cube)
    :precondition (and
        (at-truck-vertical ?t ?c2 ?c3 ?c4)  ;; Car is vertical and occupies ?c2 and ?c3 and ?c4
        (adjacent-vertical-truck ?c1 ?c2 ?c3)  ;; ?c1 is adjacent to the down of ?c2 and ?c3
        (clear ?c1)                    ;; ?c must be clear
    )
    :effect (and
        ;; Update the car's position
        (not (at-truck-vertical ?t ?c2 ?c3 ?c4))
        (at-truck-vertical ?t ?c1 ?c2 ?c3)
        
        ;; Update the grid
        (not (clear ?c1))  ;; ?c3 is now occupied
        (clear ?c4)        ;; ?c1 is now free
    )
 )

)

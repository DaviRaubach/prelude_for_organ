
#(define-event-class 'music-boxer-event 'span-event)

#(define-event-class 'box-event 'music-event)

#(define (add-grob-definition grob-name grob-entry)
   (let* ((meta-entry   (assoc-get 'meta grob-entry))
          (class        (assoc-get 'class meta-entry))
          (ifaces-entry (assoc-get 'interfaces meta-entry)))
     ;; change ly:grob-properties? to list? to work from 2.19.12 back to at least 2.18.2
     (set-object-property! grob-name 'translation-type? ly:grob-properties?)
     (set-object-property! grob-name 'is-grob? #t)
     (set! ifaces-entry (append (case class
                                  ((Item) '(item-interface))
                                  ((Spanner) '(spanner-interface))
                                  ((Paper_column) '((item-interface
                                                     paper-column-interface)))
                                  ((System) '((system-interface
                                               spanner-interface)))
                                  (else '(unknown-interface)))
                          ifaces-entry))
     (set! ifaces-entry (uniq-list (sort ifaces-entry symbol<?)))
     (set! ifaces-entry (cons 'grob-interface ifaces-entry))
     (set! meta-entry (assoc-set! meta-entry 'name grob-name))
     (set! meta-entry (assoc-set! meta-entry 'interfaces
                        ifaces-entry))
     (set! grob-entry (assoc-set! grob-entry 'meta meta-entry))
     (set! all-grob-descriptions
           (cons (cons grob-name grob-entry)
             all-grob-descriptions))))

#(define (define-grob-property symbol type? description)
   (if (not (equal? (object-property symbol 'backend-doc) #f))
       (ly:error (_ "symbol ~S redefined") symbol))

   (set-object-property! symbol 'backend-type? type?)
   (set-object-property! symbol 'backend-doc description)
   symbol)

#(map
  (lambda (x)
    (apply define-grob-property x))

  `(
     (fill-color ,color? "Background color for filling the rectangle")
     (acknowledge-finger-interface ,boolean? "Include fingerings in box?")
     (acknowledge-script-interface ,boolean? "Include scripts in box?")
     (zigzag-left  ,number? "Zigzag size for left edge")
     (zigzag-right ,number? "Zigzag size for right edge")
     ; add more properties here
     ))

#(define (makeDeltaSpan
          y-l-lower y-l-upper         ; number: Y-dimensions (left edge)
          y-r-lower y-r-upper         ; number: Y-dimensions (left edge)
          frame-color fill-color      ; (color of ##f): colors for outer and inner polygon (won't be drawn if set to ##f)
          stepLeft stepRight          ; number: size of zigzag elements for left and right edge (vertical edge / no zigzag if set to zero)
          open-on-bottom open-on-top  ; boolean: no visible frame on bottom/top edge (no distance between inner and outer polygon's edges)
          thick                       ; number: frame thickness - distance between inner and outer polygon's edges
          pad                         ; number: broken-bound-padding - amount to shorten spanners where separated by a line break
          X-ext-param                 ; pair: the spanner's X-dimensions
          open-on-left open-on-right  ; boolean: no visible frame on left/right edge (no distance between inner and outer polygon's edges)
          ;   We'll assume that this indicates a line break!
          radius                      ; number: radius for "round-filled-polygon" procedure
          )

   (let* (
           (h-thick (* thick (sqrt 2)))  ; X-distance between left and right edges of inner and outer polygon. Must be "thick" * sqrt 2  (Pythagoras)
           (l-width (* stepLeft  0.5))   ; X-distance of zigzag corners
           (r-width (* stepRight 0.5))
           (Y-ext (cons 0 0))            ; dummy, needed for ly:stencil-expr  (is there a way without it?)
           (X-ext (cons
                   (if (> stepLeft 0)    ; left edge has zigzag shape
                       (- (+ (car X-ext-param) (/ l-width 2)) h-thick)  ; Half of the zigzag space will be taken from inside, other half from the outside. Frame space taken from outside.
                       (if open-on-left  (- (car X-ext-param) h-thick) (- (car X-ext-param) thick))
                       )
                   (if (> stepRight 0)   ; right edge has zigzag shape
                       (+ (- (cdr X-ext-param) (/ r-width 2)) h-thick)
                       (if open-on-right (+ (cdr X-ext-param) h-thick) (+ (cdr X-ext-param) thick))
                       )))
           (X-ext (cons
                   (if open-on-left  (- (+ (car X-ext) pad) (/ l-width 2)) (car X-ext))     ; shorten/lengthen by broken-bound-padding if spanner is broken
                   (if open-on-right (+ (- (cdr X-ext) pad) (/ r-width 2)) (cdr X-ext))))
           (points (list))       ; will contain coordinates for outer polygon
           (points-i (list))     ; will contain coordinates for inner polygon
           (slope-upper (/ (- y-r-upper y-l-upper) (- (cdr X-ext) (car X-ext))))  ; slope of the polygon's upper edge
           (slope-lower (/ (- y-r-lower y-l-lower) (- (cdr X-ext) (car X-ext))))  ; slope of the polygon's lower edge
           (d-upper (if open-on-top    0  (* thick (sqrt (+ (expt slope-upper 2) 1)))))  ; (Pythagoras)
           ; Y-distance between upper edges of inner and outer polygon. Equal to "thick" if upper edge is horizontal.
           ; Increases as the upper edge's slope increases.
           (d-lower (if open-on-bottom 0  (* thick (sqrt (+ (expt slope-lower 2) 1)))))  ; same for lower edge
           ; stuff for later calculations:
           (xtemp 0)
           (yLowerLimit 0)
           (yUpperLimit 0)
           (xp 0)
           (yp 0)
           (jumps 0)
           )

     ; calculate outer polygon's borders:

     ; lower-left corner:
     (set! points (list (cons (car X-ext) y-l-lower)))

     ; calculate coordinates for left (outer) zigzag border:
     (if (and (> stepLeft 0) (not open-on-left))
         (let loop ((cnt y-l-lower))
           (if (< cnt y-l-upper)
               (begin
                (if (and (< cnt y-l-upper) (> cnt y-l-lower))  ; only add to list if point is inside the given Y-range
                    (set! points (cons (cons    (car X-ext)             cnt                 ) points)))
                (if (and (< (+ cnt (/ stepLeft 2)) y-l-upper) (> (+ cnt (/ stepLeft 2)) y-l-lower))
                    (set! points (cons (cons (- (car X-ext) l-width) (+ cnt (/ stepLeft 2)) ) points)))
                (loop (+ cnt stepLeft))))))

     ; upper-left corner:
     (set! points (cons
                   (cons (car X-ext) y-l-upper)
                   points ))
     ; upper-right corner:
     (set! points (cons
                   (cons (cdr X-ext) y-r-upper)
                   points ))
     ; right outer zigzag border:
     (if (and (> stepRight 0) (not open-on-right))
         (let loop ((cnt y-r-upper))
           (if (> cnt y-r-lower)
               (begin
                (if (and (< cnt y-r-upper) (> cnt y-r-lower))
                    (set! points (cons (cons    (cdr X-ext)             cnt                  ) points)))
                (if (and (< (- cnt (/ stepRight 2)) y-r-upper) (> (- cnt (/ stepRight 2)) y-r-lower))
                    (set! points (cons (cons (+ (cdr X-ext) r-width) (- cnt (/ stepRight 2)) ) points)))
                (loop (- cnt stepRight))))))

     ; lower-right corner:
     (set! points (cons
                   (cons (cdr X-ext) y-r-lower)
                   points ))

     ; shrink X-ext for use with inner stuff:
     (if (not open-on-left)
         (if (> stepLeft 0)
             (set! X-ext (cons (+ (car X-ext) h-thick) (cdr X-ext)))
             (set! X-ext (cons (+ (car X-ext)   thick) (cdr X-ext)))
             )
         )
     (if (not open-on-right)
         (if (> stepRight 0)
             (set! X-ext (cons (car X-ext) (- (cdr X-ext) h-thick)))
             (set! X-ext (cons (car X-ext) (- (cdr X-ext)   thick)))
             )
         ) ; Now X-ext represents INNER polygon's width WITHOUT the zigzag corners

     ; Now calculate inner borders:
     ; xp and yp will be the coordinates of the corner currently being calculated

     ; calculate lower-left corner:

     (set! yLowerLimit y-l-lower)
     (set! yUpperLimit y-l-upper)

     (if open-on-left
         (begin
          (set! xp (car X-ext))
          (set! yp (+ y-l-lower d-lower))
          )
         (if (> stepLeft 0)
             (if (not (eq? slope-lower -1))
                 (begin
                  (set! jumps 0)
                  (while (> (- (+ (* slope-lower h-thick) d-lower) (* jumps stepLeft)) stepLeft)
                    (set! jumps (+ 1 jumps)))
                  (set! xtemp (/ (- (+ h-thick (* jumps stepLeft)) d-lower) (+ slope-lower 1)))
                  ; results from the solution for a system of two equations. Forgive me, I'm a maths teacher :-)
                  (if (< xtemp (- h-thick (/ stepLeft 2)))
                      (if (= 1 slope-lower)
                          (set! xtemp h-thick)
                          (set! xtemp
                                (/ (+ (- d-lower (* stepLeft (+ 1 jumps))) h-thick) (- 1 slope-lower)))))  ; another system of 2 equations...
                  (set! xp (+ (- (car X-ext) h-thick) xtemp))
                  (set! yp (+ (+ y-l-lower (* slope-lower xtemp)) d-lower))
                  )
                 )
             (begin
              (set! xp (car X-ext))
              (set! yp (+ (+ y-l-lower (* thick slope-lower)) d-lower))
              )
             )
         )

     ; insert lower-left corner's coordinates into list:
     (if (not (and (and (not open-on-left) (> stepLeft 0)) (eq? slope-lower -1)))
         (begin
          (set! points-i (cons (cons xp yp) points-i))
          (set! yLowerLimit yp)
          )
         )

     ; calculate upper-left corner:
     (if open-on-left
         (begin
          (set! xp (car X-ext))
          (set! yp (- y-l-upper d-upper))
          )
         (if (> stepLeft 0)
             (if (not (eq? slope-upper 1))
                 (begin
                  (set! jumps 0)
                  (while (<
                          (+ (- (* slope-upper h-thick) d-upper) (* jumps stepLeft))
                          (- stepLeft))
                    (set! jumps (+ jumps 1)))
                  (set! xtemp (/ (- d-upper (+ h-thick (* jumps stepLeft))) (- slope-upper 1)))
                  (if (< xtemp (- h-thick (/ stepLeft 2)))
                      (if (= -1 slope-upper)
                          (set! xtemp h-thick)
                          (set! xtemp
                                (/ (- (- (* stepLeft (+ 1 jumps)) d-upper) h-thick) (- (- 1) slope-upper)))
                          )
                      )
                  (set! xp (+ (- (car X-ext) h-thick) xtemp))
                  (set! yp (- (+ y-l-upper (* slope-upper xtemp)) d-upper))
                  )
                 )
             (begin
              (set! xp (car X-ext))
              (set! yp (- (+ y-l-upper (* thick slope-upper)) d-upper))
              )
             )
         )

     (if (not
          (and (and (not open-on-left) (> stepLeft 0)) (eq? slope-upper 1))
          )
         (set! yUpperLimit yp))


     ; left (inner) zigzag:
     (if (and (> stepLeft 0) (not open-on-left))
         (begin
          (let loop ((cnt y-l-lower))
            (if (< cnt y-l-upper)
                (begin
                 (if (and (> cnt yLowerLimit) (< cnt yUpperLimit))
                     (set! points-i (cons (cons    (car X-ext)             cnt                 ) points-i))
                     )
                 (if (and (> (+ cnt (/ stepLeft 2)) yLowerLimit) (< (+ cnt (/ stepLeft 2)) yUpperLimit))
                     (set! points-i (cons (cons (- (car X-ext) l-width) (+ cnt (/ stepLeft 2)) ) points-i))
                     )
                 (loop (+ cnt stepLeft))
                 )
                )
            )
          )
         )

     ; insert upper-left corner (yes, AFTER the zigzag points, so all the points will be given in clockwise order):
     (if (not
          (and (and (not open-on-left) (> stepLeft 0)) (eq? slope-upper 1))
          )
         (set! points-i (cons (cons xp yp) points-i)))

     ; calculate upper-right corner:

     (set! yLowerLimit y-r-lower)
     (set! yUpperLimit y-r-upper)

     (if open-on-right
         (begin
          (set! xp (cdr X-ext))
          (set! yp (- y-r-upper d-upper))
          )
         (if (> stepRight 0)
             (if (not (eq? slope-upper -1))
                 (begin
                  (set! jumps 0)
                  (while (<
                          (+ (- (* slope-upper (- h-thick)) d-upper) (* jumps stepRight))
                          (- stepRight))
                    (set! jumps (+ jumps 1)))
                  (set! xtemp (/ (- d-upper (+ h-thick (* jumps stepRight))) (+ slope-upper 1)))
                  (if (> xtemp (- (/ stepRight 2) h-thick  ))
                      (if (= 1 slope-upper)
                          (set! xtemp (- h-thick))
                          (set! xtemp
                                (/ (- (- (* stepRight (+ 1 jumps)) d-upper) h-thick) (- 1 slope-upper)))
                          )
                      )
                  (set! xp (+ (+ (cdr X-ext) h-thick) xtemp))
                  (set! yp (- (+ y-r-upper (* slope-upper xtemp)) d-upper))
                  )
                 )
             (begin
              (set! xp (cdr X-ext))
              (set! yp (- (- y-r-upper (* thick slope-upper)) d-upper))
              )
             )
         )

     ; insert upper-right corner:
     (if (not
          (and (and (not open-on-right) (> stepRight 0)) (eq? slope-upper -1)))
         (begin
          (set! points-i (cons (cons xp yp) points-i))
          (set! yUpperLimit yp)))

     ; calculate lower-right corner:
     (if open-on-right
         (begin
          (set! xp (cdr X-ext))
          (set! yp (+ y-r-lower d-lower))
          )
         (if (> stepRight 0)
             (if (not (eq? slope-lower 1))
                 (begin
                  (set! jumps 0)
                  (while (> (- (- d-lower (* slope-lower h-thick)) (* jumps stepRight)) stepRight)
                    (set! jumps (+ 1 jumps)))
                  (set! xtemp (/ (- (+ h-thick (* jumps stepRight)) d-lower) (- slope-lower 1)))
                  (if (> xtemp (- (/ stepRight 2) h-thick)   )
                      (if (= -1 slope-lower)
                          (set! xtemp (- h-thick))
                          (set! xtemp
                                (/ (+ (- d-lower (* stepRight (+ 1 jumps))) h-thick) (- -1 slope-lower)))))
                  (set! xp (+ (+ (cdr X-ext) h-thick) xtemp))
                  (set! yp (+ (+ y-r-lower (* slope-lower xtemp)) d-lower))
                  )
                 )
             (begin
              (set! xp (cdr X-ext))
              (set! yp (+ (- y-r-lower (* thick slope-lower)) d-lower))
              )
             )
         )

     (if (not (and (and (not open-on-right) (> stepRight 0)) (eq? slope-lower 1)))
         (set! yLowerLimit yp))

     ; right zigzag:
     (if (and (> stepRight 0) (not open-on-right))
         (begin
          (let loop ((cnt y-r-upper))
            (if (> cnt y-r-lower)
                (begin
                 (if (and (> cnt yLowerLimit) (< cnt yUpperLimit))
                     (set! points-i (cons (cons    (cdr X-ext)             cnt                  ) points-i)))
                 (if (and (> (- cnt (/ stepRight 2)) yLowerLimit) (< (- cnt (/ stepRight 2)) yUpperLimit))
                     (set! points-i (cons (cons (+ (cdr X-ext) r-width) (- cnt (/ stepRight 2)) ) points-i)))
                 (loop (- cnt stepRight))
                 )
                )
            )
          )
         )

     ; insert lower-right corner:
     (if (not (and (and (not open-on-right) (> stepRight 0)) (eq? slope-lower 1)))
         (set! points-i (cons (cons xp yp) points-i)))

     (ly:stencil-add
      ; draw outer polygon:
      (if (color? frame-color)  ; only add stencil if set to a valid color (could also be set to ##f)
          (ly:make-stencil (list 'color frame-color
                             (ly:stencil-expr (ly:round-filled-polygon points radius))
                             X-ext Y-ext))
          empty-stencil)
      ; draw inner polygon:
      (if (color? fill-color)   ; only add stencil if set to a valid color (could also be set to ##f)
          (ly:make-stencil (list 'color fill-color
                             (ly:stencil-expr (ly:round-filled-polygon points-i radius))
                             X-ext Y-ext))
          empty-stencil)
      )
     )
   )

#(define (music-boxer-stencil grob)
   (let* ((elts (ly:grob-object grob 'elements))
          (refp-X (ly:grob-common-refpoint-of-array grob elts X))
          (X-ext (ly:relative-group-extent elts refp-X X))
          (refp-Y (ly:grob-common-refpoint-of-array grob elts Y))
          (Y-ext (ly:relative-group-extent elts refp-Y Y))
          (padding (ly:grob-property grob 'padding 0.3))
          (slope (ly:grob-property grob 'slope 0))             ; Y-difference between left and right edge (artificially applied)
          (extra-dy (ly:grob-property grob 'extra-dy 0))       ; additional box height
          (bb-padding (ly:grob-property grob 'broken-bound-padding -6))
          (thick (ly:grob-property grob 'thickness 0.1))
          (X-ext (interval-widen X-ext padding))               ; already applied here because makeDeltaSpan has no padding parameter
          (Y-ext (interval-widen Y-ext padding))               ; dto.
          (Y-ext (interval-widen Y-ext thick))                 ; because makeDeltaSpan will take the Y-space for frame thickness from inside
          (Y-ext (interval-widen Y-ext (/ extra-dy 2)))
          (frame-color (ly:grob-property grob 'color black))
          (fill-color (ly:grob-property grob 'fill-color white))
          (offset (ly:grob-relative-coordinate grob refp-X X))
          (stepLeft  (ly:grob-property grob 'zigzag-left  0))  ; zigzag size for left  edge (only used as approximate value )
          (stepRight (ly:grob-property grob 'zigzag-right 0))  ; dto., right edge
          (open-on-left
           (and (ly:spanner? grob)
                (= 1 (ly:item-break-dir (ly:spanner-bound grob LEFT)))))
          (open-on-right
           (and (ly:spanner? grob)
                (= -1 (ly:item-break-dir (ly:spanner-bound grob RIGHT)))))

          (y-l-lower (- (car Y-ext) (/ slope 2)))
          (y-l-upper (- (cdr Y-ext) (/ slope 2)))
          (y-r-lower (+ (car Y-ext) (/ slope 2)))
          (y-r-upper (+ (cdr Y-ext) (/ slope 2)))
          (cnt 0)  ; counter, will be used later...
          (stil empty-stencil))
     (if (not (= stepLeft 0))
         (begin   ; calculate exact size for only entire zigzag squiggles should be used
           (set! cnt (round (/ (- y-l-upper y-l-lower) stepLeft)))
           (if (> cnt 0)
               (set! stepLeft (/ (- y-l-upper y-l-lower) cnt))
               (set! stepLeft 0))))
     (if (not (= stepRight 0))
         (begin
          (set! cnt (round (/ (- y-r-upper y-r-lower) stepRight)))
          (if (> cnt 0)
              (set! stepRight (/ (- y-r-upper y-r-lower) cnt))
              (set! stepRight 0))))
     (set! stil
           (makeDeltaSpan
            y-l-lower y-l-upper
            y-r-lower y-r-upper
            frame-color fill-color
            stepLeft stepRight
            #f #f                     ; open-on-bottom open-on-top
            thick bb-padding X-ext open-on-left open-on-right
            0                         ; radius
            )
           )
     (ly:stencil-translate-axis stil (- offset) X)
     )
   )

%#(define box-stil music-boxer-stencil)

%% Test callback for Box.stencil
#(define (box-stil grob)
   (let* ((elts (ly:grob-object grob 'elements))
          (refp-X (ly:grob-common-refpoint-of-array grob elts X))
          (X-ext (ly:relative-group-extent elts refp-X X))
          (refp-Y (ly:grob-common-refpoint-of-array grob elts Y))

          ; following line triggers vertical spacing too early
          ;(Y-ext (ly:relative-group-extent elts refp-Y Y))
          (Y-ext '(-3 . 3))
          (padding (ly:grob-property grob 'padding 0.3))
          (slope (ly:grob-property grob 'slope 0))             ; Y-difference between left and right edge (artificially applied)
          (extra-dy (ly:grob-property grob 'extra-dy 0))       ; additional box height
          (bb-padding (ly:grob-property grob 'broken-bound-padding -6))
          (thick (ly:grob-property grob 'thickness 0.1))
          (X-ext (interval-widen X-ext padding))               ; already applied here because makeDeltaSpan has no padding parameter
          (Y-ext (interval-widen Y-ext padding))               ; dto.
          (Y-ext (interval-widen Y-ext thick))                 ; because makeDeltaSpan will take the Y-space for frame thickness from inside
          (Y-ext (interval-widen Y-ext (/ extra-dy 2)))
          (frame-color (ly:grob-property grob 'color black))
          (fill-color (ly:grob-property grob 'fill-color white))
          (offset (ly:grob-relative-coordinate grob refp-X X))
          (stepLeft  (ly:grob-property grob 'zigzag-left  0))  ; zigzag size for left  edge (only used as approximate value )
          (stepRight (ly:grob-property grob 'zigzag-right 0))  ; dto., right edge
          (open-on-left
           (and (ly:spanner? grob)
                (= 1 (ly:item-break-dir (ly:spanner-bound grob LEFT)))))
          (open-on-right
           (and (ly:spanner? grob)
                (= -1 (ly:item-break-dir (ly:spanner-bound grob RIGHT)))))

          (y-l-lower (- (car Y-ext) (/ slope 2)))
          (y-l-upper (- (cdr Y-ext) (/ slope 2)))
          (y-r-lower (+ (car Y-ext) (/ slope 2)))
          (y-r-upper (+ (cdr Y-ext) (/ slope 2)))
          (cnt 0)  ; counter, will be used later...
          (stil empty-stencil))
     (if (not (= stepLeft 0))
         (begin   ; calculate exact size for only entire zigzag squiggles should be used
           (set! cnt (round (/ (- y-l-upper y-l-lower) stepLeft)))
           (if (> cnt 0)
               (set! stepLeft (/ (- y-l-upper y-l-lower) cnt))
               (set! stepLeft 0))))
     (if (not (= stepRight 0))
         (begin
          (set! cnt (round (/ (- y-r-upper y-r-lower) stepRight)))
          (if (> cnt 0)
              (set! stepRight (/ (- y-r-upper y-r-lower) cnt))
              (set! stepRight 0))))
     (set! stil
           (makeDeltaSpan
            y-l-lower y-l-upper
            y-r-lower y-r-upper
            frame-color fill-color
            stepLeft stepRight
            #f #f                     ; open-on-bottom open-on-top
            thick bb-padding X-ext open-on-left open-on-right
            0                         ; radius
            )
           )
     (ly:stencil-translate-axis stil (- offset) X)
     )
   )

#(add-grob-definition
  'Box
  `(
     (direction . ,UP)
     (outside-staff-priority . 251) ; just larger than DynamicText
     (stencil . ,box-stil)
     (meta . ((class . Item)
              (interfaces . (outside-staff-interface))))))

#(add-grob-definition
  'MusicBoxer
  `(
     (direction . ,UP)
     (outside-staff-priority . 251) ; just larger than DynamicText
     (stencil . ,music-boxer-stencil)
     (meta . ((class . Spanner)
              (interfaces . (outside-staff-interface))))))


#(define box-types
   '(
      (BoxEvent
       . ((description . "A box encompassing music at a single timestep.")
          (types . (general-music box-event music-event event))
          ))
      ))

#(define music-boxer-types
   '(
      (MusicBoxerEvent
       . ((description . "Used to signal where boxes encompassing music start and stop.")
          (types . (general-music music-boxer-event span-event event))
          ))
      ))


#(set!
  music-boxer-types
  (map (lambda (x)
         (set-object-property! (car x)
           'music-description
           (cdr (assq 'description (cdr x))))
         (let ((lst (cdr x)))
           (set! lst (assoc-set! lst 'name (car x)))
           (set! lst (assq-remove! lst 'description))
           (hashq-set! music-name-to-property-table (car x) lst)
           (cons (car x) lst)))
    music-boxer-types))

#(set!
  box-types
  (map (lambda (x)
         (set-object-property! (car x)
           'music-description
           (cdr (assq 'description (cdr x))))
         (let ((lst (cdr x)))
           (set! lst (assoc-set! lst 'name (car x)))
           (set! lst (assq-remove! lst 'description))
           (hashq-set! music-name-to-property-table (car x) lst)
           (cons (car x) lst)))
    box-types))

#(set! music-descriptions
       (append music-boxer-types music-descriptions))

#(set! music-descriptions
       (append box-types music-descriptions))

#(set! music-descriptions
       (sort music-descriptions alist<?))


#(define (add-bound-item spanner item)
   (if (null? (ly:spanner-bound spanner LEFT))
       (ly:spanner-set-bound! spanner LEFT item)
       (ly:spanner-set-bound! spanner RIGHT item)))

musicBoxerEngraver =
#(lambda (context)
   (let ((span '())
         (finished '())
         (current-event '())
         (event-start '())
         (event-stop '())
         )

     `((listeners
        (music-boxer-event .
          ,(lambda (engraver event)
             (if (= START (ly:event-property event 'span-direction))
                 (set! event-start event)
                 (set! event-stop event)))))

       (acknowledgers
        (note-column-interface .
          ,(lambda (engraver grob source-engraver)
             (if (ly:spanner? span)
                 (begin
                  (ly:pointer-group-interface::add-grob span 'elements grob)
                  (add-bound-item span grob)))
             (if (ly:spanner? finished)
                 (begin
                  (ly:pointer-group-interface::add-grob finished 'elements grob)
                  (add-bound-item finished grob)))))

        (inline-accidental-interface .
          ,(lambda (engraver grob source-engraver)
             (if (ly:spanner? span)
                 (begin
                  (ly:pointer-group-interface::add-grob span 'elements grob)))
             (if (ly:spanner? finished)
                 (ly:pointer-group-interface::add-grob finished 'elements grob))))

        (dots-interface .
          ,(lambda (engraver grob source-engraver)
             (if (ly:spanner? span)
                 (begin
                  (ly:pointer-group-interface::add-grob span 'elements grob)))
             (if (ly:spanner? finished)
                 (ly:pointer-group-interface::add-grob finished 'elements grob))))

        (ledger-line-spanner-interface .
          ,(lambda (engraver grob source-engraver)
             (if (ly:spanner? span)
                 (begin
                  (ly:pointer-group-interface::add-grob span 'elements grob)))
             (if (ly:spanner? finished)
                 (ly:pointer-group-interface::add-grob finished 'elements grob))))

        (script-interface .
          ,(lambda (engraver grob source-engraver)
             (if (and (ly:spanner? span)
                      (eq? #t (ly:grob-property span 'acknowledge-script-interface)))
                 (begin
                  (ly:pointer-group-interface::add-grob span 'elements grob)))
             (if (and (ly:spanner? finished)
                      (eq? #t (ly:grob-property finished 'acknowledge-script-interface)))
                 (ly:pointer-group-interface::add-grob finished 'elements grob))))

        (finger-interface .
          ,(lambda (engraver grob source-engraver)
             (if (and (ly:spanner? span)
                      (eq? #t (ly:grob-property span 'acknowledge-finger-interface)))
                 (begin
                  (ly:pointer-group-interface::add-grob span 'elements grob)))
             (if (and (ly:spanner? finished)
                      (eq? #t (ly:grob-property finished 'acknowledge-finger-interface)))
                 (ly:pointer-group-interface::add-grob finished 'elements grob))))

        ;; add additional interfaces to acknowledge here

        )

       (process-music .
         ,(lambda (trans)
            (if (ly:stream-event? event-stop)
                (if (null? span)
                    (ly:warning "No start to this box.")
                    (begin
                     (set! finished span)
                     (ly:engraver-announce-end-grob trans finished event-start)
                     (set! span '())
                     (set! event-stop '()))))
            (if (ly:stream-event? event-start)
                (begin
                 (set! span (ly:engraver-make-grob trans 'MusicBoxer event-start))
                 (set! event-start '())))))

       (stop-translation-timestep .
         ,(lambda (trans)
            (if (and (ly:spanner? span)
                     (null? (ly:spanner-bound span LEFT)))
                (ly:spanner-set-bound! span LEFT
                  (ly:context-property context 'currentMusicalColumn)))
            (if (ly:spanner? finished)
                (begin
                 (if (null? (ly:spanner-bound finished RIGHT))
                     (ly:spanner-set-bound! finished RIGHT
                       (ly:context-property context 'currentMusicalColumn)))
                 (set! finished '())
                 (set! event-start '())
                 (set! event-stop '())))))

       (finalize
        (lambda (trans)
          (if (ly:spanner? finished)
              (begin
               (if (null? (ly:spanner-bound finished RIGHT))
                   (set! (ly:spanner-bound finished RIGHT)
                         (ly:context-property context 'currentMusicalColumn)))
               (set! finished '())))
          (if (ly:spanner? span)
              (begin
               (ly:warning "unterminated box :-(")
               (ly:grob-suicide! span)
               (set! span '())))
          )))))


boxEngraver =
#(lambda (context)
   (let ((box '())
         (ev '()))

     `((listeners
        (box-event .
          ,(lambda (engraver event)
             (set! ev event))))

       (acknowledgers
        (note-column-interface .
          ,(lambda (engraver grob source-engraver)
             (if (ly:grob? box)
                 (begin
                  ; (set! (ly:grob-parent box X) grob) ;; ??
                  (set! (ly:grob-parent box Y) grob)
                  (ly:pointer-group-interface::add-grob box 'elements grob)))))

        (inline-accidental-interface .
          ,(lambda (engraver grob source-engraver)
             (if (ly:item? box)
                 (ly:pointer-group-interface::add-grob box 'elements grob))))

        (dots-interface .
          ,(lambda (engraver grob source-engraver)
             (if (ly:item? box)
                 (ly:pointer-group-interface::add-grob box 'elements grob))))

        (ledger-line-spanner-interface .
          ,(lambda (engraver grob source-engraver)
             (if (ly:item? box)
                 (ly:pointer-group-interface::add-grob box 'elements grob))))

        (script-interface .
          ,(lambda (engraver grob source-engraver)
             (if (and (ly:item? box) (eq? #t (ly:grob-property box 'acknowledge-script-interface)))
                 (ly:pointer-group-interface::add-grob box 'elements grob))))

        (finger-interface .
          ,(lambda (engraver grob source-engraver)
             (if (and (ly:item? box) (eq? #t (ly:grob-property box 'acknowledge-finger-interface)))
                 (ly:pointer-group-interface::add-grob box 'elements grob))))

        ;; add additional interfaces to acknowledge here

        )

       (process-music .
         ,(lambda (trans)
            (if (ly:stream-event? ev)
                (begin
                 (set! box (ly:engraver-make-grob trans 'Box ev))
                 (set! ev '())))))
       (stop-translation-timestep .
         ,(lambda (trans)
            (set! box '()))))))

musicBoxerStart =
#(make-span-event 'MusicBoxerEvent START)

musicBoxerEnd =
#(make-span-event 'MusicBoxerEvent STOP)

box = #(make-music 'BoxEvent)

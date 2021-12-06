(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define multiples-of-three
  ;YOUR-CODE-HERE
  (cons-stream 3 (map-stream (lambda (x) (+ x 3)) multiples-of-three))
)

(define (rle s)
  ;YOUR-CODE-HERE
  (define (help value num)
    (if (equal? value (car s))
        (help value (+ num 1)
        (help (car (cdr-stream s)) 0)
)
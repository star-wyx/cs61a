;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  ;'YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s)
  ;'YOUR-CODE-HERE
  (car (cdr (cdr s)))
)

(define (unique s)
  ;'YOUR-CODE-HERE
  (if (null? s)
    nil
    (cons (car s) (unique (filter (lambda (x) (not (equal? x (car s)))) (cdr s)))))
)

(define (cons-all first rests)
  (if (null? rests)
    nil
    (cons (append (list first) (car rests)) (cons-all first (cdr rests))))
)

;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  ;'YOUR-CODE-HERE
(define (helper n xs)
    (if (null? xs)
      nil
      (if (= 0 n)
        '(nil)
        (if (< n (car xs))
          (helper n (cdr xs))
          (append
            (cons-all (car xs) (helper (- n (car xs)) denoms))
            (list-change n (cdr xs)))))))
  (helper total denoms))


; Tail recursion

(define (replicate x n)
  ;'YOUR-CODE-HERE
   (define (helper time total)
    (if (= 0 time)
        total
        (helper (- time 1) (append (list x) total))))
    (helper n ())
  )

(define (accumulate combiner start n term)
  ;'YOUR-CODE-HERE
  (define (help total i)
    (if (= i n)
        (combiner total (term i))
        (help (combiner total (term i)) (+ i 1))))
  (help start 1)
)

(define (accumulate-tail combiner start n term)
  ;'YOUR-CODE-HERE
  (define (help total i)
    (if (= i n)
        (combiner total (term i))
        (help (combiner total (term i)) (+ i 1))))
  (help start 1)
)


; Macros

(define-macro (list-of map-expr for var in lst if filter-expr)
  ;'YOUR-CODE-HERE
  (list 'map (list 'lambda (list var) map-expr) (list 'filter (list 'lambda (list var) filter-expr) lst))
  ;`(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) ,lst))
)
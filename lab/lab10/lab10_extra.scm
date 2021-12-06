;; Scheme ;;

;;lab10.scm & lab10_scm could run together


(define lst
  ;YOUR-CODE-HERE
  (list (list 1) 2 (list 3 4) 5)
)

(define (composed f g)
  ;YOUR-CODE-HERE
  (lambda (x) (f (g x)))
)

(define (remove item lst)
  ;YOUR-CODE-HERE

  (define (f x)
    (if (equal? item x)
        #f
        #t
        )
  )

  (filter-lst f lst)
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

(define (no-repeats s)
  ;YOUR-CODE-HERE
  (if (equal? s nil)
    nil
    (cons (car s) (no-repeats (remove (car s) (cdr s)))))

)

(define (substitute s old new)
  ;YOUR-CODE-HERE
    (if (null? s)
        nil
        (cons
            (if (not (pair? (car s)))
                (if (equal? (car s) old)
                    new
                    (car s))
                (substitute (car s) old new)
            )
            (substitute (cdr s) old new)))
)


(define (sub-all s olds news)
  ;YOUR-CODE-HERE
  (define (zip xs ys)
    (if (or (null? xs) (null? ys))
        nil
        (cons (list (car xs) (car ys)) (zip (cdr xs) (cdr ys)))))

  ((reduce composed (map (lambda (x-y) (lambda (s) (substitute s (car x-y) (car (cdr x-y))))) (zip olds news))) s)
)
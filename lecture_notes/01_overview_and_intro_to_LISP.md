### Some wild build up to 'What is it that programmers are doing?'

- It is intended to help us learn how to think

. . . .


. . . .


Some time passes, I pick up notes around 0:35:00

### A General Framework (for learning a computer language)

- What are the primitive elements?

- What are the means of combination?

>>>> What are the ways of putting things together?

- What are the means of abstraction?

>>>> How do we take those primitive things and
     build something complicated with them?


_Some primitive data in LISP..._

```clojure
3
```

The number 3.

However, if we're being very pedantic, it's not even the number Three itself, it's some Platonic idea of 'what Three means'.

Still, it's a 3.

```clojure
17.4
```

Some representation of 'Seventeen Point Four'

```clojure
5
```

```clojure
+
```

A name for the primitive method of adding things.

A name for Plato's concept of how you add things.

#### What is the sum of these numbers?

```clojure
( + 3 17.4 5 ) ;; -> 25.4
```

This is called a **Combination**.

A Combination consists, in general, of applying an operator to some opperands.

```clojure
( + 3 17.4 5 )
  ^ ^-^----^
   \     \_____
    operator   \
                operands
\_____________/
  combination
```
> Note: I'm using `clojure` for code highlighting.. (it's a lisp after all)


From these principles, we have enough to form more complex combinations.

The reason that we can get this complexity, is because the operands themselves can be combinations.

```clojure
( + 3 ( * 5 6 ) 8 2 ) ;; -> 43
```

#### Little bit on Syntax

LISP uses **prefix** notation, meaning the operator is written to the left of the operands. It is also _fully parenthesized_, and the parenthesis are there to make expressions written in the language less ambiguous.

In mathematics, parentheses are often used to mean grouping, and it's okay to sometimes leave them out, however in Lisp, you cannot leave out parenthesis, and you can not arbitrarily add them.

Putting in parenthesis always means precisely "this is an operation." (eg. apply an operator to operands).

Really, we're writing trees.

```clojure
;; it's hard to make ascii trees.

        +       ;; operator
       / \
      /   \
     /     \
    1       *
   / \     / \
  0   +   9   +
 /   / \     / \
2   1   7   8   8

```


>>> Really whats going on are we're writing trees, and parentheses are just a way to write a two-dimensionally structure as a linear character string.

### Let's ASK LISP !!

```clojure
(+ 3 4 8)
;; 15
```

HOLY SHIT!

```clojure
(+ (* 3 (+ 7 13.5)) 4)
;; 54.5
```

my god.

```clojure
;; indentation, "pretty printing"

(+ (* 3 5)
   (* 47
      (- 20 6.8))
   12)
;; 647.4 (or something)
```

Wow. Well, those are the primitives, eg. the Means of Combination. Let's move on to...

### The Means of **Abstraction**

We use `DEFINE`,

```clojure
(DEFINE A (+ 5 5))

(+ A A) ;; -> 625

(DEFINE B (+ A (* 5 A)))
B ;; -> 150

(* A (/ B 5)) ;; -> 55
```

Let's say we want to name the general term for, 'multiplying a number by itself' -- how would this be written?

```clojure
(DEFINE (square x)
  (* x x))

;; use it in a sentence..

    TO   SQUARE SOMETHING
(DEFINE (square x)
  (* x x))
   ^ ^ ^
MULT IT BY ITSELF
```

sort of yes!

> A notation for defining a procedure

However, it's still kind of confusing. It's not totally clear that you're _naming something_.

```clojure
(DEFINE SQUARE (LAMBDA (x) (* x x)))
```

Here, we're clearly naming something `SQUARE`.
- `Lambda` is Lisp's way of saying 'make a procedure'

In general, we'll be using the more concise, first form. However try to keep in mind that to the Lisp interpreter, there is no difference between the two, and in fact, what we're asking semantically is closer to the second form.

```clojure
(define square
  (lambda (x) (* x x) ))
    ;; MAKE A PROCEDURE
          ;; WITH THE ARGUMENT 'X'
              ;; THAT RETURNS THE RESULT OF MULTIPLYING X BY X
```

In this 1986 lecture, the author defines this ability
for an interpreter to accept either form, with one
being more human-readable as... (drum roll)

### Syntactic Sugar

"Having somewhat more convenient surface forms for typing something"

https://en.wikibooks.org/wiki/Write_Yourself_a_Scheme_in_48_Hours


Answer to finding square-roots-by-guessing
https://github.com/ivanjovanovic/sicp/blob/master/1.1/e-1.8.scm



The Little Schemer
http://www.ccs.neu.edu/home/matthias/BTLS

Tracing procedures
http://www.scheme.com/csug7/debug.html


https://obsproject.com

https://en.wikipedia.org/wiki/Halting_problem


http://mathworld.wolfram.com/PeanosAxioms.html
http://mathworld.wolfram.com/PeanoArithmetic.html


### `If` statements

Have the signature...

```
(if <predicate> <consequent> <alternative>)
```


> A formal parameter of a procedure has a very special role in the procedure definition, in that it doesn't matter what name the formal parameter has. Such a name is called a bound variable, and we say that the procedure definition binds its formal parameters. The meaning of a procedure definition is unchanged if a bound variable is consistently renamed throughout the definition.26 If a variable is not bound, we say that it is free. The set of expressions for which a binding defines a name is called the scope of that name. In a procedure definition, the bound variables declared as the formal parameters of the procedure have the body of the procedure as their scope.



### Ackermann Function

http://mathworld.wolfram.com/AckermannFunction.html

https://en.wikipedia.org/wiki/Ackermann_function



#### Exercise 1.9

- [x] The second process is iterative
- [ ] The first process is iterative
- [ ] The second process is recursive
- [x] The first process is recursive


#### Exercise 1.10


Give a mathematical notation for different x values of Ackermann

```clojure
(define (f n) (A 0 n))          ; 2n
(define (g n) (A 1 n))          ; n²
(define (h n) (A 2 n))          ; 2↑↑n
(define (k n) (* 5 n n))        ; 5n²
```


Next Time: Tree Recursion!

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

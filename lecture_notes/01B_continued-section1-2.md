## Substitution Model, continued...

> Well, you've just seen a simple **perturbational analysis**

We looked at two very similar programs and showed how they _evolved_ processes.

### _More processes and the shapes they may have_ :: The Fibonacci Numbers

More stuff that you'll never want to actually write! (or, Author's Warning: Probably the worst way that many of these problems could be expressed).

We want to know: How a program represents itself.

For reference, fibonacci numbers are given int he first row, with their
cardinal index in the second:

```clojure
0 1 1 2 3 5 8 13 21 34 55

0 1 2 3 4 5 6 7  8  9  10
```

## Example, write a simple Fibonacci-calculating program

```clojure
(DEFINE (FIB N)
  (IF (< N 2)
      N
      (+ (FIB (- N 1))
         (FIB (- N 2)))))
```

This represents the recurrence relation in the simplest possible way.

Let's figure out what this does, by computing `(FIB 4)`:

```raw
                        +-------+
                +-------+ FIB 4 +-------+
                |       +-------+       |
                |                       |
                v                       ^
             +--+--+                 +--+--+
         +---+FIB 3+---+             |FIB 2|
         |   +-----+   |             ++---++
         |             |              |   |
         |             |              |   |
         v             v          +---+   +--+
      +--+--+       +--+--+       |          |
      |FIB 2|       |FIB 1|       v          |
      ++---++       +---+-+     +-+---+      v
      |   |            |        |FIB 1|   +--+--+
      |   |            ^        +--+--+   |FIB 0|
  +---+   +--+        +++          |      +--+--+
  |          |        |1|          v         |
  v          |        +-+         +++        v
+-+---+      v                    |1|       +++
|FIB 1|   +--+--+                 +-+       |0|
+--+--+   |FIB 0|                           +-+
   |      +--+--+
   v         |
  +++        v
  |1|       +++
  +-+       |0|
            +-+
```


Notice that if we were to computer (FIB 5), we would have compute (FIB 3) twice, (FIB 2) three times, etc.


##### What are the problems with this implementation?

For every (FIB N) where N is less than 2, we have to repeatedly compute
the same computational trees.

> This is a prescription for a process that is exponential in time.

The time complexity of this computation is `time = O(fib(n))`

It grows in fibonacci time! This is neat, but also _very bad_ as the number of trees also grows exponentially.

Note: `space` is also `O(n)`

---

#### How to fix?

It's true that this program is incredibly crude. In fact, it only consists of two "rules". One that states, _FIB of N is a sum, which consists of FIB(n-1) and FIB(n-2)_ **and** the base case, where FIB(n) = n.

The first rule breaks up nodes into two parts, if n is greater than 2.

> One reason that people think programming is hard, is that we must come up with _general rules_ that govern particular instances.

We have to think of all possible processes, and write rules which guide the program toward a desired outcome.

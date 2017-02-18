[1.2 - Elements Of Programming](http://composingprograms.com/pages/12-elements-of-programming.html)

### Anatomy of a Call Expression

```python
from operators import add

add( 2, 3 )

'''
add - the Operator
2,3 - the Operands
'''
```

`Operators` and `Operands` and **_Expressions_**, so they evalutate to **_Values_**.

#### The Evalutation Procedure

1. Evaluate the `Operator`, --then--, evaluate the `Operand(s)` subexpressio dn(s)
2. Apply the function that is the _value of the **operator** subexpression_ to the **arguments** that are the _values of the **operand** subexpression_

What about a more complicated example?

```python
from operators import mul, add

mul(add(2, mul(4, 6)), add(3, 5))
```

> #### _Apply the procedure for `evaluating` `call expressions`_

```python
'''
mul - is the Operator

BUT! the first Operand is also a call expression
'''

add(2, mul(4, 6))

'''
add - is the Operator
2 is the first Operand, but the second is ANOTHER call expression
'''

mul(4, 6)

'''
mul  - is the Operator
4, 6 - are the two Operands which are simply numbers which will return values!

We now have a value, 24
'''

add(2, 24)

'''
add is the Operator
2 and 24 are the Operands
returns 26

We can now plug this in to the original expression and continue evaluating
'''

mul(26, add(3, 5))

'''
mul is the Operator
26 is an Operand
add(3, 5) is an Operand which is ALSO another call expression...

I think you know what's next!
'''

add(3, 5)

'''
add is the Operator
3 and 5 are the Operands
returns 8
'''

mul(26, 8)

# >>> 208

# WooHOO!
```


#### This _whole process_ is called an `Expression Tree`

> It looks like a tree!
> But, it's just a diagram of the computational process


## Primitive Expressions

One example is `numbers` -- this are not _really_ numbers themselves, but
digits which represent numbers in base 10. _Real_ numbers are a Platonic thing
which is better fretted over in Philosophy classes.

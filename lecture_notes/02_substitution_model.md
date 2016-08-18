#### Procedures and Processes

>> Sussman in the HOUSE

And he starts with..

### Kinds of Expressions

things like...

- Numbers
- Symbols
- Lambda Expressions
- Definitions
- Conditionals
- Combinations

Many will evaluate to themselves.
Symbols will disappear.

So, we really just need to get at how _Combinations_ are defined.

```raw
        SUBSTITUTION RULE

To evaluate an application
  Evaluate the operator to get procedure
  Evaluate the operands to get arguments
  Apply the procedure to the arguments
    Copy the body of the procedure
      substituting the arguments supplied
      for the formal parameters of the
      procedure.
    Evaluate the resulting new body.

```



```

if (a if b else c):
    1
elif b or c and d:
    2
else:
    3



if            : keyword.control.flow.python, source.python
              : source.python
(             : punctuation.parenthesis.begin.python, source.python
a             : source.python
if            : keyword.operator.python, source.python
 b            : source.python
else          : keyword.operator.python, source.python
 c            : source.python
)             : punctuation.parenthesis.end.python, source.python
:             : source.python
              : source.python
1             : constant.numeric.dec.python, source.python
elif          : keyword.control.flow.python, source.python
 b            : source.python
or            : keyword.operator.python, source.python
 c            : source.python
and           : keyword.operator.python, source.python
 d:           : source.python
              : source.python
2             : constant.numeric.dec.python, source.python
else          : keyword.control.flow.python, source.python
:             : source.python
              : source.python
3             : constant.numeric.dec.python, source.python

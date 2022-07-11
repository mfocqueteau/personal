rule(0, 3, 11, 0).
rule(0, 4,  9, 0).
rule(1, 1, 19, 0).
rule(1, 2, 18, 4).
rule(2, 0, 0, 30).
rule(3, 0, 0, 19).
rule(4, 0, 0,  4).


writable(1..3, 3..4).
writable(2..4, 1..2).

:-
  rule(X, Y, N, Z),
  

1 { cell(X, Y, 1..9) } 1 :- writable(X, Y).

x(1, 2, 3).
x(4, 5, 6).
x(7, 8, 9).

y(A, B, C) :-
    A = #sum { (A1; B1) : x(A1, B1, _) }, 
    B = #sum { B1 : x(A1, B1, C1) },
    C = #sum { C1 : x(A1, B1, C1) }.
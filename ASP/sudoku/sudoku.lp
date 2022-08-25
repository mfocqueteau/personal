row(0..8).
col(0..8).

:-% No hay dos números iguales en la misma fila
  cell(X, Y1, N),
  cell(X, Y2, N),
  Y1 != Y2.

:-% No hay dos números iguales en la misma columna
  cell(X1, Y, N),
  cell(X2, Y, N),
  X1 != X2.

:-% No hay dos números iguales en la misma sección
  cell(X1, Y1, N),
  cell(X2, Y2, N),
  X1 / 3 == X2 / 3,
  Y1 / 3 == Y2 / 3,
  (X1, Y1) != (X2, Y2).

% Elegir un único número para cada celda
{ cell(X, Y, 1..9) } = 1 :-
  row(X),
  col(Y).

#show cell/3.

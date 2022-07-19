% No se repiten emparejamientos del año pasado
:- r(X, Y),
   y(X, Y).

% Nadie queda sin amigo secreto
{ r(X, Y): p(X) } = 1 :- p(Y).

% Una persona no regala a dos
:- r(X, Y),
   r(X, Z),
   Y != Z.

% % Nadie regala a sí misme
:- r(X, X).

#show r/2.


% Todo nodo puede llegar a si mismo
edge(X, X) :- node(X).

% Una arista es un camino directo
path(X, Y) :- edge(X, Y).

% Hay camino si existe camino que llega a estar una arista del objetivo
path(X, Y) :-
   path(X, Z),
   edge(Z, Y).


{ position(X, T): node(X) } = 1 :- step(T).

:- position(X, T),
   position(Y, T+1),
   step(T+1),
   not edge(X, Y).

1 { position(X, T): step(T) } :- goal(X).

#show position/2.

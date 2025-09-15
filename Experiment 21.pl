% --- Towers of Hanoi ---
% hanoi(N, Source, Target, Auxiliary)

hanoi(1, Source, Target, _) :-
    write('Move disk 1 from '), write(Source),
    write(' to '), write(Target), nl.

hanoi(N, Source, Target, Aux) :-
    N > 1,
    M is N - 1,
    hanoi(M, Source, Aux, Target),
    write('Move disk '), write(N),
    write(' from '), write(Source),
    write(' to '), write(Target), nl,
    hanoi(M, Aux, Target, Source).

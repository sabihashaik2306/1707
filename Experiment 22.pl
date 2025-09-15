% --- Knowledge Base of birds ---
bird(sparrow).
bird(pigeon).
bird(crow).
bird(ostrich).
bird(penguin).
bird(parrot).

% --- Rules about flying ---
can_fly(sparrow).
can_fly(pigeon).
can_fly(crow).
can_fly(parrot).

cannot_fly(ostrich).
cannot_fly(penguin).

% --- General rule to check if a bird can fly ---
flies(Bird) :-
    can_fly(Bird),
    write(Bird), write(' can fly'), nl.

flies(Bird) :-
    cannot_fly(Bird),
    write(Bird), write(' cannot fly'), nl.

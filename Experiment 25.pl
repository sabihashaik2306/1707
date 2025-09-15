% --- Monkey and Banana Problem ---
% The monkey wants to get the banana hanging from the ceiling.
% Initial state: monkey(at_door, on_floor, at_door, no_banana).
% Goal state:    monkey(_, on_box, at_banana, has_banana).

% Representation: monkey(MonkeyPosition, MonkeyStatus, BoxPosition, HasBanana)

% --- Actions ---
% 1. Monkey walks to another position
move(monkey(_, S, B, H), go(X), monkey(X, S, B, H)).

% 2. Monkey pushes box to another position
move(monkey(P, on_floor, P, H), push_box(X), monkey(X, on_floor, X, H)).

% 3. Monkey climbs on box
move(monkey(P, on_floor, P, H), climb, monkey(P, on_box, P, H)).

% 4. Monkey takes banana
move(monkey(P, on_box, P, no_banana), take_banana, monkey(P, on_box, P, has_banana)).

% --- Plan: sequence of moves to reach goal ---
plan(State, State, []).

plan(State1, Goal, [Move | RestMoves]) :-
    move(State1, Move, State2),
    plan(State2, Goal, RestMoves).

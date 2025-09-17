% --- Knowledge Base (Rules) ---
% rule(IfConditions, ThenFact)

rule([has_fever, has_cough], flu).
rule([has_fever, has_chills], malaria).
rule([has_runny_nose, has_sneezing], cold).
rule([has_fever, loss_of_taste], covid19).
rule([has_headache, has_fever], typhoid).

% --- Initial facts (dynamic so we can add new ones) ---
:- dynamic(fact/1).

% --- Forward Chaining Inference ---
forward_chain :-
    new_fact(F),
    \+ fact(F),          % if F not already known
    asserta(fact(F)),    % add it as new fact
    write('Derived: '), writeln(F),
    forward_chain.       % keep chaining
forward_chain :- !.      % stop when no new fact

% --- Check rules and derive new facts ---
new_fact(F) :-
    rule(Conditions, F),
    all_true(Conditions).

% --- Verify all conditions ---
all_true([]).
all_true([H|T]) :-
    fact(H),
    all_true(T).

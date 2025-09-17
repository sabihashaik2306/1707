% --- Knowledge Base (Rules) ---
% disease(Name) :- symptoms.

disease(flu) :-
    has(fever),
    has(cough),
    has(body_ache).

disease(cold) :-
    has(runny_nose),
    has(sneezing),
    has(sore_throat).

disease(malaria) :-
    has(fever),
    has(chills),
    has(sweating).

disease(covid19) :-
    has(fever),
    has(cough),
    has(loss_of_taste).

disease(typhoid) :-
    has(fever),
    has(headache),
    has(abdominal_pain).

% --- Dynamic facts (symptoms will be added at runtime) ---
:- dynamic(has/1).

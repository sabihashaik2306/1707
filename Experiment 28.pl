% --- Knowledge Base: diseases and their symptoms ---

% disease(Name, [List of Symptoms])
disease(cold,        [runny_nose, sneezing, sore_throat]).
disease(flu,         [fever, cough, headache, body_ache]).
disease(malaria,     [fever, chills, sweating, headache]).
disease(typhoid,     [fever, abdominal_pain, headache, loss_of_appetite]).
disease(asthma,      [cough, wheezing, shortness_of_breath]).
disease(covid19,     [fever, cough, tiredness, loss_of_taste]).

% --- Rule: check if all symptoms of a disease are present ---
has_disease(Disease, Symptoms) :-
    disease(Disease, DiseaseSymptoms),
    subset(DiseaseSymptoms, Symptoms).

% --- Helper: check if list A is subset of list B ---
subset([], _).
subset([H|T], List) :-
    member(H, List),
    subset(T, List).

% --- Diagnosis rule ---
diagnose(Symptoms, Disease) :-
    has_disease(Disease, Symptoms).

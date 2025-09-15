% --- Knowledge Base: diet suggestions for diseases ---

% diabetes
diet(diabetes, 'Eat high-fiber foods like oats, green leafy vegetables, legumes, and avoid sugar.').
diet(diabetes, 'Prefer whole grains, nuts, and low-fat dairy.').

% hypertension
diet(hypertension, 'Reduce salt intake, avoid oily/fried food, eat more fruits and vegetables.').
diet(hypertension, 'Prefer DASH diet: whole grains, low-fat dairy, lean proteins.').

% obesity
diet(obesity, 'Eat low-calorie, high-fiber foods like vegetables, fruits, and legumes.').
diet(obesity, 'Avoid junk food, sugary drinks, and prefer portion control.').

% anemia
diet(anemia, 'Eat iron-rich foods like spinach, liver, beans, and jaggery.').
diet(anemia, 'Take vitamin C-rich foods (orange, lemon) to improve iron absorption.').

% heart disease
diet(heart_disease, 'Eat omega-3 rich foods like fish, flaxseeds, walnuts, avoid trans fats.').
diet(heart_disease, 'Prefer fruits, vegetables, whole grains, and olive oil.').

% --- Rule to suggest diet ---
suggest_diet(Disease) :-
    diet(Disease, Suggestion),
    write('Diet suggestion for '), write(Disease), write(': '), nl,
    write('- '), write(Suggestion), nl, fail.

suggest_diet(_).

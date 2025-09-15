% --- Database of people with Name and DOB ---
% Format: person(Name, DOB).

person('Sabiha', '12-05-2005').
person('Rahul', '23-09-2004').
person('Anjali', '01-01-2006').
person('Arjun',  '17-07-2003').
person('Fatima','29-12-2005').

% --- Rule to get DOB by Name ---
get_dob(Name, DOB) :-
    person(Name, DOB).

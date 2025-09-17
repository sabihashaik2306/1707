% Define vowels
vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).

% Base case: empty list → 0 vowels
count_vowels([], 0).

% If head is a vowel → count + 1
count_vowels([H|T], Count) :-
    vowel(H),
    count_vowels(T, RestCount),
    Count is RestCount + 1.

% If head is not a vowel → skip
count_vowels([H|T], Count) :-
    \+ vowel(H),
    count_vowels(T, Count).

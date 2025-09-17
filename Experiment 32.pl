% pattern_match(Pattern, Text) is true if Pattern appears in Text

% Case 1: Pattern matches the prefix of Text
pattern_match(Pattern, Text) :-
    prefix(Pattern, Text).

% Case 2: Otherwise, skip the first element of Text and keep checking
pattern_match(Pattern, [_|Tail]) :-
    pattern_match(Pattern, Tail).

% Helper predicate: prefix(Prefix, List) is true if Prefix is a prefix of List
prefix([], _).
prefix([H|T1], [H|T2]) :-
    prefix(T1, T2).

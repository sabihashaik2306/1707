% Facts: parent(Parent, Child)
parent(john, mary).
parent(john, tom).
parent(susan, mary).
parent(susan, tom).
parent(mary, linda).
parent(mary, james).
parent(michael, linda).
parent(michael, james).

% Rules
% father(Father, Child)
father(Father, Child) :- parent(Father, Child), male(Father).

% mother(Mother, Child)
mother(Mother, Child) :- parent(Mother, Child), female(Mother).

% male and female
male(john).
male(tom).
male(michael).
male(james).

female(susan).
female(mary).
female(linda).

% sibling(X, Y)
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.

% grandparent(GP, GC)
grandparent(GP, GC) :- parent(GP, P), parent(P, GC).

% uncle(Uncle, NieceOrNephew)
uncle(Uncle, N) :- male(Uncle), parent(P, N), sibling(Uncle, P).

% aunt(Aunt, NieceOrNephew)
aunt(Aunt, N) :- female(Aunt), parent(P, N), sibling(Aunt, P).

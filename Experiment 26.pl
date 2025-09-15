% --- Knowledge Base of fruits and their colours ---
fruit(apple, red).
fruit(banana, yellow).
fruit(orange, orange).
fruit(grapes, green).
fruit(grapes, purple).
fruit(mango, yellow).
fruit(blueberry, blue).
fruit(kiwi, brown).

% --- Rule to find fruit colour ---
fruit_colour(Fruit, Colour) :-
    fruit(Fruit, Colour).

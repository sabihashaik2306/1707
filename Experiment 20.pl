% --- Facts about planets ---
% planet(Name, PositionFromSun, Type, Moons).

planet(mercury, 1, terrestrial, 0).
planet(venus,   2, terrestrial, 0).
planet(earth,   3, terrestrial, 1).
planet(mars,    4, terrestrial, 2).
planet(jupiter, 5, gas_giant, 79).
planet(saturn,  6, gas_giant, 83).
planet(uranus,  7, ice_giant, 27).
planet(neptune, 8, ice_giant, 14).

% --- Rules ---
% Find if a planet has moons
has_moons(Planet) :-
    planet(Planet, _, _, Moons),
    Moons > 0.

% Check type of planet
planet_type(Planet, Type) :-
    planet(Planet, _, Type, _).

% Find position from Sun
position_from_sun(Planet, Pos) :-
    planet(Planet, Pos, _, _).

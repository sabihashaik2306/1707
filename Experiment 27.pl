% --- Graph representation ---
% edge(X, Y) means there is an edge from X to Y

edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(d, g).
edge(e, h).
edge(f, i).

% --- Breadth First Search Implementation ---

% bfs(Start, Goal, Path)
bfs(Start, Goal, Path) :-
    bfs_queue([[Start]], Goal, RevPath),
    reverse(RevPath, Path).

% If the first path starts with Goal, we are done
bfs_queue([[Goal | Rest] | _], Goal, [Goal | Rest]).

% Otherwise expand first path and continue with rest of queue
bfs_queue([[Node | Rest] | Paths], Goal, Result) :-
    findall([Next, Node | Rest],
            (edge(Node, Next), \+ member(Next, [Node | Rest])),
            NewPaths),
    append(Paths, NewPaths, UpdatedQueue),
    bfs_queue(UpdatedQueue, Goal, Result).

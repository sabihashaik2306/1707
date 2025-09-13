import math

def alphabeta(depth, nodeIndex, isMax, scores, alpha, beta, h):
    
    if depth == h:
        return scores[nodeIndex]

    if isMax:
        best = -math.inf
        for i in range(2):  
            val = alphabeta(depth+1, nodeIndex*2+i, False, scores, alpha, beta, h)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:   
                break
        return best
    else:
        best = math.inf
        for i in range(2): 
            val = alphabeta(depth+1, nodeIndex*2+i, True, scores, alpha, beta, h)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:  
                break
        return best



n = int(input("Enter number of leaf nodes (power of 2): "))
scores = list(map(int, input("Enter leaf node values: ").split()))

h = int(math.log(len(scores), 2))  

print("Leaf Nodes:", scores)
optimal = alphabeta(0, 0, True, scores, -math.inf, math.inf, h)
print("The Optimal Value is:", optimal)

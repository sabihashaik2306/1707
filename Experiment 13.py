import math

def minimax(depth, nodeIndex, isMax, scores, h):
   
    if depth == h:
        return scores[nodeIndex]

    if isMax:
        return max(minimax(depth+1, nodeIndex*2, False, scores, h),
                   minimax(depth+1, nodeIndex*2+1, False, scores, h))
    else:
        return min(minimax(depth+1, nodeIndex*2, True, scores, h),
                   minimax(depth+1, nodeIndex*2+1, True, scores, h))


scores = [3, 5, 6, 9, 1, 2, 0, -1]
h = int(math.log(len(scores), 2))

print("Leaf Nodes:", scores)
print("Optimal Value:", minimax(0, 0, True, scores, h))

def minimax(depth, node, isMax, scores):

    if depth == 2:
        return scores[node]

    if isMax:
        return max(
            minimax(depth + 1, node * 2, False, scores),
            minimax(depth + 1, node * 2 + 1, False, scores)
        )
    else:
        return min(
            minimax(depth + 1, node * 2, True, scores),
            minimax(depth + 1, node * 2 + 1, True, scores)
        )

scores = [3, 5, 2, 9]

print("Optimal Value:", minimax(0, 0, True, scores))
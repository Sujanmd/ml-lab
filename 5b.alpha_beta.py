def alphabeta(depth, node, alpha, beta, isMax, scores):

    if depth == 2:
        return scores[node]

    if isMax:
        best = -1000

        for i in range(2):
            val = alphabeta(depth+1, node*2+i,
                            alpha, beta, False, scores)

            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = 1000

        for i in range(2):
            val = alphabeta(depth+1, node*2+i,
                            alpha, beta, True, scores)

            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


scores = [3, 5, 2, 9]

print("Optimal Value:",
      alphabeta(0, 0, -1000, 1000, True, scores))
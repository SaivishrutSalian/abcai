tree = [[[5, 1, 2], [8, -8, -9]], [[9, 4, 5], [-3, 4, 3]]]
root = 0
pruned = 0

def children(branch, depth, alpha, beta):
    global pruned
    i = 0
    for child in branch:
        if isinstance(child, list):
            (nalpha, nbeta) = children(child, depth + 1, alpha, beta)
            if depth % 2 == 1:  # Minimizer's turn
                beta = min(beta, nalpha)
            else:  # Maximizer's turn
                alpha = max(alpha, nbeta)
            branch[i] = alpha if depth % 2 == 0 else beta
            i += 1
        else:
            if depth % 2 == 0:  # Maximizer's turn
                alpha = max(alpha, child)
            else:  # Minimizer's turn
                beta = min(beta, child)
            if alpha >= beta:  # Prune the branch
                pruned += 1
                break

    return (alpha, beta)

def alphabeta(in_tree=tree, start=root, alpha=-15, beta=15):
    global tree
    global pruned
    (final_alpha, final_beta) = children(in_tree, start, alpha, beta)
    print("(alpha, beta): ", final_alpha, final_beta)
    print("Result: ", tree)
    print("Times pruned: ", pruned)

alphabeta()

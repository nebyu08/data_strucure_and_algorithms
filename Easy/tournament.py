def tournament_winner(compitition,scores):
    """returns the team with the highest score

    Args:
        compitition (list): contains a lits where the names of the compition are listed
        scores (_type_): contains the index of who won the compition of every round held
    """

   # best_score=""  #empty value
    saved_scores=dict()
    for idx,teams in enumerate(compitition):
        index=scores[idx]  #index of the highest score
        winner=teams[index] #the winner of the compitition 
        if winner in saved_scores.keys():
            saved_scores[winner]+=3
        else:
            saved_scores[winner]=3
    return max(saved_scores)


comp=[
    ['a','b'],
    ['c','a'],
    ['b','f']
]

score=[0,0,1]
print(tournament_winner(comp,score))
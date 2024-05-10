def tournament_winner(compitition,scores):
    """returns the team with the highest score

    Args:
        compitition (list): contains a lits where the names of the compition are listed
        scores (_type_): contains the index of who won the compition of every round held
    """

    # best_score=""  #empty value
    best_team=""  #the best team
    saved_scores={best_team:0}
    for idx,teams in enumerate(compitition):
        index=scores[idx]  #index of the highest score
        winner=teams[index] #the winner of the compitition 
        
        #updating the state of the values of the dictionary
        if winner in saved_scores.keys():
            saved_scores[winner]+=3
        else:
            saved_scores[winner]=0

        #another if else statement...open for changes...
        if saved_scores[winner] > saved_scores[best_team]:
                best_team=winner
    
    return best_team


comp=[
    ['a','b'],
    ['c','a'],
    ['b','f']
]

score=[0,0,1]
print(f"the best team is:{tournament_winner(comp,score)}")
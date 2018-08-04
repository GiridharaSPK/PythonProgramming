board=[[0,0,1,1,1,1,0,0],[1,0,0,1,1,0,1,1],[2,2,0,0,1,0,0,0],[2,0,2,0,0,0,1,1],[1,2,0,2,2,0,1,1],[1,2,0,0,0,0,0,0],[1,0,0,2,2,0,0,0],[0,0,2,2,2,0,1,1]]

# start form board[0][0]
# end at board[7][7]
# move on 0s
# cant move on 1s
# can move on 2s but with penalty

pawn=board[0][0]
print(pawn)
score=0
penalty=0
path=[] 
# check zeros from position
# def movement():
    # if zeroes
        # move score=score+1
    # elif 1
        # dont move
    # elif 2
        # move score=score+1, penalty=0.5, score=score-penalty

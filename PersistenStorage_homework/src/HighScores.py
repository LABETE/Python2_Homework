import shelve
import os

def highscore(player_name, score):
        path = os.getcwd()
        shelf = shelve.open(path)
        tmp_score = 0   
        if not player_name in shelf: 
            shelf[player_name] = score
        else:
            tmp_score = shelf[player_name]
            shelf[player_name] = max(score, tmp_score)
        final_score = shelf[player_name]
        shelf.sync()
        shelf.close()
        return final_score

import random

agent_name = "forgiveness"
def cooperateOrBetray(my_past_moves,opponent_past_moves):
    if opponent_past_moves:
        if random.random() > 0.9:
                return "C"   
        return opponent_past_moves[-1]
    return "C"
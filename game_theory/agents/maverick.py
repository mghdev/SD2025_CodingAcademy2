
import random

agent_name = "maverick"
def cooperateOrBetray(my_past_moves,opponent_past_moves):
    if random.random() > 0.5:
        return "C"
    return "B"

agent_name = "copycat"
def cooperateOrBetray(my_past_moves,opponent_past_moves):
    if opponent_past_moves:
        return opponent_past_moves[-1]
    return "C"
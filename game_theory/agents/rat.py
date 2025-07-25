
agent_name = "rat"
def cooperateOrBetray(my_past_moves,opponent_past_moves):
    if opponent_past_moves:
        if len(opponent_past_moves) % 15 == 0:
            return "B"
        return opponent_past_moves[-1]
    return "C"

agent_name = "grudge-holder"
def cooperateOrBetray(my_past_moves, opponent_past_moves):
    if "B" in opponent_past_moves:
        return "B"
    return "C"
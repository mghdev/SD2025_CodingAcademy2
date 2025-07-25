
agent_name = "punisher"
def cooperateOrBetray(my_past_moves, opponent_past_moves):
    if not opponent_past_moves:
        return "C"
    if "B" in opponent_past_moves[-min(len(opponent_past_moves),3):]:
        return "B"
    return "C"

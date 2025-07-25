
agent_name = "zodiac"
def cooperateOrBetray(my_past_moves,opponent_past_moves):
    if len(opponent_past_moves) > 2:
        if opponent_past_moves[-1] == "B":
            if opponent_past_moves[-2] == "B":
                if opponent_past_moves[-3] == "B":
                    if len(opponent_past_moves) % 100 != 0:
                        return "B"
                elif len(opponent_past_moves) % 25 != 0:
                    return "B"
            elif len(opponent_past_moves) % 3 != 0:
                return "B"
        if  len(my_past_moves) % 10 == 0:
            return "B"
    return "C"

NUM_ROUNDS = 200
POINTS_COOPERATE_SUCCESS = 3
POINTS_COOPERATE_FAILURE = 0
POINTS_BETRAY_SUCCESS = 5
POINTS_BETRAY_FAILURE = 1

#==============================
# YOUR CODE HERE
agent_name = "wolf in sheep's clothing"
def cooperateOrBetray(my_past_moves,opponent_past_moves):
    return "B"
#==============================

def playRound(agent0,agent1,history):
    return [agent0(history[0],history[1]),agent1(history[1],history[0])]


def playManyRounds(agent0,agent1,n):
    history = [[],[]]
    for i in range(n):
        move_0,move_1 = playRound(agent0,agent1,history)
        history[0] += [move_0]
        history[1] += [move_1]
    return history

def scoreRounds(history):
    scores = [0,0]
    for move_0,move_1 in zip(history[0],history[1]):
        if move_0 == "C" and move_1 == "C":
            scores[0] += POINTS_COOPERATE_SUCCESS
            scores[1] += POINTS_COOPERATE_SUCCESS
        elif move_0 == "B" and move_1 == "B":
            scores[0] += POINTS_BETRAY_FAILURE
            scores[1] += POINTS_BETRAY_FAILURE
        elif move_0 == "B":
            scores[0] += POINTS_BETRAY_SUCCESS
            scores[1] += POINTS_COOPERATE_FAILURE
        else:
            scores[0] += POINTS_COOPERATE_FAILURE
            scores[1] += POINTS_BETRAY_SUCCESS
    return scores

def scoreAgents(agent1,agent2):
    history = playManyRounds(agent1,agent2,NUM_ROUNDS)
    return scoreRounds(history)

class Agent:
    def __init__(self,func,name) -> None:
        self.func = func
        self.name = name
        self.score = 0
        self.rounds_played = 0

def printScores(agent_list):
    for i in range(len(agent_list)):
        print(i+1,". ",agent_list[i].name," - ",agent_list[i].score," (",agent_list[i].rounds_played,")",sep="")

def main():
    from agents import copycat,dove,forgiveness,grudge,maverick,modulo,punisher,rat,wolf
    
    agent_list = [
        Agent(cooperateOrBetray,agent_name),
        Agent(copycat.cooperateOrBetray,copycat.agent_name),
        Agent(dove.cooperateOrBetray,dove.agent_name),
        Agent(forgiveness.cooperateOrBetray,forgiveness.agent_name),
        Agent(grudge.cooperateOrBetray,grudge.agent_name),
        Agent(maverick.cooperateOrBetray,maverick.agent_name),
        Agent(modulo.cooperateOrBetray,modulo.agent_name),
        Agent(punisher.cooperateOrBetray,punisher.agent_name),
        Agent(rat.cooperateOrBetray,rat.agent_name),
        Agent(wolf.cooperateOrBetray,wolf.agent_name),
        
    ]
    
    for i in range(len(agent_list)):
        for j in range(i,len(agent_list)):
            s = scoreAgents(agent_list[i].func,agent_list[j].func)
            agent_list[i].score += s[0]
            agent_list[i].rounds_played += 1
            
            agent_list[j].score += s[1]
            if i != j:
                agent_list[j].rounds_played += 1
    
    agent_list.sort(key=(lambda a : a.score),reverse=True)
    printScores(agent_list)
    

if __name__ == "__main__":
    main()

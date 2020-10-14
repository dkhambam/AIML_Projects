from gym import spaces
import numpy as np
import random
from itertools import groupby
from itertools import product



class TicTacToe():

    def __init__(self):
        """initialise the board"""
        
        # initialise state as an array  
        self.state = [np.nan for _ in range(9)]  # initialises the board position , can initialise to an array or matrix
        # all possible numbers
        self.all_possible_numbers = [i for i in range(1, len(self.state) + 1)] # , can initialise to an array or matrix

        self.reset()


    def is_winning(self, curr_state):
        """Takes state as an input and returns whether any row, column or diagonal has winning sum
        Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan]
        Output = False"""
        winning_combinations = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        # We will check only for the above 8 combinations to see any of them sums up to 15 which implies winning
        for combination in  winning_combinations:
            #print('Combination:',combination)
            if not np.isnan(curr_state[combination[0]]) and not np.isnan(curr_state[combination[1]]) and not np.isnan(curr_state[combination[2]]) :
                if curr_state[combination[0]] + curr_state[combination[1]] + curr_state[combination[2]]  == 15 :
                    return True
            
        #If none of the above condition is True return False        
        return False 
             
 

    def is_terminal(self, curr_state):
        # Terminal state could be winning state or when the board is filled up

        if self.is_winning(curr_state) == True:
            return True, 'Win'

        elif len(self.allowed_positions(curr_state)) ==0:
            return True, 'Tie'

        else:
            return False, 'Resume'


    def allowed_positions(self, curr_state):
        """Takes state as an input and returns all indexes that are blank"""
        return [i for i, val in enumerate(curr_state) if np.isnan(val)]


    def allowed_values(self, curr_state):
        """Takes the current state as input and returns all possible (unused) values that can be placed on the board"""

        used_values = [val for val in curr_state if not np.isnan(val)]
        agent_values = [val for val in self.all_possible_numbers if val not in used_values and val % 2 !=0]
        env_values = [val for val in self.all_possible_numbers if val not in used_values and val % 2 ==0]

        return (agent_values, env_values)


    def action_space(self, curr_state):
        """Takes the current state as input and returns all possible actions, i.e, all combinations of allowed positions and allowed values"""

        agent_actions = product(self.allowed_positions(curr_state), self.allowed_values(curr_state)[0])
        env_actions = product(self.allowed_positions(curr_state), self.allowed_values(curr_state)[1])
        return (agent_actions, env_actions)



    def state_transition(self, curr_state, curr_action):
        """Takes current state and action and returns the board position just after agent's move.
        Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan], action- [7, 9] or [position, value]
        Output = [1, 2, 3, 4, nan, nan, nan, 9, nan]
        """
        #The state transition happens from the current state to the next state based on agent's action
        curr_state[curr_action[0]]=curr_action[1]
        return curr_state


    def step(self, curr_state, curr_action):
        """Takes current state and action and returns the next state, reward and whether the state is terminal. Hint: First, check the board position after
        agent's move, whether the game is won/loss/tied. Then incorporate environment's move and again check the board status.
        Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan], action- [7, 9] or [position, value]
        Output = ([1, 2, 3, 4, nan, nan, nan, 9, nan], -1, False)"""
        transition_to_state=self.state_transition(curr_state, curr_action)
        #print('transition_to_state',transition_to_state)
        terminal_check=False
        terminal_check,game_status =self.is_terminal (transition_to_state)
        #print('terminal_check_step',terminal_check)
        #After the agent's action is reflected on the state,check to see if it is 'Win' or 'Tie'
        if terminal_check  == True :
            if game_status=='Win':
               reward = 10
            else:
               reward = 0
        else:
           #If the agent's action doesn't result in Win (or) Tie,Its the Env plays and we check to see if Env Won/Tie/no_result_yet.
            position = random.choice(self.allowed_positions(transition_to_state))
            value = random.choice(self.allowed_values(transition_to_state)[1])
            transition_to_state[position]= value
            terminal_check,game_status =self.is_terminal (transition_to_state)
            if terminal_check  == True :
                if game_status=='Win':
                   reward = -10
                else:
                   reward = 0
            else:
                reward = -1
        

        return transition_to_state, reward, terminal_check
       

    def reset(self):
        return self.state

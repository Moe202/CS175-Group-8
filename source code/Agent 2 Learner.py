# ------------------------------------------------------------------------------------------------
# Copyright (c) 2016 Microsoft Corporation
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ------------------------------------------------------------------------------------------------
# Used Malmo's tutorial_6.py as a template

import MalmoPython
import json
import logging
import os
import random
import sys
import time
import Tkinter as tk

class TabQAgent:
    """Tabular Q-learning agent for discrete state/action spaces."""
    
    def __init__(self):
        self.epsilon = 0.01 # chance of taking a random action instead of the best
        self.alpha = 0.1 # learning rate
        self.gamma = 1.0 # discount rate
        
        self.logger = logging.getLogger(__name__)
        if False: # True if you want to see more information
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)
        self.logger.handlers = []
        self.logger.addHandler(logging.StreamHandler(sys.stdout))
        # Set of actions
        self.actions = ["movewest 1", "moveeast 1", "movenorth 1", "movesouth 1", "tpn", "tps", "tpe", "tpw"]
        # Additional action costs to take into account (Each action costs 1 by default). 
        # Action cost = 1 + self.action_cost[i]
        self.action_cost = [0, 0, 0, 0, 300, 300, 300, 300]
        self.q_table = {}
        self.canvas = None
        self.root = None

    def sendAction(self, agent_host, x, y, z, action):
        if(action == 4):
            y = y + 1
            z = z + 2
            tp_command = "tp {0:0.1f} {1:0.1f} {2:0.1f}".format(x, y, z)
            agent_host.sendCommand(tp_command)
            time.sleep(0.5)
        elif(action == 5):
            y = y + 1
            z = z - 2
            tp_command = "tp {0:0.1f} {1:0.1f} {2:0.1f}".format(x, y, z)
            agent_host.sendCommand(tp_command)
            time.sleep(0.5)
        elif(action == 6):
            y = y + 1
            x = x + 2
            tp_command = "tp {0:0.1f} {1:0.1f} {2:0.1f}".format(x, y, z)
            agent_host.sendCommand(tp_command)
            time.sleep(1)
        elif(action == 7):
            y = y + 1
            x = x - 2
            tp_command = "tp {0:0.1f} {1:0.1f} {2:0.1f}".format(x, y, z)
            agent_host.sendCommand(tp_command)
            time.sleep(0.5)
        else:
            agent_host.sendCommand(self.actions[action])
            time.sleep(0.2)


    def updateQTable( self, reward, current_state ):
        """Change q_table to reflect what we have learnt."""
        
        # retrieve the old action value from the Q-table (indexed by the previous state and the previous action)
        old_q = self.q_table[self.prev_s][self.prev_a]
        
        # Calculate new action value
        new_q = ( old_q + self.alpha * (reward + self.gamma * max(self.q_table[current_state]) - old_q) )
        
        # assign the new action value to the Q-table
        self.q_table[self.prev_s][self.prev_a] = new_q
    
    def updateQTableFromTerminatingState( self, reward ):
        """Change q_table to reflect what we have learnt, after reaching a terminal state."""
        
        # retrieve the old action value from the Q-table (indexed by the previous state and the previous action)
        old_q = self.q_table[self.prev_s][self.prev_a]
        
        # Calculate new action value
        new_q = ( old_q + self.alpha * ( reward - old_q ) )
        
        # assign the new action value to the Q-table
        self.q_table[self.prev_s][self.prev_a] = new_q
    
    def act(self, world_state, agent_host, current_r ):
        """take 1 action in response to the current world state"""
        
        obs_text = world_state.observations[-1].text
        obs = json.loads(obs_text) # most recent observation
        self.logger.debug(obs)
        if not u'XPos' in obs or not u'ZPos' in obs or not u'Ypos':
            self.logger.error("Incomplete observation received: %s" % obs_text)
            return 0

        current_s = "%d:%d" % (int(obs[u'XPos']), int(obs[u'ZPos']))
        self.logger.debug("State: %s (x = %.2f, z = %.2f)" % (current_s, float(obs[u'XPos']), float(obs[u'ZPos'])))
        
        # Set initial q-values for actions in new state 
        # ("move" actions initial values are 0 while "jump" actions initial values are -2)
        if not self.q_table.has_key(current_s):
            self.q_table[current_s] = [0, 0, 0, 0, 0, 0, 0, 0]
        
        # update Q values
        if self.prev_s is not None and self.prev_a is not None:
            self.updateQTable( current_r, current_s )
        
        # select the next action
        rnd = random.random()
        if rnd < self.epsilon:
            a = random.randint(0, len(self.actions) - 1)
            self.logger.info("Random action: %s" % self.actions[a])
        else:
            m = max(self.q_table[current_s])
            self.logger.debug("Current values: %s" % ",".join(str(x) for x in self.q_table[current_s]))
            l = list()
            moveAvailable = False
            for x in range(0, len(self.actions)):
                if self.q_table[current_s][x] == m:
                    if x < 4:
                        l.append(x)
                        moveAvailable = True
                    elif not moveAvailable:
                        l.append(x)
            y = random.randint(0, len(l)-1)
            a = l[y]
            self.logger.info("Taking q action: %s" % self.actions[a])
        
        # try to send the selected action, only update prev_s if this succeeds
        try:
            self.sendAction(agent_host, obs[u'XPos'], obs[u'YPos'], obs[u'ZPos'], a)
            self.prev_s = current_s
            self.prev_a = a
        
        except RuntimeError as e:
            self.logger.error("Failed to send command: %s" % e)
        
        return (current_r)
    
    def run(self, agent_host):
        """run the agent on the world"""
        
        total_reward = 0
        cost = 0
        self.prev_s = None
        self.prev_a = None
        
        is_first_action = True
        
        # main loop:
        world_state = agent_host.getWorldState()
        while world_state.is_mission_running:
            
            # Subtract the cost of the previous action from the current reward value
            current_r = 0 - cost
            
            if is_first_action:
                # wait until have received a valid observation
                while True:
                    time.sleep(0.1)
                    world_state = agent_host.getWorldState()
                    for error in world_state.errors:
                        self.logger.error("Error: %s" % error.text)
                    for reward in world_state.rewards:
                        current_r += reward.getValue()
                    if world_state.is_mission_running and len(world_state.observations)>0 and not world_state.observations[-1].text=="{}":
                        total_reward += self.act(world_state, agent_host, current_r)
                        cost = self.action_cost[self.prev_a]
                        break
                    if not world_state.is_mission_running:
                        break
                is_first_action = False
            else:
                # wait for non-zero reward
                while world_state.is_mission_running and current_r == 0-cost:
                    time.sleep(0.1)
                    world_state = agent_host.getWorldState()
                    for error in world_state.errors:
                        self.logger.error("Error: %s" % error.text)
                    for reward in world_state.rewards:
                        current_r += reward.getValue()
                # allow time to stabilise after action
                while True:
                    time.sleep(0.1)
                    world_state = agent_host.getWorldState()
                    for error in world_state.errors:
                        self.logger.error("Error: %s" % error.text)
                    for reward in world_state.rewards:
                        current_r += reward.getValue()
                    if world_state.is_mission_running and len(world_state.observations)>0 and not world_state.observations[-1].text=="{}":
                        total_reward += self.act(world_state, agent_host, current_r)
                        cost = self.action_cost[self.prev_a]
                        break
                    if not world_state.is_mission_running:
                        break
    
        # process final reward
        self.logger.debug("Final reward: %d" % current_r)
        total_reward += current_r
        
        # update Q values
        if self.prev_s is not None and self.prev_a is not None:
            self.updateQTableFromTerminatingState( current_r )

        return total_reward

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately

agent = TabQAgent()
agent_host = MalmoPython.AgentHost()
try:
    agent_host.parse( sys.argv )
except RuntimeError as e:
    print 'ERROR:',e
    print agent_host.getUsage()
    exit(1)
if agent_host.receivedArgument("help"):
    print agent_host.getUsage()
    exit(0)

# -- set up the mission -- #
mission_file = './level0.xml'     # Change this to load different maps/missions
with open(mission_file, 'r') as f:
    print "Loading mission from %s" % mission_file
    mission_xml = f.read()
    my_mission = MalmoPython.MissionSpec(mission_xml, True)

# Let the agent run 150 times
max_retries = 3

if agent_host.receivedArgument("test"):
    num_repeats = 1
else:
    num_repeats = 300

cumulative_rewards = []
for i in range(num_repeats):
    
    print
    print 'Repeat %d of %d' % ( i+1, num_repeats )
    
    my_mission_record = MalmoPython.MissionRecordSpec()
    
    for retry in range(max_retries):
        try:
            agent_host.startMission( my_mission, my_mission_record )
            break
        except RuntimeError as e:
            if retry == max_retries - 1:
                print "Error starting mission:",e
                exit(1)
            else:
                time.sleep(2.5)

    print "Waiting for the mission to start",
    world_state = agent_host.getWorldState()
    while not world_state.has_mission_begun:
        sys.stdout.write(".")
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        for error in world_state.errors:
            print "Error:",error.text
    print
    
    # -- run the agent in the world -- #
    cumulative_reward = agent.run(agent_host)
    print 'Cumulative reward: %d' % cumulative_reward
    cumulative_rewards += [ cumulative_reward ]
    
    # -- clean up -- #
    time.sleep(0.5) # (let the Mod reset)

print "Done."

print
print "Cumulative rewards for all %d runs:" % num_repeats
print cumulative_rewards

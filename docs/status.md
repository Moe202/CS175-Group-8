---
layout: default
title: Status
---



# Project Summary
Solve an intricate maze with traps, lava, etc. Optimize by trying to improve the time the agent solves the maze or by finding the most optimal path. The input of the project would require a section of the map the agent would traverse. Output would be the most optimal path discovered by the agent. Lastly, we assume that every block is unknown and the agent must discover each path. Direct applications of this project would allow users to optimally beat multiple video games. At a high level, reinforcement learning discovered from this project can determine the ideal behavior within the manufacturing, delivery, and finance industries.

Level 1: Flat terrain, with edge boundary  (Actions: Walk, Jump)<br>
Level 2: Flat terrain, with edge boundary and hazards in the middle of the map  (Actions: Walk, Jump)<br>
Level 3: 3D terrain, hills, hazards, blocks  (Actions: Walk, Jump)<br>
Level 4: 3D terrain, hills, hazards, blocks  (Actions: Walk, Jump, Timed Jump)<br>
Level 5: Moonshot case- 3D terrain, hills, hazards, blocks and zombies  (Actions: Walk, Jump, Timed Jump)<br>

<img src="images/level1.jpeg" title="level 1 map" width="280" height="280" /> <img src="images/level2.jpeg" title="level 2 map" width="280" height="280" /> <img src="images/level3.jpeg" title="level 3 map" width="280" height="280" />



# Approach

For progress report, our approach used the Q-Learning algorithm. Here is the equation of Q-Learning algorithm and our parameter set-up.<br>
The Q-Learning equation:<br>

<img src="images/eq.gif" title="equation" />

```python
self.epsilon = 0.01 # chance of taking a random action instead of the best
self.alpha = 0.1 # learning rate
self.gamma = 1.0 # discount rate

# Set of actions
self.actions = ["movewest 1", "moveeast 1", "movenorth 1", "movesouth 1", "jumpnorth 1", \
                        "jumpsouth 1", "jumpwest 1", "jumpeast 1"]
Action cost = 1 + self.action_cost[i]
self.action_cost = [0, 0, 0, 0, 9, 9, 9, 9]
```
**Learning Rate:** Alpha represents the learning rate. It is value between 0 and 1 ( 0 \< a \< 1). It indicates how much the utility values will be updated every time the agent takes an action. alpha = 0 means the agent will not learn anything. alpha = 1 means the agent will not consider any feature states (the agent only consider most recent information). In stochastic environment, alpha is preferable closer to 0 than 1. In our approach, we decide alpha value to be 0.1<br><br>
**Discount Factor:** Gamma is the discount factor. It determines the importance of future information.  Gamma closer to 0 will encourages the agent to seek out rewards sooner rather than later. It makes the agent assign a smaller reward to the feature action. Gamma closer to 1 will makes the agent seek for high reward in the feature. This value usually closer to 1. We set gamma value to 1 in our approach<br><br>
**Random Action:** Epsilon is the possibility of taking a random action instead of the best one. (needs more here)<br>
**Immediate Reward Valuer:** r is the immediate reward value (needs more/ do we need it?)<br>
**Max Q Value:** The action has the highest utility value in next state will become the new Q value of that states<br>

### The 3 Levels
<img src="images/grid.jpeg" title="grid" width="1100" height="434" />

The  Figure shows the grid layout in two-dimensional. It specify the start and end blocks. Also，it shows the terrian of mazes(the floor of the maze is cobblestone, block is built by glass\_blocks, hill is built by cobblestone\_blocks). The number in each grid represent the **(x,z)** value and each grids has an altitude value which is  **y**.


#### Level 1:
The level 1 map is a flat terrain with lava on eages. It is a 7x7x1(LxWxH) grid. The agent start at the lapis\_block and try to reach the redstone\_block. The agent can either walk or jump. In level 1, there are () states and 2 actions
#### Level 2:
The level 1 map is built basing on Level 1 map. 5 cobble stone blocks in the middle of map were replaced by 5 lava blocks.It is a 7x7x1(LxWxH) grid. The agent start at the lapis\_block and try to reach the redstone\_block. The agent can either walk or jump. In level 2, there are () states and 2 actions
#### Level 3:
Level 3 map was built basing on level 2 map. A  2x2x2(LxWxH) glass block and a 2x2x1(LxWxH) cobble stone hill. Agent can jump over the cobble stone block(gold) but cannot jump over the glass block. The agent start at the lapis\_block and try to reach the redstone\_block. The agent can either walk or jump. In level 1, there are () states and 2 actions
#### Reward for each actions:
For each action the agent makes, there is a reward value of -1 for each move, -10 for each jump, -100 for reaching the lava block, +100 for reaching the redstone\_block(goal state)









# Evaluation
For **qualitative evaluation**, we evaluate our project by checking how well the agent can solve the all 3 level mazes. We observe the agent when it is solving the maze to verify it works correctly. Also, we can check our agent by using the Cumulative Rewards Table.<br>
**Level1:** one of the optimal path of level 1 is (1,1) move-> (1,2) move-> (1,3) move-> (1,4) move-> (1,5) move-> (1,6) move-> (2,6) move-> (3,6) move-> (4,6) move-> (5,6) move-> (6,6). It takes 10 moves. Therefore, the best reward we can get is 90. The Cumulative Rewards Table shows how the agent finds the solution with the highest reward. 
<img src="images/crt1.jpeg" title="Cumulative Rewards Table lvl 1" width="528" height="162.4" /><br>
**Level2:** one of the optimal path of level 2 is 
**Level3:** one of the optimal path of level 3 is 
<br>
In terms of **quantitative evaluation**, we evaluate our project by checking how long it takes the agent to solve each mazes. That is, we want the agent to slove the maze as quick as it can. We use the Cumulative Rewards Table to check how many runs it takes before getting the best reward.
| Tables        |    level 1    |    level 1     |    level 1    | 
| ------------- |:-------------:| :-------------:|:-------------:|
| # of runs     |               |                |               |



# Remaining Goals and Challenges
For the rest of weeks, we will add an “timed jump” which means the agent can either jump 1 blocks or 2-3 blocks. That is our level 4. It is interesting to discover how will the agent perform when we add more uncertainty into the map and how we can improve its performance by using different parameters set-up. 
Also, we will add zombies on patrol which is level 5. This will add more actions to our project. ( describe how you consider your prototype to be limited, ) (iven your experience so far, describe some of the challenges you anticipate facing by the time your final report is due, how crippling you think it might be, and what you might do to solve them.)



[image-1]:	https://github.com/Moe202/Reward-Finder/blob/master/docs/images/eq.gif

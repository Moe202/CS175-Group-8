---
layout: default
title: Status
---



# Project Summary
&nbsp;&nbsp;&nbsp;&nbsp; Solve an intricate maze with traps, lava, etc. Optimize by trying to improve the time the agent solves the maze or by finding the most optimal path. The input of the project would require a section of the map the agent would traverse. Output would be the most optimal path discovered by the agent. Lastly, we assume that every block is unknown and the agent must discover each path. Direct applications of this project would allow users to optimally beat multiple video games. At a high level, reinforcement learning discovered from this project can determine the ideal behavior within the manufacturing, delivery, and finance industries.

Level 1: Flat terrain, with edge boundary  
Level 2: Flat terrain, with edge boundary and hazards in the middle of the map  
Level 3: 3D terrain, hills, hazards, blocks  
Level 4: 3D terrain, hills, hazards, blocks, and timed jumps  
Level 5: Moonshot case- 3D terrain, hills, hazards, blocks, timed jumps, and zombies  

<img src="images/level1.jpeg" title="level 1 map" width="280" height="280" /> <img src="images/level2.jpeg" title="level 2 map" width="280" height="280" /> <img src="images/level3.jpeg" title="level 3 map" width="280" height="280" />



# Approach

```python
self.epsilon = 0.01 # chance of taking a random action instead of the best
self.alpha = 0.1 # learning rate
self.gamma = 1.0 # discount rate
        
# Set of actions
self.actions = ["movewest 1", "moveeast 1", "movenorth 1", "movesouth 1", "jumpnorth 1", \
                        "jumpsouth 1", "jumpwest 1", "jumpeast 1"]
self.action_cost = [0, 0, 0, 0, 9, 9, 9, 9]
```

![][1]([https://github.com/Moe202/Reward-Finder/blob/master/docs/images/eq.gif][2])
\<img src="images/eq.gif” title=“equation” /\>
 {% raw %}
	Q(S_t,a_t) \leftarrow Q(S_t,a_t) + \alpha[r_{t+1} + \gamma \cdot \max_a Q(S_{t+1},a_t)  -  Q(S_t,a_t)]
 {% endraw %}

 $$Q(S\_t,a\_t) \leftarrow Q(S\_t,a\_t) + \alpha[r_{t+1} + \gamma \cdot \max\_a Q(S_{t+1},a\_t)  -  Q(S\_t,a\_t)]$$

 $ Q(S\_t,a\_t) \leftarrow Q(S\_t,a\_t) + \alpha[r_{t+1} + \gamma \cdot \max\_a Q(S_{t+1},a\_t)  -  Q(S\_t,a\_t)] \$



# Evaluation


# Remaining Goals and Challenges

[1]:	https://github.com/Moe202/Reward-Finder/blob/master/docs/images/eq.gif
[2]:	https://github.com/Moe202/Reward-Finder/blob/master/docs/images/eq.gif
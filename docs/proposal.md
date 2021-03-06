---
layout: default
title:  Proposal
---

# 2.2 Summary of the Project
&nbsp;&nbsp;&nbsp;&nbsp; Solve an intricate maze with traps, lava, etc. Optimize by trying to improve the time the agent solves the maze or by finding the most optimal path. The input of the project would require a section of the map the agent would traverse. Output would be the most optimal path discovered by the agent. Lastly, we assume that every block is unknown and the agent must discover each path. Direct applications of this project would allow users to optimally beat multiple video games. At a high level, reinforcement learning discovered from this project can determine the ideal behavior within the manufacturing, delivery, and finance industries.


Level 1: Flat terrain, with edge boundary   
Level 2: Flat terrain, with edge boundary and hazards in the middle of the map  
Level 3: 3D terrain, hills, hazards, blocks  
Level 4: 3D terrain, hills, hazards, blocks, and timed jumps  
Level 5: Moonshot case- 3D terrain, hills, hazards, blocks, timed jumps, and zombies     

Inspiration: https://www.youtube.com/watch?v=9XRL6d-yxp4






# 2.3 AI/ML Algorithms
&nbsp;&nbsp;&nbsp;&nbsp; Q-learning and reinforcement learning. Plans to implement computer vision if team finishes early. For example,recognizing where the items and goal block are and avoid traps.


# 2.4 Evaluation Plan
&nbsp;&nbsp;&nbsp;&nbsp; We plan on giving each block the reward value 0 except for the goal and trap blocks (terminal states), which will have the reward values +10 and -10 respectively. Each state that is not a terminal state has 4 availble actions to take, which are move forward, move backward, move left, and move right (might add a 5th action, which is pick up item if we plan on placing items on the map). Each of those actions will cost the agent -1 to do. The initial values for each state and action pair (s, a) is going to be 0, and they will be updated as the agent traverses through the maze. Our goal is to maximize the overall value by fininding the shortest block to the goal block. We will run the Q-learning algorithm until the maximum difference between a current and previous (s,a) value is less than 0.0001. Once that happens, we will know that the agent found the shortest path and then we will return it.


&nbsp;&nbsp;&nbsp;&nbsp; We can determine whether the AI agent works corrrectly or not by observing it. If the path it takes eventually converges to the shortest possible path, then we will know that it works correctly. Also, we can precompute the length of the shortest path using Dijkstra's algorithm and check if the length of the path found using Q-learning matches it. As stated earlier, we hope to eventually use computer vision to find the shortest path and maybe place mandatory collectible items in the maze for the agent to collect before reaching the goal.

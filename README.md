# crossy-road
- Replicating the video game crossy road in Python.
- I could do this in turtle graphics or shell, I will probably start with shell.
# How it could be done
- I could set up a bunch of lanes, and then have randomized objects with randomized positions, which would update every second
- I could follow the template of grocery store game
- However, there would need to be 35+ objects moving on the screen, which may cause slowness, spotty animation, and excessive blinking
# What's done so far
- So far, in the code in the repository, there are lanes, with two objects moving so far.
- I have made a function called printlanes, which prints the lanes and the content.
- I have also made a function called refreshlanecontent which refreshed the lane content by sliding out the last space content and the concatinating the new content to the begining and pushing the rest of the content down a space. this works finefine for the first two pushed, and then the objects stop moving.
# What's left to do
- I have to get all the objects doing, and then after I do that, stuff should be pretty easy
- add a person who is crossing the road 
- have an algorithm that detects whether positionobstacle == positionperson
- randomize object location and speed of obstacles
- make different levels with different difficulties
- have a highscore board, stored by text file shelving

# Honors-Project
Algorithm 1: This Algorithm when run, averages around 65 weeks more often. However it isn't steady and usually fluctuates around 45-75 weeks on average. Algorithm 1 focuses on taking one random pair at a time from a list of contestants and then using a truthbooth method to figure out if it matches or not. If it matches it will be sent to an empty matches list, if not then does nothing about it. It will continue until it gets all the matches. 

Algorithm 2: This Algorithm when run, averages around 68 weeks more often but although its steadier than algorithm 1 it does flutuate between 65 - 75 weeks on average. Algorithm 2 focuses on creating all possible pairs from the 16 contestants in a list and then pops each pair from the list. If it matches it will remove the matched contestants from every pair in the list. The goal here is to find out how many weeks it needs for all possible pairs to reach 0. 

Algorithm 3: This Algorithm when run, averages around 55 weeks more often and only flutuates between 55 - 59 weeks on average. Algorithm 3 is the same as algorithm 2 but with a twist, every time the week counter reaches a multiple of 25, the first pair from the perfect pairs dictionary in other words the answer key and deletes all the pairs that contains those contestants. 

My original plan was to create a GUI however I was unable to make a decorative sophisticated one. It uses another algorithm I created and the GUI works as intended just not enough information to simulate the gameplay. Although it isn't my main project I put in alot of effort into learning how to use the GUI so I left it here in a separate folder if you want to take a look.

Each Algorithm's times are so fast, its almost near instantaneous. It fluctuates between, according to the reading, 0.0 - 1.19 * 10^-6. 

# python_mini_project

Python Project Idea
Maze
Concept:User picks left, right, centre then gets given more options depending on their choice.
	After initial choice they arrive at the next junction and offered a new choice
	Can reach dead-end and told to turn around
	Give up button available at all points
	

Maze layout:

				         | |       _
		       __________| |______| |_
		      |__ 2 ______1________3__|
		  _      | |
		 | |_____| |__
		 |5 _____ 4 __|			 
		 |_|     | |
		       __| |
		      E__ 6|
			     |_|



Make a series of junctions and then a function that handles the dead end. Need turn around button.

J1: LR
If L > J3
If R > J2
J2: LS
If L > J4
If S > DE
J3: LS
If L > DE
If S > DE
J4: LSR
If L > DE
If R > J5
If S > J6
J5: LR
If L > DE
If R > DE
J6: SR
If S > DE
If R > WIN

Add verifier: function that takes the direction options and returns whether or not the input is valid given the options.
Can reuse for each junction

Deliverable:
I have used all required areas of python to complete the project: while loops, for loops, variables, conditionals, user input etc. 
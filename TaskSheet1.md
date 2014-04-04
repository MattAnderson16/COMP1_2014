#Task Sheet 1

##Task 3
a)
1. GetPlayerName()
2. Using a while loop that exits once the player has entered their name
3. The extra variable is GotName and it will be a boolean value

	FUNCTION GetPlayerName():
		GotName = FALSE  
		WHILE NOT GotName DO  
			OUTPUT " "  
			PlayerName <- INPUT "Please enter your name: "  
			OUTPUT " "  
			IF PlayerName = " " THEN  
				OUTPUT "You need to input a name!"  
			ELSE  
				GotName = TRUE  
		RETURN GotName  
	END FUNCTION


b)
1. UpdateRecentScores(RecentScores, Score)

##Task 5
1. datetime
2. TRecentScore(), ResetRecentScores(), DisplayRecentScores(), UpdateRecentScores()
3. datetime.datetime.strptime(date,"%d/%m/%y")

#Additional Tasks

##Variable Roles
Fixed Value: A variable created with a hard coded value that is not changed atall in the program 
	

Stepper: A variable counting through a predictable succession of values e.g.
	for NoOfSwapsMadeSoFar in range(1, NoOfSwaps + 1):
		Position1 = random.randint(1, 52)
		...

Most recent holder: A variable holding the latest value obtained from an unpredictable succession of
values or from an input
	NextCard = ''

Most wanted holder: A variable holding the most appropriate value encountered so far.
	Choice = ''

Gatherer: A variable gathering the effect of separate values
	self.Score = 0

Transformation: A variable that always gets its value from a fixed calculation of values of other variables
	Position1 = random.randint(1, 52)

Follower: A variable that gets its new value from the old value of another data item
	LastCard = ''

Temporary: A variable that only holds data for a short amount of time
	Higher = True

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

##Functions and Parameters
1. If data is passed by value then a copy of the data is made for the function and if it gets edited within the function
then it will not effect the original value and will need to be returned. However, if the data is passed by reference then
the data within the function is pointing to the original data and any changes made to the data within it will effect the
original copy of the data outside of the function. This means the data would not need a return value.

2. 
GetRank - RankNo - Passed by reference
GetSuit - SuitNo - Passed by reference
LoadDeck - Deck - Passed by reference
ShuffleDeck - Deck - Passed by reference
DisplayCard - ThisCard - Passed by reference
GetCard - ThisCard - Passed by reference
        - Deck - Passed by reference
		- NoOfCardsTurnedOver - Passed by value
IsNextCardHigher - LastCard - Passed by reference
				 - NextCard - Passed by reference
DisplayEndOfGameMessage - Score - Passed by value
DisplayCorrectGuessMessage - Score - Passed by value
ResetRecentScores - RecentScores - Passed by reference
DisplayRecentScores - RecentScores - Passed by reference
UpdateRecentScores - RecentScores - Passed by reference
				   - Score - Passed by value
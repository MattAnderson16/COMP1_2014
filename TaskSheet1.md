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
	NoOfSwaps = 1000 - 98

Stepper: A variable that increments in a predictable sequence
	Count - 162
	NoOfCardsTurnedOver - 192
	NoOfSwapsMadeSoFar - 99
	

Most recent holder: A variable holding the latest value received when processing an unpredictable succession of values
	Choice = GetChoiceFromUser() - 197
	LineFromFile - 92
	LastCard - 187
	

Most wanted holder: A variable that holds the latest variable that the programmer or user wants
	NextCard - 198

Gatherer: A variable gathering the total of the values received so far
	No examples

Transformation: A variable that always gets its value from a calculaltion or other variables
	Higher - 124
	FoundSpace - 171

Follower: A variable that gets its new value from the old value of another variable
	LastCard - 187

Temporary: A variable used as an intermediary
	SwapSpace - 97

##Functions and Parameters
1. If data is passed by value then a copy of the data is made for the function and if it gets edited within the function
then it will not effect the original value and will need to be returned. However, if the data is passed by reference then
the data within the function is pointing to the original data and any changes made to the data within it will effect the
original copy of the data outside of the function. This means the data would not need a return value.

2. 
25 - GetRank - RankNo - Passed by value
55 - GetSuit - SuitNo - Passed by value
139 - score - Passed by value
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
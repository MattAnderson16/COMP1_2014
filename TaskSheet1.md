#Task Sheet 1

##Task 3
a)
1. GetPlayerName()
2. Using a while loop that exits once the player has entered their name
3. The extra variable is GotName and it will be a boolean value

FUNCTION GetPlayerName():
    &nbsp;&nbsp;&nbsp;GotName = FALSE  
    &nbsp;&nbsp;&nbsp;WHILE NOT GotName DO  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OUTPUT " "  
	&nbsp;&nbsp;&nbsp;PlayerName <- INPUT "Please enter your name: "  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OUTPUT " "  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IF PlayerName = " " THEN  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OUTPUT "You need to input a name!"  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ELSE  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GotName = TRUE  
    &nbsp;&nbsp;&nbsp;RETURN GotName  
END FUNCTION

b)
1. UpdateRecentScores(RecentScores, Score)

##Task 5
1. datetime
2. TRecentScore(), ResetRecentScores(), DisplayRecentScores(), UpdateRecentScores()
3. datetime.datetime.strptime(date,"%d/%m/%y")
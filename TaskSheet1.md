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
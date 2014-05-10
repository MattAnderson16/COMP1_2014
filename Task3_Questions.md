#Task Sheet 3 Questions

##Task 11
1. In the main program
2. IsNextCardHigher(LastCard, NextCard) and PlayGame(Deck, RecentScores)
3. a true/false value for if the cards are the same
4. a line for the option to choose whether cards with the same value will end the game if the user guesses
higher will need to be added to the DisplayOptions() function and and the validation in GetOptionChoice()
will need to have the new choice added

###Pseudocode

	FUNCTION SetSameScore(EndIfSame:Boolean):
		yn <- INPUT "Do you want cards of the same value as the previous one to end the game? "
		CALL lower(yn)
		WHILE yn NOT IN ["y","yes","n","no"] DO
			OUTPUT "Please enter a valid response")
			yn <- INPUT "Do you want cards of the same value as the previous one to end the game? "
		END WHILE
		yn <- yn[1]
		IF yn = 'y' THEN
			EndIfSame <- TRUE
		ELSE IF yn - 'n' THEN
			EndIfSame <- FALSE
		END IF
	END FUNCTION
#Task Sheet 2 questions

##Task 6
1. A good place to keep track of whether the ace is high or low would be in a record
2. DisplayMenu()
3.IsNextCardHigher(LastCard, NextCard)

###Pseudocode
	FUNCTION DisplayOptions()
		Ace <- Options.Ace
		OUTPUT ''
		OUTPUT 'OPTIONS'
		OUTPUT ''
		OUTPUT '1. Ace: ', Ace
		OUTPUT ''
		OUTPUT 'Select an option or press q to quit: '
	END FUNCTION
	
	FUNCTION GetOptionChoice()
		Choice <- INPUT ''
		Choice <- CALL lower(Choice)
		OUTPUT ''
		Choice <- Choice[1]
		RETURN Choice
	END FUNCTION
	
	FUNCTION SetOptions(OptionChoice):
		IF OptionChoice = '1' THEN
			CALL SetAceHighOrLow()
		END IF
	END FUNCTION
	
	FUNCTION SetAceHighOrLow():
		OUTPUT ''
		OUTPUT 'Would you like the ace to be high or low? '
		Finished = False
		WHILE NOT Finished DO
			Choice <- INPUT ''
			OUTPUT ''
			Choice <- CALL lower(Choice)
			Choice <- Choice[1]
			IF Choice = 'h' THEN
				Options.Ace <- 'high'
				Finished = TRUE
			ELSE IF Choice <- 'l' THEN
				Options.Ace <- 'low'
				Finished = TRUE
			ELSE
				OUTPUT 'Please input a valid choice'
			END IF
		END WHILE
	END FUNCTION
				
###Testing

|Test Number|Test Description|Test Data|Type|Expected Result|Actual Result|
|-----------|----------------|---------|----|---------------|-------------|
|1| |q |normal |the program will exit the options menu | |
# SlackDeleteFiles

Objective: Delete your slack files that are in the last X sent in the chosen channel.

Use:

	1. Create a token in [Legacy Tokens](https://api.slack.com/custom-integrations/legacy-tokens);
	2. Copy the token to slackDeleteMessages.py:7;
	3. Change the variable count (slackDeleteMessages.py:8) to be the desired value of X (default = 1000);
  	4. Change the variable ts_to (slackDeleteMessages.py:9) to be how the end of the interval since the start of the channel to ts_to. The variable is in seconds. So 60*60*24 (default value) means no files sent in the last 24 hours will be deleted. Only older ones.
	5. Run the script
	6. Input the index of the channel where the messages you want to delete are (from the printed list)

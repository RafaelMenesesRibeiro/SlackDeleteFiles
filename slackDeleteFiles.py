import sys
import requests
import time
import json

#TO BE FILLED BY THE USER
token = '' #Insert your user token here. Get it from: https://api.slack.com/custom-integrations/legacy-tokens
count = 1000 #Number of messages to get (min = 1, max = 1000)
ts_to = 60*60*24

#-------------------------------------------------------------------------------
userID = json.loads(requests.get('https://slack.com/api/auth.test', {'token': token}).text)['user_id']

def channelGetID():
	params = {
		'token': token,
		'exclude_archived': True,
		'exclude_members': True
	}
	response = requests.get('https://slack.com/api/channels.list', params=params)
	respT = json.loads(response.text)
	channels  = respT['channels']
	channelsMember = []
	for i in range(len(channels)):
		if channels[i]['is_member']:
			channelsMember.append(channels[i])
	for i in range(len(channelsMember)):
		print(i, ' : ', channelsMember[i]['name'])
	channelIndex = int(input('\nWhere are the messages you want to delete. (Input the index of the channel)\t'))
	if channelIndex < 0 or channelIndex > len(channelsMember):
		sys.exit('ABORTED - Invalid input - the channel index needs to be on the list presented above')
	return channelsMember[channelIndex]['id']

def filesList(channelCode):
	params = {
		'token': token,
		'channel': channelCode,
		'count': count,
		'ts_to': ts_to
	}
	response = requests.get('https://slack.com/api/files.list', params=params)
	return json.loads(response.text)['files']

def filesDelete(channelCode, files):
	c = d = 0
	for file in files:
		c += 1
		if file['user'] == userID:
			params = {
				'token': token,
				'file': file['id']
			}	
			response = requests.get('https://slack.com/api/files.delete', params=params)
			respT = json.loads(response.text)
			d = d+1 if (respT['ok'] == True) else d
			print('file #', c, ' of ', count, '. Deleted ', d, ' -> ', file['title'])
			time.sleep(1) #Used so slack doens't return 'ratelimited' ('https://api.slack.com/docs/rate-limits')
		else:
			print('file #', c, ' of ', count, '. Deleted ', d)



count = 1 if (count > 1000 or count < 1) else count
channelID = channelGetID()
files = filesList(channelID)
filesDelete(channelID, files)
print('\nDone.')

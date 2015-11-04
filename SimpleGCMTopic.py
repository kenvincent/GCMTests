#!/usr/bin/env python
#
#  A very simple script to test sending GCM topic messages.
#
#  Learn about Google Cloud Messaging here: https://developers.google.com/cloud-messaging/
#  Set up your API and get an API key here: https://console.developers.google.com/
#
#  Parameters:
#		APIkey -- Your API key
#		The JSON message that you want send to your device.
#
#  Usage: SimpleGCMTopic.py <APIkey> "{\"json\":1}"
#
#  Note: Topic messages do not need a Sender ID.  They do however require that an app has
#  subscribed to a topic. In this example the topic is 'update'.  See, the GCM link above.
#
import sys
import requests

if len(sys.argv) != 3:
	print 'Usage: SimpleGCMTopic.py API_key "{\"json\":1}"'
else:
	headers = {'Authorization': 'key=%s' % sys.argv[1]}
	headers['Content-Type'] = 'application/json'
	data = '{"to":"/topics/update","collapse_key":"update","delay_while_idle":true,"data":{"message":%s}}' % sys.argv[2]
	response = requests.post('https://gcm-http.googleapis.com/gcm/send',data=data,headers=headers)
	print
	print "Headers:"
	print headers
	print
	print "Data: "
	print data
	print
	print "Server Response: "
	print response.text
	
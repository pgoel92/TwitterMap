from tweepy import Stream
from tweepy import OAuthHandler

from tweepy.streaming import StreamListener
import time
import json
ckey = 'xtzA5ibfr0QIxWBkoOOwhMeGE'
csecret = 'KYcUcYhkHJdnolHvpFzhkPYd7bWHDKsNyME6E1frL3295O0Zih'
atoken = '603464840-T9aZZ22qqEzP8VSIRDqTvVPjAjAGh1kjqx1hierW'
asecret = 'qOO3m8ffTdeBsjqJ3Feo25EatY0vy9wxuSi3Rd6EW7cGL'
count = 1
class listener(StreamListener):

	def on_data(self, data):
		try:
			#txt = data.split(',"text":"')[1].split('","source')[0]
			#loc = data.split(',"location":"')[1].split('","url')[0]
			js = json.loads(data)
			print js['id']
			print js['text']
			print js['user']['geo_enabled']
			print js['user']['location']
			print js['user']['created_at']
			print js['geo']
			print js['place']
			'''
			if loc == '':
				loc = 'null'
			
			geoEnabled = data.find('"coordinates":null,"place"')
			coordinates = geoEnabled

			if geoEnabled != -1:
				coordinates = 'null'
			else:
				print '##############################'
				stuff = data.split('},"coordinates":{')[1].split('},"place"')[0]
				coordinates = stuff.split('"coordinates":')[1]
			saveThis = ''
			tracks = ["modi","nyc","ebola","india"]
			for word in tracks:
				if txt.lower().find(word) != -1:
					saveThis = saveThis + word
			saveThis = saveThis+':::'+txt+':::'+loc+':::'+str(coordinates)+'\n'
			#print saveThis
			'''
			saveFile = open('twitDB.csv','a')
			saveFile.write(data);
			saveFile.close();
			return True
		except BaseException, e:
			print 'failed on data', str(e)
			time.sleep(10)
	def on_error(self, status):
		print "Error"+status
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["modi","india","nyc","ebola"])

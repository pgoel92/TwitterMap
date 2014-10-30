import json
from csv import writer
import pymongo

# Connection to Mongo DB
try:
	conn=pymongo.MongoClient()
	print "Connected successfully!!!"
except pymongo.errors.ConnectionFailure, e:
	print "Could not connect to MongoDB: %s" % e
conn
db = conn.tweeted
collection = db.tweetCollection

tweets = []

for line in open('data/twitDB.csv'):
	try: 
		tweets.append(json.loads(line))
	except:
		pass

print len(tweets)
keys = [];
texts = [];
tracks = ["modi","nyc","ebola","india"]
for tweet in tweets:
	data = {}
	data['created_at'] = tweet['created_at']
	data['text'] = tweet['text']
	data['location'] = tweet['user']['location'] if tweet['user']['location'] else 'null'
	data['coordinates'] = str(tweet['geo']['coordinates']) if tweet['geo'] else 'null'
	data['id'] = tweet['id_str']	
	
	for word in tracks:
		if tweet['text'].lower().find(word) != -1:
			data['keyword'] = word
			break

	collection.insert(data)
'''
out = open('tweets.csv','w')
print >> out, 'ids, keys, times, location, lats, lons, texts' 
rows = zip(ids, keys, times, location, lats, lons, texts) 
csv = writer(out  )
for row in rows:
	values = [(value.encode('utf8') if hasattr(value, 'encode') else value) for value in row]
	csv.writerow(values)
out.close()
'''


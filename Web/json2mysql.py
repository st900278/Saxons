import MySQLdb
import json

db = MySQLdb.connect(host="localhost", user="root", passwd="creativekit", db="saxons")
cursor = db.cursor()

data = open("static/pack/dictionary.json", "r").read()
jsondata = json.loads(data)

for x in jsondata:
	#print x + ":" + jsondata[x]
	try:
		cursor.execute("""INSERT INTO engdict (word, description) VALUES (%s,%s)""",(x,jsondata[x]))
		#print "yy"
		db.commit()
	except:
		db.rollback()
db.close()
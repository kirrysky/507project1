import requests
import json
import webbrowser

CACHE_DICTION2=[]

def FetchItunesJson(query="Hey+Jude",number=0):
	base_itunes_url="https://itunes.apple.com/search?"
	query=query.replace(" ","+")
	base_itunes_url+= "term=" + query
	base_itunes_url+= "&limit=" + str(number)
	json_string = requests.get(base_itunes_url).text
	results_list = json.loads(json_string)['results']
	medias = []
	media=[]
	song=[]
	movie=[]
	for r in results_list:
		if r.__contains__('kind'):
			if "movie" in r['kind']:
				m = Movie(json_dict=r)
				media.append(r)
			elif "song" in r['kind']:
				m = Song(json_dict=r)
				song.append(r)
			else:
				m = Media(json_dict=r)
				media.append(r)
		else:
			m = Media(json_dict=r)
			media.append(r)
		medias.append(m)
	global CACHE_DICTION2
	CACHE_DICTION2 = song+movie+media
	return medias

CACHE_FRAME = 'sample_json.json'
try:
	cache_file =  open(CACHE_FRAME,'r')
	cache_contents = cache_file.read()
	CACHE_DICTION = json.loads(cache_contents)
	cache_file.close()
except:
	CACHE_DICTION = {}

class Media:

	def __init__(self, title="No Title", author="No Author", release_year="Unknown", json_dict=None):
		if json_dict is None:
			self.title = title
			self.author = author
			self.release_year = release_year
		else:
			self.process_json(json_dict)

	def process_json(self,json_dict):
		if json_dict.__contains__('trackName'):
			self.title = json_dict['trackName']
		elif json_dict.__contains__('collectionCensoredName'):
			self.title = json_dict['collectionCensoredName']
		else:
			self.title = "No Title"
		if  json_dict.__contains__('artistName'):
			self.author = json_dict['artistName']
		else:
			self.author = "No Author"
		if json_dict.__contains__('releaseDate'):
			self.release_year = json_dict['releaseDate'][0:4]
		else:
			self.release_year = "Unknown"


	def __str__(self):
		state = self.title + " by "
		state+= self.author + "("
		state+= self.release_year + ")"
		return state

	def __len__(self):
		return 0


## Other classes, functions, etc. should go here
class Song(Media):

	def __init__(self, title="No Title", author="No Author", release_year="Unknown", album="Unknown", genre="Unknown", track_length=0 ,json_dict=None):
		if json_dict is None:
			super().__init__(title,author,release_year)
			self.album = album
			self.genre = genre
			self.track_length = track_length
		else:
			self.process_json(json_dict)

	def process_json(self,json_dict):
		super().process_json(json_dict)
		if json_dict.__contains__('trackCensoredName'):
			self.album = json_dict['trackCensoredName']
		else:
			self.album = "Unknown"

		if json_dict.__contains__('primaryGenreName'):
			self.genre = json_dict['primaryGenreName']
		else:
			self.genre = "Unknown"

		if json_dict.__contains__('trackTimeMillis'):
			self.track_length = int(json_dict['trackTimeMillis']/1000)
		else:
			self.track_length = 0

	def __str__(self):
		state = self.title + " by "
		state+= self.author + "("
		state+= self.release_year + ")["
		state+= self.genre + "]"
		return state

	def __len__(self):
		return self.track_length

class Movie(Media):

	def __init__(self, title="No Title", author="No Author", release_year="Unknown", rating="Unknown", movie_length=0, json_dict=None):
		if json_dict is None:
			super().__init__(title,author,release_year)
			self.rating = rating
			self.movie_length = movie_length
		else:
			self.process_json(json_dict)

	def process_json(self,json_dict):
		super().process_json(json_dict)
		if json_dict.__contains__('contentAdvisoryRating'):
			self.rating = json_dict['contentAdvisoryRating']
		else:
			self.rating = "Unknown"

		if json_dict.__contains__('trackTimeMillis'):
			self.movie_length = int(json_dict['trackTimeMillis']/60000)
		else:
			self.movie_length = 0


	def __str__(self):
		state = self.title + " by "
		state+= self.author + "("
		state+= self.release_year + ")["
		state+= self.rating + "]"
		return state

	def __len__(self):
		return self.movie_length

if __name__ == "__main__":
	# your control code for Part 4 (interactive search) should go here
	term = input('Enter a search term, or "exit" to quit:')
	while (term!="exit"):
		medias=FetchItunesJson(term)
		media=[]
		song=[]
		movie=[]
		for m in medias:
			if isinstance(m,Song):
				song.append(m)
			elif isinstance(m,Movie):
				movie.append(m)
			else:
				media.append(m)
		print ('\nSONGS')
		n=0
		for s in song:
			n+=1
			print(str(n),end=" ")
			print (s)
		print ('\nMOVIES')
		for m in movie:
			n+=1
			print(str(n),end=" ")
			print (m)
		print ('\nOTHER MEDIA')
		for m in movie:
			n+=1
			print(str(n),end=" ")
			print (m)

		second_term = input('a number for more info, or another search term, or exit:')
		while second_term.isdigit():
			print('Launching')
			n=int(second_term)-1
			result = CACHE_DICTION2[n]
			webbrowser.open_new(result['trackViewUrl'])
			print(result['trackViewUrl'])
			print('in web browser...')
			second_term = input('a number for more info, or another search term, or exit:')
		term=second_term
	print ("Bye")

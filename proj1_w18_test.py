import unittest
import proj1_w18 as proj1

class TestMedia(unittest.TestCase):

    def testConstructor(self):
        m1 = proj1.Media()
        m2 = proj1.Media("1999", "Prince")
        m3 = proj1.Media("Bridget Jones's Diary (Unabridged)","Helen Fielding","2012")

        self.assertIsInstance(m1,proj1.Media)
        self.assertIsInstance(m2,proj1.Media)
        self.assertIsInstance(m3,proj1.Media)
        self.assertEqual(m1.title, "No Title")
        self.assertEqual(m1.author, "No Author")
        self.assertEqual(m1.release_year, "Unknown")
        self.assertEqual(m2.title, "1999")
        self.assertEqual(m2.author, "Prince")
        self.assertEqual(m2.release_year, "Unknown")
        self.assertEqual(m3.title, "Bridget Jones's Diary (Unabridged)")
        self.assertEqual(m3.author, "Helen Fielding")
        self.assertEqual(m3.release_year, "2012")

    def testFunction(self):
        m1 = proj1.Media()
        m2 = proj1.Media("1999", "Prince")
        m3 = proj1.Media("Bridget Jones's Diary (Unabridged)","Helen Fielding","2012")

        self.assertEqual(m1.__str__(), "No Title by No Author(Unknown)")
        self.assertEqual(m2.__str__(), "1999 by Prince(Unknown)")
        self.assertEqual(m3.__str__(), "Bridget Jones's Diary (Unabridged) by Helen Fielding(2012)")
        self.assertEqual(m1.__len__(), 0)
        self.assertEqual(m2.__len__(), 0)
        self.assertEqual(m3.__len__(), 0)

class TestSong(unittest.TestCase):
    def testConstructor(self):
        m1 = proj1.Song()
        m2 = proj1.Song("Hey Jude", "The Beatles","1968","Hey Jude","Rock",240)

        self.assertIsInstance(m1,proj1.Song)
        self.assertIsInstance(m2,proj1.Song)
        self.assertEqual(m1.title, "No Title")
        self.assertEqual(m1.author, "No Author")
        self.assertEqual(m1.release_year, "Unknown")
        self.assertEqual(m1.album, "Unknown")
        self.assertEqual(m1.genre, "Unknown")
        self.assertEqual(m1.track_length, 0)
        self.assertEqual(m2.title, "Hey Jude")
        self.assertEqual(m2.author, "The Beatles")
        self.assertEqual(m2.release_year, "1968")
        self.assertEqual(m2.album, "Hey Jude")
        self.assertEqual(m2.genre, "Rock")
        self.assertEqual(m2.track_length, 240)

    def testFunction(self):
        m1 = proj1.Song()
        m2 = proj1.Song("Hey Jude", "The Beatles","1968","Hey Jude","Rock",240)

        self.assertEqual(m1.__str__(), "No Title by No Author(Unknown)[Unknown]")
        self.assertEqual(m2.__str__(), "Hey Jude by The Beatles(1968)[Rock]")
        self.assertEqual(m1.__len__(), 0)
        self.assertEqual(m2.__len__(), 240)

class TestMovie(unittest.TestCase):
    def testConstructor(self):
        m1 = proj1.Movie()
        m2 = proj1.Movie("Jaws", "Steven Speilberg","1975","PG",120)
        #Jaws by Steven Speilberg (1975) [PG]

        self.assertIsInstance(m1,proj1.Movie)
        self.assertIsInstance(m2,proj1.Movie)
        self.assertEqual(m1.title, "No Title")
        self.assertEqual(m1.author, "No Author")
        self.assertEqual(m1.release_year, "Unknown")
        self.assertEqual(m1.rating, "Unknown")
        self.assertEqual(m1.movie_length, 0)
        self.assertEqual(m2.title, "Jaws")
        self.assertEqual(m2.author, "Steven Speilberg")
        self.assertEqual(m2.release_year, "1975")
        self.assertEqual(m2.rating, "PG")
        self.assertEqual(m2.movie_length, 120)


    def testFunction(self):
        m1 = proj1.Movie()
        m2 = proj1.Movie("Jaws", "Steven Speilberg","1975","PG",120)
        #Jaws by Steven Speilberg (1975) [PG]

        self.assertEqual(m1.__str__(), "No Title by No Author(Unknown)[Unknown]")
        self.assertEqual(m2.__str__(), "Jaws by Steven Speilberg(1975)[PG]")
        self.assertEqual(m1.__len__(), 0)
        self.assertEqual(m2.__len__(), 120)


class TestJsonToObject(unittest.TestCase):

    def testConstructor(self):
        movie = proj1.Movie(json_dict=proj1.CACHE_DICTION[0])
        song = proj1.Song(json_dict=proj1.CACHE_DICTION[1])
        media = proj1.Media(json_dict=proj1.CACHE_DICTION[2])

        self.assertIsInstance(movie,proj1.Movie)
        self.assertIsInstance(song,proj1.Song)
        self.assertIsInstance(media,proj1.Media)
        self.assertEqual(movie.title, "Jaws")
        self.assertEqual(movie.author, "Steven Spielberg")
        self.assertEqual(movie.release_year, "1975")
        self.assertEqual(movie.rating, "PG")
        self.assertEqual(movie.movie_length, 124)

        self.assertEqual(song.title, "Hey Jude")
        self.assertEqual(song.author, "The Beatles")
        self.assertEqual(song.release_year, "1968")
        self.assertEqual(song.album, "Hey Jude")
        self.assertEqual(song.genre, "Rock")
        self.assertEqual(song.track_length, 431)

        self.assertEqual(media.title, "Bridget Jones's Diary (Unabridged)")
        self.assertEqual(media.author, "Helen Fielding")
        self.assertEqual(media.release_year, "2012")

    def testFunction(self):
        movie = proj1.Movie(json_dict=proj1.CACHE_DICTION[0])
        song = proj1.Song(json_dict=proj1.CACHE_DICTION[1])
        media = proj1.Media(json_dict=proj1.CACHE_DICTION[2])

        self.assertEqual(movie.__str__(), "Jaws by Steven Spielberg(1975)[PG]")
        self.assertEqual(movie.__len__(), 124)
        self.assertEqual(song.__str__(), "Hey Jude by The Beatles(1968)[Rock]")
        self.assertEqual(song.__len__(), 431)
        self.assertEqual(media.__str__(), "Bridget Jones's Diary (Unabridged) by Helen Fielding(2012)")
        self.assertEqual(media.__len__(), 0)

class TestFetchItunsJson(unittest.TestCase):

    def testConstructor(self):
        medias1 = proj1.FetchItunesJson()
        medias2 = proj1.FetchItunesJson(query="Hey+Jude",number=10)
        self.assertIsInstance(medias1,list)
        self.assertIsInstance(medias2,list)
        self.assertIsInstance(medias1[0],proj1.Media)
        self.assertIsInstance(medias2[0],proj1.Media)

    def testRange(self):
        medias1 = proj1.FetchItunesJson()
        medias2 = proj1.FetchItunesJson(query="Hey+Jude",number=10)
        self.assertNotEqual(len(medias1),0)
        self.assertEqual(len(medias2),10)

    def testQuery(self):
        medias_baby = proj1.FetchItunesJson("baby")
        self.assertIsInstance(medias_baby,list)
        self.assertIsInstance(medias_baby[0],proj1.Media)
        medias_helter_skelter = proj1.FetchItunesJson("Helter Skelter")
        self.assertIsInstance(medias_helter_skelter,list)
        self.assertIsInstance(medias_helter_skelter[0],proj1.Media)
        medias_nonsence = proj1.FetchItunesJson("&@#!$")
        self.assertEqual(len(medias_nonsence),0)
        medias_blank = proj1.FetchItunesJson("")
        self.assertEqual(len(medias_blank),0)




unittest.main()

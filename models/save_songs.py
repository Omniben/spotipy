from .song import Song
from .album import Album
from .playlist import Playlist

Blackpink = {
	"The Album": [
		Song("How You Like That","Blackpink", 182),
		Song("Lovesick Girls", "Blackpink", 194),
		Song("Pretty Savage", "Blackpink", 201),
		Song("Bet You Wanna", "Blackpink", 161, ft="Cardi B"),
		Song("You Never Know", "Blackpink", 231),
		Song("Love To Hate Me", "Blackpink", 171),
		Song("Crazy Over You", "Blackpink", 163),
		Song("Ice Cream", "Blackpink", 177, ft="Selena Gomez"),
	]
}

ImagineDragons = {
	"Mercury - Acts 1 & 2" : [
	Song("Bones", "Imagine Dragons", 165),
	Song("Sharks", "Imagine Dragons", 190),
	Song("Enemy", "Imagine Dragons", 173),
	Song("My life", "Imagine Dragons", 224),
	],
	"Evolve" : [
	Song("Thunder", "Imagine Dragons", 187),
	Song("Believer", "Imagine Dragons", 204),
	Song("Whatever It Takes", "Imagine Dragons", 201),
	Song("Walking The Wire", "Imagine Dragons", 232),
	]
}


mix_songs = Blackpink["The Album"][0:4] + ImagineDragons["Mercury - Acts 1 & 2"][0:3] + ImagineDragons["Evolve"][0:2]


mix_1 = Playlist("Mi mix", songs=mix_songs)

the_album = Album("The Album", Blackpink["The Album"])


#"Mercury - Acts 1 & 2", ft="JID"
#
#"Mercury - Acts 1 & 2"
#"Evolve"
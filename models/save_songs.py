from .song import Song
from .album import Album
from .playlist import Playlist
import random

Blackpink = {
	"The Album": [
		Song("How You Like That","Blackpink", 182, 660328902),
		Song("Lovesick Girls", "Blackpink", 194, 357883028),
		Song("Pretty Savage", "Blackpink", 201, 259153208),
		Song("Bet You Wanna", "Blackpink", 161, 145685596, ft="Cardi B"),
		Song("You Never Know", "Blackpink", 231, 110837934),
		Song("Love To Hate Me", "Blackpink", 171, 154854579),
		Song("Crazy Over You", "Blackpink", 163, 134076376),
		Song("Ice Cream", "Blackpink", 177, 437138505, ft="Selena Gomez"),
	]
}

ImagineDragons = {
	"Mercury - Acts 1 & 2" : [
	Song("Bones", "Imagine Dragons", 165, 195275898),
	Song("Sharks", "Imagine Dragons", 190, 41155538),
	Song("Enemy", "Imagine Dragons", 173, 832044484, ft="JID"),
	Song("My life", "Imagine Dragons", 224, 36686765),
	],
	"Evolve" : [
	Song("Thunder", "Imagine Dragons", 187, 1783573212),
	Song("Believer", "Imagine Dragons", 204, 2181171171),
	Song("Whatever It Takes", "Imagine Dragons", 201, 215933112),
	Song("Walking The Wire", "Imagine Dragons", 232, 215933112),
	]
}


mix_songs = random.sample(Blackpink["The Album"], 4) + random.sample(ImagineDragons["Mercury - Acts 1 & 2"], 2) + random.sample(ImagineDragons["Evolve"], 2)


mix_1 = Playlist.create_mix(mix_songs)

the_album = Album("The Album", Blackpink["The Album"])
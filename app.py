from models.song import Song
from models.album import Album
from models.playlist import Playlist
from models.user import User
from models.user_premium import UserPremium
from models.user_free import UserFree
from models.save_songs import the_album, ImagineDragons, mix_1





'''Creación de una canción'''

song_prueba = Song("i'll see you again", "League of Legends, suteki", 214, 597351)



''' Creación de 1 usuario free y 1 usuario premium'''
free = UserFree('Juan', '10-10-2000', 'gratis', 'qwerty123')
bj = UserPremium('Benjamin', '13-01-2002', 'BJ', '1234567a')


'''_________Prueba del metodo para dar likes de la clase User_________'''

print("_____Likes de bj_____")

bj.give_like(ImagineDragons["Mercury - Acts 1 & 2"][0])
bj.give_like(the_album.songs[0])
bj.give_like(ImagineDragons["Mercury - Acts 1 & 2"][1])
bj.give_like(mix_1.songs[3])
bj.give_like(the_album.songs[2])
bj.give_like(mix_1)
print("\n\n")


print("_____Likes de free_____")
free.give_like(the_album.songs[3])
free.give_like(ImagineDragons["Mercury - Acts 1 & 2"][2])
free.give_like(song_prueba)
free.give_like(the_album)
print("\n\n")



'''______Reproduciendo canciones____'''

print('____________Reproduciendo desde el usuario premium____________')
input('')

bj.play(ImagineDragons["Mercury - Acts 1 & 2"][0])
print("")
bj.play(bj.liked_songs)
bj.play(the_album)
print("\n\n")


print('____________Reproduciendo desde el usuario free____________')
input('')

free.play(free.liked_songs)
print("")
free.play(the_album)
print("")
free.play(ImagineDragons["Mercury - Acts 1 & 2"][1])
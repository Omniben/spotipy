import time

#Usaremos el "time" para imprimir de una forma más legible, ya que la duracion la ingresamos como un entero que seria igual a los segundos


#Esta clase es parecida a la playlist pero con un comportamiento distinto ya que desde un principio pide las canciones y no tenemos metodos para agregar o quitar canciones ya que es un album ya completo

class Album:

	def __init__(self, name, songs):
		self.name = name
		self.songs = songs
		self.performer = []
		self.duration = 0
		

		#Aqui usamos las canciones que le ingresamos al album para tener la duracion de este sumando la duracion de cada cancion, agregamos los artistas de cada cancion a una lista y le damos el nombre del album a un atributo en las canciones

		for s in songs:
			self.duration += s.duration
			s.name_album = self.name
			if s.performer not in self.performer:
				self.performer.append(s.performer)


	def __str__(self):
		return f'{self.name} interpretado por {", ".join(self.performer)}'



	def show_album(self):
		duration = time.strftime("%M:%S",time.gmtime(self.duration))

		print(self.name)
		print(f'interpretado por {", ".join(self.performer)}')
		print(f'{len(self.songs)} songs,{duration}\n')
		for index,song in enumerate(self.songs, start=1):
			print(f"{index}  {song.read()}")
#Esta clase es parecida a la clase Playlist pero con un comportamiento distinto ya que desde un principio pide las canciones y no tenemos metodos para agregar o quitar canciones ya que es un album ya completo

import time

class Album:

	def __init__(self, name, songs):
		"""Dentro de este __init__ usaremos la lista de canciones que ingresemos para tener la duracion del album, que seria la suma de la duracion de las canciones.
		A su vez le daremos le damos un atributo a las canciones en el que le damos el nombre del album.
		Y para finalizar tomamos los artistas de cada canción y los agregamos a una lista del album, solo si no estan ya en la lista."""
		self.name = name
		self.songs = songs
		self.performer = []
		self.duration = 0
		

		for s in songs:
			self.duration += s.duration
			s.name_album = self.name
			if s.performer not in self.performer:
				self.performer.append(s.performer)


	def __str__(self):
		return f'{self.name} interpretado por {", ".join(self.performer)}'



	def show_album(self):
		"""Función para imprimir la información del album de forma ordenada.
		Usamos el modulo time para imprimir la duracion de una for más legible"""
		duration = time.strftime("%M:%S",time.gmtime(self.duration))

		print(self.name)
		print(f'interpretado por {", ".join(self.performer)}')
		print(f'{len(self.songs)} canciónes, {duration}\n')
		for index,song in enumerate(self.songs, start=1):
			print(f"{index}  {song.read()}")
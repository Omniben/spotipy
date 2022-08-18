class Playlist:
	def __init__(self, name, creator="Spotipy", description=None, **kwargs):
		self.name = name
		self.creator = creator
		self.description = description
		self.songs = []



		for key,value in kwargs.items():
			setattr(self, key, value)


	def __str__(self):
		return f'"{self.name}" creada por {self.creator}'

	def __repr__(self):
		return f'"{self.name}" creada por {self.creator}'




	def add_song(self, song):
		self.songs.append(song)


#Usamos un menu con indice para darle al usuarios las opciones para borrar

	def del_song(self):
		if self.songs:
			for index,song in enumerate(self.songs, start=1):
				print(f'{index}.→ {song}')

			while True:
				try:
					delete = int(input('\nIngresa el número de la canción que quieras borrar o presiona "0" para cancelar: '))

				except ValueError:
					print('Ingresa números')
					continue

					if delete == 0:
						break
				
					elif delete-1 < len(self.songs):
						self.songs[delete-1]
						break

					else:
						print('Número invalido')
						continue
		else:
			print('La playlist está vacia')


	def show_playlist(self):
		if self.description:
			print(self.name)
			print(self.description)
			print(f"\nCreada por {self.creator}\n")
			for index,song in enumerate(self.songs, start=1):
				print(f"{index}  {song.read()}")
		else:
			print(self.name)
			print(f"\nCreada por {self.creator}\n")
			for index,song in enumerate(self.songs, start=1):
				print(f"{index}  {song.read()}")
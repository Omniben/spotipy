import time

class Album:

	def __init__(self, name, songs):
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
		duration = time.strftime("%M:%S",time.gmtime(self.duration))

		print(self.name)
		print(f'interpretado por {", ".join(self.performer)}')
		print(f'{len(self.songs)} songs,{duration}\n')
		for index,song in enumerate(self.songs, start=1):
			print(f"{index}  {song.read()}")
import time


class Song:
	def __init__(self, name, performer, duration, plays=0, **kwargs):
		self.name = name
		self.performer = performer	
		self.duration = duration
		self.plays = plays
		self.name_album = None

		for key,value in kwargs.items():
			setattr(self, key, value)


	def __str__(self):
		return f'{self.name} de {self.performer}'

	def __repr__(self):
		return f'{self.name} de {self.performer}'


	def get_plays(self):
		return f'Plays: {self.plays}'

	def read(self):
		duration = time.strftime("%M:%S",time.gmtime(self.duration))
		if self.plays > 100:
			if self.name_album:
				return f"{self.name}   {self.performer}   {self.name_album}   {self.plays}   {duration}"

			else:
				return f"{self.name}   {self.performer}   {self.plays}   {duration}"
		else:
			if self.name_album:
				return f"{self.name}   {self.performer}   {self.name_album}   {duration}"

			else:
				return f"{self.name}   {self.performer}   {duration}"			
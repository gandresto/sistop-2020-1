class DirectoryEntry():
	"""docstring for Dir"""
	def __init__(self, name, size, cluster, creation, last_modif, non_used_space, dir_entry_id):
		self.name = name
		self.size = size
		self.cluster = cluster
		self.creation = creation
		self.last_modif = last_modif
		self.non_used_space = non_used_space
		self.dir_entry_id = dir_entry_id

	def update_cluster(self, cluster):
		self.cluster = ('%05d' % cluster).encode()
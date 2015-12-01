import json
import os
import signal
import sys

class Cache(object):
	def __init__(self, filename):
		self._filename = filename
		self._cache = {}
		if os.path.isfile(filename):
			with open(filename, 'r') as f:
				self._cache = json.load(f)
		signal.signal(signal.SIGINT, lambda signum, frame: self._persist())

	def contains(self, key):
		return key in self._cache

	def get(self, key):
		if key in self._cache:
			return self._cache[key]
		return None

	def put(self, key, value):
		self._cache[key] = value

	def _persist(self):
		with open(self._filename, 'w') as f:
			json.dump(self._cache, f)
		sys.exit(1)
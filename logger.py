import hashlib
import os

class KeptItemsHandler:
    'A class that takes care of desktop items that needs to be kept over time'

    def __init__(self):
        self.kept = list()
        self.cwd = os.getcwd()
        with open('kept.dc', 'r') as f:
            for line in f:
                self.kept.append(line)

    def save_kept_items(self):
        os.chdir(self.cwd)
        with open('kept.dc', 'w') as f:
            f.write('\n'.join(self.kept))

    def add_item(self, desktop_item):
        self.kept.append(self.create_hash(desktop_item.filename))

    def create_hash(self, string):
        return hashlib.md5(string).hexdigest()

    def contains(self, desktop_item):
        return self.create_hash(desktop_item.filename) in self.kept

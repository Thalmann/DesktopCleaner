import hashlib

class Logger:
    'A class that takes care of desktop items that needs to be kept over time'

    def __init__(self):
        kept = list()
        with open('kept.dc', 'r') as f:
            for line in f:
                kept.append(line)

    def save_kept_items():
        with open('kept.dc', 'w') as f:
            f.write('\n'.join(kept))

    def add_item(desktop_item):
        kept.append(create_hash(desktop_item.filename))

    def create_hash(string):
        return hashlib.md5(string).hexdigest()

    def contains(desktop_item):
        return create_hash(desktop_item.filename) in kept

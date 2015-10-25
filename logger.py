import hashlib

kept = list()

def load_kept_items():
    with open('kept.dc', 'r') as f:
        for line in f:
            kept.append(line)
    return kept

def save_kept_items():
    with open('kept.dc', 'w') as f:
        f.write('\n'.join(kept))

def add_item(desktop_item):
    kept.append(create_hash(desktop_item.filename))

def create_hash(string):
    return hashlib.md5(string).hexdigest()

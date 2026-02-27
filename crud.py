items = []

def create(item):
    items.append(item)

def read():
    return items

def update(index, new_item):
    if 0 <= index < len(items):
        items[index] = new_item
        return True
    return False

def delete(index):
    if 0 <= index < len(items):
        items.pop(index)
        return True
    return False
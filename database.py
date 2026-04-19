
shopping_items = []

def get_items():
    return shopping_items

def add_item(item):
    shopping_items.append(item)

def remove_item(item):
    if item in shopping_items:
        shopping_items.remove(item)
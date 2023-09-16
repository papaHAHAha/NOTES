import json
import  os
from datetime import datetime

notes = []
path = 'notes.json'

import json
import os
from datetime import datetime

notes = []
path = 'notes.json'

def load_notes():
    if os.path.exists(path):
        with open(path, 'r') as file:
            data = json.load(file)
            notes.clear()
            notes.extend(sorted(data, key=lambda x: datetime.strptime(x['created_at'], "%Y-%m-%d %H:%M:%S"), reverse=True))
    return notes


def save_notes():
    with open(path, 'w') as file:
        json.dump(notes, file, indent=4)


def create_note(title, body):
    note_id = len(notes) + 1
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_at = created_at
    new_note = {
        'note_id': note_id,
        'title': title,
        'body': body,
        'created_at': created_at,
        'updated_at': updated_at,
    }
    notes.append(new_note)
    return notes

def edit_note(index: str, new_title, new_body):
    index = int(index)
    for note in notes:
        if note['note_id'] == index:
            note['title'] = new_title
            note['body'] = new_body
            note['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return True
    return False

def view_selected_note(index: str, notes):
    index = int(index)
    for note in notes:
        if note['note_id'] == index:
            print(f"ID: {note['note_id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Тело: {note['body']}")
            print(f"Создано: {note['created_at']}")
            print(f"Обновлено: {note['updated_at']}")
            return True
    return False

def delete_note(index: str):
    index = int(index)
    for note in notes:
        if note['note_id'] == index:
            notes.remove(note)
            return True
    return False
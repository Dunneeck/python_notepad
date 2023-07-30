import json
import os.path
from datetime import datetime

class Notepad:
    def __init__(self):
        self.notes = []

    def create_note(self, title, content):
        timestamp = datetime.now()
        note = {
            "id": len(self.notes) + 1,
            "timestamp": str(timestamp),
            "title": title,
            "content": content
        }
        self.notes.append(note)
        return note

    def save_notes(self, filename):
        with open(filename, "w") as file:
            json.dump(self.notes, file, indent=4, sort_keys=True)

    def read_notes(self, filename):
        if not os.path.exists(filename):
            return

        with open(filename, "r") as file:
            self.notes = json.load(file)

    def edit_note_content(self, note_id, new_content):
        for note in self.notes:
            if str(note["id"]) == note_id:
                note["content"] = new_content
                note["timestamp"] = str(datetime.now())
                break

    def delete_note(self, note_id):
        for note in self.notes:
            if str(note["id"]) == note_id:
                self.notes.remove(note)
                break

    def sort_notes_by_timestamp(self):
        self.notes.sort(key=lambda note: datetime.fromisoformat(note["timestamp"]))
        for i, note in enumerate(self.notes):
            note["id"] = i + 1

    def print_notes(self):
        for note in self.notes:
            print(str(note["id"]) + ".\t" + note["title"] + "\n"
                  + note["content"] + "\n"
                  + "Дата записи: " + note["timestamp"])
    
    def is_not_empty(self):
        if len(self.notes) == 0:
            print("\nСписок пуст!\n")
            return False
        else:
            return True
        
    def show_note_by_id(self, note_id):
        found_note = None
        for note in self.notes:
            if str(note["id"]) == note_id:
                found_note = note
                break

        if found_note is None:
            print("\nТакого номера нет, либо вы ввели не число! Попробуйте снова.\n")
            return False

        print(str(found_note["id"]) + ".\t" + found_note["title"] + "\n"
            + found_note["content"] + "\n"
            + "Дата записи: " + found_note["timestamp"])

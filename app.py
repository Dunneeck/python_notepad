from notepad_file import Notepad

notepad = Notepad()
    
def create_note():
    new_title = input("Введите заглавие заметки. ")
    for note in notepad.notes:
            if note["title"] == new_title:
                print("Данный заголовок уже есть!")
                while(True):
                    command = input("Написать заметку заново. (add)\n" + "Доваить запись в заметку. (overwrite)\n")
                    if command.lower() == "add":
                        note["content"] = input("Введите содержание заметки. ")
                        break
                    elif command.lower() == "overwrite":
                        note["content"] = note["content"] + "\n" + input("Допишите заметку. ")
                        break
                    else:
                        print("Не верная команда!")
                        break
                notepad.sort_notes_by_timestamp()
                return
    content = input("Введите содержание заметки. ")
    notepad.create_note(new_title, content)

def save_note():
        notepad.sort_notes_by_timestamp()
        notepad.save_notes("notes.json")
        print("\nЗаметки сохранены!\n")

def edit_note():
    while(notepad.is_not_empty()):
        id = input("\nВведите номер заметки для редактирования.\n")
        if  0 < len(notepad.notes) <= int(id):
                content = input("Введите новую заметку.\n")
                notepad.edit_note_content(str(id), content)
                notepad.sort_notes_by_timestamp()
                print("\nЗаметка " + str(id) + " изменена!\n")
                return    
        print("\nТакого номера нет, либо вы ввели не число! Попробуйте снова.\n")

def delete_note():
    while(notepad.is_not_empty()):
        id = input("\nВведите номер заметки для удаления.\n")
        for note in notepad.notes:
            if str(note["id"]) == str(id):
                notepad.delete_note(str(id))
                print("\nЗаметка " + str(id) + " удалена!\n")
                return 
        print("\nТакого номера нет, либо вы ввели не число! Попробуйте снова.\n")

def show_note():
     flag = notepad.is_not_empty()
     while(flag):
        id = input("\nВведите номер заметки для просмотра.\n")
        flag = notepad.show_note_by_id(id)
        

job = True
notepad.read_notes("notes.json")

while(job):
    command = input("Выберите действие: \n" +
                    "add - добавить заметку\n" +
                    "save - сохранить заметки\n" +
                    "show - показать все заметки\n" +
                    "edit - редактировать заметку\n" +
                    "delete - удалить заметку\n" +
                    "end - закончить программу\n" +
                    "shownote - показать конкретную заметку \n")
    if command.lower() == "add":
        create_note()
    elif command.lower() == "save":
        save_note()
    elif command.lower() == "edit":
        edit_note()
    elif command.lower() == "show":
        if notepad.is_not_empty() == True:
            notepad.print_notes()
    elif command.lower() == "delete":
        delete_note()
    elif command.lower() == "shownote":
        show_note()
    elif command.lower() == "end":
        job = False
    else:
        print("\nНе правильная команда! Попробуйте снова!\n")
    
    
    
    
    



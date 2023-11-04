import json
import os
import datetime

# Путь к файлу, в котором будут храниться заметки в формате JSON
file_path = "notes.json"

def load_notes():
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            notes = json.load(file)
        return notes
    else:
        return []

def save_notes(notes):
    with open(file_path, "w") as file:
        json.dump(notes, file, indent=4)

def add_note(title, message):
    notes = load_notes()
    note = {
        "id": len(notes) + 1,
        "title": title,
        "message": message,
        "timestamp": str(datetime.datetime.now())
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена")

def list_notes():
    notes = load_notes()
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Тело заметки: {note['message']}")
        print(f"Дата/время создания: {note['timestamp']}")
        print("-" * 40)

def edit_note(note_id, title, message):
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            note['title'] = title
            note['message'] = message
            note['timestamp'] = str(datetime.datetime.now())
            save_notes(notes)
            print("Заметка успешно отредактирована")
            return
    print("Заметка с указанным ID не найдена")

def delete_note(note_id):
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена")
            return
    print("Заметка с указанным ID не найдена")

if __name__ == "__main__":
    while True:
        print("Доступные команды:")
        print("1. add - Добавить заметку")
        print("2. list - Показать список заметок")
        print("3. edit - Редактировать заметку")
        print("4. delete - Удалить заметку")
        print("5. exit - Выйти из приложения")

        command = input("Введите команду: ")

        if command == "add":
            title = input("Введите заголовок заметки: ")
            message = input("Введите тело заметки: ")
            add_note(title, message)
        elif command == "list":
            list_notes()
        elif command == "edit":
            note_id = int(input("Введите ID заметки, которую хотите отредактировать: "))
            title = input("Введите новый заголовок заметки: ")
            message = input("Введите новое тело заметки: ")
            edit_note(note_id, title, message)
        elif command == "delete":
            note_id = int(input("Введите ID заметки, которую хотите удалить: "))
            delete_note(note_id)
        elif command == "exit":
            break
        else:
            print("Неправильная команда. Попробуйте ещё раз.")

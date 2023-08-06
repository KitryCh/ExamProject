import json
import datetime


def read_note():
    try:
        with open('notes.json', 'r', encoding='utf8') as f:
            notes = json.load(f)
    except BaseException as e:
        notes = []
    return notes

def save_note(notes):
    with open('notes.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(notes, indent=4, default=str))

def print_note(notes):
    if not notes:
        print('Такой заметки нет.')
        print('---')
    else:
        for note in notes:
            print(f'ID: {note["id"]}')
            print(f'Заголовок: {note["name"]}')
            print(f'Текст заметки: {note["text"]}')
            print(f'Дата/время создания/изменения: {note["timestamp"]}')
            print('---')

def add_note(notes):
    max_id = 0
    for item in notes:
        if item['id'] > max_id:
            max_id = item['id']
    id = max_id + 1
    name = input('Введите заголовок: ')
    text = input('Введите текст заметки: ')
    timestamp = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    new_note = {'id': id, 'name': name, 'text': text, 'timestamp': timestamp}
    notes.append(new_note)
    return notes

def change_note(notes, id):
    for note in notes:
        count = 0
        if note['id'] == id:
            count = 1
            new_name = input(f'Введите новый заголовок (было: {note["name"]}): ')
            new_text = input(f'Введите новое тело заметки (было: {note["text"]}): ')
            note['name'] = new_name
            note['text'] = new_text
            note['timestamp'] = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            print(f'Заметка №{id} отредактирована')
            break
    if count == 0: print('Заметка с таким ID не найдена')
    return notes

def choose_by_date(notes,date):
    choose_notes = []
    for note in notes:
        note_date = datetime.datetime.strptime(note['timestamp'], '%d-%m-%Y %H:%M:%S')
        if note_date.date() == date:
            choose_notes.append(note)
    return choose_notes

def delete_note_by_id(notes, id):
    for index, note in enumerate(notes):
        if note['id'] == id:
            del notes[index]
    return notes

def delete_note_by_name(notes, name):
    for index, note in enumerate(notes):
        if note['name'] == name:
            del notes[index]
    return notes

def main():

    notes = read_note()

    while True:
        print('Выберите действие:')
        print('1. Вывести все заметки')
        print('2. Вывести заметки за определенную дату')
        print('3. Вывести конкретную заметку')
        print('4. Добавить новую заметку')
        print('5. Редактировать заметку')
        print('6. Удалить заметку по номеру')
        print('7. Удалить заметку по заголовку')
        print('8. Выход')

        case = input('Ваш выбор: ')
        print('---')

        if case == '1':
            print_note(notes)

        elif case == '2':
            date_str = input('Введите дату в формате ДД-ММ-ГГГГ: ')
            date = datetime.datetime.strptime(date_str, '%d-%m-%Y').date()
            filtered_notes = choose_by_date(notes, date)
            print_note(filtered_notes)

        elif case == '3':
            id = int(input('Введите ID заметки: '))
            note = [note for note in notes if note['id'] == id]
            print_note(note)

        elif case == '4':
            notes = add_note(notes)
            save_note(notes)
            print('Заметка добавлена')
            print('---')

        elif case == '5':
            id = int(input('Введите ID заметки для внесения изменений: '))
            notes = change_note(notes, id)
            save_note(notes)
            print('---')

        elif case == '6':
            id = int(input('Введите ID заметки для удаления: '))
            notes = delete_note_by_id(notes, id)
            save_note(notes)
            print(f'Заметка №{id} удалена')
            print('---')

        elif case == '7':
            name = input('Введите имя заметки для удаления: ')
            notes = delete_note_by_name(notes, name)
            save_note(notes)
            print(f'Заметка удалена')
            print('---')

        elif case == '8':
            break

        else:
            print('Такого пункта меню нет')
            print('---')


if __name__ == '__main__':
    main()
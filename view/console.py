from .text import *


def menu() -> int:
    print(main_menu)
    while True:
        choice = input(menu_choice)
        if choice.isdigit() and 0 < int(choice) < 7:
            return int(choice)
        print(input_error)


def print_msg(msg: str):
    length = len(msg)
    print('\n' + '=' * length)
    print(msg)
    print('=' * length + '\n')


def list_notes(notes):
    if not notes:
        print(notes_error)
    else:
        for note in notes:
            print(f"ID: {note['note_id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Тело: {note['body']}")
            print(f"Создано: {note['created_at']}")
            print(f"Обновлено: {note['updated_at']}")
            print("-" * 30)


def input_title_note(msg: str):
    print(msg)
    new = input()
    return new

def input_body_note(msg: str):
    print(msg)
    body = input(new_body_note)

def input_return(msg: str):
    return input(msg)
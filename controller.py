from  view import menu, list_notes, print_msg, input_title_note, input_return
import model
from view import text




def start():
    while True:
        choice = menu()
        match choice:
            case 1:
                model.load_notes()
                print_msg(text.open_successful)
            case 2:
                list_notes(model.notes)
            case 3:
                print_msg(text.input_new_note)
                title = input_title_note(text.new_title_note)
                body = input_title_note(text.new_body_note)
                model.create_note(title, body)
                model.save_notes()
                print_msg(text.note_added)
            case 4:
                list_notes(model.notes)
                index = input_return(text.input_change_index)
                new_title = input_title_note(text.new_title_note)
                new_body = input_title_note(text.new_body_note)
                if model.edit_note(index, new_title, new_body):
                    model.save_notes()
                    print_msg(text.note_changed)
                else:
                    print_msg(text.note_ID_error)
            case 5:
                list_notes(model.notes)
                index = input_return(text.input_del_index)
                if model.delete_note(index):
                    model.save_notes()
                    print_msg(text.note_deleted)
                else:
                    print_msg(text.note_ID_error)
            case 6:
                print_msg(text.goodbye_message)
                break
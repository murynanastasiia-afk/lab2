import FreeSimpleGUI as sg
import core
import functions
import time

def handle_add(window, values):
         task = values['task'].strip()
         count = values['count'].strip()
         date = values['date'].strip()
         if task and count and date and isinstance(count, int) and  date:
                  core.add_todo(task, count, date)
                  for key in ['task', 'count', 'date']:
                           window[key].update(value='')
                  window['todos_list'].update(values=functions.get_todos())
         else:
                  sg.popup_error("Заповніть всі поля у првильному форматі: Назва, Кількість, Дата!")



def handle_select_todo(window, values):
         try:
                  selected = values['todos_list'][0].strip()
                  parts = selected.split()
                  if len(parts) >= 3:
                           window['date'].update(value=parts[0])
                           window['task'].update(value=" ".join(parts[1:-1]))
                           window['count'].update(value=parts[-1].split('/')[-1])
         except IndexError:
                  pass

def handle_edit(window, values):
    try:
        index_list = window['todos_list'].get_indexes()
        index = index_list[0]
        
        new_task = values['task'].strip()
        new_count = values['count'].strip()
        new_date = values['date'].strip()
        
        if new_task and new_count and new_date:
            core.edit_todo(index, new_task, new_count, new_date)
            window['todos_list'].update(values=functions.get_todos())
            sg.popup("Зміни збережено!")
    except IndexError:
        sg.popup_error("Оберіть завдання зі списку для редагування!")

def handle_complete(window, values):
    try:
        index_list = window['todos_list'].get_indexes()
        index = index_list[0]
        print(f"DEBUG: Вибрано індекс {index}")
        result = core.complete(index)
        
        if result:
            window['todos_list'].update(values=functions.get_todos())
            if result == "виконано":
                sg.popup("Завдання повністю виконано і перенесено в архів.")
    except IndexError:
        sg.popup_error("Оберіть завдання для виконання!")

def handle_show_results(window, values):
    done_todos = functions.get_todos_done()
    
    if not done_todos:
        sg.popup("Архів поки що порожній!", title="Архів")
        return

    clean_done = [item.strip() for item in done_todos]

    archive_layout = [
        [sg.Text("Виконані завдання:")],
        [sg.Listbox(values=clean_done, size=(50, 10), key='done_list')],
        [sg.Button("", image_filename="C:\\унік\\4семестр\\Розобка\\lab2\\pngwingexit2.com.png", key='close_achive', tooltip='Архів')]
    ]

    archive_window = sg.Window("Архів", archive_layout, modal=True)
    while True:
        event, _ = archive_window.read()
        if event in (sg.WIN_CLOSED, 'close_achive'):
            break
            
    archive_window.close()
      

GUI_COMMANDS = {
    'add': handle_add,
    'todos': handle_select_todo,
    'edit': handle_edit,       
    'complete': handle_complete,
    'results' : handle_show_results
}

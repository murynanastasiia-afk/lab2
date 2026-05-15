import FreeSimpleGUI as sg
import functions


def build_layout():

    PINK_BACKGROUND = '#FFD1DC'  
    PURPLE_BUTTON = '#9370DB'    
    TEXT_COLOR = '#4B0082'       

    sg.theme_background_color(PINK_BACKGROUND)
    sg.theme_element_background_color(PINK_BACKGROUND)
    sg.theme_text_element_background_color(PINK_BACKGROUND)
    sg.theme_button_color((sg.COLOR_SYSTEM_DEFAULT, PURPLE_BUTTON))
    sg.theme_text_color(TEXT_COLOR)


    clock_row = [sg.Push(), sg.Text("", key='-CLOCK-', font=('Helvetica', 12, 'bold')), sg.Push()]

    header_ = [
        clock_row,  
        [sg.HSeparator()],
        [sg.Text("Дата:", size=(12, 1), justification='right'), sg.Input(key='date', size=(15, 1))], 
        [sg.Text("Назва:", size=(12, 1), justification='right'), sg.Input(key='task', size=(35, 1))],
        [sg.Text("Кількість:", size=(12, 1), justification='right'), sg.Input(key='count', size=(10, 1))],
        ]
    
    list_=[
        [sg.Listbox(values=functions.get_todos(), key='todos_list', 
                    size=(60, 10), enable_events=True)],
    ]

    menu_=[
         [sg.Button("", image_filename="C:\\унік\\4семестр\\Розобка\\lab2\\pngwingadd.com.png", key='add', tooltip='Додати завдання')],
         [sg.Button("", image_filename="C:\\унік\\4семестр\\Розобка\\lab2\\pngwingcomplate.com.png", key='complete', tooltip='Виконати завдання')],
         [sg.Button("", image_filename="C:\\унік\\4семестр\\Розобка\\lab2\\pngwingedit.com.png", key='edit', tooltip='Редагувати завдання')],
         [sg.Button("", image_filename="C:\\унік\\4семестр\\Розобка\\lab2\\pngwingachive.com.png", key='results', tooltip='Виконані завдання')],
         [sg.VPush()],
         [sg.Button("", image_filename="C:\\унік\\4семестр\\Розобка\\lab2\\pngwingexit.com.png", key='exit', tooltip='Вийти')]
    ]
        
    return [
        [
            sg.Column(header_ + list_, background_color=PINK_BACKGROUND, element_justification='l'),
            sg.VerticalSeparator(), 
            sg.Column(menu_, background_color=PINK_BACKGROUND, element_justification='c'),
        ]

    ]
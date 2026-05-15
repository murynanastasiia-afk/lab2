import FreeSimpleGUI as sg
import gui_view
import gui_controller
import time

def main():
    layout = gui_view.build_layout()

    window = sg.Window('Список завдань', layout, font=('Helvetica', 14))

    while True:
        event, values = window.read(timeout=500)
        if event in (sg.WIN_CLOSED, 'exit', 'Вихід'):
            break

        if event in gui_controller.GUI_COMMANDS:
            handler = gui_controller.GUI_COMMANDS[event]
            handler(window, values)
        
        if event == 'todos_list':
            gui_controller.handle_select_todo(window, values)
        
        months_ua = {
            "01": "січня", "02": "лютого", "03": "березня", 
            "04": "квітня", "05": "травня", "06": "червня",
            "07": "липня", "08": "серпня", "09": "вересня", 
            "10": "жовтня", "11": "листопада", "12": "грудня"
        }

        day = time.strftime('%d')
        month_num = time.strftime('%m')
        hms = time.strftime('%H:%M:%S')

        day = day.lstrip('0')

        current_time = f"{day} {months_ua[month_num]} {hms}"
        
        window['-CLOCK-'].update(current_time)
    window.close()
    print("Програму завершено!")

if __name__ == '__main__':
    main()
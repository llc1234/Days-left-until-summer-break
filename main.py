import time
import threading
import tkinter.ttk
from datetime import datetime


# pyinstaller: python -m PyInstaller --onefile -w main.py

def get_days():
    current_date = datetime.now()

    target_date = datetime(2024, 6, 1)

    days_until_target_date = (target_date - current_date).days

    return days_until_target_date


def exit_button(root):
    root.destroy()


def display_days(display_days):
    root = tkinter.Tk()
    root.title("Days left until summer break")
    root.resizable(False, False)

    window_width, window_height = 340, 100

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    tkinter.Label(root, text=f"days: {display_days}", font=('Times 25')).place(x=100, y=30)
    tkinter.ttk.Button(root, text="  ok  ", command=lambda: exit_button(root)).place(x=260, y=70)

    root.mainloop()


def main():
    day_1 = get_days()
    display_days(day_1)

    while True:
        for i in range(60):
            time.sleep(60)

        day_2 = get_days()

        if day_2 > day_1:
            day_1 = day_2
            display_days(day_1)


if __name__ == "__main__":
    main()
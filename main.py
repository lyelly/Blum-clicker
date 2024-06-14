import subprocess
import sys
import os

def install_requirements():
    requirements_file = os.path.join('files', 'requirements.txt')
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
    print("Успешно установлено. Перезагрузка скрипта...")
    subprocess.Popen([sys.executable, __file__], creationflags=subprocess.CREATE_NEW_CONSOLE)
    sys.exit()


def show_menu():
    print("1. Кликать по зеленым без ограничений")
    print("2. Кликать по зеленым и заморозке")
    print("3. Кликать по зеленым с рандомными перерывами и задержками")
    print("4. Кликать по зеленым и заморозке с рандомными перерывами и задержками")
    print("0. Выход")

def main():
    while True:
        show_menu()
        choice = input("Выберите режим: ")

        if choice == '1':
            subprocess.run([sys.executable, 'files/start.py'])
        elif choice == '2':
            subprocess.run([sys.executable, 'files/start_1.py'])
        elif choice == '3':
            subprocess.run([sys.executable, 'files/start_2.py'])
        elif choice == '4':
            subprocess.run([sys.executable, 'files/start_3.py'])
        elif choice == '0':
            print("Выход...")
            break
        else:
            print("Ошибка выбора.")

if __name__ == "__main__":
    try:
        import pyautogui
        import keyboard
        import pynput
        import pygetwindow
        import tkinter as tk
    except ImportError:
        install_requirements()
    else:
        main()

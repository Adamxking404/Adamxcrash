import os
import time

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print("\033[1;91m")  # Blue color
    print("       _   ___   _   __  __  ")
    print("      /_\ |   \ /_\ |  \/  | ")
    print("     / _ \| |) / _ \| |\/| | ")
    print("    /_/ \_\___/_/ \_\_|  |_| ")
    print("\033[0m")  # Reset color
    print("  A WHATSAPP NUMBER BAN TOOL BY DARK ADAM\n")
    print("\033[0;36m")  # Cyan color
    print(" - Discord : kine azul#3189")
    print(" - Github  : https://github.com/Adamxking404")
    print(" - Telegram: @Adamxking")
    print("\033[0m")  # Reset color
    print("\n [ 1 ] Ban number")
    print(" [ 2 ] Unban number")
    print(" [ 0 ] Exit")

def ban_number():
    number = input("\nEnter number to ban: ")
    print(f"\nBanning {number}...")
    time.sleep(2)
    print(f"{number} successfully banned!")

def unban_number():
    number = input("\nEnter number to unban: ")
    print(f"\nUnbanning {number}...")
    time.sleep(2)

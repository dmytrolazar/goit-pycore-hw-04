import sys
from pathlib import Path
from colorama import Fore

def print_dir_tree(cur, level = 0):
    if Path(cur).is_dir():
        print(Fore.BLUE + ' '*4*level + str(cur) + '\\' + Fore.RESET)
        for d in list(Path(cur).iterdir()):
            print_dir_tree(d, level + 1)
    else:
        print(Fore.GREEN + ' '*4*level + str(cur) + Fore.RESET)

def main():
    try:
        dir = sys.argv[1]
        if Path(dir).exists():
            if Path(dir).is_dir():
                print_dir_tree(dir)
            else:
                print("Вказаний шлях не веде до папки.")  
        else:
            print("Вказаний шлях не існує.")     
    except IndexError:
        print("Відсутній аргумент зі шляхом до папки.")

if __name__ == '__main__':
    main()

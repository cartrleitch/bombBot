import pyautogui as pg
import time

def main():
    while True:
        time.sleep(5)
        print(pg.position())

if __name__ == '__main__':
    main()


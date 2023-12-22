import discord
from discord import app_commands
import os
from dotenv import load_dotenv
import pyautogui as pg
import time

def main():

    # defines intents
    intents = discord.Intents.default()

    # allows message content to be accessed and manipulated
    intents.message_content = True

    # allows token to be stored in ENV file securely
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    # defines client intents and commands
    client = discord.Client(intents=intents, command_prefix='!')

    # makes tree for commands
    tree = app_commands.CommandTree(client, fallback_to_global=True)

    def selectStock():
        # select stock
        stockChoice = input("Enter stock: ")
        print("1. 5 min\n2. 1 hour\n3. 1 day")
        timeChoice = int(input("Enter time-frame: "))
        time.sleep(2)
        pg.moveTo(100, 96)
        pg.click()
        pg.write(stockChoice)
        pg.press('enter')
        time.sleep(1)

        # select time-frame
        pg.moveTo(214,108)
        pg.click()
        if timeChoice == 1:
            pg.moveTo(235, 393)
            pg.click()
        elif timeChoice == 2:
            pg.moveTo(229, 557)
            pg.click()
        elif timeChoice == 3:
            pg.moveTo(232, 723)
            pg.click()

        # take screenshot
        chart1 = pg.screenshot()
        chart1.save('chart.jpg')

    selectStock()
    client.run(TOKEN)

if __name__ == '__main__':
    main()

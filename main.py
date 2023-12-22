import discord
from discord import app_commands
import os
import atexit
from dotenv import load_dotenv
import pyautogui as pg
import webbrowser

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

    def exitHandler():
        pg.moveTo(1892, 12)            
        pg.click()
        print("exiting...")

    @client.event
    async def on_ready():
        """prints message when login and connection is successful (bot is up and running)"""
        await tree.sync(guild=None)
        print("Reddy")
        print("-------------")
        webbrowser.open_new("https://www.tradingview.com/chart/?symbol=SPY")

    def selectStock(stock, timeChoice):
        choice = timeChoice.replace(" ", "").lower()
        choice = choice[0:2:1]
        # select stock
        pg.moveTo(100, 96)
        pg.click()
        pg.write(stock)
        pg.press('enter')

        # select time-frame
        pg.moveTo(214,108)
        pg.click()

        if choice == "5m":
            pg.moveTo(235, 393)
            pg.click()
        elif choice == "1h":
            pg.moveTo(229, 557)
            pg.click()
        elif choice == "1d":
            pg.moveTo(232, 723)
            pg.click()
        else:
            print("No time-frame chosen")

        # take screenshot
        chart1 = pg.screenshot(region=(0, 86, 1870, 988))
        chart1.save('chart.jpg')

    @tree.command(name="stock", guild=None)
    async def stock(interaction: discord.Interaction, stock: str, timeframe: str):
        """takes screenshot of stock chart"""
        selectStock(stock, timeframe)
        await interaction.response.send_message(file=discord.File('chart.jpg'))

    client.run(TOKEN)

    atexit.register(exitHandler())

if __name__ == '__main__':
    main()

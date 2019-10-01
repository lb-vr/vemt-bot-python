# (c) 2019 lb-vr WhiteAtelier
import discord
import logging

from config import token
from logic import initialize, logger

from testfunc import testfunc

client = discord.Client()


@client.event
async def on_connect():
    print('Connected.')

"""
@client.event
async def on_ready():
    print('Bot is on ready.')
    channels = client.get_all_channels()
    for ch in channels:
        if ch.name == 'bot-status':
            await ch.send('BOT Started.')
"""


@client.event
async def on_disconnect():
    print('Disconnected.')


@client.event
async def on_message(message):
    if not message.author.bot:
        logging.getLogger().info('Message received. \n%s\nauthor id = %d', message.content, message.author.id)

        if message.content.startswith('+'):
            prms = message.content.split()[0].strip(' +\r\n').split(' ')
            if prms[0] == 'close':
                await message.channel.send('Bot Closing.')
                await client.close()
                return
            elif prms[0] == 'clear-role':
                await testfunc.clearRoles(message.guild)
                await message.channel.send('Finished ' + message.content)
            elif prms[0] == 'clear-ch':
                await testfunc.clearChannel(message.guild)
                await message.channel.send('Finished ' + message.content)
            elif prms[0] == 'clean':
                await testfunc.cleanDefault(message.guild)
                await message.channel.send('Finished ' + message.content)
            elif prms[0] == 'init':
                await initialize.initializeServer(client, message)
            else:
                await message.channel.send('コマンド「{}」は定義されていません。'.format(prms[0]))


if __name__ == "__main__":
    logger.setupLogger('vemt', logging.INFO, logging.INFO)

    tkn: str = token.loadTokenFromFile()
    if not tkn:
        logging.Logger().fatal('Token string is blank.')
        exit(-1)

    client.run(tkn)

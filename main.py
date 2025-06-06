"""
    Discord
    bot_test02
    Eloy Calatrava
    22 May 2025

    Segunda prueba de BOT para Discord
    Usando de guía el vídeo de YouTube, curso de 5 capítols
        https://www.youtube.com/watch?v=CHbN_gB30Tw&list=PL-7Dfw57ZZVQ-GCNQS4Kyz637Fffhb0Hs&index=6
        "Creating a Discord Bot in Python (2025)"

    Vídeo 1 Introducció, instal·lació

    Vídeo 2 - Events

    Vídeo 3 - Slash commands
    Són la manera d'interactuar amb el BOT.
    S'escriu / i després el nom de la funció que s'hagi implementat

    Vídeo 4 - Embeds

    Vídeo 5 - Buttons


"""

from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import app_commands

import os
import webserver

# load_dotenv()
# TOKEN = os.getenv("DISCORD_TOKEN")

TOKEN = os.environ['discordkey']


# class Client(discord.Client):
class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')

        try:
            guild = discord.Object(id=1374132519112409098)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')

        except Exception as e:
            print(f'Failed to sync guild {guild.id}: {e}')


    async def on_message(self, message):
        # print(f'Received message from {message.author}: {message.content}')
        if message.author == self.user:
            return
        if message.author.display_name == '51-yahels2an#5055':
            await message.channel.send(f'Hola Yahel, viva Canarias!!!')
        if message.author.display_name == '50-eloyhawk#9229':
            await message.channel.send(f'Hola Eloy, eres el puto amo!!!')
        if message.content.startswith('hello'):
            await message.channel.send(f'Hello, {message.author.name}!')
            await message.channel.send(f' tienes el código, {message.author.mention}')
            await message.channel.send(f' yo soy, {self.user}')
            await message.channel.send(f'{message.author.display_name}')

    # Només respon si la reacció és a l'últim missatge.
    # Aquest exemple no val per massa...
    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('Has reaccionat')



# Amb aquestes dues línies el BOT respon des de qualsevol canal
# intents = discord.Intents.default()
# intents.message_content = True

# En canvi, amb aquestes només respon si li parles a ell directament
# intents = discord.Intents.default()
# intents.messages = True

# I amb aquestes respon a tot arreu
intents = discord.Intents.all()
intents.messages = True

# es canvia la declaració del client per acceptar comandes slash
# client = Client(intents=intents)
client = Client(command_prefix='!', intents=intents)


# Aquest codi és el codi del servidor que es fa servir per en certa manera
# connectar el BOT directament al servidor, millor dit sincronitzar
# La connexió és fa en dues parts:
#       La primera és a sota posant el paràmetre guild=GUILD_ID.
#       La segona, a dalt del codi, quan es declara la classe Client,
#           on es força la connexió o sincronisme.
GUILD_ID = discord.Object(id=1374132519112409098)
# nou 1375203780743659696
# vell 1374132519112409098

# Codi per implementar slash commands
@client.tree.command(name='hola', description="Comando para saludar", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("Hola, cómo va?")

@client.tree.command(name='printer', description="Imprimo lo que quieras", guild=GUILD_ID)
async def printer(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(printer)

# Slash command per fer embeds
@client.tree.command(name='alineacion', description="Demo para EMBEDs", guild=GUILD_ID)
async def printer(interaction: discord.Interaction):
    embed = discord.Embed(title='ALINEACIÓN',
                          description='Patrullas',
                          url='https://hlltrial.wordpress.com/',
                          color=discord.Color.green(),
                          )
    # embed.set_thumbnail(url='https://cdn.pixabay.com/photo/2021/07/17/09/33/subscribe-6472639_960_720.png')
    embed.set_image(url='https://cdn.pixabay.com/photo/2021/07/17/09/33/subscribe-6472639_960_720.png')

    embed.add_field(name='CHACALES', value='Patrullas de carros', inline=False)
    embed.add_field(name='CHACAL 1', value='Makea\nNico\nKevin', inline=True)
    embed.add_field(name='CHACAL 2', value='Pal\nPater\nJuank', inline=True)
    embed.add_field(name='CHACAL 3', value='Baba\nDivision\nPorryta', inline=True)

    embed.add_field(name='DEFENSA', value='Patrullas de defensa', inline=False)
    embed.add_field(name='EDEF SECTOR 1', value='Chuchi\nFalcata\nAssasin', inline=True)
    embed.add_field(name='EDEC FUERTE', value='Eloy\nJose\nRotceh', inline=True)
    embed.add_field(name='EDEF SECTOR 2', value='Tuso\nTutan\nLadrillo', inline=True)

    embed.set_footer(text=f'Pie de página')

    embed.set_author(name=interaction.user.name,
                     url="https://eloy1969.wordpress.com/",
                     icon_url='https://cdn.pixabay.com/photo/2021/07/17/09/33/subscribe-6472639_960_720.png')

    await interaction.response.send_message(embed=embed)


# Per incloure botons

class View(discord.ui.View):
    @discord.ui.button(label='Click me!', style=discord.ButtonStyle.red, emoji='✅')
    async def one_button_callback(self, button, interaction):
        await button.response.send_message('Has pulsado check!!!')

    @discord.ui.button(label='Botón 2', style=discord.ButtonStyle.green, emoji='👌')
    async def two_button_callback(self, button, interaction):
        await button.response.send_message('Has pulsado OK!!!')

    @discord.ui.button(label='Botón 3', style=discord.ButtonStyle.gray, emoji='💋')
    async def three_button_callback(self, button, interaction):
        await button.response.send_message('Has pulsado morritos!!!')


@client.tree.command(name='boton', description="Esto es un botón", guild=GUILD_ID)
async def myButton(interaction: discord.Interaction):
    await interaction.response.send_message(view=View())


webserver.keep_alive()
client.run(TOKEN)
























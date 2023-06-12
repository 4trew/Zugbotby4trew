import discord
import requests
import json
import asyncio
import textwrap
import itertools
import os
from datetime import datetime, timedelta

from discord.ext import commands
from prettytable import PrettyTable

intents = discord.Intents.all()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='/', intents=intents)
DISCORD_TOKEN = "ODU2NjA3MzQ0NDU5OTA3MDkz.GrSABh.LEmoHqGhL5kEOx-BFMWYscr2gnjcxw-98hxNnA"
DISCORD_CHANNEL_ID = [1105394238230888581, 1105569996714803230]
MAX_MESSAGE_LENGTH = 1999


@bot.command(name="hi")
async def hallo(ctx):
    user_id = 799549032322039828
    user = discord.utils.get(ctx.guild.members, id=user_id)
    if user:
        await ctx.send(f"Hallo {user.mention}, ich hab Udo und Gerlinde dabei.")


@bot.command(name="kiemenbar")
async def Kamel(ctx):
    await ctx.send("AB JETZT BIN ICH IMMER ONLINE! ||@everyone|| ")


@bot.command(name="gn")
async def Kamel(ctx):
    await ctx.send("Ich wünsche eine gute Nacht! Und bitte nicht Udo und Gerlinde auffressen")


@bot.command(name="Kamel")
async def Kamel(ctx):
    await ctx.send(
        "'''Kamele sind wunderbare Tiere mit Flügeln und Hörnern. Sie leben in den Bergen und schwimmen gerne im Meer. Ihr Lieblingsessen ist Schokolade und ihr Lieblingsgetränk ist Limonade. Wenn sie sich freuen, fangen sie an zu singen und zu tanzen. Aber wenn sie traurig sind, können sie weinen wie Menschen. Einige Kamele können sogar sprechen und sie sprechen gerne in Rätseln. Wenn du ein Kamel triffst, musst du ihm unbedingt ein Gedicht vortragen, sonst wird es beleidigt sein. Wenn du Glück hast, wird es dir vielleicht ein Kamelrennen anbieten, bei dem du auf seinem Rücken reiten kannst. Aber pass auf, denn einige Kamele sind sehr schnell und können bis zu 100 km/h erreichen. Wenn du jemals von einem Kamel verfolgt wirst, solltest du schnell in ein Flugzeug springen, denn Kamele können nicht fliegen. Aber wenn du kein Flugzeug hast, versuche einfach, dem Kamel einen Apfel zu geben, denn Kamele lieben Äpfel. '''")


@bot.command(name="gulasch")
async def Kamel(ctx):
    await ctx.send("Warum sollte man Kamele nicht zu Gulasch machen? Nun, es gibt viele Gründe!")
    await ctx.send(
        "Erstens sind Kamele groß und schwer. Man braucht also viel Fleisch, um genug Gulasch zu machen, um eine hungrige Menge zu füttern. Und wo findet man so viel Fleisch? Natürlich bei einem Kamel.")
    await ctx.send(
        "Zweitens sind Kamele nicht gerade lecker. Sie haben eine dicke, haarige Haut und sind voller harten, zähen Muskeln. Außerdem neigen sie dazu, einen starken und unangenehmen Geruch zu haben.")
    await ctx.send(
        "Drittens haben Kamele auch einen schlechten Ruf. Sie sind dafür bekannt, störrisch und widerspenstig zu sein. Sie könnten also Schwierigkeiten haben, das Kamel zu erlegen und es in das benötigte Fleisch zu verwandeln.")
    await ctx.send(
        "Viertens gibt es noch das Problem der Zubereitung. Kamelfleisch braucht viel Zeit, um zart zu werden, und es kann schwierig sein, es richtig zu kochen. Wenn man es nicht richtig macht, bleibt es zäh und ungenießbar.")
    await ctx.send(
        "Und schließlich gibt es noch den moralischen Aspekt. Kamele sind majestätische und wunderbare Kreaturen. Sie sollten nicht einfach nur wegen eines kulinarischen Experimentes getötet werden.")
    await ctx.send(
        "Zusammenfassend lässt sich sagen, dass es viele Gründe gibt, warum man Kamele nicht zu Gulasch machen sollte. Es ist schwierig, teuer, schwierig zuzubereiten und auch ein wenig unmoralisch. Und mal ganz ehrlich, wer will schon ein Kamel essen, wenn es so viele andere leckere und einfacher zu bekommende Alternativen gibt?")


@bot.command(name='kickf')
async def kick(ctx, user_id: int):
    # Nur der spezifische Nutzer darf diesen Command verwenden
    if ctx.author.id != 719980889253216327:
        await ctx.send("Du hast keine Berechtigung, diesen Command auszuführen.")
        return

    # Versuche, den Nutzer zu kicken
    try:
        user = await bot.fetch_user(user_id)
        await ctx.guild.kick(user)
        await ctx.send(f"{user.name} wurde gekickt!")
    except:
        await ctx.send("Konnte den Nutzer nicht kicken.")


@bot.command(name='loe')
async def clear_messages(ctx):
    if ctx.author.id not in [719980889253216327, 799549032322039828]:
        await ctx.send("Du hast keine Berechtigung, diesen Befehl auszuführen.")
        return

    await ctx.send("Wie viele Nachrichten möchtest du löschen?")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.isdigit()

    msg = await bot.wait_for("message", check=check)
    num = int(msg.content)

    await ctx.channel.purge(limit=num + 1)


@bot.command(name="udoliebe")
async def Udo(ctx):
    await ctx.send(
        "💙" * 10 + "Kickl " * 5 + "💙" * 10 + "Udo Landbauer " * 5 + "💙" * 10 + "Gerlinde " * 5 + "💙" * 10 + "Steffi der Geile Horst " * 50 + "💙" * 10 + "Thorsten der russische Spion " * 5)


def length(table):
    pass


@bot.command(name="fahrplan")
async def get_train_schedule(ctx):
    # Bot sends first message
    message1 = await ctx.send('Bitte gib den Loktyp ein:')

    # Wait for user response
    loktyp_message = await bot.wait_for('message', check=lambda m: m.author == ctx.author)

    # Bot deletes its own message and the user's response
    await message1.delete()
    await loktyp_message.delete()

    # Get user response
    loktyp = loktyp_message.content

    # Bot sends second message
    message2 = await ctx.send(f'Bitte gib die Loknummer für den Loktyp {loktyp} ein:')

    # Wait for user response
    loknummer_message = await bot.wait_for('message', check=lambda m: m.author == ctx.author)

    # Bot deletes its own message and the user's response
    await message2.delete()
    await loknummer_message.delete()

    # Get user response
    loknummer = loknummer_message.content

    url = f"https://konzern-apps.web.oebb.at/lok/index/{loktyp}.0{loknummer}"
    response = requests.get(url)
    json_data = response.content.decode('utf-8')
    data = json.loads(json_data)

    stops = {}  # Dictionary to store train numbers and their stops
    train_numbers = set()  # Set to store train numbers with no other train number above or below them

    for row in data:
        if row["departure"] is not None:
            departure_time = datetime.fromisoformat(row["departure"].replace("Z", "+00:00"))
            row["departure"] = (departure_time + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S")
            row["departure"] = row["departure"].replace("2023-", "").replace("T", " ")
            row["departure"] = row["departure"][:row["departure"].find(":") + 3]

        if row["arrival"] is not None:
            arrival_time = datetime.fromisoformat(row["arrival"].replace("Z", "+00:00"))
            row["arrival"] = (arrival_time + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S")
            row["arrival"] = row["arrival"].replace("2023-", "").replace("T", " ")
            row["arrival"] = row["arrival"][:row["arrival"].find(":") + 3]

        train_number = row.get("train_number")
        if train_number:
            try:
                train_number_int = int(train_number)
                stops.setdefault(train_number_int, []).append(row["name"])
                if not any(train_number_int - i in train_numbers or train_number_int + i in train_numbers for i in
                           range(1, 5)):
                    train_numbers.add(train_number_int)
            except ValueError:
                pass

    if not data:
        await ctx.send("Keine Daten gefunden.")
        return

    table = PrettyTable()
    table.field_names = ["Zugnummer", "Bahnhof", "Loknummer", "Ankunft", "Abfahrt"]
    for row in data:
        table.add_row([
            row.get("train_number", ""),
            row.get("name", ""),
            row.get("unit_number", ""),
            row.get("arrival", ""),
            row.get("departure", ""),
        ])
    table_str = str(table)  # convert the table to a string

    channel_id = 1105569996714803230

    if len(table_str) > MAX_MESSAGE_LENGTH:
        # Nachricht ist zu lang für Discord
        # Teile die Nachricht in mehrere Teile auf
        table_list = table_str.split("\n")
        table_parts = []
        part = ""
        for row in table_list:
            if len(part + row) > MAX_MESSAGE_LENGTH:
                table_parts.append(part)
                part = row + "\n"
            else:
                part += row + "\n"
        if part:
            table_parts.append(part)

        # Schicke die aufgeteilte Nachricht an den Nutzer
        for i, part in enumerate(table_parts):
            if i == 0:
                await ctx.send(f"Hier ist der Fahrplan für Lok {loktyp} {loknummer}:\n```{part}```")
            else:
                await ctx.send(part)
    else:
        # Schicke die Nachricht an den Nutzer
        await ctx.send(f"Hier ist der Fahrplan für Lok {loktyp} {loknummer}:\n```{table_str}```")

    table2 = PrettyTable()
    table2.field_names = ["Zugnummer", "Bahnhof", "Ankunft", "Abfahrt"]
    for row in data:
        table2.add_row([
            row.get("train_number", ""),
            row.get("name", ""),
            row.get("arrival", ""),
            row.get("departure", ""),
        ])
    print(table2)

    if len(stops) == 0:
        await ctx.send("Keine Daten gefunden.")
        return

    table2_str = str(table2)

    if len(table2_str) > MAX_MESSAGE_LENGTH:
        # Nachricht ist zu lang für Discord
        # Teile die Nachricht in mehrere Teile auf
        table_list = table_str.split("\n")
        table_parts = []
        part = ""
        for row in table_list:
            if len(part + row) > MAX_MESSAGE_LENGTH:
                table_parts.append(part)
                part = row + "\n"
            else:
                part += row + "\n"
        if part:
            table_parts.append(part)

        # Schicke die aufgeteilte Nachricht an den Nutzer
        channel = bot.get_channel(1041039409266565133)
        for i, part in enumerate(table_parts):
            if i == 0:
                await channel.send(f"Hier ist der Planfahrplan für {train_number}:\n```{part}```")
            else:
                await channel.send("```{part}```")
    else:
        # Schicke die Nachricht an den Nutzer
        channel = bot.get_channel(1041039409266565133)
        await channel.send(f"Hier ist der Planfahrplan für {train_number}:\n```{table_str}```")


@bot.command(name="zug")
async def train_emoji(ctx):
    train = ":train: :train: :train: "
    message = await ctx.send("**Einsteigen bitte\nZurückbleiben bitte**")
    await asyncio.sleep(2)
    for spaces in itertools.count():
        content = f"{'⠀' * spaces}{train}"
        await message.edit(content=content)
        if spaces == len(train):
            break
        await asyncio.sleep(0.5)

    await asyncio.sleep(1)
    await message.edit(content="⠀")

    for spaces in range(len(train), 0, -1):
        content = f"{'⠀' * spaces}{train}"
        await message.edit(content=content)
        await asyncio.sleep(0.5)

    await message.edit(content="Ende der Fahrt! :octagonal_sign: ")
    await asyncio.sleep(2)
    await message.delete


@bot.command(name="lokf")
async def get_train_schedules(ctx, loktyp: str):
    channel_id = 1105394238230888581  # Channel ID to send the table to

    loktyp_mapping = {
        "2016": "2016",
        "2070": "2070",
        "1144": "1144",
        "5022": "5022",
        "1142": "1142",
        "5047": "5047",
        "4020": "4020"
    }

    if loktyp not in loktyp_mapping:
        await ctx.send(f"Ungültiger Loktyp: {loktyp}. Bitte verwende einen der folgenden: 2016, 2070, 1144.")
        return

    loktyp = loktyp_mapping[loktyp]

    for num in range(801):
        loknummer = f"{num:03d}"
        url = f"https://konzern-apps.web.oebb.at/lok/index/{loktyp}.0{loknummer}"
        response = requests.get(url)
        json_data = response.content.decode('utf-8')
        data = json.loads(json_data)

        stops = {}  # Dictionary to store train numbers and their stops
        train_numbers = set()  # Set to store train numbers with no other train number above or below them

        for row in data:
            if row["departure"] is not None:
                departure_time = datetime.fromisoformat(row["departure"].replace("Z", "+00:00"))
                row["departure"] = (departure_time + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S")
                row["departure"] = row["departure"].replace("2023-", "").replace("T", " ")
                row["departure"] = row["departure"][:row["departure"].find(":") + 3]

            if row["arrival"] is not None:
                arrival_time = datetime.fromisoformat(row["arrival"].replace("Z", "+00:00"))
                row["arrival"] = (arrival_time + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S")
                row["arrival"] = row["arrival"].replace("2023-", "").replace("T", " ")
                row["arrival"] = row["arrival"][:row["arrival"].find(":") + 3]

            train_number = row.get("train_number")
            if train_number:
                try:
                    train_number_int = int(train_number)
                    stops.setdefault(train_number_int, []).append(row["name"])
                    if not any(train_number_int - i in train_numbers or train_number_int + i in train_numbers for i in
                               range(1, 5)):
                        train_numbers.add(train_number_int)
                except ValueError:
                    pass

        if not data:
            continue

        table = PrettyTable()
        table.field_names = ["Zugnummer", "Bahnhof", "Loknummer", "Ankunft", "Abfahrt"]
        for row in data:
            table.add_row([
                row.get("train_number", ""),
                row.get("name", ""),
                row.get("unit_number", ""),
                row.get("arrival", ""),
                row.get("departure", ""),
            ])
        table_str = str(table)  # convert the table to a string

        if len(table_str) > MAX_MESSAGE_LENGTH:
            # Nachricht ist zu lang für Discord
            # Teile die Nachricht in mehrere Teile auf
            table_list = table_str.split("\n")
            table_parts = []
            part = ""
            for row in table_list:
                if len(part + row) > MAX_MESSAGE_LENGTH:
                    table_parts.append(part)
                    part = row + "\n"
                else:
                    part += row + "\n"
            if part:
                table_parts.append(part)

            # Schicke die aufgeteilte Nachricht an den Nutzer
            for i, part in enumerate(table_parts):
                if i == 0:
                    await ctx.send(f"Hier ist der Fahrplan für Lok {loktyp} {loknummer}:", delete_after=10.0)
                else:
                    await asyncio.sleep(0.5)
                await ctx.send(f"```\n{part}\n```")
        else:
            await ctx.send(f"Hier ist der Fahrplan für Lok {loktyp} {loknummer}:")
            await ctx.send(f"```\n{table_str}\n```")

        # Schicke die Nachricht in den gewünschten Channel
        channel = bot.get_channel(channel_id)
        if channel:
            await channel.send(f"Der Fahrplan für Lok {loktyp} {loknummer} wurde abgerufen:")
            await channel.send(f"```\n{table_str}\n```")
        else:
            await ctx.send("Der angegebene Channel existiert nicht.")


# bot.command(name="lok")
async def choose_loktyp(ctx):
    await ctx.send(
        "Zu welchem Loktyp möchtest du alle Loknummern mit Fahrplänen haben? (2016, 1016, 1116, 1216, 5047, 4746, 4748, 5022, 1144, 1142)")
    loktyp_message = await bot.wait_for("message", check=lambda message: message.author == ctx.author)

    loktyp = loktyp_message.content.lower()
    if loktyp not in loktypen:
        await ctx.send(f"Ungültiger Loktyp. Gültige Werte sind: {', '.join(loktypen)}")
        return

    channel_id = 1105569996714803230  # Channel ID to send the table to
    channel = bot.get_channel(channel_id)
    await channel.send("**Kann kurz dauern!**")
    # Rest of the code

    if loktyp == "1142":
        start_num = 500
        end_num = 700
    else:
        start_num = 0
        end_num = 201

    for num in range(start_num, end_num):
        loknummer = f"{num:03d}"
        url = f"https://konzern-apps.web.oebb.at/lok/index/{loktyp}.0{loknummer}"
        response = requests.get(url)
        json_data = response.content.decode('utf-8')
        data = json.loads(json_data)

        stops = {}  # Dictionary to store train numbers and their stops
        train_numbers = set()  # Set to store train numbers with no other train number above or below them

        for row in data:
            if row["departure"] is not None:
                departure_time = datetime.fromisoformat(row["departure"].replace("Z", "+00:00"))
                row["departure"] = (departure_time + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S")
                row["departure"] = row["departure"].replace("2023-", "").replace("T", " ")
                row["departure"] = row["departure"][:row["departure"].find(":") + 3]

            if row["arrival"] is not None:
                arrival_time = datetime.fromisoformat(row["arrival"].replace("Z", "+00:00"))
                row["arrival"] = (arrival_time + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S")
                row["arrival"] = row["arrival"].replace("2023-", "").replace("T", " ")
                row["arrival"] = row["arrival"][:row["arrival"].find(":") + 3]

            train_number = row.get("train_number")
            if train_number:
                try:
                    train_number_int = int(train_number)
                    stops.setdefault(train_number_int, []).append(row["name"])
                    if not any(train_number_int - i in train_numbers or train_number_int + i in train_numbers for i in
                               range(1, 5)):
                        train_numbers.add(train_number_int)
                except ValueError:
                    pass

        if not data:
            continue

        table = PrettyTable()
        table.field_names = ["Zugnummer", "Bahnhof", "Loknummer", "Ankunft", "Abfahrt"]
        for row in data:
            table.add_row([
                row.get("train_number", ""),
                row.get("name", ""),
                row.get("unit_number", ""),
                row.get("arrival", ""),
                row.get("departure", ""),
            ])
        table_str = str(table)  # convert the table to a string

        if len(table_str) > MAX_MESSAGE_LENGTH:
            # Nachricht ist zu lang für Discord
            # Teile die Nachricht in mehrere Teile auf
            table_list = table_str.split("\n")
            table_parts = []
            part = ""
            for row in table_list:
                if len(part + row) > MAX_MESSAGE_LENGTH:
                    table_parts.append(part)
                    part = row + "\n"
                else:
                    part += row + "\n"
            if part:
                table_parts.append(part)

            # Schicke die aufgeteilte Nachricht an den angegebenen Channel
            for part in table_parts:
                await channel.send(f"```\n{part}```")
        else:
            # Schicke die Nachricht an den angegebenen Channel
            await channel.send(f"```\n{table_str}```")


bot.run(DISCORD_TOKEN)









import asyncio
import json
import random
import re
import sys
import time
from time import sleep
from io import StringIO
import requests
import discord
from discord.ext import commands

from BotProfiles.Adept import Adept
from BotProfiles.ANB import ANB
from BotProfiles.Balko import Balko
from BotProfiles.Cyber import Cyber
from BotProfiles.Dashe import Dashe
from BotProfiles.Eve import Eve
from BotProfiles.Feather import Feather
from BotProfiles.Hastey import Hastey
from BotProfiles.Kinesis import Kinesis
from BotProfiles.Kodai import Kodai
from BotProfiles.Mek import Mek
from BotProfiles.NSB import NSB
from BotProfiles.PD import PD
from BotProfiles.Phantom import Phantom
from BotProfiles.Polaris import Polaris
from BotProfiles.Prism import Prism
from BotProfiles.Rush import Rush
from BotProfiles.SoleAIO import SoleAIO
from BotProfiles.SplashForce import SplashForce
from BotProfiles.TKS import TKS
from BotProfiles.Tohru import Tohru
from BotProfiles.Velox import Velox
from BotProfiles.WhatBot import WhatBot
from BotProfiles.Wrath import Wrath
from BotProfiles.Fluid import Fluid

from Config import Config
from Profile import Profile

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
regex_custom = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
token = 'NzQ5MTA0NTM4NDk3MTg3OTAw.X0nH9w.opu4UYUODKxv2A2M1aRcQKy4oJA'
supported_bots = {
    'adept': Adept(),
    'anb': ANB(),
    'balko': Balko(),
    'cyber': Cyber(),
    'dashe': Dashe(),
    'eve': Eve(),
    'feather': Feather(),
    'kinesis': Kinesis(),
    'hastey': Hastey(),
    'kodai': Kodai(),
    'mek': Mek(),
    'nsb': NSB(),
    'pd': PD(),
    'phantom': Phantom(),
    'polaris': Polaris(),
    'prism': Prism(),
    'rush': Rush(),
    'soleaio': SoleAIO(),
    'splashforce': SplashForce(),
    'tks': TKS(),
    'tohru': Tohru(),
    'velox': Velox(),
    'wrath': Wrath(),
    'whatbot': WhatBot(),
    'fluid': Fluid(),
    'template': None
}
client = commands.Bot(command_prefix="!", help_command=None)
client.remove_command('help')


def validate_email(email):
    if re.search(regex, email) or re.search(regex_custom, email):
        return True
    else:
        return False


def create_embed():
    embed = discord.Embed(
        color=discord.Colour.green()
    )
    embed.set_footer(text="Your information is not saved.\tMade by: nokiny#0001",
                     icon_url="https://cdn.discordapp.com/avatars/164478290168381450/11af8b7982a8e7797d6bb86dcd4ec0ce.png?size=256")
    return embed


def has_numbers(input):
    return any(char.isdigit() for char in input)


def isValid(number):
    # Return true if the card number is valid
    # hint you will have to call function sumOfDoubleEvenPlace() and sumOfOddPlace
    even_sum = sumOfDoubleEvenPlace(number)
    odd_sum = sumOfOddPlace(number)
    return (even_sum + odd_sum) % 10 == 0


def sumOfDoubleEvenPlace(number):
    flag = False
    total = 0
    while number > 0:
        if flag:
            total += getDigit(2 * (number % 10))
        flag = not flag
        number //= 10
    return total


def getDigit(number):
    if number < 10:
        return number
    else:
        return getDigit((number // 10) + (number % 10))


def sumOfOddPlace(number):
    flag = True
    total = 0
    while number > 0:
        if flag:
            total += number % 10
        flag = not flag
        number //= 10
    return total


def minute_passed(minutes, oldepoch):
    print(minutes)
    print(oldepoch)
    print(time.time())
    print(time.time() - oldepoch >= minutes * 60)
    return time.time() - oldepoch >= minutes * 60


def hour_passed(hours, oldepoch):
    return time.time() - oldepoch >= hours * 60 * 60


def day_passed(days, oldepoch):
    return time.time() - oldepoch >= days * 86400


def getKeysByValue(dictOfElements, valueToFind):
    element = ""
    for item in dictOfElements.items():
        if item[1] == valueToFind:
            element = item[0]
    return element


async def is_dm_check(ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        return True
    else:
        return False


async def add_user_file(ctx):
    def check(msg):
        if msg.author == ctx and isinstance(msg.channel, discord.DMChannel) and not msg.author.bot:
            return msg.content

    cnt = await client.wait_for('message', check=check, timeout=90)
    cnt = cnt.content
    return cnt


export_embed = create_embed().add_field(name='Export to another bot?', value='Respond: Yes or No')

bots = ""
for bot in supported_bots:
    bots += f"{bot}\n"
export_embed_bot_question = create_embed().add_field(name='What bot would you like to export to?',
                                                     value=f'Respond with: \n{bots}')
thank_you_embed = create_embed().add_field(name="Thank you for using Profile Manager!",
                                           value="See you soon!")

async def create_profile_catchall(ctx, use_input_profile_name, catch_all):
    if use_input_profile_name:
        def check(msg):
            if isinstance(msg.channel,
                          discord.channel.DMChannel) and not msg.author.bot and msg.author.id == ctx.id:
                return msg.content
    else:
        def check(msg):
            if isinstance(msg.channel,
                          discord.channel.DMChannel) and not msg.author.bot and msg.author.id == ctx.message.author.id:
                return msg.content

    config = Config()
    embed = discord.Embed(
        color=discord.Colour.green(),
        title='**Welcome to the Profile Creator!**\n',
        description='*Follow the step by step instructions to create your file.*\n\n__*Please mimic '
                    'the formatted examples **exactly**.*__\n\n**To start, react** ✅. '
    )
    embed.set_footer(text="Your information is not saved.\tMade by: nokiny#0001",
                     icon_url="https://cdn.discordapp.com/avatars/164478290168381450/11af8b7982a8e7797d6bb86dcd4ec0ce.png?size=256")
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('✅')
    await client.wait_for('reaction_add',
                          check=lambda reaction,
                                       user: not user.bot and reaction.emoji == '✅' and reaction.message.id == msg.id,
                          timeout=120)
    while True:

        embed = create_embed().add_field(name='To start, enter the name for the profile.',
                                         value='Example: Profile1')
        await ctx.send(embed=embed)
        embed.clear_fields()
        profile_name = await client.wait_for('message', check=check, timeout=90)
        profile_name = profile_name.content
        print(">>>>> Received profile name")
        embed = create_embed().add_field(name='To start, please enter your first and last name.',
                                         value='Example: John Smith')
        await ctx.send(embed=embed)

        while True:
            name = await client.wait_for('message', check=check, timeout=90)
            name = name.content
            if len(name.split()) != 2:
                embed = create_embed().add_field(name='Try again!',
                                                 value='Incorrect format\n\nExample: John Smith')
                await ctx.send(embed=embed)
            else:
                break
        print(">>>>> Received name")

        embed = create_embed().add_field(name='Hello {0} please enter your email address!'.format(name),
                                         value='Example: nokiny@gmail.com')
        await ctx.send(embed=embed)

        while True:
            email = await client.wait_for('message', check=check, timeout=90)
            email = email.content
            if validate_email(email.lower()):
                email = email.lower()
                break
            else:
                embed = create_embed().add_field(name='Try again!',
                                                 value='Incorrect format\n\nExample: nokiny@gmail.com')
                await ctx.send(embed=embed)
        print(">>>>> Received email")

        embed = create_embed().add_field(name='Please enter your address'.format(name),
                                         value='Example: 123 Example St')
        await ctx.send(embed=embed)

        address = await client.wait_for('message', check=check, timeout=90)
        address = address.content
        print(">>>>> Received address")

        embed = create_embed().add_field(
            name='Please enter your apt number, if applicable, if not, respond None.'.format(name),
            value='Example: 104 ***or*** None')
        await ctx.send(embed=embed)

        while True:
            apt = await client.wait_for('message', check=check, timeout=90)
            if has_numbers(apt.content):
                apt = apt.content
                break
            elif apt.content.lower() == "none":
                apt = ""
                break
            else:
                embed = create_embed().add_field(name='Try again!',
                                                 value='Incorrect format.\nExample: 104 ***or*** None')
                await ctx.send(embed=embed)
        print(">>>>> Received apt")

        embed = create_embed().add_field(name='Please enter shipping/billing city, these must be the same.',
                                         value='Example: New York City')
        await ctx.send(embed=embed)

        city = await client.wait_for('message', check=check, timeout=90)
        city = city.content
        print(">>>>> Received city")

        embed = create_embed().add_field(name='Please enter shipping/billing state.',
                                         value='Example: New York ***or*** NY')
        await ctx.send(embed=embed)

        while True:
            state = await client.wait_for('message', check=check, timeout=90)
            state = state.content
            if state in config.us_state_abbreviations.keys():
                break
            elif state in config.us_state_abbreviations.values():
                state = getKeysByValue(config.us_state_abbreviations, state)
                break
            else:
                embed = create_embed().add_field(name='Try again!',
                                                 value='Incorrect format.\nExample: New York ***or*** NY')
                await ctx.send(embed=embed)
        print(">>>>> Received state")

        embed = create_embed().add_field(name='Please enter shipping/biling zipcode.',
                                         value='Example: 10021')
        await ctx.send(embed=embed)

        zip_code = await client.wait_for('message', check=check, timeout=90)
        zip_code = zip_code.content
        print(">>>>> Received zipcode")

        embed = create_embed().add_field(name='Please enter your country.',
                                         value='Example: United States ***or*** US')
        await ctx.send(embed=embed)

        while True:
            country = await client.wait_for('message', check=check, timeout=90)
            country = country.content
            if country in config.country_abbrev.keys():
                break
            elif country in config.country_abbrev.values():
                country = getKeysByValue(config.country_abbrev, country)
                break
            else:
                embed = create_embed().add_field(name='Try again!',
                                                 value='Incorrect format.\n Example: United States ***or*** '
                                                       'US')
                await ctx.send(embed=embed)
        print(">>>>> Received country")

        embed = create_embed().add_field(name='Please enter your phone number.',
                                         value='Example: 1231231234')
        await ctx.send(embed=embed)

        phone_number = await client.wait_for('message', check=check, timeout=90)
        phone_number = phone_number.content

        embed = create_embed().add_field(name='Please enter the cardholder name.',
                                         value='Example: John Smith')
        await ctx.send(embed=embed)

        while True:
            card_holder_name = await client.wait_for('message', check=check, timeout=90)
            card_holder_name = card_holder_name.content
            if len(card_holder_name.split()) != 2:
                embed = create_embed().add_field(name='Try again!',
                                                 value='Incorrect format\n\nExample: John Smith')
                await ctx.send(embed=embed)
            else:
                break
        print(">>>>> Received card holder name")

        embed = create_embed().add_field(name='Please enter card number.',
                                         value='Example: 3716820019271998    ')
        await ctx.send(embed=embed)

        while True:
            card_number = await client.wait_for('message', check=check, timeout=90)
            card_number = card_number.content
            if isValid(int(card_number)):
                break
            else:
                embed = create_embed().add_field(name='Try again!',
                                                 value='Invalid card number!\nExample: 3716820019271998')
                await ctx.send(embed=embed)
        print(">>>>> Received card number")

        embed = create_embed().add_field(name='Please enter expiration date.',
                                         value="Example: 03 / 22\n\n*Note: add a space before and after the /*")
        await ctx.send(embed=embed)

        while True:
            exp_date = await client.wait_for('message', check=check, timeout=90)
            exp_date = exp_date.content
            if ' / ' in exp_date:
                break
            else:
                embed = create_embed().add_field(name='Try again!',
                                                 value='Incorrect format.\n Example: 03 / 22')
                await ctx.send(embed=embed)
        print(">>>>> Received exp date")

        embed = create_embed().add_field(name='Please enter the cvv.', value="Example: 599")
        await ctx.send(embed=embed)

        cvv = await client.wait_for('message', check=check, timeout=90)
        cvv = cvv.content
        print(">>>>> Received cvv")

        embed = create_embed().add_field(name='Verification',
                                         value='Validate the information below, if it is correct react '
                                               '✅ if it is not correct, react ❎.\nIf it is not correct, bot may take some time to restart.',
                                         inline=False)
        embed.add_field(name='Provided information',
                        value=f'Profile Name: {profile_name}\nName: {name}\nEmail: {email}\nAddress: {address}\nApt: {apt}\nCity: {city}\n'
                              f'Zip Code: {zip_code}\nState: {state}\nCountry: {country}\nPhone: {phone_number}\nCard Holder Name: {card_holder_name}\nCard Number: {card_number}\nExp Date: {exp_date}\nCVV: {cvv}')
        msg = await ctx.send(embed=embed)

        await msg.add_reaction('✅')
        await msg.add_reaction('❎')
        reaction, user = await client.wait_for('reaction_add',
                                               check=lambda reaction,
                                                            user: not user.bot and reaction.emoji == '✅' or not user.bot and reaction.emoji == '❎' and reaction.message.id == msg.id,
                                               timeout=90)
        if str(reaction) == '✅':
            break
        if str(reaction) == '❎':
            print('Invalid information, restarting...')

    if use_input_profile_name:
        print(f"Successfully created profile for {ctx.name}!")
        email = email.split("@")[0] + f"@{catch_all}"
        return Profile(profile_name=ctx.name, address=address, apt=apt, city=city, country=country,
                       first_name=name.split()[0], last_name=name.split()[1], phone=phone_number,
                       state=state,
                       zip_code=zip_code, card_holder_name=card_holder_name, card_number=card_number,
                       exp_date=exp_date, cvv=cvv, email=email)
    else:
        return Profile(profile_name=profile_name, address=address, apt=apt, city=city, country=country,
                       first_name=name.split()[0], last_name=name.split()[1], phone=phone_number,
                       state=state,
                       zip_code=zip_code, card_holder_name=card_holder_name, card_number=card_number,
                       exp_date=exp_date, cvv=cvv, email=email)


async def create_profile(ctx, use_input_profile_name):
    if use_input_profile_name:
        def check(msg):
            if isinstance(msg.channel,
                          discord.channel.DMChannel) and not msg.author.bot and msg.author.id == ctx.id:
                return msg.content
    else:
        def check(msg):
            if isinstance(msg.channel,
                          discord.channel.DMChannel) and not msg.author.bot and msg.author.id == ctx.message.author.id:
                return msg.content

    config = Config()
    embed = discord.Embed(
        color=discord.Colour.green(),
        title='**Welcome to the Profile Creator!**\n',
        description='*Follow the step by step instructions to create your file.*\n\n__*Please mimic '
                    'the formatted examples **exactly**.*__\n\n**To start, react** ✅. '
    )
    embed.set_footer(text="Your information is not saved.\tMade by: nokiny#0001",
                     icon_url="https://cdn.discordapp.com/avatars/164478290168381450/11af8b7982a8e7797d6bb86dcd4ec0ce.png?size=256")
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('✅')
    await client.wait_for('reaction_add',
                          check=lambda reaction,
                                       user: not user.bot and reaction.emoji == '✅' and reaction.message.id == msg.id,
                          timeout=120)
    while True:

        embed = create_embed().add_field(name='To start, enter the name for the profile.',
                                         value='Example: Profile1')
        await ctx.send(embed=embed)
        embed.clear_fields()
        profile_name = await client.wait_for('message', check=check, timeout=90)
        profile_name = profile_name.content
        print(">>>>> Received profile name")
        embed = create_embed().add_field(name='To start, please enter your first and last name.',
                                         value='Example: John Smith')
        await ctx.send(embed=embed)

        while True:
            name = await client.wait_for('message', check=check, timeout=90)
            name = name.content
            if len(name.split()) != 2:
                embed = create_embed().add_field(name='Try again!',
                                                 value='Incorrect format\n\nExample: John Smith')
                await ctx.send(embed=embed)
            else:
                break
        print(">>>>> Received name")

        embed = create_embed().add_field(name='Hello {0} please enter your email address!'.format(name),
                                         value='Example: nokiny@gmail.com')
        await ctx.send(embed=embed)

        while True:
            email = await client.wait_for('message', check=check, timeout=90)
            email = email.content
            if validate_email(email.lower()):
                email = email.lower()
                break
            else:
                embed = create_embed().add_field(name='Try again!',
                                                 value='Incorrect format\n\nExample: nokiny@gmail.com')
                await ctx.send(embed=embed)
        print(">>>>> Received email")

        embed = create_embed().add_field(name='Please enter your address'.format(name),
                                         value='Example: 123 Example St')
        await ctx.send(embed=embed)

        address = await client.wait_for('message', check=check, timeout=90)
        address = address.content
        print(">>>>> Received address")

        embed = create_embed().add_field(
            name='Please enter your apt number, if applicable, if not, respond None.'.format(name),
            value='Example: 104 ***or*** None')
        await ctx.send(embed=embed)

        while True:
            apt = await client.wait_for('message', check=check, timeout=90)
            if has_numbers(apt.content):
                apt = apt.content
                break
            elif apt.content.lower() == "none":
                apt = ""
                break
            else:
                embed = create_embed().add_field(name='Try again!',
                                                 value='Incorrect format.\nExample: 104 ***or*** None')
                await ctx.send(embed=embed)
        print(">>>>> Received apt")

        embed = create_embed().add_field(name='Please enter shipping/billing city, these must be the same.',
                                         value='Example: New York City')
        await ctx.send(embed=embed)

        city = await client.wait_for('message', check=check, timeout=90)
        city = city.content
        print(">>>>> Received city")

        embed = create_embed().add_field(name='Please enter shipping/billing state.',
                                         value='Example: New York ***or*** NY')
        await ctx.send(embed=embed)

        while True:
            state = await client.wait_for('message', check=check, timeout=90)
            state = state.content
            if state in config.us_state_abbreviations.keys():
                break
            elif state in config.us_state_abbreviations.values():
                state = getKeysByValue(config.us_state_abbreviations, state)
                break
            else:
                embed = create_embed().add_field(name='Try again!',
                                                 value='Incorrect format.\nExample: New York ***or*** NY')
                await ctx.send(embed=embed)
        print(">>>>> Received state")

        embed = create_embed().add_field(name='Please enter shipping/biling zipcode.',
                                         value='Example: 10021')
        await ctx.send(embed=embed)

        zip_code = await client.wait_for('message', check=check, timeout=90)
        zip_code = zip_code.content
        print(">>>>> Received zipcode")

        embed = create_embed().add_field(name='Please enter your country.',
                                         value='Example: United States ***or*** US')
        await ctx.send(embed=embed)

        while True:
            country = await client.wait_for('message', check=check, timeout=90)
            country = country.content
            if country in config.country_abbrev.keys():
                break
            elif country in config.country_abbrev.values():
                country = getKeysByValue(config.country_abbrev, country)
                break
            else:
                embed = create_embed().add_field(name='Try again!',
                                                 value='Incorrect format.\n Example: United States ***or*** '
                                                       'US')
                await ctx.send(embed=embed)
        print(">>>>> Received country")

        embed = create_embed().add_field(name='Please enter your phone number.',
                                         value='Example: 1231231234')
        await ctx.send(embed=embed)

        phone_number = await client.wait_for('message', check=check, timeout=90)
        phone_number = phone_number.content

        embed = create_embed().add_field(name='Please enter the cardholder name.',
                                         value='Example: John Smith')
        await ctx.send(embed=embed)

        while True:
            card_holder_name = await client.wait_for('message', check=check, timeout=90)
            card_holder_name = card_holder_name.content
            if len(card_holder_name.split()) != 2:
                embed = create_embed().add_field(name='Try again!',
                                                 value='Incorrect format\n\nExample: John Smith')
                await ctx.send(embed=embed)
            else:
                break
        print(">>>>> Received card holder name")

        embed = create_embed().add_field(name='Please enter card number.',
                                         value='Example: 3716820019271998    ')
        await ctx.send(embed=embed)

        while True:
            card_number = await client.wait_for('message', check=check, timeout=90)
            card_number = card_number.content
            if isValid(int(card_number)):
                break
            else:
                embed = create_embed().add_field(name='Try again!',
                                                 value='Invalid card number!\nExample: 3716820019271998')
                await ctx.send(embed=embed)
        print(">>>>> Received card number")

        embed = create_embed().add_field(name='Please enter expiration date.',
                                         value="Example: 03 / 22\n\n*Note: add a space before and after the /*")
        await ctx.send(embed=embed)

        while True:
            exp_date = await client.wait_for('message', check=check, timeout=90)
            exp_date = exp_date.content
            if ' / ' in exp_date:
                break
            else:
                embed = create_embed().add_field(name='Try again!',
                                                 value='Incorrect format.\n Example: 03 / 22')
                await ctx.send(embed=embed)
        print(">>>>> Received exp date")

        embed = create_embed().add_field(name='Please enter the cvv.', value="Example: 599")
        await ctx.send(embed=embed)

        cvv = await client.wait_for('message', check=check, timeout=90)
        cvv = cvv.content
        print(">>>>> Received cvv")

        embed = create_embed().add_field(name='Verification',
                                         value='Validate the information below, if it is correct react '
                                               '✅ if it is not correct, react ❎.\nIf it is not correct, bot may take some time to restart.',
                                         inline=False)
        embed.add_field(name='Provided information',
                        value=f'Profile Name: {profile_name}\nName: {name}\nEmail: {email}\nAddress: {address}\nApt: {apt}\nCity: {city}\n'
                              f'Zip Code: {zip_code}\nState: {state}\nCountry: {country}\nPhone: {phone_number}\nCard Holder Name: {card_holder_name}\nCard Number: {card_number}\nExp Date: {exp_date}\nCVV: {cvv}')
        msg = await ctx.send(embed=embed)

        await msg.add_reaction('✅')
        await msg.add_reaction('❎')
        reaction, user = await client.wait_for('reaction_add',
                                               check=lambda reaction,
                                                            user: not user.bot and reaction.emoji == '✅' or not user.bot and reaction.emoji == '❎' and reaction.message.id == msg.id,
                                               timeout=90)
        if str(reaction) == '✅':
            break
        if str(reaction) == '❎':
            print('Invalid information, restarting...')

    if use_input_profile_name:
        print(f"Successfully created profile for {ctx.name}!")
        return Profile(profile_name=ctx.name, address=address, apt=apt, city=city, country=country,
                       first_name=name.split()[0], last_name=name.split()[1], phone=phone_number,
                       state=state,
                       zip_code=zip_code, card_holder_name=card_holder_name, card_number=card_number,
                       exp_date=exp_date, cvv=cvv, email=email)
    else:
        return Profile(profile_name=profile_name, address=address, apt=apt, city=city, country=country,
                       first_name=name.split()[0], last_name=name.split()[1], phone=phone_number,
                       state=state,
                       zip_code=zip_code, card_holder_name=card_holder_name, card_number=card_number,
                       exp_date=exp_date, cvv=cvv, email=email)


@client.event
async def on_ready():
    print("Bot is running...")


@client.command()
async def help(ctx):
    embed = create_embed()
    embed.title = "**Welcome to the Profile Manager!**"
    embed.description = "This will help keep all of your bot profiles managed!\nIt will also eliminate errors from " \
                        "forms. "
    embed.add_field(name="Commands", value="`!convert`\nConverts the .csv template to any bot "
                                           "format\n`!combine [bot_name]`\nUser sends files containging 1 or more "
                                           "specific bot profile (1 at a time) and combines it to 1 file for the given "
                                           "bot\n`!create [bot_name]`\nCreates 1 profile for the given "
                                           "bot\n`!start [time] [amount_of_aco] [#channel] [aco_item]`\nCreates a "
                                           "giveaway type ACO, FCFS react style.\nWhen giveaway is over, users will "
                                           "get messaged with steps to complete.\nOnce all users complete the steps, "
                                           "the host gets sent a file to convert\n!`!supported`\nLists all currently "
                                           "supported bots\n`!template`\nGives "
                                           "user the template to mass create profiles!")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/164478290168381450/11af8b7982a8e7797d6bb86dcd4ec0ce"
                            ".png?size=256")
    await ctx.message.author.send(embed=embed)


@client.command()
@commands.check(is_dm_check)
async def template(ctx):
    embed = create_embed().add_field(name=f'Welcome {ctx.message.author.name} 👑!',
                                     value='\nHere is the link to the template I use 😁\n\n[Click me!](https://docs.google.com/spreadsheets/d/1z_xpRhGZbSjUMYKpQsMxt9yBtBESjmppaDRE9WkBQ0E/copy)\n\n*Fill out this template correctly and then export it as a .csv to convert your profiles to any bot format!*')
    await ctx.message.author.send(embed=embed)


@client.command()
async def start(ctx):
    def check(msg):
        if isinstance(msg.channel,
                      discord.channel.DMChannel) and not msg.author.bot and msg.author.id == ctx.message.author.id:
            return msg.content

    await ctx.message.delete()
    author = ctx.message.author.id
    message = str(ctx.message.content).split()
    profiles = []
    print(message[4].split()[0])
    if len(message) > 5:
        total_slots = message[2]
        channel = client.get_channel(int(message[3][2:-1]))
        given_time = message[1]
        time_type = given_time[len(given_time) - 1]
        catch_all = message[4]
        if time_type == "h":
            if given_time[:-1] == "1":
                time_type = "hour"
            else:
                time_type = "hours"
        elif time_type == "d":
            if given_time[:-1] == "1":
                time_type = "day"
            else:
                time_type = "days"
        elif time_type == 'm':
            if given_time[:-1] == "1":
                time_type = "minute"
            else:
                time_type = "minutes"
        else:
            await ctx.send("Invalid time given.\nValid time examples: 2m 4h 3d")
        slot_for = message[5:]
        giveaway = ""
        for s in slot_for:
            giveaway += f"{s} "
        embed = create_embed()
        embed.set_footer(text="Made by: nokiny#0001",
                         icon_url="https://cdn.discordapp.com/avatars/164478290168381450/11af8b7982a8e7797d6bb86dcd4ec0ce.png?size=256")
        embed.set_author(name=f"{giveaway}")
        embed.description = f"\n\nReact 👑 to enter!\nACO will be up for {given_time[:-1]} {time_type}.\nHosted by: <@{author}>"
        embed.add_field(name="\u200b", value="[Terms and Conditions](https://pastebin.com/Uw0acC1M)", inline=False)
        react = await channel.send(f":tada: New ACO! :tada:", embed=embed)
        await react.add_reaction('👑')
        count = 0
        users = []
        length = False
        start_time = time.time()

        while count != int(total_slots) and length == False:
            try:
                reaction, user = await client.wait_for('reaction_add', check=lambda reaction,
                                                                                    user: not user.bot and reaction.emoji == '👑' and reaction.message.id == react.id,
                                                       timeout=70)
                count += 1
                users.append(user)
            except:
                if time_type == "hour" or time_type == "hours":
                    length = hour_passed(hours=int(given_time[:-1]), oldepoch=start_time)
                elif time_type == "minute" or time_type == "minutes":
                    length = minute_passed(minutes=int(given_time[:-1]), oldepoch=start_time)
                elif time_type == "day" or time_type == "days":
                    length = day_passed(days=int(given_time[:-1]), oldepoch=start_time)
                print("Checking time...")
        embed = create_embed()
        embed.set_footer(text="Made by: nokiny#0001",
                         icon_url="https://cdn.discordapp.com/avatars/164478290168381450/11af8b7982a8e7797d6bb86dcd4ec0ce.png?size=256")
        embed.add_field(name=f"{giveaway}", value="\u200b", inline=False)
        embed.add_field(name=f":tada: ACO has ended! :tada:", value=f"\u200b")
        embed.add_field(name="\u200b", value="[Terms and Conditions](https://pastebin.com/Uw0acC1M)", inline=False)
        await react.edit(embed=embed)
        finished = {}
        reactors = ""
        for user in users:
            reactors += f'<@{user.id}>\n'
        embed = discord.Embed(
            title="Your ACO has ended!",
            description="Please wait as users fill out their info.\nOnce every user completes their info, I will send you your file to convert.",
            color=discord.Colour.green()
        )

        embed.add_field(name="Users", value=reactors)

        await ctx.author.send(embed=embed)
        print(f"ACO for {ctx.message.author} has ended.. messaging winners now.")
        len_users = len(users)
        tally = {}
        for i in range(len_users):

            user = random.choice(users)
            users.remove(user)
            tally[user] = ""
            print(f"Currently messaging: {user}...")

            def check_user(msg):
                if isinstance(msg.channel,
                              discord.channel.DMChannel) and not msg.author.bot and msg.author.id == user.id:
                    return msg.content

            try:
                embed = create_embed().add_field(
                    name=f":tada: Congratulations! You have won the ACO hosted by {ctx.message.author.name} :tada:\n\nPlease enter your size.",
                    value="Example:\n10\nMedium\nN/A")
                embed.add_field(name="\u200b",
                                value="*You will have 2 minutes to respond to each message.\nFailure to do so will result in a loss of your ACO.*",
                                inline=False)
                await user.send(embed=embed)
                try:
                    size = await client.wait_for('message', check=check_user, timeout=120)
                    finished[user] = size.content
                except asyncio.TimeoutError:
                    print("ACO winner did not respond.")
                    continue

                embed = create_embed().add_field(
                    name=f"Please enter your email address.", value="Example:\nnokiny@gmail.com\n**This will be the email that your order confirmation(s) get sent to.**")
                await user.send(embed=embed)
                try:
                    email = await client.wait_for('message', check=check_user, timeout=120)
                    email = email.content
                except asyncio.TimeoutError:
                    print("ACO winner did not respond.")
                    continue

                tally[user] = f'{email},{size.content}'

                embed = create_embed().add_field(
                    name="Submission",
                    value="You have two options:\nWould you like to send in my formatted .csv file?\nOr create your profile now?\n\n\n**React:**\n✍️\n(to create profile now)\n💾\n(to send in .csv file)\n")
                msg = await user.send(embed=embed)
                await msg.add_reaction('💾')
                await msg.add_reaction('✍️')
                try:
                    reaction, user = await client.wait_for('reaction_add',
                                                           check=lambda reaction,
                                                                        user: not user.bot and reaction.emoji == '💾' or not user.bot and reaction.emoji == '✍️' and reaction.message.id == msg.id,
                                                           timeout=120)
                except:
                    print("ACO winner did not respond.")
                    continue

                while True:
                    # msg = await client.wait_for('message', check=check_user, timeout=90)
                    if str(reaction) == "💾":
                        print(">>>>> Sending in csv file")
                        embed = create_embed().add_field(name="Send in your .csv file!",
                                                         value="When sending, make sure to add a comment or I will not receive it, resulting in losing your ACO!")
                        await user.send(embed=embed)
                        while True:
                            try:
                                file = await client.wait_for('message', check=check_user, timeout=120)
                            except asyncio.TimeoutError:
                                await user.send("Sorry, bot timed out and you have missed your chance for this ACO!")
                                break
                            if file.attachments:
                                for attachment in file.attachments:
                                    file = requests.get(url=attachment.url)
                                    content = StringIO(file.text)
                                    prof = []
                                    for line in content:
                                        prof.append(line)
                                    prof.remove(prof[0])
                                    for p in prof:
                                        info = p.rstrip().split(",")
                                        user_email = info[14].split("@")[0] + f"@{catch_all}"
                                        profile = Profile(profile_name=user.name, address=info[1], apt=info[2],
                                                          city=info[3],
                                                          country=info[4], first_name=info[5], last_name=info[6],
                                                          phone=info[7],
                                                          state=info[8], zip_code=info[9], card_holder_name=info[10],
                                                          card_number=info[11], exp_date=info[12], cvv=info[13],
                                                          email=user_email)
                                        profiles.append(profile)
                                await user.send("File has been received!")
                                print(">>>>> File received")
                                break
                            else:
                                embed = create_embed()
                                embed.add_field(name="No file was attached!",
                                                value="Try sending the file with a comment again.")
                                await user.send(embed=embed)
                    elif str(reaction) == "✍️":
                        try:
                            profiles.append(await create_profile_catchall(user, use_input_profile_name=True, catch_all=catch_all))
                            sent = True
                        except:
                            sent = False
                            print("ACO winnder did not respond.")
                        if sent:
                            await user.send("Information has been sent!")
                        else:
                            await user.send("Sorry, bot timed out and you have missed your chance at this ACO.")
                        break
                    else:
                        print("Wrong emoji")

                    break
            except Exception as e:
                print(sys.exc_info())
                print("ACO winner did not respond.")
                continue
            print("Moving onto next user...")
        all_users = ""
        for key, value in finished.items():
            all_users += f"<@{key.id}> | Size: {value}\n"
        if all_users != "":
            print("Sending host the file!")
            host_embed = create_embed().add_field(name="Your ACO has ended!",
                                                  value="Below is your .csv file which you can use to convert to any bot.")
            host_embed.add_field(name="Below is every user who won.", value=all_users, inline=False)
            await ctx.author.send(f"<@{ctx.author.id}>", embed=host_embed)

            formatted_profiles = "Profile Name,Address,Apt,City,Country,First Name,Last Name,Phone,State,Zip Code,Card Holder Name,Card Number,Exp Date,CVV,Email"
            for profile in profiles:
                if profile == profiles[len(profiles) - 1]:
                    formatted_profiles += (str(profile)[127:-1]) + "\n"
                else:
                    formatted_profiles += (str(profile)[127:-1])

            formatted_users = "Discord User,Email,Size,Successful,Paid\n"
            for key, value in tally.items():
                formatted_users += f'{key},{value},No,No\n'
            file_tracker = StringIO(formatted_users)
            file = StringIO(formatted_profiles)
            embed = create_embed().add_field(name="What bot would you like to export these profiles to?",
                                             value='\n'.join(str(support) for support in supported_bots.keys()))

            await ctx.author.send(embed=create_embed().add_field(name="Tracker File", value="Please use the above "
                                                                                            "file to keep track of "
                                                                                            "users and their "
                                                                                            "payments/successes."),
                                  file=discord.File(filename="{0}_Tracker.xlsx".format(ctx.message.author),
                                                    fp=file_tracker))
            await ctx.author.send(file=discord.File(filename="{0}_ACO.csv".format(ctx.message.author), fp=file),
                                  embed=embed)

            selected_bot = await client.wait_for('message', check=check_user, timeout=90)
            selected_bot = selected_bot.content
            if selected_bot in supported_bots.keys():
                print('Creating profile for: {0}'.format(ctx.message.author))
                try:
                    creating = True
                    while creating is True:
                        generator = supported_bots[selected_bot]
                        file = generator.create_profiles(profiles)
                        if selected_bot == "anb" or selected_bot == "rush":
                            await ctx.author.send(f'Your {selected_bot.upper()} file is here!',
                                                  file=discord.File(
                                                      filename="{0}_{1}.csv".format(ctx.message.author,
                                                                                    selected_bot.upper()),
                                                      fp=file))
                        elif selected_bot == "whatbot":
                            await ctx.author.send(f'Your {selected_bot.upper()} file is here!',
                                                  file=discord.File(
                                                      filename="{0}_{1}.db".format(ctx.message.author,
                                                                                   selected_bot.upper()),
                                                      fp=file))
                        elif selected_bot == "eve":
                            await ctx.author.send(f'Your {selected_bot.upper()} file is here!',
                                                  file=discord.File(
                                                      filename="{0}_{1}.xml".format(ctx.message.author,
                                                                                    selected_bot.upper()),
                                                      fp=file))
                        else:
                            await ctx.author.send(f'Your {selected_bot.upper()} file is here!',
                                                  file=discord.File(
                                                      filename="{0}_{1}.json".format(ctx.message.author,
                                                                                     selected_bot.upper()),
                                                      fp=file))

                        print('Profile created!')
                        await ctx.author.send(embed=export_embed)
                        another = await client.wait_for('message', check=check, timeout=30)
                        if another.content.lower() == "yes":
                            await ctx.author.send(embed=export_embed_bot_question)
                            selected_bot = await client.wait_for('message', check=check, timeout=30)
                            selected_bot = selected_bot.content
                        else:
                            await ctx.author.send(embed=thank_you_embed)
                            creating = False
                except KeyError:
                    embed = create_embed()
                    embed.add_field(name="Unsupported bot given.",
                                    value="Bot given is unsupported.\nTry again.")
                    await ctx.author.send(embed=embed)
                    await ctx.author.send(embed=export_embed_bot_question)
                    selected_bot = await client.wait_for('message', check=check, timeout=30)
                    selected_bot = selected_bot.content
        else:
            print("No one filled out their information | Did not send host the file.")
    else:
        await ctx.send("Invalid entry! Try again")


@client.command()
async def supported(ctx):
    embed = create_embed()
    bots = ""
    config = Config()
    for bot in supported_bots.keys():
        if bot == "template":
            bots += f"__**{bot}**__"
        else:
            bots += f"{bot}\n"
    embed.add_field(name=f'Supported Bots [{len(supported_bots)}]', value=bots)
    await ctx.send(embed=embed)


@client.command()
@commands.check(is_dm_check)
async def convert(ctx):
    def check(msg):
        if isinstance(msg.channel,
                      discord.channel.DMChannel) and not msg.author.bot and msg.author.id == ctx.message.author.id:
            return msg.content

    embed = create_embed().add_field(name="Please reply with your .csv file!",
                                     value="When uploading, **add the bot name** you would like to \nexport to in the **comment section**.\n\n***If the bot name is not added, I will not be able to convert for you!***")
    await ctx.send(embed=embed)
    profiles = []
    try:
        while True:
            file = await client.wait_for('message', check=check, timeout=90)
            selected_bot = file.content
            if selected_bot in supported_bots:
                if file.attachments:
                    for a in file.attachments:
                        file = requests.get(url=a.url)
                        content = StringIO(file.text)
                        prof = []
                        for line in content:
                            prof.append(line)
                        prof.remove(prof[0])
                        for p in prof:
                            info = p.rstrip().split(",")
                            print(p)
                            profile = Profile(profile_name=info[0], address=info[1], apt=info[2], city=info[3],
                                              country=info[4], first_name=info[5], last_name=info[6], phone=info[7],
                                              state=info[8], zip_code=info[9], card_holder_name=info[10],
                                              card_number=info[11], exp_date=info[12], cvv=info[13], email=info[14])
                            profiles.append(profile)
                        creating = True
                        while creating is True:
                            generator = supported_bots[selected_bot]
                            file = generator.create_profiles(profiles)
                            try:
                                if selected_bot == "anb" or selected_bot == "rush":
                                    await ctx.send(f'Your {selected_bot.upper()} file is here!',
                                                   file=discord.File(
                                                       filename="{0}_{1}.csv".format(ctx.message.author,
                                                                                     selected_bot.upper()),
                                                       fp=file))
                                elif selected_bot == "whatbot":
                                    await ctx.send(f'Your {selected_bot.upper()} file is here!',
                                                   file=discord.File(
                                                       filename="{0}_{1}.db".format(ctx.message.author,
                                                                                    selected_bot.upper()),
                                                       fp=file))
                                elif selected_bot == "eve":
                                    await ctx.send(f'Your {selected_bot.upper()} file is here!',
                                                   file=discord.File(
                                                       filename="{0}_{1}.xml".format(ctx.message.author,
                                                                                     selected_bot.upper()),
                                                       fp=file))
                                else:
                                    await ctx.send(f'Your {selected_bot.upper()} file is here!',
                                                   file=discord.File(
                                                       filename="{0}_{1}.json".format(ctx.message.author,
                                                                                      selected_bot.upper()),
                                                       fp=file))

                                print('Profile created!')
                                await ctx.send(embed=export_embed)
                                another = await client.wait_for('message', check=check, timeout=60)
                                if another.content.lower() == "yes":
                                    await ctx.send(embed=export_embed_bot_question)
                                    selected_bot = await client.wait_for('message', check=check, timeout=60)
                                    selected_bot = selected_bot.content
                                else:
                                    await ctx.send(embed=thank_you_embed)
                                    creating = False
                            except KeyError:
                                embed = create_embed()
                                embed.add_field(name="Unsupported bot given.",
                                                value="Bot given is unsupported.\nTry again.")
                                await ctx.send(embed=embed)
                                await ctx.send(embed=export_embed_bot_question)
                                selected_bot = await client.wait_for('message', check=check, timeout=30)
                                selected_bot = selected_bot.content
                else:
                    embed = create_embed()
                    embed.add_field(name="No file was attached!", value="Try sending the file with the bot name again.")
                    await ctx.send(embed=embed)
            else:
                embed = create_embed()
                embed.add_field(name="Unsupported bot given.",
                                value="Bot given is unsupported.\n\nPlease send !convert ***again*** if you'd like to convert profiles.\n\nReply !supported to see a list of supported bots.")
                await ctx.send(embed=embed)
    except Exception as e:
        print(e)
        print(f"Bot has timed out for {ctx.message.author}")


@client.command()
@commands.check(is_dm_check)
async def combine(ctx):
    def check(msg):
        if isinstance(ctx.channel, discord.channel.DMChannel) and not msg.author.bot:
            return msg.content

    print(f"Combining profiles for {ctx.message.author}")
    message = ctx.message.content.split()
    selected_bot = message[1]
    profiles = []
    if selected_bot in supported_bots.keys():
        embed = create_embed().add_field(name="How many profiles would you like to convert to 1 file?",
                                         value="Example: 4")
        await ctx.send(embed=embed)
        while True:
            amount_of_files = await client.wait_for('message', check=check, timeout=90)
            amount_of_files = amount_of_files.content
            if amount_of_files.isdigit():
                break
            else:
                embed = create_embed().add_field(name="Invalid amount given!", value="Example: 4")
                await ctx.send(embed=embed)
        embed = create_embed().add_field(name="Please send your files 1 at a time.",
                                         value="Please add a message (can be random) with each file sent, or the bot "
                                               "will not receive it.")
        await ctx.send(embed=embed)
        for f in range(int(amount_of_files)):
            uploaded_file = await client.wait_for('message', check=check, timeout=90)
            embed = create_embed().add_field(name="File received!", value="Thank you!")
            await ctx.send(embed=embed)
            if uploaded_file.attachments:
                for a in uploaded_file.attachments:
                    file = requests.get(url=a.url)
                    generator = supported_bots[selected_bot]
                    profile = ""
                    if selected_bot == "anb" or selected_bot == "rush" or selected_bot == "eve":
                        content = StringIO(str(file.text))
                        for line in content:
                            profile += line
                        profiles.append(profile)
                    else:
                        profiles.append(json.loads(file.text))

        file = generator.create_profiles(profiles=profiles)

        if selected_bot == "anb" or selected_bot == "rush":
            await ctx.send(f'Your {selected_bot.upper()} file is here!',
                           file=discord.File(
                               filename="{0}_{1}.csv".format(ctx.message.author, selected_bot.upper()),
                               fp=file))
        elif selected_bot == "whatbot":
            await ctx.send(f'Your {selected_bot.upper()} file is here!',
                           file=discord.File(
                               filename="{0}_{1}.db".format(ctx.message.author, selected_bot.upper()),
                               fp=file))
        elif selected_bot == "eve":
            await ctx.send(f'Your {selected_bot.upper()} file is here!',
                           file=discord.File(
                               filename="{0}_{1}.xml".format(ctx.message.author, selected_bot.upper()),
                               fp=file))
        else:
            await ctx.send(f'Your {selected_bot.upper()} file is here!',
                           file=discord.File(
                               filename="{0}_{1}.json".format(ctx.message.author, selected_bot.upper()),
                               fp=file))
    else:
        embed = create_embed()
        embed.add_field(name="Unsupported bot given.",
                        value="Bot given is unsupported.\nReply !supported to see a list of supported bots.")
        await ctx.send(embed=embed)


@client.command()
@commands.check(is_dm_check)
async def create(ctx):
    def check(msg):
        if isinstance(msg.channel,
                      discord.channel.DMChannel) and not msg.author.bot and msg.author.id == ctx.message.author.id:
            return msg.content

    config = Config()
    message = ctx.message.content.split()
    selected_bot = message[1]

    if selected_bot in supported_bots.keys():
        if await is_dm_check(ctx):
            print('Creating profile for: {0}'.format(ctx.message.author))
            try:
                profile = await create_profile(ctx, use_input_profile_name=False)

                creating = True
                while creating is True:
                    try:

                        if selected_bot == "template":
                            file = StringIO(str(profile))
                            await ctx.send(f'Your {selected_bot.upper()} file is here!',
                                           file=discord.File(
                                               filename="{0}_{1}.csv".format(ctx.message.author, selected_bot.upper()),
                                               fp=file))

                        else:
                            generator = supported_bots[selected_bot]
                            file = generator.create_profile(profile)
                            if selected_bot == "anb" or selected_bot == "rush":
                                await ctx.send(f'Your {selected_bot.upper()} file is here!',
                                               file=discord.File(
                                                   filename="{0}_{1}.csv".format(ctx.message.author,
                                                                                 selected_bot.upper()),
                                                   fp=file))
                            elif selected_bot == "whatbot":
                                await ctx.send(f'Your {selected_bot.upper()} file is here!',
                                               file=discord.File(
                                                   filename="{0}_{1}.db".format(ctx.message.author,
                                                                                selected_bot.upper()),
                                                   fp=file))
                            elif selected_bot == "eve":
                                await ctx.send(f'Your {selected_bot.upper()} file is here!',
                                               file=discord.File(
                                                   filename="{0}_{1}.xml".format(ctx.message.author,
                                                                                 selected_bot.upper()),
                                                   fp=file))
                            else:
                                await ctx.send(f'Your {selected_bot.upper()} file is here!',
                                               file=discord.File(
                                                   filename="{0}_{1}.json".format(ctx.message.author,
                                                                                  selected_bot.upper()),
                                                   fp=file))

                        print('Profile created!')
                        await ctx.send(embed=export_embed)
                        another = await client.wait_for('message', check=check, timeout=30)
                        if another.content.lower() == "yes":
                            await ctx.send(embed=export_embed_bot_question)
                            selected_bot = await client.wait_for('message', check=check, timeout=30)
                            selected_bot = selected_bot.content
                        else:
                            await ctx.send(embed=thank_you_embed)
                            creating = False
                    except KeyError:
                        embed = create_embed()
                        embed.add_field(name="Unsupported bot given.",
                                        value="Bot given is unsupported.\nTry again.")
                        await ctx.send(embed=embed)
                        await ctx.send(embed=export_embed_bot_question)
                        selected_bot = await client.wait_for('message', check=check, timeout=30)
                        selected_bot = selected_bot.content

            except asyncio.TimeoutError:
                print(f'Bot has timed out for {ctx.message.author}')
                embed = create_embed()
                embed.add_field(name="Command has timed out...", value="Please run the !create command again!")
                await ctx.send(embed=embed)
    else:
        embed = create_embed()
        embed.add_field(name="Unsupported bot given.",
                        value="Bot given is unsupported.\nReply !supported to see a list of supported bots.")
        await ctx.send(embed=embed)


client.run(token)

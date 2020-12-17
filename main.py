import asyncio
import calendar
import json
import random
import re
import string
import time
from io import StringIO
import requests
import discord
from discord.ext import commands

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
regex_custom = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

token = 'NzQ5MTA0NTM4NDk3MTg3OTAw.X0nH9w.opu4UYUODKxv2A2M1aRcQKy4oJA'

client = commands.Bot(command_prefix="!")

us_state_abbreviations = us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands': 'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}
country_abbrev = {
    'Andorra': 'AN',
    'United Arab Emirates': 'AE',
    'Afghanistan': 'AF',
    'Antigua and Barbuda': 'AC',
    'Anguilla': 'AV',
    'Albania': 'AL',
    'Armenia': 'AM',
    'Angola': 'AO',
    'Antarctica': 'AY',
    'Argentina': 'AR',
    'American Samoa': 'AQ',
    'Austria': 'AU',
    'Australia': 'AS',
    'Aruba': 'AA',
    'Azerbaijan': 'AJ',
    'Bosnia and Herzegovina': 'BK',
    'Barbados': 'BB',
    'Bangladesh': 'BG',
    'Belgium': 'BE',
    'Burkina Faso': 'UV',
    'Bulgaria': 'BU',
    'Bahrain': 'BA',
    'Burundi': 'BY',
    'Benin': 'BN',
    'Saint Barthalemy': 'TB',
    'Bermuda': 'BD',
    'Brunei': 'BX',
    'Bolivia': 'BL',
    'Brazil': 'BR',
    'Bahamas': 'BF',
    'Bhutan': 'BT',
    'Bouvet Island': 'BV',
    'Botswana': 'BC',
    'Belarus': 'BO',
    'Belize': 'BH',
    'Canada': 'CA',
    'Cocos Islands': 'CK',
    'Democratic Republic of the Congo': 'CG',
    'Central African Republic': 'CT',
    'Republic of the Congo': 'CF',
    'Switzerland': 'SZ',
    'Ivory Coast': 'IV',
    'Cook Islands': 'CW',
    'Chile': 'CI',
    'Cameroon': 'CM',
    'China': 'CH',
    'Colombia': 'CO',
    'Costa Rica': 'CS',
    'Cuba': 'CU',
    'Cape Verde': 'CV',
    'Curacao': 'UC',
    'Christmas Island': 'KT',
    'Cyprus': 'CY',
    'Czech Republic': 'EZ',
    'Germany': 'GM',
    'Djibouti': 'DJ',
    'Denmark': 'DA',
    'Dominica': 'DO',
    'Dominican Republic': 'DR',
    'Algeria': 'AG',
    'Ecuador': 'EC',
    'Estonia': 'EN',
    'Egypt': 'EG',
    'Western Sahara': 'WI',
    'Eritrea': 'ER',
    'Spain': 'SP',
    'Ethiopia': 'ET',
    'Finland': 'FI',
    'Fiji': 'FJ',
    'Falkland Islands': 'FK',
    'Micronesia': 'FM',
    'Faroe Islands': 'FO',
    'France': 'FR',
    'Gabon': 'GB',
    'United Kingdom': 'UK',
    'Grenada': 'GJ',
    'Georgia': 'GG',
    'French Guiana': 'FG',
    'Guernsey': 'GK',
    'Ghana': 'GH',
    'Gibraltar': 'GI',
    'Greenland': 'GL',
    'Gambia': 'GA',
    'Guinea': 'GV',
    'Guadeloupe': 'GP',
    'Equatorial Guinea': 'EK',
    'Greece': 'GR',
    'South Georgia and the South Sandwich Islands': 'SX',
    'Guatemala': 'GT',
    'Guam': 'GQ',
    'Guinea-Bissau': 'PU',
    'Guyana': 'GY',
    'Hong Kong': 'HK',
    'Heard Island and McDonald Islands': 'HM',
    'Honduras': 'HO',
    'Croatia': 'HR',
    'Haiti': 'HA',
    'Hungary': 'HU',
    'Indonesia': 'ID',
    'Ireland': 'EI',
    'Israel': 'IS',
    'Isle of Man': 'IM',
    'India': 'IN',
    'British Indian Ocean Territory': 'IO',
    'Iraq': 'IZ',
    'Iran': 'IR',
    'Iceland': 'IC',
    'Italy': 'IT',
    'Jersey': 'JE',
    'Jamaica': 'JM',
    'Jordan': 'JO',
    'Japan': 'JA',
    'Kenya': 'KE',
    'Kyrgyzstan': 'KG',
    'Cambodia': 'CB',
    'Kiribati': 'KR',
    'Comoros': 'CN',
    'Saint Kitts and Nevis': 'SC',
    'North Korea': 'KN',
    'South Korea': 'KS',
    'Kosovo': 'KV',
    'Kuwait': 'KU',
    'Cayman Islands': 'CJ',
    'Kazakhstan': 'KZ',
    'Laos': 'LA',
    'Lebanon': 'LE',
    'Saint Lucia': 'ST',
    'Liechtenstein': 'LS',
    'Sri Lanka': 'CE',
    'Liberia': 'LI',
    'Lesotho': 'LT',
    'Lithuania': 'LH',
    'Luxembourg': 'LU',
    'Latvia': 'LG',
    'Libya': 'LY',
    'Morocco': 'MO',
    'Monaco': 'MN',
    'Moldova': 'MD',
    'Montenegro': 'MJ',
    'Saint Martin': 'RN',
    'Madagascar': 'MA',
    'Marshall Islands': 'RM',
    'Macedonia': 'MK',
    'Mali': 'ML',
    'Myanmar': 'BM',
    'Mongolia': 'MG',
    'Macao': 'MC',
    'Northern Mariana Islands': 'CQ',
    'Martinique': 'MB',
    'Mauritania': 'MR',
    'Montserrat': 'MH',
    'Malta': 'MT',
    'Mauritius': 'MP',
    'Maldives': 'MV',
    'Malawi': 'MI',
    'Mexico': 'MX',
    'Malaysia': 'MY',
    'Mozambique': 'MZ',
    'Namibia': 'WA',
    'New Caledonia': 'NC',
    'Niger': 'NG',
    'Norfolk Island': 'NF',
    'Nigeria': 'NI',
    'Nicaragua': 'NU',
    'Netherlands': 'NL',
    'Norway': 'NO',
    'Nepal': 'NP',
    'Nauru': 'NR',
    'Niue': 'NE',
    'New Zealand': 'NZ',
    'Oman': 'MU',
    'Panama': 'PM',
    'Peru': 'PE',
    'French Polynesia': 'FP',
    'Papua New Guinea': 'PP',
    'Philippines': 'RP',
    'Pakistan': 'PK',
    'Poland': 'PL',
    'Saint Pierre and Miquelon': 'SB',
    'Pitcairn': 'PC',
    'Puerto Rico': 'RQ',
    'Palestinian Territory': 'WE',
    'Portugal': 'PO',
    'Palau': 'PS',
    'Paraguay': 'PA',
    'Qatar': 'QA',
    'Reunion': 'RE',
    'Romania': 'RO',
    'Serbia': 'RI',
    'Russia': 'RS',
    'Rwanda': 'RW',
    'Saudi Arabia': 'SA',
    'Solomon Islands': 'BP',
    'Seychelles': 'SE',
    'Sudan': 'SU',
    'South Sudan': 'OD',
    'Sweden': 'SW',
    'Singapore': 'SN',
    'Saint Helena': 'SH',
    'Slovenia': 'SI',
    'Svalbard and Jan Mayen': 'SV',
    'Slovakia': 'LO',
    'Sierra Leone': 'SL',
    'San Marino': 'SM',
    'Senegal': 'SG',
    'Somalia': 'SO',
    'Suriname': 'NS',
    'Sao Tome and Principe': 'TP',
    'El Salvador': 'ES',
    'Sint Maarten': 'NN',
    'Syria': 'SY',
    'Swaziland': 'WZ',
    'Turks and Caicos Islands': 'TK',
    'Chad': 'CD',
    'French Southern Territories': 'FS',
    'Togo': 'TO',
    'Thailand': 'TH',
    'Tajikistan': 'TI',
    'Tokelau': 'TL',
    'East Timor': 'TT',
    'Turkmenistan': 'TX',
    'Tunisia': 'TS',
    'Tonga': 'TN',
    'Turkey': 'TU',
    'Trinidad and Tobago': 'TD',
    'Tuvalu': 'TV',
    'Taiwan': 'TW',
    'Tanzania': 'TZ',
    'Ukraine': 'UP',
    'Uganda': 'UG',
    'United States': 'US',
    'Uruguay': 'UY',
    'Uzbekistan': 'UZ',
    'Vatican': 'VT',
    'Saint Vincent and the Grenadines': 'VC',
    'Venezuela': 'VE',
    'British Virgin Islands': 'VI',
    'U.S. Virgin Islands': 'VQ',
    'Vietnam': 'VM',
    'Vanuatu': 'NH',
    'Wallis and Futuna': 'WF',
    'Samoa': 'WS',
    'Yemen': 'YM',
    'Mayotte': 'MF',
    'South Africa': 'SF',
    'Zambia': 'ZA',
    'Zimbabwe': 'ZI',
    'Serbia and Montenegro': 'YI',
    'Netherlands Antilles': 'NT',
}
states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AS': 'American Samoa',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'GU': 'Guam',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MP': 'Northern Mariana Islands',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NA': 'National',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VI': 'Virgin Islands',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}

supported_bots = [
    'pd',
    'nsb',
    'tohru',
    'tks',
    'phantom',
    'wrath',
    'dashe',
    'cyber',
    'balko',
    'splashforce',
    'whatbot',
    'feather',
    'hastey',
    'mek',
    'adept',
    'prism',
    'kodai',
    'sole',
    'anb',
    'eve',
    'velox',
    'polaris',
    'rush',
    'kinesis'
]
supported_bots.sort()


def validate_email(email):
    if re.search(regex, email) or re.search(regex_custom, email):
        return True
    else:
        return False


def cc_type(cc_number):
    AMEX_CC_RE = re.compile(r"^3[47][0-9]{13}$")
    VISA_CC_RE = re.compile(r"^4[0-9]{12}(?:[0-9]{3})?$")
    MASTERCARD_CC_RE = re.compile(r"^5[1-5][0-9]{14}$")
    DISCOVER_CC_RE = re.compile(r"^6(?:011|5[0-9]{2})[0-9]{12}$")

    CC_MAP = {"American Express": AMEX_CC_RE, "Visa": VISA_CC_RE,
              "MasterCard": MASTERCARD_CC_RE, "Discover": DISCOVER_CC_RE}

    for type, regexp in CC_MAP.items():
        if regexp.match(str(cc_number)):
            return type
    return None


def create_embed():
    embed = discord.Embed(
        color=discord.Colour.green()
    )
    embed.set_footer(text="Your information is not saved.")
    return embed


def get_random_string(length):
    letters = string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def get_random_string_both(length):
    letters = string.ascii_uppercase + string.digits + string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def get_random_string_lowercase(length):
    letters = string.ascii_lowercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


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


@client.event
async def on_ready():
    print("Bot is running...")

@client.command()
async def new_create(ctx):


@client.command()
async def start(ctx):
    def check(msg):
        if not msg.author.bot:
            return msg.content

    author = ctx.message.author.id
    message = str(ctx.message.content).split()
    if len(message) > 4:
        total_slots = message[1]
        channel = client.get_channel(int(message[2][2:-1]))
        time = message[3]
        slot_for = message[4:]
        giveaway = ""
        for s in slot_for:
            giveaway += f"{s} "
        # await ctx.message.delete()
        embed = create_embed()
        embed.description = "*If the bot does not DM you, you were not selected!*"
        embed.add_field(name=f"{giveaway}", value=f"React 👑 to enter!\nSlots will be up for {time}.")
        react = await channel.send(f"ACO hosted by <@{author}>!", embed=embed)
        await react.add_reaction('👑')

        def check(msg):
            if msg.reaction.emoji == '👑':
                if not msg.author.bot and msg == react:
                    return msg.content

        count = 0
        hi = ""
        users = []
        while count != int(total_slots):
            # TODO: Create a dictionary which adds the user and author to the list,
            #  have a task always looping to message the author
            reaction, user = await client.wait_for('reaction_add',  check=lambda reaction, user: not user.bot and reaction.emoji == '👑' and reaction.message.id == react.id)
            print(reaction.message)
            count += 1
            users.append(user)
        embed = create_embed()
        embed.add_field(name=f"{giveaway}", value="\u200b", inline=False)
        embed.add_field(name=f"🎊 Giveaway has ended! 🎊", value=f"\u200b")
        await react.edit(embed=embed)
        for i in range(len(users)):
            user = random.choice(users)
            users.remove(user)
            await user.send(f"Congrats! You have won the ACO by {ctx.message.author.name}.\nPlease reply with the .csv file correctly formatted.")
            hi += str(await add_user_file(user))
        print(f"{ctx.message.author.name}: {hi}")

    else:
        ctx.send("Invalid entry! Try again")


async def add_user_file(ctx):
    print(ctx)

    def check(msg):
        print(msg.author)
        if msg.author == ctx and isinstance(msg.channel, discord.DMChannel) and not msg.author.bot:
            return msg.content

    cnt = await client.wait_for('message', check=check, timeout=90)
    cnt = cnt.content
    return cnt


# @tasks.loop(milliseconds=500)
# async def test():
#

@client.command()
async def supported(ctx):
    embed = create_embed()
    bots = ""
    for bot in supported_bots:
        bots += f"{bot}\n"
    embed.add_field(name=f'Supported Bots [{len(supported_bots)}]', value=bots)
    await ctx.send(embed=embed)


@client.command()
@commands.check(is_dm_check)
async def convert(ctx):
    def check(msg):
        if isinstance(ctx.channel, discord.channel.DMChannel) and not msg.author.bot:
            return msg.content

    author = ctx.message.author.name
    message = ctx.message.content.split()
    selected_bot = message[1]
    new_file = ""
    if selected_bot in supported_bots:
        embed = create_embed()
        embed.add_field(name="How many profiles would you like to convert to 1 file?", value="Example: 4")
        await ctx.send(embed=embed)
        while True:
            amount_of_files = await client.wait_for('message', check=check, timeout=90)
            amount_of_files = amount_of_files.content
            if amount_of_files.isdigit():
                break
            else:
                embed = create_embed()
                embed.add_field(name="Invalid amount given!", value="Example: 4")
                await ctx.send(embed=embed)
        embed = create_embed()
        embed.add_field(name="Please send your files 1 at a time.",
                        value="Please add a message (can be random) with each file sent, or the bot will not receive it.")
        await ctx.send(embed=embed)
        print(int(amount_of_files))
        for f in range(int(amount_of_files)):
            uploaded_file = await client.wait_for('message', check=check, timeout=90)
            embed = create_embed()
            embed.add_field(name="File received!", value="Thank you!")
            await ctx.send(embed=embed)
            if uploaded_file.attachments:
                for a in uploaded_file.attachments:
                    url = a.url
                file = requests.get(url=url)
                content = json.loads(file.content)
                if selected_bot == "phantom" or selected_bot == "cyber":
                    new_file += f"{str(content)[1:-1]},"
                if selected_bot == "dashe":
                    if f != int(amount_of_files) - 1:
                        new_file += f"{str(content)[:-1]},"
                    else:
                        new_file += f"{str(content)[1:]}"
                if selected_bot == "tks":
                    content = str(content)[43:-409]
                    if f == 0:
                        new_file += '{"Locale":"EN","Tasks":[],"Profiles":['
                    new_file += f"{str(content)},"
                    if f == int(amount_of_files) - 1:
                        new_file = new_file[:-1]
                        new_file += '],"Proxies":[],"CaptchaSolvers":[],"RemoteTaskSettings":[{"WebsiteId":"master","RetryDelayFrom":500,"RetryDelayTo":1000,"MonitoringProxyListId":null,"CheckoutProxyListId":null,"PaymentMethodId":null,"AutoStart":false,"Sizes":"Any Available","Profiles":[]}],"ShopifyStores":[],"Logins":{},"DiscordWebhook":null,"SendCheckoutToGroupDiscord":false,"TaskToastNotifications":false}'

        if selected_bot == "phantom" or selected_bot == "cyber":
            new_file = f"[{str(new_file)[:-1]}]"
            new_file = new_file.replace("'", '"')
            new_file = new_file.replace(": ", ":")
            new_file = new_file.replace(", ", ",")
            new_file = new_file.replace('True', "true")
            new_file = new_file.replace('False', "false")
            file = StringIO(new_file)
            await ctx.send(f'Your {selected_bot.capitalize()} file is here!',
                           file=discord.File(filename=f"{ctx.message.author}_{selected_bot.capitalize()}.json",
                                             fp=file))
        if selected_bot == "dashe" or selected_bot == "tks":
            if selected_bot == "dashe":
                new_file = f"{str(new_file)}"

            new_file = new_file.replace("'", '"')
            new_file = new_file.replace(": ", ":")
            new_file = new_file.replace(", ", ",")
            new_file = new_file.replace('True', "true")
            new_file = new_file.replace('False', "false")
            new_file = new_file.replace("None", "null")
            file = StringIO(new_file)
            await ctx.send(f'Your {selected_bot.capitalize()} file is here!',
                           file=discord.File(filename=f"{ctx.message.author}_{selected_bot.capitalize()}.json",
                                             fp=file))


@client.command()
@commands.check(is_dm_check)
async def create(ctx):
    def check(msg):
        if isinstance(ctx.channel, discord.channel.DMChannel) and not msg.author.bot:
            return msg.content

    author = ctx.message.author.name
    message = ctx.message.content.split()
    selected_bot = message[1]
    if selected_bot in supported_bots:
        if await is_dm_check(ctx):
            print('Creating profile for: {0}'.format(ctx.message.author))
            embed = discord.Embed(
                color=discord.Colour.green(),
                description='Welcome to the profile manager.\n\nWith this bot you can create profiles and export them '
                            'for any bot!\n\n__*Please follow the formatted examples **exactly**.*__\n\nTo start, '
                            'react :thumbsup:. '
            )
            embed.set_footer(text="Your information is not saved.")
            msg = await ctx.send(embed=embed)
            await msg.add_reaction('👍')
            await client.wait_for('reaction_add',
                                  check=lambda reaction, user: not user.bot and reaction.emoji == '👍',
                                  timeout=120)
            try:
                while True:

                    embed = create_embed()
                    embed.add_field(name='To start, enter the name for the profile.', value='Example: Profile1')
                    await ctx.send(embed=embed)
                    profile_name = await client.wait_for('message', check=check, timeout=90)
                    profile_name = profile_name.content

                    embed = create_embed()
                    embed.add_field(name='To start, please enter your first and last name.',
                                    value='Example: John Smith')
                    await ctx.send(embed=embed)

                    while True:
                        name = await client.wait_for('message', check=check, timeout=90)
                        name = name.content
                        if len(name.split()) != 2:
                            embed = create_embed()
                            embed.add_field(name='Try again!', value='Incorrect format\n\nExample: John Smith')
                            await ctx.send(embed=embed)
                        else:
                            break

                    embed = create_embed()
                    embed.add_field(name='Hello {0} please enter your email address!'.format(name),
                                    value='Example: nokiny@gmail.com')
                    await ctx.send(embed=embed)

                    while True:
                        email = await client.wait_for('message', check=check, timeout=90)
                        email = email.content
                        if validate_email(email.lower()):
                            email = email.lower()
                            break
                        else:
                            embed = create_embed()
                            embed.add_field(name='Try again!', value='Incorrect format\n\nExample: nokiny@gmail.com')
                            await ctx.send(embed=embed)

                    embed = create_embed()
                    embed.add_field(name='Please enter your address'.format(name), value='Example: 123 Example St')
                    await ctx.send(embed=embed)
                    address = await client.wait_for('message', check=check, timeout=90)
                    address = address.content

                    embed = create_embed()
                    embed.add_field(
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
                            embed = create_embed()
                            embed.add_field(name='Try again!', value='Incorrect format.\nExample: 104 ***or*** None')
                            await ctx.send(embed=embed)

                    embed = create_embed()
                    embed.add_field(name='Please enter shipping/billing city, these must be the same.',
                                    value='Example: New York City')
                    await ctx.send(embed=embed)
                    city = await client.wait_for('message', check=check, timeout=90)
                    city = city.content

                    embed = create_embed()
                    embed.add_field(name='Please enter shipping/billing state.', value='Example: New York ***or*** NY')
                    await ctx.send(embed=embed)
                    while True:
                        state = await client.wait_for('message', check=check, timeout=90)
                        state = state.content
                        if state in us_state_abbreviations.keys():
                            break
                        elif state in us_state_abbreviations.values():
                            state = getKeysByValue(us_state_abbreviations, state)
                            break
                        else:
                            embed = create_embed()
                            embed.add_field(name='Try again!', value='Incorrect format.\nExample: New York ***or*** NY')
                            await ctx.send(embed=embed)

                    embed = create_embed()
                    embed.add_field(name='Please enter shipping/biling zipcode.', value='Example: 10021')
                    await ctx.send(embed=embed)
                    zip_code = await client.wait_for('message', check=check, timeout=90)
                    zip_code = zip_code.content

                    embed = create_embed()
                    embed.add_field(name='Please enter your country.', value='Example: United States ***or*** US')
                    await ctx.send(embed=embed)

                    while True:
                        country = await client.wait_for('message', check=check, timeout=90)
                        country = country.content
                        if country in country_abbrev.keys():
                            break
                        elif country in country_abbrev.values():
                            country = getKeysByValue(country_abbrev, country)
                            break
                        else:
                            embed = create_embed()
                            embed.add_field(name='Try again!',
                                            value='Incorrect format.\n Example: United States ***or*** '
                                                  'US')
                            await ctx.send(embed=embed)

                    embed = create_embed()
                    embed.add_field(name='Please enter your phone number.', value='Example: 1231231234')
                    await ctx.send(embed=embed)
                    phone_number = await client.wait_for('message', check=check, timeout=90)
                    phone_number = phone_number.content

                    embed = create_embed()
                    embed.add_field(name='Please enter the cardholder name.', value='Example: John Smith')
                    await ctx.send(embed=embed)
                    card_holder_name = await client.wait_for('message', check=check, timeout=90)
                    card_holder_name = card_holder_name.content

                    embed = create_embed()
                    embed.add_field(name='Please enter card number.', value='Example: 3716820019271998    ')
                    await ctx.send(embed=embed)

                    while True:
                        card_number = await client.wait_for('message', check=check, timeout=90)
                        card_number = card_number.content
                        if isValid(int(card_number)):
                            break
                        else:
                            embed = create_embed()
                            embed.add_field(name='Try again!',
                                            value='Invalid card number!\nExample: 3716820019271998')
                            await ctx.send(embed=embed)

                    embed = create_embed()
                    embed.add_field(name='Please enter expiration date.', value="Example: 03 / 22")
                    await ctx.send(embed=embed)

                    while True:
                        exp_date = await client.wait_for('message', check=check, timeout=90)
                        exp_date = exp_date.content
                        if ' / ' in exp_date:
                            break
                        else:
                            embed = create_embed()
                            embed.add_field(name='Try again!',
                                            value='Incorrect format.\n Example: 03 / 22')
                            await ctx.send(embed=embed)

                    embed = create_embed()
                    embed.add_field(name='Please enter the cvv.', value="Example: 599")
                    await ctx.send(embed=embed)
                    cvv = await client.wait_for('message', check=check, timeout=90)
                    cvv = cvv.content

                    embed = create_embed()
                    embed.add_field(name='Verification', value='Validate the information below, if it is correct react '
                                                               ':thumbsup: if it is not correct, react :thumbsdown:.\nIf it is not correct, bot may take some time to restart.',
                                    inline=False)
                    embed.add_field(name='Provided information',
                                    value=f'Profile Name: {profile_name}\nName: {name}\nEmail: {email}\nAddress: {address}\nApt: {apt}\nCity: {city}\n'
                                          f'Zip Code: {zip_code}\nState: {state}\nCountry: {country}\nPhone: {phone_number}\nCard Holder Name: {card_holder_name}\nCard Number: {card_number}\nExp Date: {exp_date}\nCVV: {cvv}')
                    msg = await ctx.send(embed=embed)
                    await msg.add_reaction('👍')
                    await msg.add_reaction('👎')
                    reaction, user = await client.wait_for('reaction_add',
                                                           check=lambda reaction,
                                                                        user: not user.bot and reaction.emoji == '👍' or not user.bot and reaction.emoji == '👎',
                                                           timeout=10)
                    if str(reaction) == '👍':
                        break
                    if str(reaction) == '👎':
                        print('Invalid information, restarting...')

                creating = True
                export_embed = create_embed()
                export_embed.add_field(name='Export to another bot?', value='Respond: Yes or No')

                bots = ""
                for bot in supported_bots:
                    bots += f"{bot}\n"
                export_embed_bot_question = create_embed()
                export_embed_bot_question.add_field(name='What bot would you like to export to?',
                                                    value=f'Respond with: \n{bots}')
                thank_you_embed = create_embed()
                thank_you_embed.add_field(name="Thank you for using Profile Manager!", value="See you soon!")

                while creating is True:
                    if selected_bot == "pd":
                        content = str(create_pd_file(
                            profile_name=profile_name,
                            address=address,
                            apt=apt,
                            city=city,
                            country=country,
                            name=name.split(),
                            phone=phone_number,
                            state=state,
                            zip=zip_code,
                            cardholder_name=card_holder_name,
                            card_number=card_number,
                            exp_date=exp_date,
                            cvv=cvv,
                            email=email
                        ))
                        file = StringIO(content)
                        await ctx.send('Your PD file is here!',
                                       file=discord.File(filename="{0}_PD.json".format(ctx.message.author), fp=file))
                        print('Profile created!')
                        await ctx.send(embed=export_embed)
                        another = await client.wait_for('message', check=check, timeout=30)
                        if another.content.lower() == "yes":
                            creating = True
                            await ctx.send(embed=export_embed_bot_question)
                            selected_bot = await client.wait_for('message', check=check, timeout=30)
                            selected_bot = selected_bot.content
                            print(selected_bot)
                        else:
                            await ctx.send(embed=thank_you_embed)
                            creating = False
                    if selected_bot == "nsb":
                        content = str(create_nsb_file(
                            profile_name=profile_name,
                            address=address,
                            apt=apt,
                            city=city,
                            country=country,
                            name=name.split(),
                            phone=phone_number,
                            state=state,
                            zip=zip_code,
                            cardholder_name=card_holder_name,
                            card_number=card_number,
                            exp_date=exp_date,
                            cvv=cvv,
                            email=email
                        ))
                        file = StringIO(content)
                        await ctx.send('Your NSB file is here!',
                                       file=discord.File(filename="{0}_NSB.json".format(ctx.message.author), fp=file))
                        print('Profile created!')
                        await ctx.send(embed=export_embed)
                        another = await client.wait_for('message', check=check, timeout=30)
                        if another.content.lower() == "yes":
                            creating = True
                            await ctx.send(embed=export_embed_bot_question)
                            selected_bot = await client.wait_for('message', check=check, timeout=30)
                            selected_bot = selected_bot.content
                            print(selected_bot)
                        else:
                            await ctx.send(embed=thank_you_embed)
                            creating = False
                    if selected_bot == "tohru":
                        content = str(create_tohru_file(
                            profile_name=profile_name,
                            address=address,
                            apt=apt,
                            city=city,
                            country=country,
                            name=name.split(),
                            phone=phone_number,
                            state=state,
                            zip=zip_code,
                            cardholder_name=card_holder_name,
                            card_number=card_number,
                            exp_date=exp_date,
                            cvv=cvv,
                            email=email
                        ))
                        file = StringIO(content)
                        await ctx.send('Your Tohru file is here!',
                                       file=discord.File(filename="{0}_Tohru.json".format(ctx.message.author), fp=file))
                        print('Profile created!')
                        await ctx.send(embed=export_embed)
                        another = await client.wait_for('message', check=check, timeout=30)
                        if another.content.lower() == "yes":
                            creating = True
                            await ctx.send(embed=export_embed_bot_question)
                            selected_bot = await client.wait_for('message', check=check, timeout=30)
                            selected_bot = selected_bot.content
                            print(selected_bot)
                        else:
                            await ctx.send(embed=thank_you_embed)
                            creating = False
                    if selected_bot == "tks":
                        content = str(create_tks_file(
                            profile_name=profile_name,
                            address=address,
                            apt=apt,
                            city=city,
                            country=country,
                            name=name.split(),
                            phone=phone_number,
                            state=state,
                            zip=zip_code,
                            cardholder_name=card_holder_name,
                            card_number=card_number,
                            exp_date=exp_date,
                            cvv=cvv,
                            email=email
                        ))
                        file = StringIO(content)
                        await ctx.send('Your TKS file is here!',
                                       file=discord.File(filename="{0}_TKS.json".format(ctx.message.author), fp=file))
                        print('Profile created!')
                        await ctx.send(embed=export_embed)
                        another = await client.wait_for('message', check=check, timeout=30)
                        if another.content.lower() == "yes":
                            creating = True
                            await ctx.send(embed=export_embed_bot_question)
                            selected_bot = await client.wait_for('message', check=check, timeout=30)
                            selected_bot = selected_bot.content
                            print(selected_bot)
                        else:
                            await ctx.send(embed=thank_you_embed)
                            creating = False
                    if selected_bot == "phantom":
                        content = str(create_phantom_file(
                            profile_name=profile_name,
                            address=address,
                            apt=apt,
                            city=city,
                            country=country,
                            name=name.split(),
                            phone=phone_number,
                            state=state,
                            zip=zip_code,
                            cardholder_name=card_holder_name,
                            card_number=card_number,
                            exp_date=exp_date,
                            cvv=cvv,
                            email=email
                        ))
                        file = StringIO(content)
                        await ctx.send('Your Phantom file is here!',
                                       file=discord.File(filename="{0}_Phantom.json".format(ctx.message.author),
                                                         fp=file))
                        print('Profile created!')
                        await ctx.send(embed=export_embed)
                        another = await client.wait_for('message', check=check, timeout=30)
                        if another.content.lower() == "yes":
                            creating = True
                            await ctx.send(embed=export_embed_bot_question)
                            selected_bot = await client.wait_for('message', check=check, timeout=30)
                            selected_bot = selected_bot.content
                            print(selected_bot)
                        else:
                            await ctx.send(embed=thank_you_embed)
                            creating = False
                    if selected_bot == "wrath":
                        content = str(create_wrath_file(
                            profile_name=profile_name,
                            address=address,
                            apt=apt,
                            city=city,
                            country=country,
                            name=name.split(),
                            phone=phone_number,
                            state=state,
                            zip=zip_code,
                            cardholder_name=card_holder_name,
                            card_number=card_number,
                            exp_date=exp_date,
                            cvv=cvv,
                            email=email
                        ))
                        file = StringIO(content)
                        await ctx.send('Your Wrath file is here!',
                                       file=discord.File(filename="{0}_Wrath.json".format(ctx.message.author),
                                                         fp=file))
                        print('Profile created!')
                        await ctx.send(embed=export_embed)
                        another = await client.wait_for('message', check=check, timeout=30)
                        if another.content.lower() == "yes":
                            creating = True
                            await ctx.send(embed=export_embed_bot_question)
                            selected_bot = await client.wait_for('message', check=check, timeout=30)
                            selected_bot = selected_bot.content
                            print(selected_bot)
                        else:
                            await ctx.send(embed=thank_you_embed)
                            creating = False
                    if selected_bot == "dashe":
                        content = str(create_dashe_file(
                            profile_name=profile_name,
                            address=address,
                            apt=apt,
                            city=city,
                            country=country,
                            name=name.split(),
                            phone=phone_number,
                            state=state,
                            zip=zip_code,
                            cardholder_name=card_holder_name,
                            card_number=card_number,
                            exp_date=exp_date,
                            cvv=cvv,
                            email=email
                        ))
                        file = StringIO(content)
                        await ctx.send('Your Dashe file is here!',
                                       file=discord.File(filename="{0}_Dashe.json".format(ctx.message.author),
                                                         fp=file))
                        print('Profile created!')
                        await ctx.send(embed=export_embed)
                        another = await client.wait_for('message', check=check, timeout=30)
                        if another.content.lower() == "yes":
                            creating = True
                            await ctx.send(embed=export_embed_bot_question)
                            selected_bot = await client.wait_for('message', check=check, timeout=30)
                            selected_bot = selected_bot.content
                            print(selected_bot)
                        else:
                            await ctx.send(embed=thank_you_embed)
                            creating = False
                    if selected_bot == "cyber":
                        content = str(create_cyber_file(
                            profile_name=profile_name,
                            address=address,
                            apt=apt,
                            city=city,
                            country=country,
                            name=name.split(),
                            phone=phone_number,
                            state=state,
                            zip=zip_code,
                            cardholder_name=card_holder_name,
                            card_number=card_number,
                            exp_date=exp_date,
                            cvv=cvv,
                            email=email
                        ))
                        file = StringIO(content)
                        await ctx.send('Your Cyber file is here!',
                                       file=discord.File(filename="{0}_Cyber.json".format(ctx.message.author),
                                                         fp=file))
                        print('Profile created!')
                        await ctx.send(embed=export_embed)
                        another = await client.wait_for('message', check=check, timeout=30)
                        if another.content.lower() == "yes":
                            creating = True
                            await ctx.send(embed=export_embed_bot_question)
                            selected_bot = await client.wait_for('message', check=check, timeout=30)
                            selected_bot = selected_bot.content
                            print(selected_bot)
                        else:
                            await ctx.send(embed=thank_you_embed)
                            creating = False
                    if selected_bot == "balko":
                        content = str(create_balko_file(
                            profile_name=profile_name,
                            address=address,
                            apt=apt,
                            city=city,
                            country=country,
                            name=name.split(),
                            phone=phone_number,
                            state=state,
                            zip=zip_code,
                            cardholder_name=card_holder_name,
                            card_number=card_number,
                            exp_date=exp_date,
                            cvv=cvv,
                            email=email
                        ))
                        file = StringIO(content)
                        await ctx.send('Your Balko file is here!',
                                       file=discord.File(filename="{0}_Balko.json".format(ctx.message.author),
                                                         fp=file))
                        print('Profile created!')
                        await ctx.send(embed=export_embed)
                        another = await client.wait_for('message', check=check, timeout=30)
                        if another.content.lower() == "yes":
                            creating = True
                            await ctx.send(embed=export_embed_bot_question)
                            selected_bot = await client.wait_for('message', check=check, timeout=30)
                            selected_bot = selected_bot.content
                            print(selected_bot)
                        else:
                            await ctx.send(embed=thank_you_embed)
                            creating = False
                    if selected_bot == "splashforce":
                        content = str(create_splashforce_file(
                            profile_name=profile_name,
                            address=address,
                            apt=apt,
                            city=city,
                            country=country,
                            name=name.split(),
                            phone=phone_number,
                            state=state,
                            zip=zip_code,
                            cardholder_name=card_holder_name,
                            card_number=card_number,
                            exp_date=exp_date,
                            cvv=cvv,
                            email=email
                        ))
                        file = StringIO(content)
                        await ctx.send('Your Splashforce file is here!',
                                       file=discord.File(filename="{0}_Splashforce.json".format(ctx.message.author),
                                                         fp=file))
                        print('Profile created!')
                        await ctx.send(embed=export_embed)
                        another = await client.wait_for('message', check=check, timeout=30)
                        if another.content.lower() == "yes":
                            creating = True
                            await ctx.send(embed=export_embed_bot_question)
                            selected_bot = await client.wait_for('message', check=check, timeout=30)
                            selected_bot = selected_bot.content
                            print(selected_bot)
                        else:
                            await ctx.send(embed=thank_you_embed)
                            creating = False
                    if selected_bot == "whatbot":
                        content = str(create_whatbot_file(
                            profile_name=profile_name,
                            address=address,
                            apt=apt,
                            city=city,
                            country=country,
                            name=name.split(),
                            phone=phone_number,
                            state=state,
                            zip=zip_code,
                            cardholder_name=card_holder_name,
                            card_number=card_number,
                            exp_date=exp_date,
                            cvv=cvv,
                            email=email
                        ))
                        file = StringIO(content)
                        await ctx.send('Your WhatBot file is here!',
                                       file=discord.File(filename="{0}_WhatBot.db".format(ctx.message.author),
                                                         fp=file))
                        print('Profile created!')
                        await ctx.send(embed=export_embed)
                        another = await client.wait_for('message', check=check, timeout=30)
                        if another.content.lower() == "yes":
                            creating = True
                            await ctx.send(embed=export_embed_bot_question)
                            selected_bot = await client.wait_for('message', check=check, timeout=30)
                            selected_bot = selected_bot.content
                            print(selected_bot)
                        else:
                            await ctx.send(embed=thank_you_embed)
                            creating = False
                    if selected_bot == "feather":
                        content = str(create_feather_file(
                            profile_name=profile_name,
                            address=address,
                            apt=apt,
                            city=city,
                            country=country,
                            name=name.split(),
                            phone=phone_number,
                            state=state,
                            zip=zip_code,
                            cardholder_name=card_holder_name,
                            card_number=card_number,
                            exp_date=exp_date,
                            cvv=cvv,
                            email=email
                        ))
                        file = StringIO(content)
                        await ctx.send('Your Feather file is here!',
                                       file=discord.File(filename="{0}_Feather.json".format(ctx.message.author),
                                                         fp=file))
                        print('Profile created!')
                        await ctx.send(embed=export_embed)
                        another = await client.wait_for('message', check=check, timeout=30)
                        if another.content.lower() == "yes":
                            creating = True
                            await ctx.send(embed=export_embed_bot_question)
                            selected_bot = await client.wait_for('message', check=check, timeout=30)
                            selected_bot = selected_bot.content
                            print(selected_bot)
                        else:
                            await ctx.send(embed=thank_you_embed)
                            creating = False
                    if selected_bot == "hastey":
                        content = str(create_hastey_file(
                            profile_name=profile_name,
                            address=address,
                            apt=apt,
                            city=city,
                            country=country,
                            name=name.split(),
                            phone=phone_number,
                            state=state,
                            zip=zip_code,
                            cardholder_name=card_holder_name,
                            card_number=card_number,
                            exp_date=exp_date,
                            cvv=cvv,
                            email=email
                        ))
                        file = StringIO(content)
                        await ctx.send('Your Hastey file is here!',
                                       file=discord.File(filename="{0}_Hastey.json".format(ctx.message.author),
                                                         fp=file))
                        print('Profile created!')
                        await ctx.send(embed=export_embed)
                        another = await client.wait_for('message', check=check, timeout=30)
                        if another.content.lower() == "yes":
                            creating = True
                            await ctx.send(embed=export_embed_bot_question)
                            selected_bot = await client.wait_for('message', check=check, timeout=30)
                            selected_bot = selected_bot.content
                            print(selected_bot)
                        else:
                            await ctx.send(embed=thank_you_embed)
                            creating = False
                    if selected_bot == "mek":
                        content = str(create_mek_file(
                            profile_name=profile_name,
                            address=address,
                            apt=apt,
                            city=city,
                            country=country,
                            name=name.split(),
                            phone=phone_number,
                            state=state,
                            zip=zip_code,
                            cardholder_name=card_holder_name,
                            card_number=card_number,
                            exp_date=exp_date,
                            cvv=cvv,
                            email=email
                        ))
                        file = StringIO(content)
                        await ctx.send('Your Mek file is here!',
                                       file=discord.File(filename="{0}_Mek.json".format(ctx.message.author),
                                                         fp=file))
                        print('Profile created!')
                        await ctx.send(embed=export_embed)
                        another = await client.wait_for('message', check=check, timeout=30)
                        if another.content.lower() == "yes":
                            creating = True
                            await ctx.send(embed=export_embed_bot_question)
                            selected_bot = await client.wait_for('message', check=check, timeout=30)
                            selected_bot = selected_bot.content
                            print(selected_bot)
                        else:
                            await ctx.send(embed=thank_you_embed)
                            creating = False
                    if selected_bot == "adept":
                        content = str(create_adept_file(
                            profile_name=profile_name,
                            address=address,
                            apt=apt,
                            city=city,
                            country=country,
                            name=name.split(),
                            phone=phone_number,
                            state=state,
                            zip=zip_code,
                            cardholder_name=card_holder_name,
                            card_number=card_number,
                            exp_date=exp_date,
                            cvv=cvv,
                            email=email
                        ))
                        file = StringIO(content)
                        await ctx.send('Your Adept file is here!',
                                       file=discord.File(filename="{0}_Adept.json".format(ctx.message.author),
                                                         fp=file))
                        print('Profile created!')
                        await ctx.send(embed=export_embed)
                        another = await client.wait_for('message', check=check, timeout=30)
                        if another.content.lower() == "yes":
                            creating = True
                            await ctx.send(embed=export_embed_bot_question)
                            selected_bot = await client.wait_for('message', check=check, timeout=30)
                            selected_bot = selected_bot.content
                            print(selected_bot)
                        else:
                            await ctx.send(embed=thank_you_embed)
                            creating = False
                    if selected_bot == "prism":
                        content = str(create_prism_file(
                            profile_name=profile_name,
                            address=address,
                            apt=apt,
                            city=city,
                            country=country,
                            name=name.split(),
                            phone=phone_number,
                            state=state,
                            zip=zip_code,
                            cardholder_name=card_holder_name,
                            card_number=card_number,
                            exp_date=exp_date,
                            cvv=cvv,
                            email=email
                        ))
                        file = StringIO(content)
                        await ctx.send('Your Prism file is here!',
                                       file=discord.File(filename="{0}_Prism.json".format(ctx.message.author),
                                                         fp=file))
                        print('Profile created!')
                        await ctx.send(embed=export_embed)
                        another = await client.wait_for('message', check=check, timeout=30)
                        if another.content.lower() == "yes":
                            creating = True
                            await ctx.send(embed=export_embed_bot_question)
                            selected_bot = await client.wait_for('message', check=check, timeout=30)
                            selected_bot = selected_bot.content
                            print(selected_bot)
                        else:
                            await ctx.send(embed=thank_you_embed)
                            creating = False
                    if selected_bot == "kodai":
                        content = str(create_kodai_file(
                            profile_name=profile_name,
                            address=address,
                            apt=apt,
                            city=city,
                            country=country,
                            name=name.split(),
                            phone=phone_number,
                            state=state,
                            zip=zip_code,
                            cardholder_name=card_holder_name,
                            card_number=card_number,
                            exp_date=exp_date,
                            cvv=cvv,
                            email=email
                        ))
                        file = StringIO(content)
                        await ctx.send('Your Kodai file is here!',
                                       file=discord.File(filename="{0}_Kodai.json".format(ctx.message.author),
                                                         fp=file))
                        print('Profile created!')
                        await ctx.send(embed=export_embed)
                        another = await client.wait_for('message', check=check, timeout=30)
                        if another.content.lower() == "yes":
                            creating = True
                            await ctx.send(embed=export_embed_bot_question)
                            selected_bot = await client.wait_for('message', check=check, timeout=30)
                            selected_bot = selected_bot.content
                            print(selected_bot)
                        else:
                            await ctx.send(embed=thank_you_embed)
                            creating = False
                    if selected_bot == "sole":
                        content = str(create_soleaio_file(
                            profile_name=profile_name,
                            address=address,
                            apt=apt,
                            city=city,
                            country=country,
                            name=name.split(),
                            phone=phone_number,
                            state=state,
                            zip=zip_code,
                            cardholder_name=card_holder_name,
                            card_number=card_number,
                            exp_date=exp_date,
                            cvv=cvv,
                            email=email
                        ))
                        file = StringIO(content)
                        await ctx.send('Your Sole AIO file is here!',
                                       file=discord.File(filename="{0}_Sole_AIO.json".format(ctx.message.author),
                                                         fp=file))
                        print('Profile created!')
                        await ctx.send(embed=export_embed)
                        another = await client.wait_for('message', check=check, timeout=30)
                        if another.content.lower() == "yes":
                            creating = True
                            await ctx.send(embed=export_embed_bot_question)
                            selected_bot = await client.wait_for('message', check=check, timeout=30)
                            selected_bot = selected_bot.content
                            print(selected_bot)
                        else:
                            await ctx.send(embed=thank_you_embed)
                            creating = False
                    if selected_bot == "anb":
                        content = str(create_anb_file(
                            profile_name=profile_name,
                            address=address,
                            apt=apt,
                            city=city,
                            country=country,
                            name=name.split(),
                            phone=phone_number,
                            state=state,
                            zip=zip_code,
                            cardholder_name=card_holder_name,
                            card_number=card_number,
                            exp_date=exp_date,
                            cvv=cvv,
                            email=email
                        ))
                        file = StringIO(content)
                        await ctx.send('Your ANB file is here!',
                                       file=discord.File(filename="{0}_ANB.csv".format(ctx.message.author),
                                                         fp=file))
                        print('Profile created!')
                        await ctx.send(embed=export_embed)
                        another = await client.wait_for('message', check=check, timeout=30)
                        if another.content.lower() == "yes":
                            creating = True
                            await ctx.send(embed=export_embed_bot_question)
                            selected_bot = await client.wait_for('message', check=check, timeout=30)
                            selected_bot = selected_bot.content
                            print(selected_bot)
                        else:
                            await ctx.send(embed=thank_you_embed)
                            creating = False
                    if selected_bot == "eve":
                        content = str(create_eve_file(
                            profile_name=profile_name,
                            address=address,
                            apt=apt,
                            city=city,
                            country=country,
                            name=name.split(),
                            phone=phone_number,
                            state=state,
                            zip=zip_code,
                            cardholder_name=card_holder_name,
                            card_number=card_number,
                            exp_date=exp_date,
                            cvv=cvv,
                            email=email
                        ))
                        file = StringIO(content)
                        await ctx.send('Your EVE file is here!',
                                       file=discord.File(filename="{0}_EVE.xml".format(ctx.message.author),
                                                         fp=file))
                        print('Profile created!')
                        await ctx.send(embed=export_embed)
                        another = await client.wait_for('message', check=check, timeout=30)
                        if another.content.lower() == "yes":
                            creating = True
                            await ctx.send(embed=export_embed_bot_question)
                            selected_bot = await client.wait_for('message', check=check, timeout=30)
                            selected_bot = selected_bot.content
                            print(selected_bot)
                        else:
                            await ctx.send(embed=thank_you_embed)
                            creating = False
                    if selected_bot == "velox":
                        content = str(create_velox_file(
                            profile_name=profile_name,
                            address=address,
                            apt=apt,
                            city=city,
                            country=country,
                            name=name.split(),
                            phone=phone_number,
                            state=state,
                            zip=zip_code,
                            cardholder_name=card_holder_name,
                            card_number=card_number,
                            exp_date=exp_date,
                            cvv=cvv,
                            email=email
                        ))
                        file = StringIO(content)
                        await ctx.send('Your Velox file is here!',
                                       file=discord.File(filename="{0}_Velox.json".format(ctx.message.author),
                                                         fp=file))
                        print('Profile created!')
                        await ctx.send(embed=export_embed)
                        another = await client.wait_for('message', check=check, timeout=30)
                        if another.content.lower() == "yes":
                            creating = True
                            await ctx.send(embed=export_embed_bot_question)
                            selected_bot = await client.wait_for('message', check=check, timeout=30)
                            selected_bot = selected_bot.content
                            print(selected_bot)
                        else:
                            await ctx.send(embed=thank_you_embed)
                            creating = False
                    if selected_bot == "polaris":
                        content = str(create_polaris_file(
                            profile_name=profile_name,
                            address=address,
                            apt=apt,
                            city=city,
                            country=country,
                            name=name.split(),
                            phone=phone_number,
                            state=state,
                            zip=zip_code,
                            cardholder_name=card_holder_name,
                            card_number=card_number,
                            exp_date=exp_date,
                            cvv=cvv,
                            email=email
                        ))
                        file = StringIO(content)
                        await ctx.send('Your Polaris file is here!',
                                       file=discord.File(filename="{0}_Polaris.json".format(ctx.message.author),
                                                         fp=file))
                        print('Profile created!')
                        await ctx.send(embed=export_embed)
                        another = await client.wait_for('message', check=check, timeout=30)
                        if another.content.lower() == "yes":
                            creating = True
                            await ctx.send(embed=export_embed_bot_question)
                            selected_bot = await client.wait_for('message', check=check, timeout=30)
                            selected_bot = selected_bot.content
                            print(selected_bot)
                        else:
                            await ctx.send(embed=thank_you_embed)
                            creating = False
                    if selected_bot == "rush":
                        content = str(create_rush_file(
                            profile_name=profile_name,
                            address=address,
                            apt=apt,
                            city=city,
                            country=country,
                            name=name.split(),
                            phone=phone_number,
                            state=state,
                            zip=zip_code,
                            cardholder_name=card_holder_name,
                            card_number=card_number,
                            exp_date=exp_date,
                            cvv=cvv,
                            email=email
                        ))
                        file = StringIO(content)
                        await ctx.send('Your Rush file is here!',
                                       file=discord.File(filename="{0}_Rush.json".format(ctx.message.author),
                                                         fp=file))
                        print('Profile created!')
                        await ctx.send(embed=export_embed)
                        another = await client.wait_for('message', check=check, timeout=30)
                        if another.content.lower() == "yes":
                            creating = True
                            await ctx.send(embed=export_embed_bot_question)
                            selected_bot = await client.wait_for('message', check=check, timeout=30)
                            selected_bot = selected_bot.content
                            print(selected_bot)
                        else:
                            await ctx.send(embed=thank_you_embed)
                            creating = False
                    if selected_bot == "kinesis":
                        content = str(create_kinesis_file(
                            profile_name=profile_name,
                            address=address,
                            apt=apt,
                            city=city,
                            country=country,
                            name=name.split(),
                            phone=phone_number,
                            state=state,
                            zip=zip_code,
                            cardholder_name=card_holder_name,
                            card_number=card_number,
                            exp_date=exp_date,
                            cvv=cvv,
                            email=email
                        ))
                        file = StringIO(content)
                        await ctx.send('Your Kinesis file is here!',
                                       file=discord.File(filename="{0}_Kinesis.json".format(ctx.message.author),
                                                         fp=file))
                        print('Profile created!')
                        await ctx.send(embed=export_embed)
                        another = await client.wait_for('message', check=check, timeout=30)
                        if another.content.lower() == "yes":
                            creating = True
                            await ctx.send(embed=export_embed_bot_question)
                            selected_bot = await client.wait_for('message', check=check, timeout=30)
                            selected_bot = selected_bot.content
                            print(selected_bot)
                        else:
                            await ctx.send(embed=thank_you_embed)
                            creating = False
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

"""

What this class does


"""
import re
import string
import random

class Config:
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

    def get_card_type(self, card_number):
        AMEX_CC_RE = re.compile(r"^3[47][0-9]{13}$")
        VISA_CC_RE = re.compile(r"^4[0-9]{12}(?:[0-9]{3})?$")
        MASTERCARD_CC_RE = re.compile(r"^5[1-5][0-9]{14}$")
        DISCOVER_CC_RE = re.compile(r"^6(?:011|5[0-9]{2})[0-9]{12}$")

        CC_MAP = {"American Express": AMEX_CC_RE, "Visa": VISA_CC_RE,
                  "MasterCard": MASTERCARD_CC_RE, "Discover": DISCOVER_CC_RE}

        for type, regexp in CC_MAP.items():
            if regexp.match(str(card_number)):
                return type
        return None

    def get_random_string_uppercase(self, length):
        letters = string.ascii_uppercase + string.digits
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    def get_random_string_upper_and_lowercase(self, length):
        letters = string.ascii_uppercase + string.digits + string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    def get_random_string_lowercase(self, length):
        letters = string.ascii_lowercase + string.digits
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str
"""

What this class does

"""
from io import StringIO

from Config import Config
from Profile import Profile

class Hastey:

    def create_profile(self, profile):
        config = Config()
        if profile.country.lower() == 'united states':
            country = "USA"
        else:
            country = profile.country.lower()
        expdate = profile.exp_date.split()
        exp_month = expdate[0]
        exp_year = f'20{expdate[2]}'
        file = str([{
            "__profile__name": profile.profile_name,
            "address": profile.address,
            "address_2": profile.apt,
            "cardType": "null",
            "cc_cvv": profile.cvv,
            "cc_month": exp_month,
            "cc_number": profile.card_number,
            "cc_year": exp_year,
            "city": profile.city,
            "country": country,
            "email": profile.email,
            "id": f'{config.get_random_string_lowercase(8)}-{config.get_random_string_lowercase(4)}-{config.get_random_string_lowercase(4)}-{config.get_random_string_lowercase(4)}-{config.get_random_string_lowercase(12)}',
            "name": profile.card_holder_name,
            "state": config.us_state_abbreviations[profile.state],
            "tel": f'{profile.phone[0:3]}-{profile.phone[3:6]}-{profile.phone[6:len(profile.phone)]}',
            "zip": profile.zip_code
        }])
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"null"', "null")
        file = StringIO(file)
        return file

    def create_profiles(self, profiles):
        file = ""
        if type(profiles[0]) == Profile:
            for profile in profiles:
                file += f'{str(self.create_profile(profile).readline())[1:-1]},'
        else:
            for profile in profiles:
                file += f'{str(profile)[1:-1]},'
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"null"', "null").replace("None","null")
        file = f"[{str(file)[:-1]}]"
        file = StringIO(file)
        return file

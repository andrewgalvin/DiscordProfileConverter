"""

What this class does

"""
from io import StringIO

from Config import Config
from Profile import Profile

class Feather:

    def create_profile(self, profile):
        config = Config()
        if profile.country.lower() == 'united states':
            country = "USA"
        else:
            country = profile.lower()
        expdate = profile.exp_date.split()
        exp_month = expdate[0]
        exp_year = f'20{expdate[2]}'
        file = str([{
            "nickname": profile.profile_name,
            "name": f"{profile.first_name} {profile.last_name}",
            "email": profile.email,
            "phone": profile.phone,
            "address": profile.address,
            "address2": profile.apt,
            "address3": "",
            "city": profile.city,
            "zip": profile.zip_code,
            "country": country,
            "state": config.us_state_abbreviations[profile.state],
            "cardType": "null",
            "card": profile.card_number,
            "month": exp_month,
            "year": exp_year,
            "cvc": profile.cvv,
            "region": "NA"
        }])
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"null"', "null").replace("None","null")
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
        file = f"[{str(file)[:-1]}]"
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"null"', "null").replace("None","null")
        file = StringIO(file)
        return file
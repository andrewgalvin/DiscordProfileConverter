"""

What this class does

"""
from io import StringIO

from Config import Config
from Profile import Profile

class Velox:

    def create_profile(self, profile):
        config = Config()
        if config.country_abbrev[profile.country] == "US":
            country = "USA"
        else:
            country = config.country_abbrev[profile.country]
        card_type = str(config.get_card_type(profile.card_number)).lower()

        exp_date = profile.exp_date.replace(" ", "")
        if len(profile.card_number) > 16:
            cardnumber = f'{profile.card_number[0:4]} {profile.card_number[4:8]} {profile.card_number[8:12]} {profile.card_number[12:16]} {profile.card_number[16:len(profile.card_number)]}'
        else:
            cardnumber = f'{profile.card_number[0:4]} {profile.card_number[4:8]} {profile.card_number[8:12]} {profile.card_number[12:16]}'

        file = str([{

            "name": profile.profile_name,
            "shipping": {
                "firstName": f"{profile.first_name}", "lastName": f"{profile.last_name}", "email": f"{profile.email}", "phone": f"{profile.phone}",
                "address": f"{profile.address}", "address2": f"{profile.apt}", "city": f"{profile.city}", "zipcode": f"{profile.zip_code}",
                "country": f"{country}",
                "state": f"{config.us_state_abbreviations[profile.state]}"
            }

            ,
            "card": {
                "type": f"{card_type}", "number": f"{cardnumber}", "expiry": f"{exp_date}", "cvv": f"{profile.cvv}"
            }
        }

        ])
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",")
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
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",")
        file = f"[{str(file)[:-1]}]"
        file = StringIO(file)
        return file

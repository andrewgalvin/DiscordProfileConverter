"""

What this class does


"""
from io import StringIO

from Config import Config
from Profile import Profile


class Dashe:

    def create_profile(self, profile):
        config = Config()
        expdate = profile.exp_date.split()
        exp_month = expdate[0]
        exp_year = f'20{expdate[2]}'
        file = str({
            profile.profile_name: {
                "billing": {
                    "address": profile.address,
                    "apt": profile.apt,
                    "city": profile.city,
                    "country": profile.country,
                    "firstName": profile.first_name,
                    "lastName": profile.last_name,
                    "phoneNumber": profile.phone,
                    "state": config.us_state_abbreviations[profile.state],
                    "zipCode": profile.zip_code
                },
                "billingMatch": "true",
                "card": {
                    "cvv": profile.cvv,
                    "holder": profile.card_holder_name,
                    "month": exp_month,
                    "number": profile.card_number,
                    "year": exp_year
                },
                "email": profile.email,
                "profileName": profile.profile_name,
                "shipping": {
                    "address": profile.address,
                    "apt": profile.apt,
                    "city": profile.city,
                    "country": profile.country,
                    "firstName": profile.first_name,
                    "lastName": profile.last_name,
                    "phoneNumber": profile.phone,
                    "state": config.us_state_abbreviations[profile.state],
                    "zipCode": profile.zip_code
                }
            }
        })
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"true"', "true").replace('"false"',"false").replace('True', "true").replace('False', "false").replace("None", "null")

        file = StringIO(file)
        return file

    def create_profiles(self, profiles):
        file = ""
        if type(profiles[0]) == Profile:
            for profile in profiles:
                if profile is profiles[0]:
                    file += f"{str(self.create_profile(profile).readline())[:-1]},"
                else:
                    file += f"{str(self.create_profile(profile).readline())[1:]}"
        else:
            for profile in profiles:
                if profile is profiles[0]:
                    file += f"{str(profile)[:-1]},"
                else:
                    file += f"{str(profile)[1:]}"
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"true"', "true").replace('"false"',"false").replace('True', "true").replace('False', "false").replace("None", "null")
        file = StringIO(file)
        return file
"""

What this class does

"""
from io import StringIO

from Config import Config
from Profile import Profile
class WhatBot:

    def create_profile(self, profile):
        config = Config()
        expdate = profile.exp_date.split()
        exp_month = expdate[0]
        exp_year = expdate[2]

        file = str({
            "_id": config.get_random_string_upper_and_lowercase(16),
            "name": profile.profile_name,
            "diffBilling": "false",
            "firstName": profile.first_name,
            "lastName": profile.last_name,
            "address": profile.address,
            "address2": f"{profile.apt}",
            "city": profile.city,
            "state": profile.state,
            "country": profile.country,
            "zipCode": profile.zip_code,
            "phone": profile.phone,
            "firstNameB": "",
            "lastNameB": "",
            "addressB": "",
            "address2B": "",
            "cityB": "",
            "stateB": "",
            "countryB": "",
            "zipCodeB": "",
            "phoneB": profile.phone,
            "email": profile.email,
            "cardNumber": profile.card_number,
            "cardName": profile.card_holder_name,
            "cardMonth": exp_month,
            "cardYear": exp_year,
            "cardCvv": profile.cvv
        })
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"false"', "false").replace("False","false")
        file = StringIO(file)
        return file

    def create_profiles(self, profiles):
        file = ""
        if type(profiles[0]) == Profile:
            for profile in profiles:
                file += f'{str(self.create_profile(profile).readline())}\n'
        else:
            for profile in profiles:
                file += f'{str(profile)}\n'
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"false"', "false").replace("False","false")
        file = StringIO(file)
        return file
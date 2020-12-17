"""

What this class does

"""
from io import StringIO

from Config import Config
from Profile import Profile

class Mek:

    def create_profile(self, profile):
        config = Config()
        if profile.country == "United States":
            country = "USA"
        else:
            country = profile.country
        id = config.get_random_string_uppercase(9)
        expdate = profile.exp_date.split()
        exp_month = expdate[0]
        exp_year = f'20{expdate[2]}'

        if config.get_card_type(profile.card_number) == "American Express":
            card_type = "american_express"
        elif config.get_card_type(profile.card_number) == "MasterCard":
            card_type = "master"
        else:
            card_type = str(config.get_card_type(profile.card_number)).lower()

        if len(profile.card_number) > 16:
            cardnumber = f'{profile.card_number[0:4]} {profile.card_number[4:8]} {profile.card_number[8:12]} {profile.card_number[12:16]} {profile.card_number[16:len(profile.card_number)]}'
        else:
            cardnumber = f'{profile.card_number[0:4]} {profile.card_number[4:8]} {profile.card_number[8:12]} {profile.card_number[12:16]}'
        file = str({
            id: {
                "id": id,
                "profile_name": profile.profile_name,
                "billing_name": profile.card_holder_name,
                "order_email": profile.email,
                "order_address": profile.address,
                "order_address_2": profile.apt,
                "order_tel": profile.phone,
                "order_billing_zip": profile.zip_code,
                "order_billing_city": profile.city,
                "area": country,
                "order_billing_state": config.us_state_abbreviations[profile.state],
                "order_billing_country": country,
                "card_type": card_type,
                "cnb": cardnumber,
                "month": exp_month,
                "year": exp_year,
                "vval": profile.cvv
            }
        })
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",")
        file = StringIO(file)
        return file

    def create_profiles(self, profiles):
        file = "{"
        if type(profiles[0]) == Profile:
            for profile in profiles:
                file += f'{str(self.create_profile(profile).readline())[1:-1]},'
        else:
            for profile in profiles:
                file += f'{str(profile)[1:-1]},'
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",")
        file = "{0}".format(str(file)[:-1])
        file += "}"
        file = StringIO(file)
        return file
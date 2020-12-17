"""

What this class does

"""
from io import StringIO

from Config import Config
from Profile import Profile

class Adept:

    def create_profile(self, profile):
        config = Config()
        expdate = profile.exp_date.split()
        exp_month = expdate[0]
        exp_year = f'20{expdate[2]}'
        file = str([{
            "BillingAddress1": profile.address,
            "BillingAddress2": profile.apt,
            "BillingAddress3": "",
            "BillingCity": profile.city,
            "BillingCountryCode": config.country_abbrev[profile.country],
            "BillingCountryName": profile.country,
            "BillingState": config.us_state_abbreviations[profile.state],
            "BillingZip": profile.zip_code,
            "CreditCardCV2": profile.cvv,
            "CreditCardMonth": exp_month,
            "CreditCardNumber": profile.card_number,
            "CreditCardType": "",
            "CreditCardYear": exp_year,
            "Email": profile.email,
            "FirstName": profile.first_name,
            "LastName": profile.last_name,
            "Phone": profile.phone,
            "ProfileName": profile.profile_name
        }])
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
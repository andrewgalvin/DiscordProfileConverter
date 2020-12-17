"""

What this class does


"""
from io import StringIO

from Config import Config
from Profile import Profile


class Tohru:

    def create_profile(self, profile):
        config = Config()
        expdate = profile.exp_date.split()
        exp_month = expdate[0]
        exp_year = f'20{expdate[2]}'
        if profile.country == "United States":
            country = "USA"
        else:
            country = profile.country
        file = str([{
            "profileName": profile.profile_name,
            "phone": profile.phone,
            "cardHolder": profile.card_holder_name,
            "cardNumber": profile.card_number,
            "expiryMonth": exp_month,
            "expiryYear": exp_year,
            "cardCVV": profile.cvv,
            "email": profile.email,
            "billingFirstName": profile.first_name,
            "billingLastName": profile.last_name,
            "billingAddress1": profile.address,
            "billingAddress2": profile.apt,
            "billingCountry": country,
            "billingCity": profile.city,
            "billingState": config.us_state_abbreviations[profile.state],
            "billingZip": profile.zip_code,
            "shippingFirstName": profile.first_name,
            "shippingLastName": profile.last_name,
            "shippingAddress1": profile.address,
            "shippingAddress2": profile.apt,
            "shippingCountry": country,
            "shippingCity": profile.city,
            "shippingState": config.us_state_abbreviations[profile.state],
            "shippingZip": profile.zip_code,
            "oneCheckoutPer": "false"
        }])
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"true"', "true").replace('"false"', "false").replace('"null"', "null").replace("True","true").replace("False","false").replace("None","null")
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
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"true"', "true").replace('"false"', "false").replace('"null"', "null").replace("True","true").replace("False","false").replace("None","null")
        file = f"[{str(file)[:-1]}]"
        file = StringIO(file)
        return file
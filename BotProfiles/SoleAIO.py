"""

What this class does

"""
import random
from io import StringIO

from Config import Config
from Profile import Profile

class SoleAIO:

    def create_profile(self, profile):
        config = Config()
        expdate = profile.exp_date.split()
        exp_month = expdate[0]
        exp_year = expdate[2]
        if config.get_card_type(profile.card_number) == "MasterCard":
            card_type = "Mastercard"
        else:
            card_type = config.get_card_type(profile.card_number)
        file = str([{
            "ID": random.randint(0, 100),
            "ProfileName": profile.profile_name,
            "Email": profile.email,
            "Phone": profile.phone,
            "ShippingFirstName": profile.first_name,
            "ShippingLastName": profile.last_name,
            "ShippingAddress1": profile.address,
            "ShippingAddress2": profile.apt,
            "ShippingCity": profile.city,
            "ShippingZip": profile.zip_code,
            "ShippingCountry": profile.country,
            "ShippingState": profile.state,
            "UseBilling": "false",
            "BillingFirstName": "",
            "BillingLastName": "",
            "BillingAddress1": "",
            "BillingAddress2": "",
            "BillingCity": "",
            "BillingZip": "",
            "BillingCountry": profile.country,
            "BillingState": "",
            "CardNumber": profile.card_number,
            "CardName": profile.card_holder_name,
            "CardCvv": profile.cvv,
            "CardExpiryMonth": exp_month,
            "CardExpiryYear": exp_year,
            "CardType": card_type,
            "CheckoutLimit": "No checkout limit"
        }])
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"false"', "false")
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
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"true"', "true").replace("False","false").replace("True","true")
        file = f"[{str(file)[:-1]}]"
        file = StringIO(file)
        return file
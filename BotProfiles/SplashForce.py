"""

What this class does

"""
from io import StringIO

from Profile import Profile


class SplashForce:

    def create_profile(self, profile):
        expdate = profile.exp_date.split()
        exp_month = expdate[0]
        exp_year = f'20{expdate[2]}'
        file = str([{
            "profileName": profile.profile_name,
            "email": profile.email,
            "billingAddress": {
                "firstName": profile.first_name,
                "lastName": profile.last_name,
                "addressOne": profile.address,
                "addressTwo": profile.apt,
                "zip": profile.zip_code,
                "city": profile.city,
                "state": profile.state,
                "country": profile.country,
                "phone": profile.phone
            },
            "shippingAddress": {
                "firstName": profile.first_name,
                "lastName": profile.last_name,
                "addressOne": profile.address,
                "addressTwo": profile.apt,
                "zip": profile.zip_code,
                "city": profile.city,
                "state": profile.state,
                "country": profile.country,
                "phone": profile.phone
            },
            "card": {
                "cardHolderName": profile.card_holder_name,
                "cardNumber": profile.card_number,
                "cardExpiryMonth": exp_month,
                "cardExpiryYear": exp_year,
                "cardCVV": profile.cvv
            },
            "jigAddress": "false",
            "oneCheckout": "false",
            "shipToBill": "false"
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
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"false"', "false").replace("False","false")
        file = f"[{str(file)[:-1]}]"
        file = StringIO(file)
        return file
"""

What this class does


"""
from io import StringIO

from Config import Config
from Profile import Profile


class Wrath:

    def create_profile(self, profile):
        config = Config()
        expdate = profile.exp_date.split()
        exp_month = expdate[0]
        exp_year = expdate[2]
        card_type = config.get_card_type(profile.card_number)
        if card_type == 'American Express':
            card_type = 'Amex'
        file = str([{
            "billingAddress": {
                "city": profile.city,
                "country": profile.country,
                "email": profile.email,
                "line1": profile.address,
                "line2": profile.apt,
                "line3": "",
                "name": f'{profile.first_name} {profile.last_name}',
                "phone": profile.phone,
                "postCode": profile.zip_code,
                "state": config.us_state_abbreviations[profile.state]
            },
            "name": profile.profile_name,
            "onlyCheckoutOnce": "FALSE",
            "paymentDetails": {
                "cardCvv": profile.cvv,
                "cardExpMonth": exp_month,
                "cardExpYear": exp_year,
                "cardNumber": profile.card_number,
                "cardType": card_type,
                "nameOnCard": profile.card_holder_name
            },
            "sameBillingAndShippingAddress": "true",
            "shippingAddress": {
                "city": profile.city,
                "country": profile.country,
                "email": profile.email,
                "line1": profile.address,
                "line2": profile.apt,
                "line3": "",
                "name": f'{profile.first_name} {profile.last_name}',
                "phone": profile.phone,
                "postCode": profile.zip_code,
                "state": config.us_state_abbreviations[profile.state]
            }
        }])
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"true"', "true").replace("False","false").replace("True", "true")
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
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"true"', "true").replace("False","false").replace("True", "true")
        file = f"[{str(file)[:-1]}]"
        file = StringIO(file)
        return file

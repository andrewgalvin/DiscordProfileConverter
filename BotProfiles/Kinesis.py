"""

What this class does

"""
from io import StringIO

from Config import Config
from Profile import Profile

class Kinesis:

    def create_profile(self, profile):
        config = Config()
        expdate = profile.exp_date.split()
        exp_month = expdate[0]

        if '0' in exp_month[0]:
            exp_month = exp_month[1]
        else:
            exp_month = exp_month
        exp_year = f'20{expdate[2]}'
        id = f"{config.get_random_string_lowercase(8)}-{config.get_random_string_lowercase(4)}-{config.get_random_string_lowercase(4)}-{config.get_random_string_lowercase(4)}-{config.get_random_string_lowercase(12)}"
        file = str({
            id: {
                "profileID": id, "profileName": f"{profile.profile_name}", "sameBilling": "true", "email": f"{profile.email}",
                "cardHolderName": f"{profile.card_holder_name}", "cardNumber": f"{profile.card_number}",
                "cardExpiration": f"{exp_month}/{exp_year}", "cardCVV": f"{profile.cvv}",
                "shippingName": f"{profile.first_name} {profile.last_name}",
                "shippingAddress": f"{profile.address}", "shippingAddressTwo": f"{profile.apt}", "shippingCountry": f"{profile.country}",
                "shippingState": f"{config.us_state_abbreviations[profile.state]}", "shippingCity": f"{profile.city}", "shippingZip": f"{profile.zip_code}",
                "shippingPhone": f"{profile.phone}", "billingName": f"{profile.card_holder_name}", "billingAddress": f"{profile.address}",
                "billingAddressTwo": f"{profile.apt}", "billingCountry": f"{profile.country}",
                "billingState": f"{config.us_state_abbreviations[profile.state]}", "billingCity": f"{profile.city}", "billingZip": f"{profile.zip_code}",
                "billingPhone": f"{profile.phone}"
            }
        })
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"true"', "true")
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
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"true"', "true").replace("True","true")
        file = f"{str(file)[:-1]}"
        file += "}"
        file = StringIO(file)
        return file
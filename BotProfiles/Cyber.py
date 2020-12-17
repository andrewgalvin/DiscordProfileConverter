"""

What this class does


"""
from io import StringIO

from Profile import Profile


class Cyber:

    def create_profile(self, profile):
        expdate = profile.exp_date.split()
        exp_month = expdate[0]
        exp_year = f'20{expdate[2]}'

        if len(profile.card_number) > 16:
            card_number = f'{profile.card_number[0:4]} {profile.card_number[4:8]} {profile.card_number[8:12]} {profile.card_number[12:16]} {profile.card_number[16:len(profile.card_number)]}'
        else:
            card_number = f'{profile.card_number[0:4]} {profile.card_number[4:8]} {profile.card_number[8:12]} {profile.card_number[12:16]}'
        file = str([{
            "name": profile.profile_name,
            "email": profile.email,
            "phone": profile.phone,
            "sizes": ["Random"],
            "taskAmount": 1,
            "singleCheckout": "false",
            "billingDifferent": "false",
            "favorite": "false",
            "card": {
                "number": card_number,
                "expiryMonth": exp_month,
                "expiryYear": exp_year,
                "cvv": profile.cvv
            },
            "delivery": {
                "firstName": profile.first_name,
                "lastName": profile.last_name,
                "address1": profile.address,
                "address2": profile.apt,
                "zip": profile.zip_code,
                "city": profile.city,
                "country": profile.country,
                "state": profile.state
            },
            "billing": {
                "firstName": profile.first_name,
                "lastName": profile.last_name,
                "address1": profile.address,
                "address2": profile.apt,
                "zip": profile.zip_code,
                "city": profile.city,
                "country": profile.country,
                "state": profile.state
            }
        }])
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"true"', "true").replace("False","false").replace("True","true")
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

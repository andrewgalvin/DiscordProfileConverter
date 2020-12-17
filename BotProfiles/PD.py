"""

What this class does

"""
from io import StringIO

from Config import Config
from Profile import Profile

class PD:

    def create_profile(self, profile):
        if len(profile.card_number) > 16:
            card_number = f'{profile.card_number[0:4]} {profile.card_number[4:8]} {profile.card_number[8:12]} {profile.card_number[12:16]} {profile.card_number[16:len(profile.card_number)]}'
        else:
            card_number = f'{profile.card_number[0:4]} {profile.card_number[4:8]} {profile.card_number[8:12]} {profile.card_number[12:16]}'
        config = Config()
        file = str([{
            "title": profile.profile_name,
            "billing": {
                "address1": profile.address,
                "address2": profile.apt,
                "city": profile.city,
                "country": profile.country,
                "firstName": profile.first_name,
                "lastName": profile.last_name,
                "phone": profile.phone,
                "state": profile.state,
                "zipcode": profile.zip_code
            },
            "card": {
                "name": profile.card_holder_name,
                "number": card_number,
                "expire": profile.exp_date,
                "code": profile.cvv
            },
            "email": profile.email,
            "id": config.get_random_string_uppercase(9),
            "limit": "true",
            "match": "true",
            "dotTrick": "false",
            "jigAddress": "false",
            "jigPhone": "false",
            "shipping": {
                "firstName": profile.first_name,
                "lastName": profile.last_name,
                "address1": profile.address,
                "address2": profile.apt,
                "city": profile.city,
                "state": profile.state,
                "zipcode": profile.zip_code,
                "country": profile.country,
                "phone": profile.phone
            }
        }])
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"true"', "true").replace('"false"', "false")
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

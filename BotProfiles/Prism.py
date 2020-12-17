"""

What this class does

"""
import time
from io import StringIO

from Config import Config
from Profile import Profile


class Prism:

    def create_profile(self, profile):
        config = Config()
        expdate = profile.exp_date.split()
        exp_month = expdate[0]
        exp_year = f'20{expdate[2]}'
        file = str([{
            "id": f"{config.get_random_string_lowercase(8)}-{config.get_random_string_lowercase(4)}-{config.get_random_string_lowercase(4)}-{config.get_random_string_lowercase(4)}-{config.get_random_string_lowercase(12)}",
            "createdAt": 0,
            "updatedAt": int(time.time()),
            "name": profile.profile_name,
            "email": profile.email,
            "oneTimeUse": "false",
            "shipping": {
                "firstName": profile.first_name,
                "lastName": profile.last_name,
                "address1": profile.address,
                "address2": profile.apt,
                "city": profile.city,
                "province": profile.state,
                "postalCode": profile.zip_code,
                "country": profile.country,
                "phone": profile.phone
            },
            "billing": {
                "sameAsShipping": "true",
                "firstName": profile.first_name,
                "lastName": profile.last_name,
                "address1": profile.address,
                "address2": profile.apt,
                "city": profile.city,
                "province": profile.state,
                "postalCode": profile.zip_code,
                "country": profile.country,
                "phone": profile.phone
            },
            "payment": {
                "name": profile.card_holder_name,
                "num": profile.card_number,
                "cvv": profile.cvv,
                "year": exp_year,
                "month": exp_month
            }
        }])
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"true"', "true").replace('"false"',
                                                                                                              "false")
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
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"true"', "true").replace('"false"',"false").replace("True","true").replace("False","false")
        file = f"[{str(file)[:-1]}]"
        file = StringIO(file)
        return file

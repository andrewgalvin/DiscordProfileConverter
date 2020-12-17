"""

What this class does

"""
from io import StringIO

from Config import Config
from Profile import Profile

class Polaris:

    def create_profile(self, profile):
        config = Config()
        expdate = profile.exp_date.split()
        exp_month = expdate[0]

        if '0' in exp_month[0]:
            exp_month_value = exp_month[1]
        else:
            exp_month_value = exp_month
        exp_year = f'20{expdate[2]}'
        file = str([{

            "name": profile.profile_name,
            "uuid": f'{config.get_random_string_lowercase(8)}-{config.get_random_string_lowercase(4)}-{config.get_random_string_lowercase(4)}-{config.get_random_string_lowercase(4)}-{config.get_random_string_lowercase(12)}',
            "email": profile.email,
            "shipping": {

                "first_name": profile.first_name,
                "last_name": profile.last_name,
                "address_line_1": profile.address,
                "address_line_2": profile.apt,
                "company": "",
                "state": {
                    "label": profile.state, "value": config.us_state_abbreviations[profile.state]
                }

                ,
                "country": {
                    "label": profile.country, "value": config.country_abbrev[profile.country]
                }

                ,
                "phone": profile.phone,
                "city": profile.city,
                "zipcode": profile.zip_code
            }

            ,
            "billing": {

                "first_name": profile.first_name,
                "last_name": profile.last_name,
                "address_line_1": profile.address,
                "address_line_2": profile.apt,
                "company": "",
                "state": {
                    "label": profile.state, "value": config.us_state_abbreviations[profile.state]
                }

                ,
                "country": {
                    "label": profile.country, "value": config.country_abbrev[profile.country]
                }

                ,
                "phone": profile.phone,
                "city": profile.city,
                "zipcode": profile.zip_code
            }

            ,
            "card": {

                "number": profile.card_number,
                "expiry": {
                    "month": {
                        "label": exp_month, "value": exp_month_value
                    }

                    ,
                    "year": {
                        "label": exp_year, "value": exp_year
                    }
                }

                ,
                "cvv": profile.cvv
            }

            ,
            "sameAddress": "true",
            "id": config.get_random_string_uppercase(9)
        }

        ])
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"true"', "true")
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
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"true"', "true").replace("True","true")
        file = f"[{str(file)[:-1]}]"
        file = StringIO(file)
        return file
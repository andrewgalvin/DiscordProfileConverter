"""

What this class does


"""
import calendar
import time
from io import StringIO
from Config import Config
from Profile import Profile


class NSB:

    def create_profile(self, profile):
        config = Config

        file = str([{
            "shipping": {
                "firstname": profile.first_name,
                "lastname": profile.last_name,
                "country": config.country_abbrev[profile.country],
                "city": profile.city,
                "address": profile.address,
                "address2": profile.apt,
                "state": config.us_state_abbreviations[profile.state],
                "zip": profile.zip_code,
                "phone": profile.phone
            },
            "name": profile.profile_name,
            "cc": {
                "number": profile.card_number,
                "expiry": profile.exp_date,
                "cvc": profile.cvv,
                "name": profile.card_holder_name
            },
            "email": profile.email,
            "checkoutLimit": "1",
            "billingSame": "True",
            "date": calendar.timegm(time.gmtime())
        }])
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"true"', "true").replace("True","true")
        file = StringIO(file)
        return file

    def create_profiles(self, profiles):
        file = ""
        if type(profiles[0]) == Profile:
            for profile in profiles:
                file += f"{str(self.create_profile(profile).readline())[1:-1]},"
        else:
            for profile in profiles:
                file += f"{str(profile)[1:-1]},"
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"true"', "true").replace("True","true")
        file = f"[{str(file)[:-1]}]"
        file = StringIO(file)
        return file
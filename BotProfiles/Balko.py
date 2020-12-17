"""

What this bot does

"""
from io import StringIO

from Profile import Profile


class Balko:

    def create_profile(self, profile):
        expdate = profile.exp_date.split()
        exp_month = expdate[0]
        exp_year = f'20{expdate[2]}'
        file = str([{
            "id": profile.profile_name,
            "firstname": profile.first_name,
            "lastname": profile.last_name,
            "email": profile.email,
            "phone": profile.phone,
            "add1": profile.address,
            "add2": profile.apt,
            "state": profile.state,
            "zip": profile.zip_code,
            "country": profile.country,
            "city": profile.city,
            "ccfirst": profile.card_holder_name.split()[0],
            "cclast": profile.card_holder_name.split()[1],
            "cc": profile.card_number,
            "expm": exp_month,
            "expy": exp_year,
            "ccv": profile.cvv,
            "random": "false",
            "dotTrick": "false",
            "oneCheckout": "false",
            "bfirstname": profile.card_holder_name.split()[0],
            "blastname": profile.card_holder_name.split()[1],
            "badd1": profile.address,
            "badd2": profile.apt,
            "bstate": profile.state,
            "bzip": profile.zip_code,
            "bcountry": profile.country,
            "bcity": profile.city
        }])
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"true"', "true").replace("False","false").replace("True", "true").replace('"false"',"false")
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
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"true"', "true").replace("False","false").replace("True", "true").replace('"false"',"false")
        file = f"[{str(file)[:-1]}]"
        file = StringIO(file)
        return file
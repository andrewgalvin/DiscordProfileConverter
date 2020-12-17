"""

What this class does

"""
import json
from io import StringIO
from Config import Config
from Profile import Profile

class Fluid:

    def create_profile(self, profile):
        config = Config()
        expdate = profile.exp_date.split()
        exp_month = expdate[0]
        exp_year = expdate[2]
        card_type = str(config.get_card_type(profile.card_number)).lower()
        file = str({
            profile.profile_name: {
                "shippingInfo": {
                  "firstName": profile.first_name,
                  "lastName": profile.last_name,
                  "email": profile.email,
                  "phoneNumber": profile.phone,
                  "addressLineOne": profile.address,
                  "addressLineTwo": profile.apt,
                  "country": "USA",
                  "city": profile.city,
                  "state": config.us_state_abbreviations[profile.state],
                  "zipCode": profile.zip_code
                },
                "isBilling": "false",
                "billingInfo": {
                  "firstName": "null",
                  "lastName": "null",
                  "email": "null",
                  "phoneNumber": "null",
                  "addressLineOne": "null",
                  "addressLineTwo": "null",
                  "country": "null",
                  "city": "null",
                  "state": "null",
                  "zipCode": "null"
                },
                "cardInfo": {
                  "cardHolderFull": profile.card_holder_name,
                  "cardType": card_type,
                  "cardNumber": profile.card_number,
                  "cardExpMonth": exp_month,
                  "cardExpYear": exp_year,
                  "cardCvv": profile.cvv
                }
                }
        })
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"true"', "true").replace('"false"',"false").replace('"null"',"null")
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
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"true"', "true").replace("True","true").replace("False","false")
        file = "{0}".format(str(file)[:-1])
        file += "}"
        file = StringIO(file)
        return file
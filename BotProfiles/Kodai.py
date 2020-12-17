"""

What this class does

"""
from io import StringIO

from Profile import Profile

class Kodai:

    def create_profile(self, profile):
        exp_date = profile.exp_date.replace(" ", "")
        file = str({
            profile.profile_name: {
                "billingAddress": {
                    "address": profile.address,
                    "apt": profile.apt,
                    "city": profile.city,
                    "firstName": profile.first_name,
                    "lastName": profile.last_name,
                    "phoneNumber": profile.phone,
                    "state": profile.state,
                    "zipCode": profile.zip_code,
                    "region": profile.country
                },
                "deliveryAddress": {
                    "address": profile.address,
                    "apt": profile.apt,
                    "city": profile.city,
                    "firstName": profile.first_name,
                    "lastName": profile.last_name,
                    "phoneNumber": profile.phone,
                    "state": profile.state,
                    "zipCode": profile.zip_code,
                },
                "miscellaneousInformation": {
                    "deliverySameAsBilling": "false"
                },
                "paymentDetails": {
                    "cardHolder": profile.card_holder_name,
                    "cardNumber": profile.card_number,
                    "cvv": profile.cvv,
                    "emailAddress": profile.email,
                    "expirationDate": exp_date
                },
                "profileName": profile.profile_name,
                "region": profile.country
            }
        })
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"true"', "true").replace('"false"',"false")
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
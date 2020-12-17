"""

What this class does


"""
from io import StringIO
from Config import Config
from Profile import Profile


class Phantom:

    def create_profile(self, profile):
        config = Config()
        card_type = str(config.get_card_type(profile.card_number)).lower()
        if card_type == "american express":
            card_type = "amex"
        expdate = profile.exp_date.split()
        exp_month = expdate[0]
        exp_year = f'20{expdate[2]}'
        file = str([{
            "Billing": {
                "Address": profile.address,
                "Apt": profile.apt,
                "City": profile.city,
                "FirstName": profile.first_name,
                "LastName": profile.last_name,
                "State": config.us_state_abbreviations[profile.state],
                "Zip": profile.zip_code
            },
            "CCNumber": profile.card_number,
            "CVV": profile.cvv,
            "CardType": card_type,
            "Country": config.country_abbrev[profile.country],
            "Email": profile.email,
            "ExpMonth": exp_month,
            "ExpYear": exp_year,
            "Name": profile.profile_name,
            "Phone": profile.phone,
            "Same": "true",
            "Shipping": {
                "Address": profile.address,
                "Apt": profile.apt,
                "City": profile.city,
                "FirstName": profile.first_name,
                "LastName": profile.last_name,
                "State": config.us_state_abbreviations[profile.state],
                "Zip": profile.zip_code
            }
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

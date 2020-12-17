"""

What this class does

"""
from io import StringIO

from Config import Config
from Profile import Profile

class Rush:

    def create_profile(self, profile):
        config = Config()
        expdate = profile.exp_date.split()
        exp_month = expdate[0]
        exp_year = f'20{expdate[2]}'
        csv = "profile_name,email,ship_name,ship_phone,ship_address1,ship_address2,ship_city,ship_zip,ship_state,ship_country,card_name,card_address1,card_address2,card_city,card_zip,card_state,card_country,card_phone,card_number,card_cvc,card_expmonth,card_expyear,size" \
              f"\n{profile.profile_name},{profile.email},{profile.first_name} {profile.last_name},1-{profile.phone[0:3]}-{profile.phone[3:6]}-{profile.phone[6:len(profile.phone)]},{profile.address},{profile.apt},{profile.city},{profile.zip_code},{config.us_state_abbreviations[profile.state]},{config.country_abbrev[profile.country]},{profile.card_holder_name},{profile.address},{profile.apt},{profile.city},{profile.zip_code},{config.us_state_abbreviations[profile.state]},{config.country_abbrev[profile.country]},1-{profile.phone[0:3]}-{profile.phone[3:6]}-{profile.phone[6:len(profile.phone)]},{profile.card_number},{profile.cvv},{exp_month},{exp_year},\n"
        csv = StringIO(csv)
        return csv

    def create_profiles(self, profiles):
        file = ""
        if type(profiles[0]) is Profile:
            for profile in profiles:
                if profiles[0] == profile:
                    for line in self.create_profile(profile).readlines():
                        file += f"{line}"
                else:
                    for line in self.create_profile(profile).readlines():
                        print(line)
                        if line != self.create_profile(profile).readlines()[0]:
                            file += f"{line}"
        else:
            for profile in profiles:
                if profiles[0] == profile:
                    print("here")
                    file += f"{profile}"
                else:
                    file = file[:-1]
                    file += f"{profile[255:]}"
        file = StringIO(file)
        return file
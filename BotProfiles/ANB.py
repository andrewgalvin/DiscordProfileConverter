"""

What this class does

"""
from io import StringIO

from Config import Config
from Profile import Profile


class ANB:

    def create_profile(self, profile):
        config = Config()
        expdate = profile.exp_date.split()
        exp_month = expdate[0]
        if '0' in exp_month[0]:
            exp_month = exp_month[1]
        exp_year = f'20{expdate[2]}'

        if config.get_card_type(profile.card_number) == "American Express":
            card_type = "AMEX"
        else:
            card_type = str(config.get_card_type(profile.card_number)).upper()

        csv_file = 'ShippingAsBilling,FirstNameBilling,LastNameBilling,address1Billing,address2Billing,cityBilling,' \
                   'stateBilling,zipCodeBilling,countryBilling,phoneBilling,houseNbBilling,FirstNameShipping,' \
                   'LastNameShipping,address1Shipping,address2Shipping,cityShipping,stateShipping,zipCodeShipping,' \
                   'countryShipping,phoneShipping,houseNbShipping,friendlyName,NameOnCard,DOB,cardType,CardNumber,' \
                   'CardExpirationMonth,CardExpirationYear,CardSecurityCode,billingEmail,paypalEmail,paypalPassword,' \
                   'CheckoutDelaySeconds,CheckoutOncePerWebsite'
        csv_file += f'\n"False","{profile.first_name}","{profile.last_name}","{profile.address}","{profile.apt}","{profile.city}","{config.us_state_abbreviations[profile.state]}","{profile.zip_code}","{config.country_abbrev[profile.country]}","{profile.phone}","","{profile.first_name}","{profile.last_name}","{profile.address}","{profile.apt}","{profile.city}","{config.us_state_abbreviations[profile.state]}","{profile.zip_code}","{config.country_abbrev[profile.country]}","{profile.phone}","","{profile.profile_name}","{profile.card_holder_name}","2/17/1997","{card_type}","{profile.card_number}","{exp_month}","{exp_year}","{profile.cvv}","{profile.email}","","","0","False"\n'
        csv_file = StringIO(csv_file)
        return csv_file

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
                    file += f"{profile}"
                else:
                    file = file[:-1]
                    file += f"{profile[511:]}"
        file = StringIO(file)
        return file

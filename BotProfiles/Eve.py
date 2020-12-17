"""

What this class does

"""
from io import StringIO

from Config import Config
from Profile import Profile


class Eve:

    def create_profile(self, profile):
        expdate = profile.exp_date.split()
        exp_month = expdate[0]
        exp_year = f'20{expdate[2]}'
        config = Config()
        xml = '<?xml version="1.0" encoding="utf-8"?>'
        xml += '\n<ArrayOfProfile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
        xml += "\n\t<Profile>"
        xml += f"\n\t\t<ProfileName>{profile.profile_name}</ProfileName>"
        xml += f"\n\t\t<BillingFirstName>{profile.first_name}</BillingFirstName>"
        xml += f"\n\t\t<BillingLastName>{profile.last_name}</BillingLastName>"
        xml += f"\n\t\t<BillingAddressLine1>{profile.address}</BillingAddressLine1>"
        if profile.apt == "":
            xml += f"\n\t\t<BillingAddressLine2 />"
        else:
            xml += f"\n\t\t<BillingAddressLine2>{profile.apt}</BillingAddressLine2>"
        xml += f"\n\t\t<BillingCity>{profile.city}</BillingCity>"
        xml += f"\n\t\t<BillingState>{config.us_state_abbreviations[profile.state]}</BillingState>"
        xml += f"\n\t\t<BillingCountryCode>{config.country_abbrev[profile.country]}</BillingCountryCode>"
        xml += f"\n\t\t<BillingZip>{profile.zip_code}</BillingZip>"
        xml += f"\n\t\t<BillingPhone>{profile.phone}</BillingPhone>"
        xml += f"\n\t\t<BillingEmail>{profile.email}</BillingEmail>"
        xml += f"\n\t\t<ShippingFirstName>{profile.first_name}</ShippingFirstName>"
        xml += f"\n\t\t<ShippingLastName>{profile.last_name}</ShippingLastName>"
        xml += f"\n\t\t<ShippingAddressLine1>{profile.address}</ShippingAddressLine1>"
        if profile.apt == "":
            xml += f"\n\t\t<ShippingAddressLine2>{profile.apt}</ShippingAddressLine2>"
        else:
            xml += f"\n\t\t<ShippingAddressLine2 />"
        xml += f"\n\t\t<ShippingCity>{profile.city}</ShippingCity>"
        xml += f"\n\t\t<ShippingState>{config.us_state_abbreviations[profile.state]}</ShippingState>"
        xml += f"\n\t\t<ShippingCountryCode>{config.country_abbrev[profile.country]}</ShippingCountryCode>"
        xml += f"\n\t\t<ShippingZip>{profile.zip_code}</ShippingZip>"
        xml += f"\n\t\t<ShippingPhone>{profile.phone}</ShippingPhone>"
        xml += f"\n\t\t<ShippingEmail>{profile.email}</ShippingEmail>"
        xml += f"\n\t\t<NameOnCard>{profile.card_holder_name}</NameOnCard>"
        xml += f"\n\t\t<CreditCardNumber>{profile.card_number}</CreditCardNumber>"
        xml += f"\n\t\t<ExpirationMonth>{exp_month}</ExpirationMonth>"
        xml += f"\n\t\t<ExpirationYear>{exp_year}</ExpirationYear>"
        xml += f"\n\t\t<Cvv>{profile.cvv}</Cvv>"
        xml += f"\n\t\t<CardType>{config.get_card_type(profile.card_number)}</CardType>"
        xml += "\n\t\t<OneCheckoutPerWebsite>false</OneCheckoutPerWebsite>"
        xml += "\n\t\t<SameBillingShipping>true</SameBillingShipping>"
        xml += "\n\t\t<BirthDay>12</BirthDay>"
        xml += "\n\t\t<BirthMonth>25</BirthMonth>"
        xml += "\n\t\t<BirthYear>1975</BirthYear>"
        xml += "\n\t</Profile>"
        xml += "\n</ArrayOfProfile>"
        return xml

    def create_profiles(self, profiles):
        file = ""
        if type(profiles[0]) == Profile:
            for profile in profiles:
                print(profile)
                if profiles[0] == profile and profile != profiles[len(profiles)-1]:
                    file += f"{str(self.create_profile(profile))[:-19]}"
                elif profile == profiles[len(profiles)-1] and profiles[0] == profile:
                    file += f"{str(self.create_profile(profile))}"
                elif profile == profiles[len(profiles)-1]:
                    file += f"{str(self.create_profile(profile))[37:]}"
                else:
                    file += f"{str(self.create_profile(profile))[37:-19]}"
        else:
            for profile in profiles:
                if profiles[0] == profile:
                    file += f"{str(profile)[:-19]}"
                elif profile == profiles[len(profiles) - 1]:
                    file += f"{str(profile)[38:]}"
                else:
                    file += f"{str(profile)[38:-19]}"
        print(file)
        file = StringIO(file)
        return file
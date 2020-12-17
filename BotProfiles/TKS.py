"""

What this class does


"""
from io import StringIO

from Config import Config
from Profile import Profile


class TKS:

    def create_profile(self, profile):
        config = Config()
        expdate = profile.exp_date.split()
        exp_month = expdate[0]
        exp_year = f'20{expdate[2]}'
        file = str({
            "Locale": "EN",
            "Tasks": [],
            "Profiles": [{
                "Id": f"{config.get_random_string_lowercase(length=8)}-{config.get_random_string_lowercase(length=4)}-{config.get_random_string_lowercase(length=4)}-{config.get_random_string_lowercase(length=4)}-{config.get_random_string_lowercase(length=12)}",
                "Name": profile.profile_name,
                "Billing": {
                    "Pccc": "null",
                    "Email": profile.email,
                    "FirstName": profile.first_name,
                    "Lastname": profile.last_name,
                    "AddressLine1": profile.address,
                    "AddressLine2": profile.apt,
                    "Zip": profile.zip_code,
                    "City": profile.city,
                    "CountryCode": config.country_abbrev[profile.country],
                    "StateCode": config.us_state_abbreviations[profile.state],
                    "Phone": profile.phone
                },
                "Shipping": {
                    "Pccc": "null",
                    "Email": profile.email,
                    "FirstName": profile.first_name,
                    "Lastname": profile.last_name,
                    "AddressLine1": profile.address,
                    "AddressLine2": profile.apt,
                    "Zip": profile.zip_code,
                    "City": profile.city,
                    "CountryCode": config.country_abbrev[profile.country],
                    "StateCode": config.us_state_abbreviations[profile.state],
                    "Phone": profile.phone
                },
                "Payment": {
                    "CardHolder": profile.card_holder_name,
                    "CardNumber": profile.card_number,
                    "ExpirationMonth": exp_month,
                    "ExpirationYear": exp_year,
                    "SecurityCode": profile.cvv,
                    "CardType": 1
                },
                "Options": {
                    "UseBillingForShipping": "true",
                    "OneItemPerWebsite": "true"
                }
            }],
            "Proxies": [],
            "CaptchaSolvers": [],
            "RemoteTaskSettings": [{
                "WebsiteId": "master",
                "RetryDelayFrom": 500,
                "RetryDelayTo": 1000,
                "MonitoringProxyListId": "null",
                "CheckoutProxyListId": "null",
                "PaymentMethodId": "null",
                "AutoStart": "false",
                "Sizes": "Any Available",
                "Profiles": []
            }],
            "ShopifyStores": [],
            "Logins": {},
            "DiscordWebhook": "null",
            "SendCheckoutToGroupDiscord": "false",
            "TaskToastNotifications": "false"
        })
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"true"', "true").replace('"false"', "false").replace('"null"', "null").replace("True","true").replace("None","null")
        file = StringIO(file)
        return file

    def create_profiles(self, profiles):
        file = ""
        if type(profiles[0]) == Profile:
            for profile in profiles:
                content = str(self.create_profile(profile).readline())[38:-376]
                if profile == profiles[0]:
                    file += '{"Locale":"EN","Tasks":[],"Profiles":['
                file += f"{str(content)},"
                if profile == profiles[-1]:
                    file = file[:-1]
                    file += '],"Proxies":[],"CaptchaSolvers":[],"RemoteTaskSettings":[{"WebsiteId":"master","RetryDelayFrom":500,"RetryDelayTo":1000,"MonitoringProxyListId":null,"CheckoutProxyListId":null,"PaymentMethodId":null,"AutoStart":false,"Sizes":"Any Available","Profiles":[]}],"ShopifyStores":[],"Logins":{},"DiscordWebhook":null,"SendCheckoutToGroupDiscord":false,"TaskToastNotifications":false}'
        else:
            for profile in profiles:
                content = str(profile)[43:-409]
                if profile == profiles[0]:
                    file += '{"Locale":"EN","Tasks":[],"Profiles":['
                file += f"{str(content)},"
                if profile == profiles[-1]:
                    file = file[:-1]
                    file += '],"Proxies":[],"CaptchaSolvers":[],"RemoteTaskSettings":[{"WebsiteId":"master","RetryDelayFrom":500,"RetryDelayTo":1000,"MonitoringProxyListId":null,"CheckoutProxyListId":null,"PaymentMethodId":null,"AutoStart":false,"Sizes":"Any Available","Profiles":[]}],"ShopifyStores":[],"Logins":{},"DiscordWebhook":null,"SendCheckoutToGroupDiscord":false,"TaskToastNotifications":false}'
        file = file.replace("'", '"').replace(": ", ":").replace(", ", ",").replace('"true"', "true").replace('"false"', "false").replace('"null"', "null").replace("True","true").replace("None","null")
        file = StringIO(file)
        return file
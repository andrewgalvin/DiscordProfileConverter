"""

What this class does


"""
class Profile:

    global profile_name
    global address
    global apt
    global city
    global country
    global first_name
    global last_name
    global phone
    global state
    global zip_code
    global card_holder_name
    global card_number
    global exp_date
    global cvv
    global email

    def __init__(self, profile_name, address, apt, city, country, first_name, last_name, phone, state, zip_code, card_holder_name, card_number, exp_date, cvv, email):
        self.profile_name = profile_name
        self.address = address
        self.apt = apt
        self.city = city
        self.country = country
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.state = state
        self.zip_code = zip_code
        self.card_holder_name = card_holder_name
        self.card_number = card_number
        self.exp_date = exp_date
        self.cvv = cvv
        self.email = email

    def __str__(self):
        return "Profile Name,Address,Apt,City,Country,First Name,Last Name,Phone,State,Zip Code,Card Holder Name,Card Number,Exp Date,CVV,Email\n{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14}\n".format(self.profile_name, self.address, self.apt, self.city, self.country, self.first_name,self.last_name,self.phone, self.state, self.zip_code,self.card_holder_name,self.card_number,self.exp_date,self.cvv, self.email)
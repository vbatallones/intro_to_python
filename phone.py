class Phone():
    def __init__(self, phone_number):
        self.number = phone_number

    def call(self, other_number):
        print("Calling {} from {}".format(other_number, self.number))

    def text(self, other_number, msg):
        print(f"Sending text to {other_number} from {self.number}")
        print(msg)

    def open_app(self, app_name):
        print("Opening {} on device".format(app_name))


class Iphone(Phone):
    def __init__(self, phone_number):
        super().__init__(phone_number)
        self.fingerprint = None

    def sef_fingerprint(self, new_fingerprint):
        self.fingerprint = new_fingerprint

    def unlock(self, fingerprint=None):
        if(fingerprint == None and self.fingerprint == None):
            print("Phone is unlocked because no fingerprint is currently set")

        if (fingerprint == self.fingerprint):
            print("Phone is unlocked")
        else: 
            print("Phone locked. Fingerprint does not match")

vin_iphone = Iphone(1234444999)
print("Vin's number is {}".format(vin_iphone.number))

vin_iphone.sef_fingerprint("password")
print(vin_iphone.fingerprint)

vin_iphone.unlock("passwordss")

vin_iphone.call(9713346461)

vin_iphone.open_app("Email")
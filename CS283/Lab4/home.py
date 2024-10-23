class Home:
    def __init__(self, zip, price, year, size):
        self.zip = zip
        self.price = price
        self.year = year
        self.size = size

    def psf(self):
        return self.price/self.size

    def isModern(self):
        if self.year >= 2012:
            return True
        else:
            return False
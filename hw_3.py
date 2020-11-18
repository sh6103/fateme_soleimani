from datetime import datetime


class SingleTripCard:
    """
    Single trip card that can be used only once
    """

    def __init__(self, price_of_trip):
        self.price_of_trip = price_of_trip

    def use(self):
        """
        Use the card to travel
        :return: Done or not
        """
        if self.price_of_trip == 0:
            print("Sorry your card has been used")
        else:
            self.price_of_trip -= self.price_of_trip
            print("Done")


class CreditTimeCard:
    """
    If the card has not expired, it can be used or increased if it has credit
    """
    flag = True

    def __init__(self, price_of_trip, credit, date):
        """
        :param price_of_trip:Unit price per trip
        :param credit:Card credit
        :param date:Card expiration date
        """
        self.credit = credit
        self.date = date
        self.price_of_trip = price_of_trip

    def check(self):
        """
        Checks the expiration date of the card
        :return: True or False
        """
        validity_year = int(self.date[0:4])
        validity_month = int(self.date[5:7])
        validity_day = int(self.date[8:10])
        if datetime.today().year > validity_year:
            self.flag = False
        elif datetime.today().year == validity_year:
            if datetime.today().month > validity_month:
                self.flag = False
            elif datetime.today().month == validity_month:
                if datetime.today().day > validity_day:
                    self.flag = False
                else:
                    self.flag = True
            else:
                self.flag = True
        else:
            self.flag = True

    def use(self):
        """
        Use the card to travel
        :return: Done or not
        """
        if self.flag:
            if self.credit < self.price_of_trip:
                return "Your credit is not enough, please increase your credit"
            else:
                self.credit -= self.price_of_trip
                return "Done"
        else:
            return "Sorry, your card has expired."

    def charge(self, other):
        """
        Increases the credit of the card
        :param other:The rate of credit increase
        :return:Current validity rate
        """
        if self.flag:
            self.credit += other
            return "{} Tomans has been added to your card credit and now the credit of your card is {} Tomans".format(
                other, self.credit)
        else:
            return "Sorry, your card has expired."

    def __str__(self):
        return "credit of card:" + str(self.credit)


class CreditCard:
    """
    You can use it,if you have credit and you can also increase the credit.
    """

    def __init__(self, price_of_trip, credit):
        self.price_of_trip = price_of_trip
        self.credit = credit

    def charge(self, other):
        """
        Increases the credit of the card
        :param other:The rate of credit increase
        :return:Current validity rate
        """
        self.credit += other
        print("{} Tomans has been added to your card credit and now the credit of your card is {} Tomans".format(other,
                                                                                                                 self.credit))

    def use(self):
        """
        Use the card to travel
        :return: Done or not
        """
        if self.credit < self.price_of_trip:
            print("Your credit is not enough, please increase your credit")
        else:
            self.credit -= self.price_of_trip
            print("Done")

    def __str__(self):
        return "credit of card:" + str(self.credit)


price_of_each_trip = 100  # The cost of each trip is 100 Tomans
single_trip = SingleTripCard(price_of_each_trip)
single_trip.use()
single_trip.use()

credit_time = CreditTimeCard(price_of_each_trip, 700, "2020 11 07")
credit_time.check()
print(credit_time.use())

credit_card = CreditCard(price_of_each_trip, 200)
print(credit_card)
credit_card.charge(1000)

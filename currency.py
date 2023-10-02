#initializing
class Currency:
    def __init__(self):
        self.from_currency: str = None
        self.to_currency: str = None
        self.amount: float = 0
        self.rate: float = 0
        self.inverse_rate: float = 0
        self.date: str = None

    def from_json(self, result: dict):
        self.from_currency = result.get("base")
        self.to_currency = list(result.get("rates").keys())[0]
        self.amount = result.get("amount")
        self.rate = result.get("rates").get(self.to_currency)
        self.date = result.get("date")

   
    def round_rate(rate):
        """
        Function that will round an input float to 4 decimals places.

        Parameters
        ----------
        rate: float
            Rate to be rounded

        Returns
        -------
        float
            Rounded rate
        """
        rate = round(rate,4)
        return rate
        

    def reverse_rate(self):
        """
        Function that will calculate the inverse rate from the provided input rate.
        It will check if the provided input rate is not equal to zero.
        If it not the case, it will calculate the inverse rate and round it to 4 decimal places.
        Otherwise it will return zero.

        Parameters
        ----------
        rate: float
            FX conversion rate to be inverted

        Returns
        -------
        float
            Inverse of input FX conversion rate
        """
        self.inverse_rate = round((1/self.rate),4)
        


    def format_output(self):
        """
        Function that will calculate the inverse rate from the provided input rate.
        It will check if the provided input rate is not equal to zero.
        If it not the case, it will calculate the inverse rate and round it to 4 decimal places.
        Otherwise it will return zero.

        Parameters
        ----------
        rate: float
            FX conversion rate to be inverted

        Returns
        -------
        float
            Inverse of input FX conversion rate
        """

        self.inverse_rate = round((1/self.rate),4)

        return "The conversion rate on "+ self.date + " from " + self.from_currency + " to " + self.to_currency + " was " + str(self.rate) + ". So " + str(self.amount) + " in " + self.from_currency + " correspond to " + str(round((self.rate * self.amount),4)) +" in " + self.to_currency + ". The inverse rate was "+ str(self.inverse_rate)
    


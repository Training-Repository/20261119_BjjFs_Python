class Money:
    _RATES_IN_INR = {"INR": 1.0, "USD": 83.0, "EUR": 90.0, "GBP": 105.0}

    def __init__(self, denomination, currency):
        self.__denomination = self.__validate_denomination(denomination)
        self.__currency = self.__validate_currency(currency)

    # ---------- validation helpers ----------
    @staticmethod
    def __validate_denomination(value):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(f"denomination must be a number, got {type(value).__name__}")
        if value < 0:
            raise ValueError(f"denomination cannot be negative: {value}")
        return value

    @classmethod
    def __validate_currency(cls, value):
        if not isinstance(value, str):
            raise TypeError(f"currency must be a str, got {type(value).__name__}")
        value = value.strip().upper()
        if value not in cls._RATES_IN_INR:
            raise ValueError(f"unsupported currency: {value!r}")
        return value

    # ---------- properties ----------
    @property
    def denomination(self):
        return self.__denomination

    @denomination.setter
    def denomination(self, value):
        self.__denomination = self.__validate_denomination(value)

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, value):
        new_currency = self.__validate_currency(value)
        if new_currency == self.__currency:
            return
        print(f"Converting {self.__currency!r} to {new_currency!r}")
        amount_in_inr = self.__denomination * self._RATES_IN_INR[self.__currency]
        self.__denomination = round(amount_in_inr / self._RATES_IN_INR[new_currency], 2)
        self.__currency = new_currency

    # ---------- operators ----------
    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.__currency != other.__currency:
            raise ValueError(
                f"Cannot add {self.__currency!r} and {other.__currency!r}; "
                f"convert one of them first"
            )
        return Money(self.__denomination + other.__denomination, self.__currency)

    def __repr__(self):
        return f"Money({self.__denomination!r}, {self.__currency!r})"


#--------------------------------

if __name__ == '__main__':
    m1 = Money(10, "INR")
    m2 = Money(20, "INR")
    m3 = Money(20, "INR")

    print(m3.currency)      # o/p: "INR"
    m3.currency = "USD"     # o/p: "Converting 'INR' to 'USD'"

    m4 = m1 + m2
    print(f"{m4 = }")


    # m5 = m1 + m3
    # print(f"{m5 = }")

    val = 12//5
    print(val)

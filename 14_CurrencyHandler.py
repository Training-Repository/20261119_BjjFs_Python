class Money:
    pass

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

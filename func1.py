def voters_verification(name,age):
    """ This is a function that accepts the name and age as
    parameters and checks for voter eligibility"""
    if age >= 18:
        print (name + ", you are " + str(age) + " years old. You are eligigible to vote.")
    else:
        print(name + ", you are " + str(age) + " years old. You are not eligigible to vote")
voters_verification('john',12)
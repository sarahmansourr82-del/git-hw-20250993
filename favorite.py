# This is a code that takes a positive  decimal number and converts it to binary
def convert_deci_to_bi(number):
    opp_result = []
    binary = ""
    if number == 0:
        return "0"
    while number > 0:
        opp_result += str(number % 2)
        number = number//2
    for i in range(len(opp_result)):
        binary += opp_result[-1]
        opp_result.pop()
    return (binary)

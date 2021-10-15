"""
unittest class - Test black box credit_card_validator() function.

General Rules:
    Visa
        Prefix(es): 4
        Length: 16
    MasterCard
        Prefix(es): 51 through 55 and 2221 through 2720
        Length: 16
    American Express
        Prefix(es): 34 and 37
        Length: 15

# BUG1: Function takes empty argument returns True.
# BUG2: 15 digit Visa with correct prefix and check digit returns True.
# BUG3: 16 digit Visa with correct prefix and check digit returns False.
# BUG4: 15 digit Amex with incorrect check digit returns True.
# BUG5: 16 digit Amex with correct check digit returns True.
# BUG6: 16 digit MC with correct check digit and prefix 2720 returns False.

TODO : add Amex with correct chk digit check.
"""

import unittest
from credit_card_validator import credit_card_validator


class TestStuff(unittest.TestCase):

    def luhn(self, input_digits):
        """
        Build check digits
        """
        iteration = 1
        total = 0
        for digit in reversed(input_digits):
            if iteration % 2 == 1:
                #  Sum of the digits in product
                temp = str(int(digit) * 2)
                for each_digit in temp:
                    total += int(each_digit)
            else:
                total += int(digit)
            iteration += 1
        check_luhn = 10 - (total % 10)
        if str(check_luhn)[-1] == "0":
            return 0
        else:
            return check_luhn

            #  Test all prefix combinations

    def test_mc_prefix(self):
        """
        check first and last digit prefix range of MC
        -Does not take any arguments, uses hard coded seed_number as base.
        """
        seed_number = "7484055663735"
        start = 51
        #  Test MC prefix 51-55
        while start <= 55:
            new_card = str(start) + seed_number
            chck_digit = self.luhn(new_card)
            new_card = new_card + str(chck_digit)

            with self.subTest(new_card):
                self.assertTrue(credit_card_validator(new_card) is True)
            start += 4

    def test_mc_prefix2(self):
        """
        Test first and last value of MC prefix range
        -Does not take any arguments, uses hard coded seed_number as base.
        """
        seed_number = "84055663735"
        start = 2221
        #  Test MC prefix 2221-2720
        while start <= 2720:
            new_card = str(start) + seed_number
            chck_digit = self.luhn(new_card)
            new_card = new_card + str(chck_digit)

            with self.subTest(new_card):
                self.assertTrue(credit_card_validator(new_card) is True)
            start += 499

    def test_Amex_prefix2(self):
        """
        Test first and last value of Amex prefix range
        -Does not take any arguments, uses hard coded seed_number as base.
        """
        seed_number = "1184055663735"
        start = 34
        #  Test MC prefix 2221-2720
        while start <= 37:
            new_card = str(start) + seed_number
            chck_digit = self.luhn(new_card)
            new_card = new_card + str(chck_digit)

            with self.subTest(new_card):
                self.assertTrue(credit_card_validator(new_card) is True)
            start += 3

    def test_visa_prefix(self):
        """Just a basic prefix test with good check digit"""
        assert credit_card_validator("4347903443661110") is True

    @classmethod
    def test_visa_prefix2(cls):
        """Basic prefix test with good check digit - playing with lint rules"""
        assert credit_card_validator("4588622317564881") is True

    def test_amex_bad_check_digit(self):
        """  Bad check digits  """
        assert credit_card_validator("340000000000000") is True

    def test4_amex_prefix2(self):
        assert credit_card_validator("370000000000000") is True

        # General testing

    def test_no_prefix(self):
        "  No prefix, correct check digit  "
        assert credit_card_validator("1111222233334444") is False

    def test_empty_argument(self):
        " No val"
        assert credit_card_validator("") is False

    def test_bad_prefix_chkdigit(self):
        "  No prefix, correct check digit  "
        assert credit_card_validator("1111222233334444") is False

        #  Test length settings.

    def test_visa_15digit(self):
        """  Visa prefix with 15 digits  """
        assert credit_card_validator("434790344366119") is False

    def test_mc_15digit(self):
        """  MasterCard prefix with 15 digits  """
        assert credit_card_validator("557484055663739") is False

    def test_mc_15digit2(self):
        assert credit_card_validator("222134343454343") is False

    def test_amex_16digit1(self):
        """  Amex prefix with 16 digits  """
        assert credit_card_validator("3418533739429892") is False


if __name__ == '__main__':
    unittest.main()
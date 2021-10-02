from credit_card_validator import credit_card_validator
import unittest

class TestStuff(unittest.TestCase):

    def luhn(self, input_digits):
        iteration = 1
        total = 0
        for digit in reversed(input_digits):
            if iteration % 2 == 1:
                temp = str(int(digit) * 2) #  Sum of the digits in product
                for each_digit in temp:
                    total += int(each_digit)
            else:
                total += int(digit)
            iteration += 1
        check_luhn = 10 - (total%10)
        if str(check_luhn)[-1]== "0":
            return 0
        else:
            return check_luhn

    def test_mc_prefix(self):
        seed_number = "7484055663735"
        start = 51
        "  Test MC prefix 51-55  "
        while start <= 55:
            new_card = str(start) + seed_number
            chck_digit = self.luhn(new_card)
            new_card = new_card + str(chck_digit)

            with self.subTest(new_card):
                self.assertTrue(credit_card_validator(new_card) is True)
            start += 1


    def test_mc_prefix2(self):
        seed_number = "84055663735"
        start = 2221
        "  Test MC prefix 2221-2720  "
        while start <= 2720:
            new_card = str(start) + seed_number
            chck_digit = self.luhn(new_card)
            new_card = new_card + str(chck_digit)

            with self.subTest(new_card):
                self.assertTrue(credit_card_validator(new_card) is True)
            start += 1


    def test1(self):
        "  No prefix, correct check digit  "
        assert credit_card_validator("1111222233334444") is False

    def test2(self):
        " No val"
        assert credit_card_validator("") is False

    def test1(self):
        "  No prefix, correct check digit  "
        assert credit_card_validator("1111222233334444") is False

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

    """  Prefix Testings """
    def test_visa_prefix(self):
        assert credit_card_validator("4347903443661110") is True

    def test_visa_prefix2(self):
        assert credit_card_validator("4588622317564881") is True

    def test_mc_prefix(self):
        assert credit_card_validator("5574840556637357") is True

    def test_mc_prefix2(self):
        assert credit_card_validator("2221333322224449") is True

    def test_amex_bad_check_digit(self):
        "  No check digits  "
        assert credit_card_validator("340000000000000") is True

    def test4_amex_prefix2(self):
        assert credit_card_validator("370000000000000") is True



if __name__ == '__main__':
    unittest.main()

import pytest


class Test002:
    @pytest.mark.math
    @pytest.mark.regression
    @pytest.mark.smoke

    def test_sum_004(self):
        print("Test001")
        a=1
        b=10
        sum=a+b
        print(f"sum of {a} and {b} is {sum}")
        assert  sum == 11
    @pytest.mark.regression
    @pytest.mark.smoke

    def test_sum_005(self):
        print("Test002")
        a=12
        b=10
        sum=a+b
        print(f"sum of {a} and {b} is {sum}")
        assert sum==22

    @pytest.mark.regression
    @pytest.mark.sanity

    def test_mul_06(self):
        print("Test003")
        a = 12
        b = 10
        mul = a * b
        print(f"Mul of {a} and {b} is {mul}")
        assert mul == 120

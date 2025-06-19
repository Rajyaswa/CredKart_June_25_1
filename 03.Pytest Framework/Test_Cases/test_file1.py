import pytest


class Test001:

    @pytest.mark.math
    @pytest.mark.sanity
    def test_sum_001(self):
        print("Test001")
        a = 1
        b = 10
        sum = a + b
        print(f"Sum of {a} and {b} is {sum}")
        assert sum == 11 # pass

    @pytest.mark.math
    @pytest.mark.sanity
    def test_sum_002(self):
        print("Test002")
        a = 12
        b = 10
        sum = a + b
        print(f"Sum of {a} and {b} is {sum}")
        assert sum == 22 # fail

    @pytest.mark.math
    @pytest.mark.smoke
    def test_mul_03(self):
        print("Test003")
        a = 12
        b = 10
        mul = a * b
        print(f"Mul of {a} and {b} is {mul}")
        assert mul == 120

    def mul_test(self):
        print("Test003")
        a = 12
        b = 12
        mul = a * b
        print(f"Mul of {a} and {b} is {mul}")
        assert mul == 144

    def div_05(self):
        print("Test005")
        a = 12
        b = 10
        div = a / b
        print(f"Div of {a} and {b} is {div}")
        assert div == 1.2
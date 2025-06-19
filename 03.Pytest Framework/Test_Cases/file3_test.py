class Test003:

    def test_sum_007(self):
        print("Test001")
        a = 1
        b = 10
        sum = a + b
        print(f"Sum of {a} and {b} is {sum}")
        assert sum == 11 # pass

    def test_sum_008(self):
        print("Test002")
        a = 12
        b = 10
        sum = a + b
        print(f"Sum of {a} and {b} is {sum}")
        assert sum == 22 # fail

    def test_mul_09(self):
        print("Test003")
        a = 12
        b = 10
        mul = a * b
        print(f"Mul of {a} and {b} is {mul}")
        assert mul == 120

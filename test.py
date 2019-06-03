class Test():
    @classmethod
    def test(cls, var):
        cls.test2(var)


    @staticmethod
    def test2(var):
        print(var)

Test.test("hallo")
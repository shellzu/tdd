class TestCase:
    def __init__(self, name):
        self.name = name

class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        super().__init__(name)

test = WasRun("testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)
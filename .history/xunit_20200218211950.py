class TestCase:
    def __init__(self, name):
        self.name = name

class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
    def run(self):
        method = getter(self, self.name)
    def testMethod(self):
        self.wasRun = 1

test = WasRun("testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)
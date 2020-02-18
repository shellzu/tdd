class TestCase:
    def __init__(self, name):
        self.name = name

class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        self.name = name
    def run(self):
        method = getter(self, self.name)
        method()

test = WasRun("testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)
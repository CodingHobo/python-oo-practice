class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """


    def __init__(self, start):
        """Accept a start value and assign a counter variable to the start value"""
        self.start = start
        self.counter = start

    def generate(self):
        """Increment the value of counter every time it is called and return the
        counter less one"""

        self.counter += 1
        return self.counter - 1

    def reset(self):
        """When called, reset the counter back to the start value"""
        self.counter = self.start



class A:
    def __init__(self):
        self.message = []
        self.__private()
        self.public()

    def __private(self):
        self.message.append("A.private()")

    def public(self):
        self.message.append("A.public()")


class B(A):
    def __private(self):
        self.message.append("B.private()")

    def public(self):
        self.message.append("B.public()")

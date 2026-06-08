from OopsDemo import Calculator


class ChildImplementation(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 250, 350)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()  # 200 + 100 + (250+350+100)


objChild = ChildImplementation()
print(objChild.getCompleteData())

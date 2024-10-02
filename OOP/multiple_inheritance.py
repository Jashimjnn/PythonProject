class Family:
    def __init__(self, address) -> None:
        self.address = address
    def ab(self):
        print('Bangladesh is a popular country')

class School:
    def __init__(self, id, level) -> None:
        self.id = id
        self.level = level
    def abc(self):
        print('Bangladesh is a beautiful country')

class Sports:
    def __init__(self, game) -> None:
        self.game = game
    def mf(self):
        print('Bangladesh is a rivering country')
class Student(Family, School, Sports):
    def __init__(self, address, id, level, game) -> None:
        School.__init__(self, id, level)
        Sports.__init__(self, game)
        Family.__init__(self, address)

    def __repr__(self) -> str:
        return f'I love Bangladesh {self.address} {self.id} {self.level} {self.game}'

st = Student(123,1,5,'Cricket')
print(st)
st.ab()
st.abc()
st.mf()
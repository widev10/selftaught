
#membuat script untk mengulang inheritance



class Mobil():
    def __init__(self,name):
        self.name = name
        
    def __repr__(self):
        return self.name

a_car = Mobil("Jazz")
print(a_car)
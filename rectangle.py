class Rectangle():
    def __init__(self, w, l):
        self.w = w
        self.l = l

    def calculate_perimeter(self):
        return self.w * 2 + self.l * 2
       
class Square():
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4 
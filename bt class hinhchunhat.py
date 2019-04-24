class HCN:
    def __init__ (self,dai, rong):
         self .dai=dai
         self .rong=rong
    def dientich(self):
         return self.dai *self.rong
a=HCN(5,7)
b=HCN(6,7)
print(a.dientich())
print(b.dientich())
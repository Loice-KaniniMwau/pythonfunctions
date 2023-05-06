class Fruit:
    def __init__(self,name,size,color,count) :
        self.name=name
        self.size=size
        self.color=color
        self.count=count
    def fruit_description(self):
        return f"{self.size} {self.color} {self.name}"
    def count_fruits(self,price,discount):
        totalprice=self.count*price
        if(totalprice>800):
           return(totalprice-discount)
        else:
            return totalprice
    def taste(self,taste):
        return f"{self.name} is a {taste} fruit"
    

    

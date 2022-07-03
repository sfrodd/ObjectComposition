
class Car:
    def __init__(self,name,model,engine,year=1995):
        self.name=name
        self.model=model
        self.year=year
        self.engine=engine

    def show(self):
        print(self.name + " Car of the year "+str(self.year))

    def accelerate(self,speed):
        print(self.name+" is accelaereated at "+str(speed))
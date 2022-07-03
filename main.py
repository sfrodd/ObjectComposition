from Engine import Engine
from Car import Car
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    e=Engine(192833,4)
    c=Car("Maruti","Zen",e)
    c.show()
    c.accelerate(50)
    print("This a Composition Project")
    print("Torque is = "+str(c.engine.generateTorque(50))+" Nw-Mtrs")




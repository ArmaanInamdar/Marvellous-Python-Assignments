class Vehicle:

    def start(self):
        print("Starting")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car started")
    
def main():
    obj1 = Car()
    obj1.start()
    

if __name__ == "__main__":
    main()
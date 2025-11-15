class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32  
    
    def to_kelvin(self):
        return self.celsius + 273.15      
    
input = int(input("Enter temperature in Celsius: "))
temp = Temperature(input)
print("Fahrenheit:", temp.to_fahrenheit())
print("Kelvin:", temp.to_kelvin())
 
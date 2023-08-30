class ConvertirTemperatura:
    @staticmethod
    def celsius_a_fahrenheit(celsius):
        return celsius * 9 / 5 + 32
    
    @staticmethod
    def fahrenheit_a_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9
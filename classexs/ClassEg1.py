from abc import abstractmethod


class BookAuthor:
    def __init__(self, name_author):
        self.name_author = name_author


    def return_details_object(self):
        self.name = self.name_author.split("-")[0]
        self.author = self.name_author.split("-")[1]
        return {"name": self.name, "author": self.author}

book_author = BookAuthor("Harry Potter - JK ROwling")
print(book_author.return_details_object())

class CalcTemp:
    @staticmethod
    def temp_celsius(farenheit_temp):
        return (farenheit_temp-32) *5/9
    @staticmethod
    def to_farenheit(celcius_temp):
        return (celcius_temp*1.8) +32

res = CalcTemp.temp_celsius(190)
print(res)
res = CalcTemp.to_farenheit(87.77)
print(res)


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
    @abstractmethod
    def miles(self):
        print("enforece sub classes to implement this method")

    def start(self):
        print("public method")

class Hyundai(Car):

    def __init__(self, make, model, year):

        super().__init__(make, model, year)

    def miles(self):
        print("Implemented..")



h = Hyundai("Honda", "Mercury", "2003")
h.start()
h.miles()
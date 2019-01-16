
# Car Models
# Use Python to build a console app that interacts with two files:

# car-makes --This file should contain just the names of several makes.
# car-models-- This file should contain the names of several models for each make. The format will be as follows: {first letter of make}={model name}

# Requirements
# Create a single class that implements all functionality.
# Create a method for reading the car makes file.
# Create a method for reading the car models file.
# Create a method that invokes the previous two methods and generates a dictionary.
# The dictionary keys will be the make names.
# The value for each key will be a list of model names.


class MakeCars:

    def read_makes(self):
        with open('data/car_makes.txt', 'r') as makes:
            make_list = makes.readlines()
            return make_list

    def read_models(self):
        with open('data/car_models.txt', 'r') as models:
            model_list = models.readlines()
            return model_list

    def create_car_dict(self):
        make_list = self.read_makes()
        model_list = self.read_models()
        car_dict = {}

        for make in make_list:
            make = make.strip()
            all_models = []
            for model in model_list:
                model = model.strip().split('=')
                if make[0] == model[0]:
                    all_models.append(model[1])
            car_dict[make] = all_models

        return car_dict


    def __str__(self):
        return f'Your car list: {self.create_car_dict()}'



making_cars = MakeCars()

print(making_cars)
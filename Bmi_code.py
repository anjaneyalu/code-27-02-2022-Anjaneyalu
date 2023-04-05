## calculate BMI and count the number of people who are Overweight
#import pandas as pd
#Code changes testing
import json
import argparse
import time

def calculate_bmi(data):
    """Function to calculate the BMI from input given a Json file and returns number of
    entries with overweight"""
    over_weight = []
    for i in data:
        BMI = i["WeightKg"]/((i["HeightCm"])/100)**2    
        if BMI <= 18.4:
            print("BMI:{} underweight, Health risk : Malnutrition risk".format(round(BMI, 2)))
        elif BMI <= 24.9:
            print("BMI:{} Normal Weight, Health risk: Low Risk".format(round(BMI, 2)))
        elif BMI <= 29.9:
            print("BMI:{} Overweight, Health risk: Enhanced Risk".format(round(BMI, 2)))
            over_weight.append(i["WeightKg"])
        elif BMI <= 34.9:
            print("BMI:{} Moderately obese, Health risk: Medium Risk".format(round(BMI, 2)))
        elif BMI <= 39.9:
            print("BMI:{} High Risk, Health risk: High Risk".format(round(BMI, 2)))
        else:
            print("BMI:{} very severely obese".format(round(BMI, 2)))
    print ("Number of people who are over weight are: ",len(over_weight))
    return len(over_weight)

if __name__ == "__main__":
    start = time.time()
    parser = argparse.ArgumentParser(description='Calculate BMI')
    parser.add_argument('--config', 
                        required=False,
                        default="path.json",    
                        help='absolute path of configuration json')
    args = parser.parse_args()
    
    # reading parameters form the passed configuration json file
    json_file = ".\input_data.json"
    with open(json_file) as f:
        data = json.load(f)
    # Calling the function
    calculate_bmi(data)
    end = time.time()
    print(f"Runtime of the program is {end - start}")

# Code changes completed.
#!/usr/bin/env python3

def get_bmi(weight, height):
    bmi = (weight / (height * height)) * 703
    return bmi

if __name__=='__main__':
    height_in = 65
    weight_lb = 175
    bmi = get_bmi(weight_lb, height_in)
    print("bmi: ", bmi)

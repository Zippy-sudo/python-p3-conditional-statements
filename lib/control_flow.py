#!/usr/bin/env python3

def admin_login(username, password):
    login_status = "Access granted" if username.upper() == "ADMIN" and password == "12345" else "Access denied"
    return login_status


def hows_the_weather(temperature):
    if temperature < 40 :
        return "It's brisk out there!"
    elif temperature >= 40 and temperature <= 65 :
        return "It's a little chilly out there!"
    elif temperature > 85 :
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(num):
    if num%3 != 0 and num%5 != 0:
        return num
    elif num%3 == 0 and num%5 != 0:
        return "Fizz"
    elif num%3 != 0 and num%5 == 0:
        return "Buzz"
    else:
        return "FizzBuzz"

def calculator(operation, num1, num2):

    dict_map = {
        "+" : num1 + num2,
        "-" : num1 - num2,
        "*" : num1 * num2,
        "/" : num1 / num2
    }
    
    answer = dict_map.get(operation, "Invalid operation!")
    
    if answer == "Invalid operation!":
        print("Invalid operation!")
        return None
    else:
        return answer

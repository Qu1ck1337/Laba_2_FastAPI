from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Calculator(BaseModel):
    first_num: float
    operation: str
    second_num: float


@app.post("/calculate")
def calculate(arguments: Calculator):
    '''Calculate query expects:\n
    first_num - float,\n
    operation - string (ONLY +, -, *, /, //, %),\n
    second_num - float'''
    if arguments.operation == "+":
        return {"Addition_total": arguments.first_num + arguments.second_num}
    if arguments.operation == "-":
        return {"Subtraction_total": arguments.first_num - arguments.second_num}
    if arguments.operation == "*":
        return {"Multiplication_total": arguments.first_num * arguments.second_num}
    if arguments.operation == "/":
        return {"Division_total": arguments.first_num / arguments.second_num}
    if arguments.operation == "//":
        return {"Integer_division_total": arguments.first_num // arguments.second_num}
    if arguments.operation == "%":
        return {"Remainder_total": arguments.first_num % arguments.second_num}
    return {"Operator_error": "You wrote a wrong operator, expected: +, -, *, /, //, %"}


# class Greeting(BaseModel):
#     action: str
#     name: str
#
#
# @app.get("/greeting/{name}", response_model=Greeting)
# def special_hello_friend(greeting: str, name: str):
#     '''Особое приветствие'''
#     return Greeting(action=greeting, name=name)
#
#
# @app.get("/")
# def hello():
#     return {"Hello": "World"}
#
#
# @app.get("/{name}")
# def hello_friend(name: str):
#     return {"Hello": name}
#
#
# @app.post("/")
# def greeting(greeting: Greeting):
#     return {greeting.action: greeting.name}
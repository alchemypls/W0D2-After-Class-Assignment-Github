def hello_world():
    return "Hello from Richard!"

def greet_person(name):
    return f"Hello, {name}"

if __name__ == "__main__":
    print(hello_world())
    print(greet_person(__name__))
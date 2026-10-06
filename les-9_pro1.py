class Robot:
    
    type = "Robot"

    def __init__(self, name):
        self.name = name

Tom = Robot("Tom")
Jerry = Robot("Jerry")

print("Hello, I am {}".format(Tom.name) + " and I am a {}".format(Tom.type))
print("Hello, I am {}".format(Jerry.name) + " and I am a {}".format(Jerry.type))
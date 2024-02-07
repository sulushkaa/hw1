class StringManipulator:
    def getString(self, input_string):
        self.input_string = input_string

    def printString(self):
        print("String in uppercase:", self.input_string.upper())


string_manipulator = StringManipulator()


user_input = input("Enter a string: ")


string_manipulator.getString(user_input)


string_manipulator.printString()
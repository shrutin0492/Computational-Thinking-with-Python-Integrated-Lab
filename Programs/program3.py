# 3.
# Defines two classes, "Python" and "Java," with data members "Version" and "name," and a method "display()" to print appropriate messages using object instances.


class Python:
    def __init__(self, version, name):
        self.version = version
        self.name = name

    def display(self):
        print(f"Language: {self.name}")
        print(f"Version: {self.version}")
        print("Python is known for its simplicity and readability.")

class Java:
    def __init__(self, version, name):
        self.version = version
        self.name = name

    def display(self):
        print(f"Language: {self.name}")
        print(f"Version: {self.version}")
        print("Java is known for its platform independence and strong typing.")

# Creating objects of the classes
python_obj = Python("3.9", "Python")
java_obj = Java("11", "Java")

# Displaying information using the display() method
print("Python Information:")
python_obj.display()
print("\nJava Information:")
java_obj.display()
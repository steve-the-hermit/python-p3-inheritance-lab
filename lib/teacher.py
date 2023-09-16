from user import User

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = ["Math", "Science", "History"]

    def teach(self):
        return "Math"  # You can change this to teach different subjects.

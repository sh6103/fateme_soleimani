from message import *


class User(Message):
    messages_box = {"fateme": [], "maryam": []}
    information = {"fateme": "sd", "maryam": "mam"}

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.login_status = False

    def create(self):
        """
        Create a new account
        :return: Saves new user information
        """
        if self.user_name in self.information:
            print("This name is used..try again")
        self.information[self.user_name] = self.password

    def login(self):
        """
        Login to account
        :return: done or not
        """
        if self.check():
            self.login_status = True
            print("You have successfully logged in to your account")
        else:
            print("Your username or password is incorrect")

    def logout(self):
        self.login_status = False
        print("You are logged out of your account")

    def check(self):
        """
        Checks user information correctly
        :return: True or False
        """
        if self.user_name in self.information.keys():
            if self.information[self.user_name] == self.password:
                return True
        print("Your username or password is incorrect")
        return False

    def change_pass(self, other):
        """
        change your password
        :param other: new password
        :return: done or not
        """
        if self.login_status:
            self.information[self.user_name] = other
            print("done.. password change")
        else:
            print("Log in to your account first")

    def send_message(self):
        if self.login_status:
            sender = self.user_name
            receiver = input("receiver:")
            title = input("Title:")
            text = input("text:")
            other = Message(sender, receiver, title, text)
            print("\nsend")
            self.messages_box[self.user_name].append(other.read())
        else:
            print("Log in to your account first")

    def message_box(self):
        """
        :return:Total user messages
        """
        if self.login_status:
            print(*self.messages_box[self.user_name])
        else:
            print("Log in to your account first")

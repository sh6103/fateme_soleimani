from datetime import datetime


class Message:
    """
    Manages working with a message
    """

    def __init__(self, sender, receiver, title, text):
        self.sender = sender
        self.receiver = receiver
        self.title = title
        self.text = text
        self.time = datetime.today()
        self.status = 'unread'

    def read(self):
        """
        Allows you to read a message
        :return: your massage
        """
        self.status = 'read'
        return "from {} to {}:\n{}\n{}\n{}\n".format(self.sender,self.receiver, self.title, self.text, self.time)

    def delete(self):
        """
        Allows you to delete a message
        :return: Message Delete message
        """
        self.status = 'delete'
        self.sender = self.text = self.title = self.time = ""
        return "your massage delete"

    def edit(self, other):
        """
        Allows you to edit a message
        :param other:Edited text
        :return:Edited message
        """
        self.status = 'edit'
        self.text = other
        return self.text


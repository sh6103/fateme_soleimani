class Quiz:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check(self, users_answer):
        """
        Checks the user's answer
        :param users_answer:User answer
        :return:True or False
        """
        for j in self.answer:
            if j == ''.join(users_answer.lower().split()):
                return True
        else:
            return False

    def __str__(self):
        return self.question


class ShortAnswer(Quiz):
    pass


class MultipleChoice(Quiz):
    list_answer = {1: "1.Termites\t\t2.locust\t\t3.Ant\t\t4.Spider", 2: "1.Caspian\t\t2.Baikal\t\t3.Titicaca\t\t4.Van",
                   3: "1.Cedar\t\t2.Olive\t\t3.Apple\t\t4.Orange",
                   4: "1.Singapore\t\t2.Canada\t\t3.Belgium\t\t4.Switzerland",
                   5: "1.Hugo \t\t2.Gabriel Garissa Marx\t\t3.George Orwell\t\t4.Ernest Hemingway"}

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        """
        :return:options for multiple choice questions
        """
        return self.list_answer[self.answer]


class TrueFalse(Quiz):

    def __str__(self):
        return "1.True\t\t\t2.False"


class Score:
    """
    Updates User Scores
    """

    def __init__(self, score, status=""):
        self.score = score
        self.status = status

    def __add__(self, other):
        self.score += other
        return self

    def __sub__(self, other):
        self.score -= other
        return self

    def __str__(self):
        """
        :return:User Scores
        """
        return "Score:{}".format(self.score)

    def check_status(self):
        """
        Checks the winning status of the user
        :return:Win or Lose
        """
        if self.score >= 40:
            self.status = "***Congratulations you win***"
        else:
            self.status = "Sorry..You lose,it 's better to increase your information and try again"





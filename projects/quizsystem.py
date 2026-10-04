class Question():
    def __init__(self,q_no,q_txt,q_key):
        self.q_no=q_no
        self.q_txt=q_txt
        self.q_key=q_key

    def ask(self):
        return input(f"{self.q_no}. {self.q_txt}")
    def check_answer(self,given_answer):
        return given_answer==self.q_key

class Mcq(Question):
    def __init__(self, q_no, q_txt,options, q_key):
        super().__init__(q_no, q_txt, q_key)
        self.options=options

    def ask(self):
        print(f"{self.q_no}. {self.q_txt}")
        for key,val in self.options.items():
            print(f"  {key}) {val}")
        return input("your answer: ").strip().upper()    

    def check_answer(self, given_answer):
       return given_answer.strip().upper()==self.q_key.upper()
       

class TrueFalseQuestion(Question):
    def check_answer(self, given_answer):
        return given_answer.strip().lower() == str(self.q_key).lower()


class FillBlankQuestion(Question):
    def check_answer(self, given_answer):
        return given_answer.strip().lower() == self.q_key.strip().lower()


q1 = Mcq(1, "Which keyword defines a function in Python?", {"A": "func", "B": "def", "C": "function", "D": "define"}, "B")
answer = q1.ask()
print(q1.check_answer(answer))        
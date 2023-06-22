import random

class Student:

    def __init__(self, age, completion, track):
        self.age = age
        self.completion = completion
        self.track = track

    
    def study(self, hours):
        if self.completion == 100:
            return "No need to study - you've completed your track!"
        if self.completion < 100 and hours * 2 + self.completion <= 100:
            self.completion += hours * 2
            return f"Nice job studying! You are now {self.completion}% complete!"
        return "You finished your studies!"
    

    def __repr__(self):
        return f'''{self.age} year old {self.track} student 
                    {self.completion}% done with their studies.'''


class BloomTechStudent(Student):

    def __init__(self, age, completion, track, sprint):
        super().__init__(age, completion, track)
        self.sprint = sprint


    def finish_sprint(self):
        self.sprint += 1
        return f"You advanced a Sprint! Now on Sprint {self.sprint}"


    def __repr__(self):
        return f'''{self.age} year old {self.track} student on Sprint {self.sprint} 
                {self.completion}% done with their studies.'''



def student_generator(n):
    age_lower = 18
    age_upper = 99
    completion = 100
    track = ['DS', 'FE', 'BE', 'FS']
    sprint_first = 1
    sprint_last = 25
    rr = random.randrange
    rc = random.choice

    student_list = []

    for i in range(n):
        new_student = BloomTechStudent(rr(age_lower, age_upper), rr(completion),
                                        rc(track), rr(sprint_first, sprint_last))
        student_list.append(new_student)

    return student_list








if __name__ == '__main__':
    # my_student = Student(30, 20, "math")
    # my_student = BloomTechStudent(30, 50, 'DS', 9, 'gorilla')
    # print(my_student)
    # print(my_student.study(10))
    # my_student.finish_sprint()
    # print(my_student)
    print(student_generator(30))



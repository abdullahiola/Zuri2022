class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks,score):
        self.name= str(name)
        self.age=int(age)
        self.tracks= list(tracks)
        self.score= float(score)

    def change_name(self,name):
        self.name= name
        print(f"name changed to {self.name}")

    def get_score(self):
        return self.score

    def change_age(self,age):
        self.age=int(age)

    def add_track(self,track):
        self.tracks.append(track)



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()


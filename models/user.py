
class User:
    def __init__(self, age, gender, income,
                 utilities, entertainment,
                 schoolfees, shopping, healthcare):

        self.age = age
        self.gender = gender
        self.income = income
        self.utilities = utilities
        self.entertainment = entertainment
        self.schoolfees = schoolfees
        self.shopping = shopping
        self.healthcare = healthcare

    def to_dict(self):
        return vars(self)

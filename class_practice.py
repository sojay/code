class FamilyMember:

    monthly_bonus = 20000
    number_of_family = 0

    def __init__(self, first, last, connection):
        self.first = first
        self.last = last
        self.connection = connection
        self.email = first+'.'+last+'@theokories.com'

        FamilyMember.number_of_family += 1

    def fullname(self):
        return '{first} {last}'.format(first=self.first, last=self.last)

    def emailadd(self):
        return '{}.{}{}'.format(self.first, self.last, '@theokories.com')

    def christmasbonus(self):
        return (self.monthly_bonus * 2)

class Salary(FamilyMember):


    def __init__(self, amount):
        super().__init__(first, last)
        




mother = FamilyMember('Theresa', 'Okorie', 'Mother')
brother = FamilyMember('Oscar', 'Okorie', 'Brother')
sister_1 = FamilyMember('Wendy', 'Okorie', 'Sister')
sister_2 = FamilyMember('Cynthia', 'Okorie', 'Sister')


#print(sister_1.fullname())
#print(FamilyMember.fullname(mother))

#print(mother.email).lower()

print(mother.christmasbonus())

mother.monthly_bonus = 24000
brother.monthly_bonus = 21300


print('Christmas bonus for the {} Family;\n{} is {}\n{} is {}\nAnd the two {} are {}'.format(brother.last, mother.connection,mother.christmasbonus(), brother.connection, brother.christmasbonus(), sister_1.connection, sister_1.christmasbonus()))

#print('There are {} members in the family'.format(FamilyMember.number_of_family))
#print(FamilyMember.__dict__)

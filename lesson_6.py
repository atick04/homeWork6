class Summa:
    def __init__(self, numbers, desired_sum: int):
        self.numbers = numbers
        self.desired_sum = desired_sum

    def find_count(self):
        for index in range(len(self.numbers)):
            for inner_count in range(index + 1, len(self.numbers)):
                if (self.numbers[index] + self.numbers[inner_count]) == self.desired_sum:
                    return [index, inner_count]
        return None
    
    def __str__(self):
        return f'number lists: {self.numbers}\n'\
            f'desired numbers:{self.desired_sum}\n'

we_number = Summa(numbers=[16,3,2,7,15,13,5,4,1,9], desired_sum=5)
print(we_number)
print(we_number.find_count())
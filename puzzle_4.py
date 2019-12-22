class Code:
    def __init__(self, number):
        self.digits = []
        
        for i in range(0, len(number)):
            self.digits.append(int(number[i]))

    def __add__(self, value):
        if(isinstance(value, int)):
            self.__apply_add(len(self.digits)-1, value)    
        else:
            raise TypeError("Only int is supported")

        return self

    def __str__(self):
        return "".join(str(x) for x in self.digits)
    
    def __apply_add(self, digit, value):
        self.digits[digit] += value
        
        # If we reached 10, then apply the overflow
        if self.digits[digit] >= 10:
            self.__apply_add(digit-1, int(self.digits[digit]/10))
            self.digits[digit] %= 10

    def is_valid(self):
        has_adjacent_pair = False
        digits_never_decrease = True

        # First check if there are adjacent digits
        for i in range(0,len(self.digits)-1):
            if self.digits[i] == self.digits[i+1]:
                has_adjacent_pair = True
                break
        
        # Then check if the digits never decrease
        for i in range(0,len(self.digits)-1):
            if self.digits[i] < self.digits[i+1]:
                digits_never_decrease = False
                break

        return has_adjacent_pair and digits_never_decrease



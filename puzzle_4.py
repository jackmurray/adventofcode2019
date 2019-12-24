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
            has_prev = False
            has_next = False
            prev = -1
            next = -1

            if self.digits[i] == self.digits[i+1]:
                has_adjacent_pair = True

                if i+2 <= len(self.digits)-1: # there are more numbers to check
                    has_next = True
                    next = self.digits[i+2]
                if i-1 >= 0:
                    has_prev = True
                    prev = self.digits[i-1]
                    
                if has_next and next == self.digits[i]:
                    has_adjacent_pair = False
                
                if has_prev and prev == self.digits[i]:
                    has_adjacent_pair = False
                
                if has_adjacent_pair == True:
                    break # If we're still here then we don't need to check any other digits - we know we have a valid pair.
                
        
        # Then check if the digits never decrease
        for i in range(0,len(self.digits)-1):
            if self.digits[i] > self.digits[i+1]:
                digits_never_decrease = False
                break

        return has_adjacent_pair and digits_never_decrease


if __name__ == "__main__":
    start = Code("146810")
    end   = Code("612564")
    count = 0
    while start.digits != end.digits:
        if start.is_valid():
            count += 1
            print("{0} is valid".format(start))
        start += 1
    print(count)
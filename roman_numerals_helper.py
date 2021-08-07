class RomanNumerals:
    roman_numeral = {'I': 1,
                     'IV': 4,
                     'V': 5,
                     'X': 10,
                     'L': 50,
                     'C': 100,
                     'D': 500,
                     'M': 1000}

    numeral_roman = {1: 'I',
                     4: 'IV',
                     5: 'V',
                     10: 'X',
                     50: 'L',
                     100: 'C',
                     500: 'D',
                     1000: 'M'}

    def from_roman(self, roman):
        num = 0
        double_char = 0
        for i in range(len(roman)):
            if i + 1 <= len(roman) - 1:
                if roman[i:i+2] in self.roman_numeral:
                    double_char = 1
                    num += self.roman_numeral[roman[i:i+2]]
                else:
                    if self.roman_numeral[roman[i]] < self.roman_numeral[roman[i+1]]:
                        double_char = 1
                        num += self.roman_numeral[roman[i+1]] - self.roman_numeral[roman[i]]
                    else:
                        if not double_char:
                            double_char = 0
                            num += self.roman_numeral[roman[i]]
            else:
                if double_char:
                    break
                else:
                    num += self.roman_numeral[roman[i]]
        return num

    def greater_less_than(self,number):
        return max(k for k in self.numeral_roman if k <= number)

    def smaller_bigger_than(self, number):
        return min(k for k in self.numeral_roman if k >= number)

    def to_roman(self,numeral):
        roman = ''
        double_char = 0
        for n in range(len(str(numeral))):
            number_to_check = (int(str(numeral)[n:]) // 10 ** (len(str(numeral)) - (n + 1))) * 10 ** (len(str(numeral)) - (n + 1))
            if number_to_check in self.numeral_roman:
                double_char = 0
                roman += self.numeral_roman[number_to_check]
                if number_to_check == numeral:
                    break
            else:
                if str(numeral)[n] not in ('0','4','9'):
                    double_char = 0
                    to_look_for = self.greater_less_than(number_to_check)
                    while number_to_check not in self.numeral_roman:
                        roman += self.numeral_roman[to_look_for]
                        number_to_check -= to_look_for
                        to_look_for = self.greater_less_than(number_to_check)
                    roman += self.numeral_roman[number_to_check]
                else:
                    if str(numeral)[n] in ('4','9'):
                        if n + 1 <= len(str(numeral)) - 1:
                            double_char = 1
                            roman += self.numeral_roman[self.smaller_bigger_than(number_to_check) - number_to_check]
                            roman += self.numeral_roman[self.smaller_bigger_than(number_to_check)]
                        else:
                            if double_char:
                                break
        return roman
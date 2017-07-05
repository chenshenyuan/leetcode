# Ⅰ（1）、Ⅴ（5）、Ⅹ（10）、Ⅼ（50）、Ⅽ（100）、Ⅾ（500）和Ⅿ（1000）

def sing_numb(char1,char5,char10,numb):
    if numb<=3:
        return char1*numb #like III
    elif numb ==4:
        return (char1+char5) #like IV
    elif numb ==5:
        return char5
    elif numb<=8: #like VII
        return (char5+char1*(numb-5))
    else:
        return (char1+char10) #like IX


class Solution(object):
    def intToRoman(self, num):
        list_cha = ['I','V','X','L','C','D','M']
        list_cha_mean = [1,5,10,50,100,500,1000]

        if num in list_cha_mean:
            return list_cha[list_cha_mean.index(num)]
        if num>1000:
            first_numb = num//1000
            first_part = sing_numb(list_cha[6],' ',' ',first_numb) #less than 4000,second and third char will not be used
            num = num % 1000
            second_part = self.intToRoman(num)
            return first_part+second_part
        elif num>100:
            first_numb = num // 100
            first_part = sing_numb(list_cha[4], list_cha[5], list_cha[6], first_numb)
            num = num % 100
            second_part = self.intToRoman(num)
            return first_part + second_part
        elif num>10:
            first_numb = num // 10
            first_part = sing_numb(list_cha[2], list_cha[3], list_cha[4], first_numb)
            num = num % 10
            second_part = self.intToRoman(num)
            return first_part + second_part
        else:
            first_part = sing_numb(list_cha[0], list_cha[1], list_cha[2], num)
            return first_part




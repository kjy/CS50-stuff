#Enter a credit card number with only digits. Prompt user if they enter a symbol such as '-' or characters. 
#Return the credit card type (MasterCard, Visa, or American Express) if card is valid.

num = raw_input('Number: ')
while num.isdigit()!=True:
    num = raw_input('Retry: ')


#Use Luhn's algorithm (checksum) to check if credit card number is syntactically valid

x = num[-2::-2]  #extract every other digit starting with the credit card number's second-to-last digit (going backwards from index -2 to index 0 or 1)
sumcount = 0     #set counter to 0
for i in x:      #multiply each digit by 2 and sum, convert from string to integer
     prod_digits=str(2*int(i))
     for e in prod_digits:
         sumcount += int(e)
print (sumcount)
y = num[-1::-2]  #extract the remaining digits and sum
counter = 0
for u in y:
    counter +=int(u)
print (counter)
total = str(sumcount + counter) #add the two parts together to get the checksum
print (total)

if total[-1]=='0':   #if last digit ends in '0', then credit card number is valid or use mod 10 to get remainder==0
    
    #Determine which credit card type is valid (nested branch)
    if len(num)==15 and (num[0:2]=='34' or num[0:2]=='37'):
        print ("American Express")
    
    elif len(num)==16 and (num[0:2]=='51' or num[0:2]=='52' or num[0:2]=='53' or num[0:2]=='54' or num[0:2]=='55'):
        print ("MasterCard")
    
    elif ((len(num)==13 or len(num)==16) and num[0]=='4'):
        print ("Visa")
    else:
        print ("INVALID") #invalid if length of credit card number or starting numbers are not valid
else:
    print ("INVALID")  #invalid if last digit does not end in '0'



'''
Test cases:


Number: 378282246310005
27
33
60
American Express


Number: 4195040131181433
33
27
60
Visa


Number: 5524680315334917
26
44
70
MasterCard

Number: 4012888888881881
47
43
90
Visa

Number: 5105105105105100
7
13
20
MasterCard

Number: 371449635398431
47
33
80
American Express

Number: 38520000023237
19
21
40
INVALID  (Diner's Club)

Number: 5610591081018250
21
19
40
INVALID  (Australian BankCard)


Number: 3148-223-7283
Retry: whatsup
Retry: (spacebar)
Retry: ?
Retry: #
Retry: 4
0
4
4
INVALID

Number: 0
0
0
0
INVALID


Number: Gurly
Retry: 50
1
0
1
INVALID

Number: 6331101999990016
33
37
70
INVALID

'''

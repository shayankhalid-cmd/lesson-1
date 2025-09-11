amount =int(input("enter the amount:"))
note_1 = (amount//100)
note_2 = (amount%100)//50
note_3 = ((amount%100)%50)//10
print ("100 note_1",note_1)
print (" 50 note_2",note_2)
print (" 10 note_3",note_3)



print ("enter the marks:")
math = int(input("enter math's marks"))
science = int(input("enter science's marks"))
english = int(input("enter english's marks"))
total = math + science + english
print ("total marks:",total)
percentage =  total/3
print ("your percentage:",percentage)

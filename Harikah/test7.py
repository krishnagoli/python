sub1, sub2, sub3, sub4, sub5, sub6 = input('Enter the marks for 6 subjects seperated by , :').split(',')

sub1 = float(sub1)
sub2 = float(sub2)
sub3 = float(sub3)
sub4 = float(sub4)
sub5 = float(sub5)
sub6 = float(sub6)

sum = sub1+sub2+sub3+sub4+sub5+sub6
avg = sum/6

print('The student has scored a total of {} with an average of {} in this semester'.format(sum,avg))
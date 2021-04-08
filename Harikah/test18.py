def alph_type_count(str):
    v_count=0
    c_count=0
    s_count=0
    for i in str:
        if i==' ':
            s_count=s_count+1
        elif i in 'aeiouAEIOU':
            v_count=v_count+1
        else:
            c_count=c_count+1
    print('Your string has ',v_count,'vowels')
    print('Your string has ',c_count, 'consonants')
    print('Your string has ',s_count, 'spaces')

string=input('Enter your string')
alph_type_count(string)
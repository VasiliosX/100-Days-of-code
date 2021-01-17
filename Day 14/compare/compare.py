import random

dic={'Neymar':100,'Messi':300,'Tzavelas':2,'Kane':50,'Salah':80,'Werner':40,'Ronaldo':290,'Dybala':60,'Mitroglou':700}
names=['Neymar','Messi','Tzavelas','Kane','Salah','Werner','Ronaldo','Dybala','Mitroglou']

random_names=[]

rand_choice=random.choice(names)

random_names.append(rand_choice)


names.remove(rand_choice)
rights=0

cont=True
while cont:
    rand_choice=random.choice(names)

    names.remove(rand_choice)

    random_names.append(rand_choice)





    ind=len(random_names)

    answer=input(f'{random_names[ind-2]}, with {dic[random_names[ind-2]]} followers\nDoes {random_names[ind-1]} have more followers than {random_names[ind-2]} or not?, Type "y" for yes, "n" for no:')

    bool=dic[random_names[ind-2]]<dic[random_names[ind-1]]


    if answer=='y' and bool==True:
        print('You are right')
        rights+=1
    elif answer=='n' and bool==True:
        print('You are wrong')
        cont=False
    elif answer=='y' and bool==False:
        print('You are wrong')
        cont=False
    elif answer=='n'and bool==False:
        print('You are right')
        rights+=1

    if len(names)<1:
        cont=False
        print('You answered everything right')



if rights<=1:
    print(f'Just {rights}!, you are a fucking idiot')
elif rights<=4:
    print(f'{rights} right answers, really bad, you can do better, expand your football knowledge immediately')
elif rights<=7:
    print(f'{rights} right answers, not bad, but you can do better')
else:
    print(f'{rights} right answers, wow, impressive, your knowledge about football is outstanding')

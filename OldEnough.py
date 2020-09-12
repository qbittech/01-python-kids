driving_age = eval(input("小朋友，你多大可以自己出去玩?"))
your_age = eval(input("你几岁了?"))
if your_age >= driving_age:
    print("你可以自己出去玩了")
if your_age < driving_age:
    print("你",driving_age - your_age,"年后可以自己出去玩了！")                
                   

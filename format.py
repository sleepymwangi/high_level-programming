#format

formatter = "{} {} {} {}"

print("i love coding,my favourite language is {}".format('python'))
print("hello world\n"* 10)


#formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one","two","three","four"))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format("python","c","HTML","CSS"))


my_dog = "\nspot\tand\tzoe"
color = """
spot is black
\t* but has a touch of browm
\t* zoe is pure white
\t* spot\n\t* zoe
"""
print(my_dog)
print(color)

#inputting values to get output

print("how old are you?", end=' ')
age = input()
print("how tall are you?", end=' ') 
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"lemme comfirm, you're  {age} old,{height} tall,{weight} kgs right??")

dogs = input("how many dogs: ")
cats = input("how many cats: ")
total = int(dogs) + int(cats)
print(f"the total dogs and cats: {total}")


from sys import argv

script,name,position,age = argv

print("file name ",script)
print("students name: ",name)
print("position : ",position)
print("students age : ",age)




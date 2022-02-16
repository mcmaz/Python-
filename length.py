message="Hello my friends"
print(len(message))
i=0
while i<len(message):
    print (message[i])
    i=i+1

def wordcount(msg):
    i=0
    space = 0
    while i<len(msg):
        if msg[i]==" ":
            space=space+1
        i=i+1
    print(("in the message we found:"),space+1)



wordcount("hello my friends")

def printing(msg):
    word=""
    i=0
    while i >len(msg):
        if msg[i]==" ":
            print(word)
            word=""
        else:
            word=word+msg[i]
        i=i+1
    print(word)

printing("hello hi hello")


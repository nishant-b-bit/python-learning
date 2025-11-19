#nested dictionary
info={
    "name":"nishant",
    "subjects":{ #here inside subject we created another dictionary, this is called nesting
        "science":50,
        "maths":80,
        "computer":90
    }, #the program was getting error because i forget to enter , after }
    "class":39
}
print(info["subjects"])
print(info["subjects"]["science"]) # here it is used to print vlaue of science key 
info={ #here we are going to give many values inside a single variable that is the main advantage of dictionary
    "name":"nishant budha", # here name is the key and nishant budha is value but both are string so inside " " 
    "class":"bachelors",
    "marks":80.78,
   "subjects":["python","computer system"]
}
print(info["class"])# this is used to get the value from a certain key in dictionary
print(info["class"])
info["name"]="nishant" # dictionary being mutable we can change the value
print(info["name"]) 
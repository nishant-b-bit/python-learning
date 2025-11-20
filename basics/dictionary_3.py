# dictionary methods
info={
    "name":"nishant",
    "subjects":{ 
        "science":50,
        "maths":80,
        "computer":90
    },
}
print(info.keys()) #all the keys except nexted keys are printed 
print(info.values()) #will print all the values inside the dictionary including nested dictionary because that is the value of the key subjects
print(info.items()) # will return all pairs of keys and values in dictionary as tuples
print(info.get("name"))
#print(info["name"]) this will also give same value as print(info.get("name")) but difference is that when we call the key which don't exist like name2 then print(info.get("name2")) will give none but print(info["name2"]) will give error so while writing program writing code as print(info.get("name")) is considered better
info.update({"city":"kathmandu","college":"softwarica"})#here we might think that why we use { }, genereally after function we use ( ) but as here we are trying to update dictionary so dictionary should always be written inside { }
# above line can also be written as information={"city":"kathmandu","college":"softwarica"} and info.update(information) and then print(info)
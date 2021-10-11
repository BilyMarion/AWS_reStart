#Lists
myFruitList=["apple","banana","cherry"]
print(myFruitList)
print(type(myFruitList))

print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

myFruitList[0]="Watermelon" #Lists are changeable: Mutable
print(myFruitList)

#Tuples
myFinalAnswerTuple=("apple","banana","pineapple",3)
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

#myFinalAnswerTuple[0]="Watermelon" #Tuples are Immutable. 
#print(myFinalAnswerTuple)

#Dictionaries
myFavoriteFruitDictionary={
    "Akua":"apple",
    "Saanvi":"banana",
    "Paulo":"pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])

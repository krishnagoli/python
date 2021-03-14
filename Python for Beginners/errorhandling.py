score = input("Enter Score between 0.0 and 1.0 :")

try:
    fscore = float(score)
except:
    print("Error, please enter numberic value")
    quit()

if fscore < 0 or fscore > 1 :
    print("Please enter score between 0.0 and 1.0")
elif fscore > 0.9:
    print ("Score Grade : A")
elif fscore >= 0.8 and fscore <0.9:
    print ("Score Grade : B")
elif fscore >= 0.7 and fscore <0.8:
    print ("Score Grade : C")
elif fscore >= 0.6 and fscore <0.7:
    print ("Score Grade : D")
elif fscore <0.6:
    print ("Score Grade : F")

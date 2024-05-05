import csv

qestions = []

f = open("data/questions.csv", "r")
for x in f:
  qestions.append(x.strip())

print(qestions)




with open('data/test.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print("####################")
        Userid = row[0]
        caseN1 = row[1]
        caseN2 = row[2]
        caseN3 = row[3]

        print("Userid: ", Userid)
        print("Qestions", qestions[0])
        print("caseN1: ", caseN1)
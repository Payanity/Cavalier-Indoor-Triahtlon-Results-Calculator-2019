import math
import operator
file = open('Men26-35.txt', 'r')
category = file.readline()
firsty = file.readline()
nameList = []
scorelist = []

#Calculates the ranking for each leg of the race from time!!
for line in file:
    #n = number, s = swim, b = bike, r = run, fN = first name, lN = last name
    n,s,b,r, fN, lN = line.split()
    name = fN + " " + lN
    #tmplist holds the number, swim bike and run for THIS ENTRY
    tmpList = []
    countlist = []
    tmpList.append(float(n))
    #swim is in yards(1 lap = 25 yards)
    tmpList.append(float(s)*25)
    tmpList.append(float(b))
    #run is in miles (11 laps = 1 mile)
    tmpList.append(float(r)*.099)
    tmpList.append(name)
    countlist.append(name)
    nameList.append(tmpList)
    finalScore = {}
    numMap={}



########################################################################################################################
##############KEY PART##################################################################################################


def swim (elem):
    return elem[1]
def bike (elem):
    return elem[2]
def run(elem):
   return elem[3]



########################################################################################################################
#SWIM RANKINGSM##################################################################################################


swimlist=nameList
swimlist.sort(key=swim)


swimlist = swimlist[::-1]
#getting out individual swim distances for swim-specific award
swimmap ={1:[]}
a=1

#print(swimmap)
swimmap[a].append(swimlist[0])
for i in range (1, len(swimlist)):
    if swimlist[i][1]== swimlist[i-1][1]:
        swimmap[a].append(swimlist[i])
    else:
        a+=1
        swimmap[a] = []
        swimmap[a].append(swimlist[i])

#print(swimmap)
print("SWIM RANKINGS FOR " + category)
a = 0
i=0
for i in swimmap:
    for j in swimmap[i]:
        print(str(i) + ") ", int(j[0]), " " + j[4] + " ", str(j[1]), "yards")
        finalScore[j[4]]=int(i)
        numMap[j[4]]=int(j[0])
        #print(finalScore)


#print(scorelist)
print("\n")




########################################################################################################################
#######BIKE RANKINGS#############################################################################################################



bikelist=nameList
bikelist.sort(key=bike)

bikelist = bikelist[::-1]
bikemap ={1:[]}
a=1

#print(bikemap)
bikemap[a].append(bikelist[0])
for i in range (1, len(bikelist)):
    if bikelist[i][2]== bikelist[i-1][2]:
       bikemap[a].append(bikelist[i])
    else:
        a+=1
        bikemap[a] = []
        bikemap[a].append(bikelist[i])

#print(bikemap)
print("BIKE RANKINGS FOR " + category)
a = 0
i=0
for i in bikemap:
    for j in bikemap[i]:
        print(str(i) + ") ", int(j[0]), " " + j[4] + " ", str(j[2]), "spin bike distance (it's b/w km and miles)")
        finalScore[j[4]]+=int(i)
        #print(finalScore)


#print(scorelist)
print("\n")



########################################################################################################################
#######RUN RANKINGS###################################################################################################



runlist=nameList
runlist.sort(key=run)
runlist = runlist[::-1]
 
#gettdel dictionary[old_key]ing out individual run distances for run-specific award
#print(runlist)
runmap ={1:[]}
a=1

#print(runmap)
runmap[a].append(runlist[0])
for i in range (1, len(runlist)):
    if runlist[i][3]== runlist[i-1][3]:
       runmap[a].append(runlist[i])
    else:
        a+=1
        runmap[a] = []
        runmap[a].append(runlist[i])

#print(runmap)
print("RUN RANKINGS FOR " + category)
a = 0
i=0
for i in runmap:
    for j in runmap[i]:
        print(str(i) + ") ", int(j[0]), " " + j[4] + " ", round(j[3], 2), "miles")
        #print(j[4])
        finalScore[j[4]]+=int(i)
        #print(finalScore)
print("\n")





#######################################################################################################################
############FINAL######################################################################################################


sortedPpl= sorted(finalScore.items(), key=operator.itemgetter(1))
print(sortedPpl)

print("OVERALL RANKINGS FOR " + category)
print(str(1) + ") ", " " + str(numMap[sortedPpl[0][0]]) + " ", sortedPpl[0][0], " " + str(sortedPpl[0][1]) + " ",  "- summed leg rank")
i=1
a=1
while(i<len(sortedPpl)):
    if(sortedPpl[i][1]==sortedPpl[i-1][1]):
        print(str(a) + ") ", " " + str(numMap[sortedPpl[i][0]]) + " ", sortedPpl[i][0]," " + str(sortedPpl[i][1]) + " ",  "- summed leg rank")
    else:
        a+=1
        print(str(a) + ") ", " " + str(numMap[sortedPpl[i][0]]) + " ", sortedPpl[i][0], " " + str(sortedPpl[i][1]) + " ", "- summed leg rank")

    i+=1
print("\n")
print("= Award won! Go to the AFC to claim your medal! Due to technical difficulties from ties, some people were falsely given medals whereas others were not given medals for their positions.  If you were falsely given a medal - keep it! - however if you did not receive a medal you earned and do not already have at least one medal, please come to the AFC to retrieve it! Thank you so much; EVERYONE did amazing this year!!! :D ")
print('\n')
print("  How did we score?  This triathlon has a set time  - not set distance - so rather than scoring by time, we scored by summing up the three leg rankings for each participant and granting final scores based on the lowest sum leg ranking for each category. It's not perfect, but it's fairer than summing up the distances, for that would strongly favor one sport over another (it would strongly favor biking because of the larger typical distance length covered on a bike, and strongly mimimize swimming because the distance is simply in yards).")







from numpy import zeros

class Stirling:
    """
    Defining a class holding our Stirling numbers of second kind in an array up to some order m
    """
    def __init__(self, m):
        """
        Initialising an array of storling numbers up until S(m,m)
        """
        self.m = m
        if type(m) == int and m>0: #initialiser with criteria 
            DummyArray = zeros([m,m],dtype=int) #generating an array holding Stirling numbers up until S(m,m)
            for i in range(m):
                DummyArray[i,0], DummyArray[i,i] = 1, 1 #initial values for S(m,1), S(m.m)


            for l in range(1,m):
                for k in range(1,l):
                    DummyArray[l,k] = DummyArray[l-1,k-1] + (k+1)*DummyArray[l-1,k] #generating S(m.n) uptowards 1<_n<_m<_N, note that the 0 element can be read as NaN
            self.DummyArray = DummyArray
        
        
        
        elif type(m) != int: #obviously if m is not of correct data time, cannot initialise 
            print("m is of wrong data type")
        elif m<=0:
            print("Not well defined index value")




    def AssignmentTask(self, x,y):
        """
        Initialising the "specific task" for this paper.
        """
        return self.DummyArray[x-1,y-1]/(x+y) 


TrimF = 3 #Triming the output by to show up to the TrimF:th decimal point
scale = 10**int(TrimF) #Scaling factor for triming 


print("---------------")
print("Task 1:")
print("Since this task is code writing, please see content of the .py file for the written code.")
print("---------------")
print("Task 2:")
InitialisingValue = 13
Number2 = Stirling(InitialisingValue)

print("First value: S(12,5)/17 = ", Number2.AssignmentTask(12,5), " ~ ", int(Number2.AssignmentTask(12,5)))
print("Second value: S(13,8)/21 = ", Number2.AssignmentTask(13,8), " ~ ", int(Number2.AssignmentTask(13,8)))

print("---------------")
print("Task 3: (NOTE: we have trimmed the output to third decimal place)")
mMax = 10 #from our previous generated value, we can pick out the first 10 rows of Stirling numbers


for r in range(1,mMax + 1): #running over the indicies (x,y) in question for S(x,y)/(x+y)
    outputstr = "Row {}:".format(r) + int((TrimF+1)*(mMax - r))*" "
    L = [] #dummy list to store values and "prink them" row-by-row
    for s in range(1,r+1):
        L.append(int(scale*Number2.AssignmentTask(r,s))/scale)
    print(outputstr, L)

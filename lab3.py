## LAB - 3: SEMIVARIOGRAM ANALYSIS TO ESTIMATE GRADE IN A PARTICULAR ORE BODY
## Submitted by - Suresh Gandhi(14MI31024)
import numpy as np

# Taking in the input as the number of rows and columns
rows = int (input ("ENTER THE NUMBER OF ROWS: "))
columns = int (input ("ENTER THE NUMBER OF COLUMNS: "))

# data structure for storing the grade values
grade =[]
for i in range (rows * columns):
    val = float (input("ENTER GRADE (NOTE: ENTER -1 IF THE VALUE IS UNKNOWN): "))
    grade.append(val)
    
# convering the grade array into a two array by reshaping it in the form of rows * columns
grade = np.array(grade)
grade = grade.reshape(rows,columns)

# showing the user the grade multid array
print(grade)

# prompting the user to enter the lag distance and the borehole distance in that direction
lag=int(input ("ENTER THE LAG DISTANCE: "))
dist=int(input ("ENTER THE BOREHOLE DISTANCE IN THAT DIRECTION: "))

# calculating the number of pairs and filling up the delz table
jump=int (lag/dist)
delz=[]
pairs=0
for i in range (rows):
    for j in range (0,columns-jump):
        if (grade [i][j]!= -1 and grade [i][j+jump]!=-1):
            pairs=pairs+1
            temp=grade [i][j]-grade [i][j+jump]
            delz.append (temp)

# showing the user the number of pairs
print ("NUMBER OF PAIRS: " + str (pairs))            

# calculating the semi-variogram
delz=np.array (delz)         
ans=np.sum (delz*delz)/(2*(pairs))

# showing the user the semi variogram
print ("SEMI VARIOGRAM: " + str (ans))

# Problem link : https://www.hackerrank.com/challenges/grading/problem

def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if(grades[i]<38):
            continue
        else:
            up = (grades[i]//5)+1
            if((up*5) - grades[i] < 3):
                grades[i] = up*5
    return grades
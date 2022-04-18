#!/usr/bin/env python3
#shebang & set python3
import sys
import os
import re

#set all of the names to be switched
i, j, k = "<<", ">>", ["dept_code", "dept_name", "course_name", "course_start", "course_end", "credit_hours", "num_students", "course_num", "datestamp"]

#get command line args
if len(sys.argv) == 5 or len(sys.argv) == 7:
    if len(sys.argv) > 5:
        i, j = sys.argv[5], sys.argv[6]

    if not os.path.isdir(sys.argv[4]):
        os.mkdir(sys.argv[4])

    if os.path.isdir(sys.argv[1]):
        for pf in os.listdir(sys.argv[1]): #4pf
            if re.match("[A-Z]{2,3}[0-9]{4}", pf):
                #replace lines
                with open(sys.argv[1] + "/" + pf, "r+") as crs:
                    lines = crs.readlines()
                    variableList = [lines[0].split()[0], " ".join(lines[0].split()[1:]), " ".join(lines[1].split()), lines[2].split()[1], lines[2].split()[2], "".join(lines[3].split()), "".join(lines[4].split()), re.search("([0-9]{4})", crs.name).group(1), sys.argv[3]]
                    #less than 70 students
                    if int(variableList[6]) > 70:
                        with open(sys.argv[4] + "/" + variableList[0] + variableList[-2] + ".warn", "w+") as outfile:
                            with open(sys.argv[2]) as template:
                                for line in template:
                                    l = 0 
                                    while l <= 8:
                                        line = line.replace(i+k[l]+j, variableList[l])
                                        l += 1
                                    outfile.write(line)


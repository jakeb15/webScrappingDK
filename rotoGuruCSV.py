__author__ = 'Jake'
import re

def FixCSV(file):
    f = open(file, 'r')
    header = '"Date","GID","Pos","Name","Starter","DK Pts","DK Salary","Team","H/A","Oppt","Team Score","Oppt Score","Minutes","Stat line"'
    print(header)
    lineNumb = 0
    line_list = [] # list of lines to be written to file
    for line in f:
        temp_line = ""
        if lineNumb == 0:
            #skips header
            lineNumb+= 1
        else:
            lineNumb+= 1
            items = line.split(';')
            count = 0
            for x in items:
                if count == 3:
                    name = x.split(',')
                    print(name)
                    new_name = name[1] + ' ' + name[0]
                    temp_line += '"' + new_name + '"' + ','
                    count+=1
                elif count < 13:
                    temp_line = temp_line + '"' + x + '"' + ','
                    count +=1
                else:
                    temp_line += '"' + x + '"'
            print(temp_line)
            line_list.append(temp_line)
            temp_line = ""
    f.close()
    f = open(file, 'w')
    f.write(header + "\n")
    for x in line_list:
        f.write(x + "\n")
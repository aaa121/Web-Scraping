with open('hopedale.txt','r') as hopedale:
    for line in hopedale:
        linex=line.strip()

# READLINE TECHNIQUE I
#Each call on function readline moves the file cursor to the
#  beginning of the next line.
sum=0
with open('hopedale.txt', 'r') as hopedalex:
    data=hopedalex.readline().strip() # For 1st call, the file cursor move to the beginning of the 2nd line
    data=hopedalex.readline().strip() # For 2nd call, the file cursor move to the beginning of the 3rd line
    data=hopedalex.readline().strip() # For 3rd call, the file cursor move to the beginning of the data, 22
    for line in hopedalex: # The hopedalex file start from 22 i.e. the 4th line
        line.strip() # Stripping the file of whitespaces is optional but recommended
        sum+=int(line)
print(sum)

# READLINE TECHNIQUE II
with open('hopedale.txt', 'r') as hopedale:
    hopedale.readline().strip()
    data=hopedale.readline().strip() # The second line is now read but the file now begins with the third line.
    print(data)
    while data.startswith('#'): # Read each line that start with # but stop the loop when the condition is False
        data=hopedale.readline().strip() # The 3rd line is TRUE but stop because the 4th line is FALSE.
        # The 3rd is read but the 4th is FALSE. After the read command,the file data starts from the new line with 22 as a string
        # The variable last call is on 22. Each call on function readline moves the file cursor to the
        #  begining of the next line.
        print(data)
    total_fox=int(data)
    for data in hopedale:
        fox=int(data.strip())
        total_fox=total_fox + fox
        print(fox)
    print(total_fox)

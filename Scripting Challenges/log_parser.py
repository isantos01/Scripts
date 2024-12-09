# Objective: Write a script that reads a log file and identifies failed login attempts.


# Open and read the file
with open (file, "r") as log:
    # Going throuhg the file lines
    for line in log:
        # checks for the character "Failed password" in the file
        if "Failed password" in line:
            timestamp = line[0:14].strip()
            # locate "from" in the text returns the index of the letter "f" for the first occurrence of the word "from"
            from_location = line.find('from')
            # locate "port" in the text returns the index of the letter "p" 
            port_location = line.find('port')
            # locate "for" in the text returns the index of the letter "f" 
            for_location = line.find('for')
            # Using those index to pull out the IP as well as the user and timestamp
            ip = line[from_location+4:port_location].strip()
            user = line[for_location+3:from_location].strip()
            print('Timestamp: '+ timestamp +' User(s): ' + user +' IP: '+ ip)
file = input("name of the log file: ")

# Open and read the file
with open (file, "r") as log:
    # Going throuhg the file lines
    for line in log:
        # checks for the character "Failed password" in the file
        if "Failed password" in line:
            timestamp = line[0:14].strip()
            # locate "from" in the text returns the index of the letter "f" for the first occurrence of the word "from"
            from_location = line.find('from')
            # locate "port" in the text returns the index of the letter "p" 
            port_location = line.find('port')
            # locate "for" in the text returns the index of the letter "f" 
            for_location = line.find('for')
            # Using those index to pull out the IP as well as the user and timestamp
            ip = line[from_location+4:port_location].strip()
            user = line[for_location+3:from_location].strip()
            print('Timestamp: '+ timestamp +' User(s): ' + user +' IP: '+ ip)


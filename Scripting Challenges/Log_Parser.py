# Objective: Write a script that reads a log file and identifies failed login attempts.

file = input("name of the log file: ")

with open (file, "r") as log:
    for line in log:
        if "Failed password" in line:
            # Now will print the
            timestamp = line[0:14].strip()
            # locate "from" in the text
            from_location = line.find('from')
            port_location = line.find('port')
            for_location = line.find('for')
            ip = line[from_location+4:port_location].strip()
            user = line[for_location+3:from_location].strip()
            print('Timestamp: '+ timestamp +' User(s): ' + user +' IP: '+ ip)
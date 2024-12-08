# Removing spam from emails

email = "eedaaas" # This is your mailbox
new_mail = ""

# Let's store each letter of email in 'character'
for character in email:
    # Counting the occurrance of each letter
    spam = email.count(character)
    # If it's more than 3 times store it in the empty variable
    if spam < 3:
        # adding each of the letter in character to the empty variable
        new_mail += character
print(new_mail)
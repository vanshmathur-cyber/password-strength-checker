print("WELCOME TO PASSWORD STRENGTH CHECKER :")
password = input("Enter a Password:")
common_passwords  = ("password","123456","12345678","123")

if password.lower() in common_passwords:
    print("Warning: This is a common password!")

print("==========PASSWORD ANALYSIS==============") 
print("Length of the Password is:" , len(password))

has_uppercase = False 
has_lowercase = False
has_number    = False
has_special   = False

for character in password:
    if character.isupper():
       has_uppercase = True
       

    elif character.islower():
       has_lowercase = True
      

    elif character.isdigit():
       has_number = True
       

    else:
       has_special = True
   
print("Contains uppercase:" , has_uppercase)
print("Contains lowercase:" , has_lowercase)
print("Contains number :" , has_number)  
print("Contains special character:" , has_special)

score = 0

if has_uppercase:
   score = score + 1

if has_lowercase:
   score = score + 1

if has_number:
   score = score + 1

if has_special:
   score = score + 1

if len(password) >= 8:
   score = score + 1


print("Password Score:", score, "/ 5")


if score<=2:
   print("Password strength : WEAK")

elif 3<=score<=4:
   print("Password strength : MEDIUM")

else:
   print("Password Strength : STRONG")



if score<=4:
   print("============IMPROVEMENTS================ ")


if len(password)<8:
   print("At least 8 chracters")


if not has_uppercase:
   print("An uppercase character")


if not has_number:
   print("A number")



if not has_lowercase:
   print("A lowercase character")


if not has_special:
   print("A special character")


import re

def chkpassword_strength(password):
    strength = 0
    weakness = []
    
    if len(password) >= 8:
        strength = strength + 1 
    else:
        weakness.append("Too Short (minimum 8 characters)")
        
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        strength = strength + 1
    else:
        weakness.append("Make sure to mix upper and lowercase letters")
        
    if re.search(r"\d", password):
        strength = strength + 1
    else:
        weakness.append("Add numbers to your password")
        
    if re.search(r"[@$!%*?&]", password):
        strength = strength + 1
    else:
        weakness.append("Please Add Special Characters")  
        
    if strength == 4:
        return "Strong",weakness
    elif strength == 3:
        return "Medium",weakness
    else:
        return "Weak", weakness
   
        
password = input("Enter a password: ")
result, feedback = chkpassword_strength(password)
print ("\nPassword Strength is" ,result)
if feedback:
    print("\nProblems with password: ")
    for f in feedback:
        print("\n",f)


        
        
    
    
    
    
    
        

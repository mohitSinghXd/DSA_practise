def toLowerCase( s):
        newstring = ""

        for i in range(len(s)):
            if 65 <= ord(s[i]) <= 90:
                newstring += chr(ord(s[i]) + 32)
            else:
                newstring += s[i]

        return newstring

name  = "Mohit"
ans = toLowerCase(name) 
print(ans)
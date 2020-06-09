"""
""Lance & Janice"". You know how much Commander Lambda hates waste, so if you can prove that 
these minions are wasting her time passing non-job-related notes, it'll put you that much closer to a promotion. 

Fortunately for you, the minions aren't exactly advanced cryptographers. In their code, every lowercase letter 
[a..z] is replaced with the corresponding one in [z..a], while every other character (including uppercase letters and 
punctuation) is left untouched.  That is, 'a' becomes 'z', 'b' becomes 'y', 'c' 
becomes 'x', etc.  For instance, the word ""vmxibkgrlm"", when decoded, would become 
""encryption"".

Write a function called solution(s) which takes in a string and returns the deciphered string so you can show the 
commander proof that these minions are talking about ""Lance & Janice"" instead of doing their 
jobs. 
"""

def solution(x):

   return "".join(
                map(
                    lambda code: chr(abs((code - 97) - 25) + 97)  \
                            if code >= 97 and code <= 122 else code, 
                    [ord(w) for w in x] 
                )
            )

if __name__ == "__main__":
    print( solution("vmxibkgrlm") )

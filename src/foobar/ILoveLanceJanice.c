#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/*
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
*/

int main() {
    char *x = "vmxibkgrlm";

    char response[strlen(x)];
    int code;
    char ch; 

    for (; *x != '\0'; x++) {

        code = (int)*x;
        if (code >= 97 && code <= 122) {
            code -= 97; 
            code = abs(code - 25);
            code += 97; 
        }   

        ch = (char)code;
        strncat(response, &ch, 1); 
    }   


    printf("%s\n", response); 

    return 0;
}

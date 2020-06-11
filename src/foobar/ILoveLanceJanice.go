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
package main

import "fmt"
import "math"
import "time"

func main() {
    fmt.Println(solution("vmxibkgrlm"))

    mychan := make(chan string)
    go add_cripto(mychan, "vmxibkgrlm")
    go fetch_cripto(mychan)


    time.Sleep(1 * time.Millisecond)
}

func add_cripto(ch chan string, x string) {
    var code int

    for _, char := range x {
        code = int(char)
        if (code >= 97 && code <= 122) {
	        code -= 97
            code = code - 25
			code = int(math.Abs(float64(code)))
			code += 97;
        }
        ch <- string(code)
    }
    close(ch)
}

func fetch_cripto(ch chan string) {
    for {
        x, flag := <-ch
        if flag == true {
			fmt.Print(x)
		} else {
            fmt.Println()
			break
		}
    }
}

func solution(x string) string {

    var code int
    var result string

    for _, char := range x {
        code = int(char)
        if (code >= 97 && code <= 122) {
	        code -= 97
            code = code - 25
			code = int(math.Abs(float64(code)))
			code += 97;
        }
        result += string(code)
    }

    return result
}

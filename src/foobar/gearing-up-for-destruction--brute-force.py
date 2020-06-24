from fractions import Fraction
def solution(pegs):
    if len(pegs) < 2:
        return (-1, -1)
    if len(pegs) == 2:
        r = (Fraction(pegs[1] - pegs[0]) / Fraction(3)) * Fraction(2)
        if (r.numerator < 1) or (r.numerator < r.denominator):
            return [-1, -1]  
        return [r.numerator, r.denominator]

    r0 = Fraction(1)
    step = Fraction(1)
    while True:
        if r0 >= Fraction(pegs[1] - pegs[0]):
            return [-1, -1]
        ratios = [r0]
        c = True
        for i in range(1, len(pegs)-1):
            curr_rn = Fraction(pegs[i] - pegs[i-1]) - ratios[-1]
            maxr = Fraction(pegs[i+1] - pegs[i])
            if curr_rn >= maxr:
                r0 = Fraction(r0 + step)
                c = False
                break
            if (curr_rn.numerator < 1) or (curr_rn.numerator < curr_rn.denominator):
                return [-1, -1]
            ratios.append(curr_rn)

        if c:
            ratios.append( Fraction(pegs[-1] - pegs[-2]) - curr_rn)
            if ratios[0] == Fraction(2) * ratios[-1]:
                return [ratios[0].numerator, ratios[0].denominator]

            if (ratios[0] + Fraction(1)) == (Fraction(2) * ratios[-1]):
                return [(ratios[0] * Fraction(3)) + Fraction(1), 3]

            if (ratios[0] + Fraction(2)) == (Fraction(2) * ratios[-1]):
                return [(ratios[0] * Fraction(3)) + Fraction(2), 3]
            
            r0 = Fraction(r0 + step)

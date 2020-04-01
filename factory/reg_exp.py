class RegExp:
    def __init__(self):
        pass

    def illegalSpace(self):
        r1 = "(\d\s+\d)"  # num+<space>+num
        r2 = "(\*\s+\*)"  # *+<space>+*
        r3 = "(([+-]\s{0,}){2}[+-]\s+\d)"  # [+-]+<space>+num in coef
        r4 = "([\*]{2}\s{0,}[+-]\s+\d)"  # [+-]+<space>_num in index
        r5 = "((s\s{1,}i\s{0,}n)|(s\s{0,}i\s{1,}n))"  # sin <space>
        r6 = "((c\s{1,}o\s{0,}s)|(c\s{0,}o\s{1,}s))"  # cos <space>
        return r1 + "|" + r2 + "|" + r3 + "|" + r4 + "|" + r5 + "|" + r6

    def duplicatePosSig(self):
        r1 = "([+]{2})"
        r2 = "([-]{2})"
        r3 = "([+]{3})"
        r4 = "(\+\-\-)"
        r5 = "(\-\+\-)"
        r6 = "(\-\-\+)"
        return r1 + "|" + r2 + "|" + r3 + "|" + r4 + "|" + r5 + "|" + r6

    def duplicateNegSig(self):
        r1 = "(\+\-)"
        r2 = "(\-\+)"
        r3 = "(\+\+\-)"
        r4 = "(\+\-\+)"
        r5 = "(\-\+\+)"
        r6 = "(\-\-\-)"
        return r1 + "|" + r2 + "|" + r3 + "|" + r4 + "|" + r5 + "|" + r6

    def illegalOmit(self):
        r1 = "([+-]{3}(x|sin\(x\)|cos\(x\)))"  # +++x
        r2 = "(\^[+-]{2,}\d)"  # ^++2
        r3 = "([+-]{4,})"  # ++++2 etc.
        return r1 + "|" + r2 + "|" + r3

    def termSep(self):
        r1 = "([^\*\^][+-])"
        r2 = "(^[+-])"
        return "(" + r1 + "|" + r2 + ")"

    def factor(self):
        constant = "([+-]{0,1}(([1-9]\d{0,2})|(0)))"
        signed_constant = "([+-]{1}\d+)"
        index = "([\*]{2}[ \t]{0,3}[+-]{0,1}[0-3]){0,1}"
        power = "(x" + index + ")"
        sin = "(sin\(x\)" + index + ")"
        cos = "(cos\(x\)" + index + ")"
        return "(" + constant + "|" + signed_constant + "|" + power + "|" + sin + "|" + cos + ")"


if __name__ == "__main__":
    my_exp = RegExp()
    print(my_exp.duplicateNegSig())
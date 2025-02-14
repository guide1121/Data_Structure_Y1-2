from array_stack import ArrayStack


def is_balanced(raw):
    s =  ()
    pair  = {")":"(","}":"{","]":"["}
    for c in raw:
        if c in "({[":
            s.push(c)
        elif c in ")}]":
            if s.pop() != pair[c]:
                return False
    return s.is_empty()


print("Testing Balanced Parenthesses")
expression = ["(a+b) * (c+d)",
              "({[a+b]}-c)",
              "((a+b))",
              "(a+b))",
              "{[()]}"
              ]


for expr in expression :
    print(f"Expression: {expr} ---> Balanced : {is_balanced(expr)}")

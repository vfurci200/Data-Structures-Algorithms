# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    indexed_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            indexed_stack.append(i)
            pass
        elif next in ")]}":
            if  opening_brackets_stack == []:
                return i + 1
            else:
                top = opening_brackets_stack[-1]
                
                if (top == '[' and next != ']') or (top == '(' and next != ')') or (top == '{' and next != '}'):
                    return i +1
                else:
                    opening_brackets_stack.pop()
                    indexed_stack.pop()
    if  opening_brackets_stack == []:
        return "Success"               
    else:
        return indexed_stack[0]+1
        # 
        #     # Process closing bracket, write your code here
            
        #     pass


def main():
    text = input()
    # text = "(s({[]}))"
    # text = "[](()"
    # text = "("
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)

if __name__ == "__main__":
    main()

#solution online
#this should close wherever it wants
#best approach is using dict to store and count
#at the end, if the total of open == close then => True, else => False
'''
Success
Details 
Runtime: 54 ms, faster than 10.45% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.2 MB, less than 63.48% of Python3 online submissions for Valid Parentheses.
'''
def isValid(s: str) -> bool:
    #first need to have a stack
    stack = [] 
    #we need something that store the open symbol
    mapping = {
        #this purpose to check the open is in the stack
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }
    
    for char in s:
        #loop through each character
        if char in mapping:
        #if char in the mapping (means it is close char)
            if len(stack) == 0:
                #if the stack is empty then return False
                #because it should be something to compare
                return False
            else:
                var = stack.pop()
                #store a variable to save stack pop top char
                if var != mapping[char]:
                #then compare the variable with mapping value
                    return False
                    #if it is the same then it is a match => continue
                    #else => return false
        else:
            stack.append(char)
            #else char not in mapping (means it is open char)
            #then append to stack
    return len(stack) == 0 #make sure everything is checked and popped off the stack





#best solution
#clean ver
#33ms
def isValid2(s: str) -> bool:
    paranthesis = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    stack = []
    
    for bracket in s:
        if bracket in paranthesis:
            stack.append(bracket)
        elif len(stack) == 0 or paranthesis[stack.pop()] != bracket:
            return False
    return len(stack) == 0

print(isValid2('{[]}'))
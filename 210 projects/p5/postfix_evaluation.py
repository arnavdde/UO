import math

def is_operand(operand: str) -> bool:
    '''
    
    '''
    if operand[0] == '-':
        operand = operand[1]
    return operand.isdigit()

def is_operator(op:str) -> bool:
    '''
    
    '''
    ops = {'+', '-', '*', '/'}
    if op in ops:
        return True
    else:
        return False
    
def apply_operator(op:str, oper_1:float, oper_2:float) -> float:
    '''
    
    '''
    if op == '+':
        return oper_1 + oper_2
    elif op == '-':
        return oper_1 - oper_2
    elif op == '*':
        return oper_1 * oper_2
    elif op == '/':
        if oper_1 != 0 and oper_2 != 0:
            return oper_1 / oper_2
        else:
            return ValueError("ERR: Dividing by 0")
        
def eval_postfix(expr_str:str) -> float:
    stack = []
    split_expr = expr_str.split()
    i = 0
    for ch in split_expr:
        if is_operand(ch):
            stack.append(float(ch))
        elif is_operator(ch):
            if is_operator(split_expr[ch - 1]):
                return ValueError('invalid postfix expression')
            else:
                oper_2 = stack.pop()
                oper_1 = stack.pop()
                stack.append(apply_operator(ch, oper_1, oper_2))
        else: 
            return ValueError('invalid postfix expression')
    
    if len(stack) == 1:
        return stack.pop()
    else:
        return ValueError('invalid postfix expression')

if __name__ == '__main__':
    print(eval_postfix("3 4 +"))
    print(eval_postfix("3 4 + 7 *"))
    print(eval_postfix("3 3.5 4 + 7 * /"))
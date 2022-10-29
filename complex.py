import model_sum as complex_sum
import model_sub as complex_sub
import model_mult as complex_mult
import model_div as complex_div
import model_pow as complex_pow
import model_sqrt as complex_sqrt


def calc(operator, args):
    if operator == 'sum':
        return complex_sum.sum(args[0], args[1])
    elif operator == 'sub':
        return complex_sub.sub(args[0], args[1])
    elif operator == 'mult':
        return complex_mult.mult(args[0], args[1])
    elif operator == 'div':
        return complex_div.div(args[0], args[1])
    elif operator == 'pow':
        return complex_pow.pow(args[0], args[1])
    elif operator == 'sqrt':
        return complex_sqrt.sqrt(args[0])
    else:
        return None
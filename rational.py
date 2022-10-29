import model_sum as rational_sum
import model_sub as rational_sub
import model_mult as rational_mult
import model_div as rational_div
import model_pow as rational_pow
import model_sqrt as rational_sqrt


def calc(operator, args):
    if operator == 'sum':
        return rational_sum.sum(args[0], args[1])
    elif operator == 'sub':
        return rational_sub.sub(args[0], args[1])
    elif operator == 'mult':
        return rational_mult.mult(args[0], args[1])
    elif operator == 'div':
        return rational_div.div(args[0], args[1])
    elif operator == 'int_div':
        return rational_div.div(args[0], args[1])
    elif operator == 'div_int':
        return rational_div.int_div(args[0], args[1])
    elif operator == 'rem_div':
        return rational_div.rem_div(args[0], args[1])
    elif operator == 'pow':
        return rational_pow.pow(args[0], args[1])
    elif operator == 'sqrt':
        return rational_sqrt.sqrt(args[0])
    else:
        return None
import input_data
import prog
import out

def sum():
    a1 = input_data.get_value()
    b1 = input_data.get_value()
    input_data.number(a1, b1)
    num=input_data.get_data()
    # prog.plus(num[0], num[1])
    out.view_data(prog.plus(num[0], num[1]))
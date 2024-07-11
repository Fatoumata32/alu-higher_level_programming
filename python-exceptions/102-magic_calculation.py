def magic_calculation(a, b):
    result = 0  # Corresponds to LOAD_CONST 1 (0) and STORE_FAST 2 (result)

    for i in range(1, 3):  # Corresponds to the setup of the loop
        try:  # Corresponds to SETUP_EXCEPT 49 (to 80)
            if i > a:  # Corresponds to LOAD_FAST 3 (i) and COMPARE_OP 4 (>)
                raise Exception('Too far')  # Corresponds to RAISE_VARARGS 1
            else:
                result += a ** b / i  # Corresponds to the calculations and INPLACE_ADD
        except Exception:  # Corresponds to POP_TOP
            result = b + a  # Corresponds to BINARY_ADD
            break  # Corresponds to BREAK_LOOP
    
    return result

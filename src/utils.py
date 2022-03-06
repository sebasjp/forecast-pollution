def add_zero(x):
    return "0"+str(x) if len(str(x)) == 1 else str(x)

def fix_colnames(x):
    return x.str.lower().str.replace(".", "_")
def zh(s):
    try:
        if type(eval(s))==int:
            s=int(s)
        elif type(eval(s))==float:
            s=float(s)
    except Exception as e:
        print(e)
        print("输入非数字")
        return "error"
    else:
        return s
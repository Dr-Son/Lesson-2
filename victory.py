# Will Smith was born in 1968y
# Jennifer Lopez was born in 1969y
# Marilyn Monroe was born in 1926y
# Natalie Portman was born in 1981y
# Dwayne Johnson was born in 1972y
i = None
while i != ("no"):
    smith = int(input("What year was Will Smith born?"))
    lopez = int(input("What year was Jennifer Lopez born?"))
    monroe = int(input("What year was Marilyn Monroe born?"))
    portman = int(input("What year was Natalie Portman born?"))
    johnson = int(input("What year was Dwayne Johnson born?"))

    st = 0
    sf = 0
    if smith == 1968:
        st = st + 1
    #    print("smith st =", st)
    else:
        #    print("Не верно!")
        sf = sf + 1
    #    print("smith sf = ", sf)

    lt = 0
    lf = 0
    if lopez == 1969:
        #    print("Верно!")
        lt = lt + 1
    #    print("lopez lt =", lt)
    else:
        #    print("Не верно!")
        #    print("lopez lf =", lf)
        lf = lf + 1

    mt = 0
    mf = 0
    if monroe == 1926:
        #    print("Верно!")
        mt = mt + 1
    #    print("monroe mt =", mt)
    else:
        #    print("Не верно!")
        mf = mf + 1
    #    print("monroe mf = ", mf)
    pt = 0
    pf = 0
    if portman == 1981:
        pt = pt + 1
    else:
        pf = pf + 1
    jt = 0
    jf = 0
    if johnson == 1972:
        jt = jt + 1
    else:
        jf = jf + 1

    right = st + lt + mt + pt + jt
    wrong = sf + lf + mf + pf + jf
    print("right ", right)
    print("wrong ", wrong)
    print(right*100/5)
    print(wrong * 100 / 5)
    i = input("продолжить?")
    if i == "yes":
        print()


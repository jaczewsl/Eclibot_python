def play(list):
    # ---------------------------------------- VARIABLES ---------------------------------------------------------------
    final_list = []                                         # Final list with all commands "understandable" for EcliBot
    initial_list = list.split(',')                          # Initial list extracted from String
    initial_size = len(initial_list)                        # Initial list's size
    flag_list = [False, False, False, True, False, True]    # Pattern: [RED, GREEN, BLUE, NO COLOUR, BUZZER, No BUZZER]
                                                            # Initially Eclibot's LED and Buzzer are set to OFF so:
                                                            # flag_list[3] = True and flag_list[5] = True

    # these lists are used as a reference during decision making
    action = ["for", "bac", "lef", "rig", "cre", "cgr", "cbl", "cnc", "bon", "bof"]  # moves, colours and buzzer
    repeat = ["rep", "rep_end", "2", "3", "4", "5"]                                  # repeat
    ifs = ["iff_cr", "iff_cg", "iff_cb", "iff_cn", "iff_bo", "iff_bf", "iff_cr_end", "iff_cg_end", "iff_cb_end",
           "iff_cn_end", "iff_bo_end", "iff_bf_end", "iff_end"]                      # iff

    counter = 0
    x = 0                   # Initial_list pointer

    rep_ends_list = []      # keeps indexes of last position in every loop
    counter_cr = 0          # counts how many times IF RED statement was selected by the user
    cr_end_list = []        # keeps indexes of last position in every IF RED statement
    counter_cg = 0          # counts how many times IF GREEN statement was selected by the user
    cg_end_list = []        # keeps indexes of last position in every IF GREEN statement
    counter_cb = 0          # counts how many times IF BLUE statement was selected by the user
    cb_end_list = []        # keeps indexes of last position in every IF BLUE statement
    counter_cn = 0          # counts how many times IF NO COLOUR statement was selected by the user
    cn_end_list = []        # keeps indexes of last position in every IF NO COLOUR statement
    counter_bo = 0          # counts how many times IF BUZZER ON statement was selected by the user
    bo_end_list = []        # keeps indexes of last position in every IF BUZZER ON statement
    counter_bf = 0          # counts how many times IF BUZZER OFF statement was selected by the user
    bf_end_list = []        # keeps indexes of last position in every IF BUZZER OFF statement

    # ---------------------------------------- FILLING THE LISTS -------------------------------------------------------

    for r in range(initial_size):
        if initial_list[r] == "rep_end":
            rep_ends_list.append(r)
        elif initial_list[r] == "iff_cr_end":
            cr_end_list.append(r)
        elif initial_list[r] == "iff_cg_end":
            cg_end_list.append(r)
        elif initial_list[r] == "iff_cb_end":
            cb_end_list.append(r)
        elif initial_list[r] == "iff_cn_end":
            cn_end_list.append(r)
        elif initial_list[r] == "iff_bo_end":
            bo_end_list.append(r)
        elif initial_list[r] == "iff_bf_end":
            bf_end_list.append(r)

    # ---------------------------------------- MAIN ALGORITHM ----------------------------------------------------------

    while x < initial_size:                                 # Goes through every element in initial list

        if initial_list[x].lower() in action:               # Move, Colour change or Buzzer will be appended to
            final_list.append(initial_list[x])              # our final list; flag list update
            flag_list = flags(flag_list, initial_list[x])
            x += 1

        elif initial_list[x].lower() in repeat:             # Every element inside the loop will be appended to the
            if initial_list[x].lower() == "rep":            # final list, appropriate amount of times.
                counter += 1
                rep_index = x
                rep_end_index = rep_ends_list[counter - 1]
                repeat_number = int(initial_list[int(rep_end_index) - 1])

                z = 0
                x += 1

                while z < repeat_number:
                    while x < rep_end_index - 1:
                        final_list.append(initial_list[x])
                        flag_list = flags(flag_list, initial_list[x])
                        x += 1
                    x = rep_index + 1
                    z += 1
                x = rep_end_index + 1

        elif initial_list[x].lower() in ifs:                # If the element is a start of the IF statement, flag goes
                                                            # up and the condition is checked. If it evaluates to True
            if initial_list[x].lower() == "iff_cr":         # do_ifs() function is called otherwise pointer jumps to the
                                                            # next element outside the IF statement
                counter_cr += 1
                cr_end_if_index = cr_end_list[counter_cr - 1]
                if flag_list[0]:
                    dic = do_ifs(initial_list, final_list, flag_list, x, cr_end_if_index)
                    final_list = dic['new_list']
                    flag_list = dic['flags']
                    x = cr_end_if_index
                else:
                    x = cr_end_if_index
                    print x
            elif initial_list[x].lower() == "iff_cg":
                counter_cg += 1
                cg_end_if_index = cg_end_list[counter_cg - 1]
                if flag_list[1]:
                    dic = do_ifs(initial_list, final_list, flag_list, x, cg_end_if_index)
                    final_list = dic['new_list']
                    flag_list = dic['flags']
                    x = cg_end_if_index
                else:
                    x = cg_end_if_index
            elif initial_list[x].lower() == "iff_cb":
                counter_cb += 1
                cb_end_if_index = cb_end_list[counter_cb - 1]
                if flag_list[2]:
                    dic = do_ifs(initial_list, final_list, flag_list, x, cb_end_if_index)
                    final_list = dic['new_list']
                    flag_list = dic['flags']
                    x = cb_end_if_index
                else:
                    x = cb_end_if_index
            elif initial_list[x].lower() == "iff_cn":
                counter_cn += 1
                cn_end_if_index = cn_end_list[counter_cn - 1]
                if flag_list[3]:
                    dic = do_ifs(initial_list, final_list, flag_list, x, cn_end_if_index)
                    final_list = dic['new_list']
                    flag_list = dic['flags']
                    x = cn_end_if_index
                else:
                    x = cn_end_if_index
            elif initial_list[x].lower() == "iff_bo":
                counter_bo += 1
                bo_end_if_index = bo_end_list[counter_bo - 1]
                if flag_list[4]:
                    dic = do_ifs(initial_list, final_list, flag_list, x, bo_end_if_index)
                    final_list = dic['new_list']
                    flag_list = dic['flags']
                    x = bo_end_if_index
                else:
                    x = bo_end_if_index
            elif initial_list[x].lower() == "iff_bf":
                counter_bf += 1
                bf_end_if_index = bf_end_list[counter_bf - 1]
                if flag_list[5]:
                    dic = do_ifs(initial_list, final_list, flag_list, x, bf_end_if_index)
                    final_list = dic['new_list']
                    flag_list = dic['flags']
                    x = bf_end_if_index
                else:
                    x = bf_end_if_index

            x += 1
    return final_list

    # -------------------------- do_ifs(initial_list, final_list, flag_list, x, if_end_index)---------------------------


def do_ifs(list1, list2, f_list, x, end):       # Returns dictionary that consists two lists:
    x = x + 1                                   # 1. Our altered final list
    iff_end_index = end                         # 2. Altered flag list
    while x < iff_end_index:
        print "+++ do_ifs() called"
        list2.append(list1[x])
        f_list = flags(f_list, list1[x])
        x += 1
    d = dict();
    d['new_list'] = list2
    d['flags'] = f_list

    return d

    # ---------------------------------------- flags(flag_list, element) -----------------------------------------------


def flags(list, flag):      # Each time this method is called the flags for Colours (red, green, blue, no colour) and
    cr = list[0]            # for Buzzer (buzzer on/off) are adjusted
    cg = list[1]
    cb = list[2]
    cn = list[3]
    bon = list[4]
    bof = list[5]
    print "flag:", flag

    if flag == "cre":
        list = [True, False, False, False, bon, bof]    # Keep in mind that any colour flag leaves buzzer flag
    elif flag == "cgr":                                 # unchanged and vice versa
        list = [False, True, False, False, bon, bof]
    elif flag == "cbl":
        list = [False, False, True, False, bon, bof]
    elif flag == "cnc":
        list = [False, False, False, True, bon, bof]
    elif flag == "bon":
        list = [cr, cg, cb, cn, True, False]
    elif flag == "bof":
        list = [cr, cg, cb, cn, False, True]

    print "Flags", list
    return list                                         # return altered flag list


#                                               TESTING
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------


# l1 = "for,bac,lef,rig,rep,for,lef,3,rep_end"
# l2 = "for,bac,lef,rig,rep,for,lef,1,rep_end"
# l3 = ""     # ERROR
# l4 = "for"  # ERROR
# l5 = "for,bac,rep,for,lef,5,rep_end,lef,bac"
# # TESTING IF COMMANDS
# l6 = "for,lef,iff_cr,bon,for,for,bof,iff_end,bac"
# l7 = "for,cre,lef,iff_cr,bon,for,for,bof,iff_cr_end,bac"
# j7 = "for,cgr,lef,iff_cr,bon,for,for,bof,iff_cr_end,bac"
# j8 = "iff_cr,for,iff_cr_end,iff_cg,lef,iff_cg_end,iff_cb,bon,iff_cb_end,cre,cre,iff_cr,lef,iff_cr_end,cre"
# j9 = "iff_cg,for,iff_cg_end,iff_cg,lef,iff_cg_end,iff_cb,bon,iff_cb_end,cre,cre,iff_cr,lef,iff_cr_end,cre"
# j10 = "iff_cg,for,iff_cg_end,iff_cg,lef,iff_cg_end,iff_cb,bon,iff_cb_end,cre,cre,iff_cr,lef,iff_cr_end,cre"
# j11 = "cgr,iff_cg,for,iff_cg_end,iff_cg,lef,iff_cg_end,iff_cb,bon,iff_cb_end,cre,cre,iff_cr,lef,iff_cr_end,cre"
# j12 = "cgr,iff_cg,for,iff_cg_end,cbl,iff_cg,lef,iff_cg_end,iff_cb,bon,iff_cb_end,cre,cre,iff_cr,lef,iff_cr_end,cre"
#
#
# # TESTING ALL TOGOTHER
# l8 = 'for,bon,rig,rep,for,for,lef,2,rep_end,iff_cr,bof,cbl,iff_end,bac,bof'
# l9 = "for,bac,lef,rig,rep,for,lef,3,rep_end,iff_cb,bon,iff_cb_end,cre,iff_cr,lef,iff_cr_end"
#
# # MULTIPLE IF's
# i1 = 'for,cbl,iff_cr,bon,iff_cg,rig,iff_bl,cre,rig'
# i2 = 'for,cgr,iff_cr,bac,iff_cr_end,iff_cb,bon,iff_cb_end,iff_cg,cbl,rig,iff_cg_end'
# i3 = 'for,cgr,iff_cr,bac,iff_cr_end,iff_cb,bon,iff_cb_end,iff_cg,cbl,rig,iff_cg_end'
#
# # BUZZER
# b1 = "iff_bf,cre,iff_bf_end"
# b2 = "iff_bf,cre,iff_bf_end,iff_cr,bon,iff_cr_end"
#
#
# # REPEAT TESTING
# r1 = 'rep,for,cgr,1,rep_end'
# r2 = 'rep,for,cgr,2,rep_end'
# r3 = 'rep,for,cgr,3,rep_end'
# r4 = 'rep,for,cgr,4,rep_end'
# r5 = 'for,rep,for,cgr,2,rep_end,bac,for,cgr,iff_cr,bac,iff_cr_end,iff_cb,bon,iff_cb_end,iff_cg,cbl,rig,iff_cg_end'
#
# r6 = 'rep,for,cgr,3,rep_end,rep,for,cgr,2,rep_end'
# r7 = 'rep,for,cgr,3,rep_end,lef,rep,for,cgr,2,rep_end,bac,rep,bon,3,rep_end,rig'
# x8 = "rep,cre,cgr,cbl,cnc,2,rep_end,iff_cn,bon,cre,iff_cn_end"
# x9 = "rep,bac,2,rep_end,for,rep,bac,bac,2,rep_end"
#
#
# x1 = play(l7)
#
# print "origin: ", l7
# print "result: ", x1
#
# print "---------------"
#
# del x1[:]
#
# print "x1: ", x1
#
# x1 = play(j7)
# # print "r1: ", r1
# print "origin: ", j7
# print "result: ", x1
# print "---------------"
# del x1[:]
#
# x1 = play(i2)
# print "origin: ", i2
# print "result: ", x1
# print "---------------"
# del x1[:]
#
# x1 = play(i3)
# print "origin: ", i3
# print "result: ", x1
#
# print "---------------"
# del x1[:]
#
# x1 = play(r1)
# print "origin: ", r1
# print "result: ", x1
# print "---------------"
# del x1[:]
#
# x1 = play(r2)
# print "origin: ", r2
# print "result: ", x1
# print "---------------"
# del x1[:]
#
# x1 = play(r3)
# print "origin: ", r3
# print "result: ", x1
# print "---------------"
# del x1[:]
#
# x1 = play(r4)
# print "origin: ", r4
# print "result: ", x1
# print "---------------"
# del x1[:]
#
# x1 = play(r5)
# print "origin: ", r5
# print "result: ", x1
# print "---------------"
# del x1[:]
#
# x1 = play(r6)
# print "origin: ", r6
# print "result: ", x1
# print "---------------"
# del x1[:]
#
# x1 = play(r7)
# print "origin: ", r7
# print "result: ", x1
# print "---------------"
# del x1[:]
#
# x1 = play(j8)
# print "origin: ", j8
# print "result: ", x1
# print "---------------"
# del x1[:]
#
# x1 = play(j10)
# print "origin: ", j10
# print "result: ", x1
# print "---------------"
# del x1[:]
#
# x1 = play(j11)
# print "origin: ", j11
# print "result: ", x1
# print "---------------"
# del x1[:]
#
# x1 = play(j12)
# print "origin: ", j12
# print "result: ", x1
# print "---------------"
# del x1[:]
#
# x1 = play(b1)
# print "origin: ", b1
# print "result: ", x1
# print "---------------"
# del x1[:]
#
# x1 = play(x8)
# print "origin: ", x8
# print "result: ", x1
# print "---------------"
# del x1[:]
#
# x1 = play(x9)
# print "origin: ", x9
# print "result: ", x1
# print "---------------"
# del x1[:]

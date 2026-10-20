def book_position(codes,wanted):
    for i in range(len(codes)):
        #idx=-1
        if codes[i]==wanted:
            #idx=i
            #break
            return i
    #return idx
    # return codes.index(wanted)
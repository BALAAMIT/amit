import random
st = input("input Enter..._")
words= st.split(" ")
coding = input("1 for coding or 0 for decodng")
coding = True  if  (coding =="1") else  False
if(coding):
    nwords = []
    for word in words:
        if (len(word)>=3):
            r1 ="kly"
            r2 = "mno"
            stnew= r1+word[1:]+word[0]+r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
            

    
else:
    nwords = []
    for word in words:
        if (len(word)>=3):
            r1 ="kly"
            r2 = "mno"
            stnew= word[3:-3]
            stnew = stnew[-1]+stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

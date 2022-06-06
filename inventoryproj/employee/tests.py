s="aabbcdddabb"

def compress_string(s):
    n=len(s)
    new_s=''
    count=1

    for i in range(n-1):
        if s[i]==s[i+1]:
            count+=1
        else:
            new_s+=(s[i]+str(count))
            count=1
    new_s+=s[n-1]+str(count)


print(compress_string(s))
#a2b2c1d3a1b2
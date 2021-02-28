def div(a,b):
    return a/b
#if I want Numerator to always be greater than denominator

#decorator - modifying original func without touching it

def smartdiv(func):
    def inf(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inf

#making obj to call func,
#modified div - old div (we can assign like this, since everything in python is an obejct)
div=smartdiv(div)
res=div(2,4)
print(res)
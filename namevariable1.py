

#print("Hi : ", __name__) - this will return main only when this is the first file to run

def exe():
    print("Hi I'm testing")

#I want to call this function only when its primary to be called

if __name__=="__main__":
    exe()
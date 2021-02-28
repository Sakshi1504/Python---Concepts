from threading import Thread
from time import sleep
class Hello(Thread):
    #run necessorily need to be used while working on threads
    def run(self):
        for i in range(6):
            sleep(1)
            print("heeeellloooo")

class Hii(Thread):

    def run(self):
        for i in range(6):
            sleep(1)
            print("Hiiii")


t1=Hello()
t2=Hii()
'''
run has to be present in the thread class, to run thread we use start method and then it calls run from inside
t1.run()
t2.run()
'''

t1.start()
sleep(0.1) #to avoid collisions between threads
t2.start()

t1.join()
t2.join()
print("Bye") #this will be run using Mainthread - to make it run at last, we'll have to wait for both the threads to join back

#to make class run using thread - make it a subclass of Thread class, import using threading module


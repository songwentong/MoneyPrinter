import time
print("12345")

class Main:
    
    loopIndex = 0

    def loop(self):
        print("loop:" + str(loopIndex))
        time.sleep(1)
        loopIndex+=1
        self.loop()
    def main():
        print("main")
        loop()

    
p = Main()
p.loop()
#print(p)
#loop()
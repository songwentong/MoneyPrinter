import time
print("12345")
def main():
    print("main")

def loop():
    print("loop")
    time.sleep(1)
    loop()

loop()
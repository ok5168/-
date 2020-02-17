

def a(b):
    print("a11111")
    b()
    print("a22222")
@a 
def b(bb="good:"):
    print(bb,"bbbb")
b()
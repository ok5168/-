from pathlib import Path
p = Path('.')
print([x for x in p.iterdir() if x.is_dir()])
def a(b):
    print("a11111")
    b()
    print("a22222")
@a:
def b():
    print("bbbb")

a()
 

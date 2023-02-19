e = 1
r = 1
def setup():
    size(900,900)
    background(255)
def draw():
    global e,r
    ellipse(650,r,100,100)
    r = r + 1
    if e <= 0:
        r = r + 1
        global e,r
    ellipse(300,r,100,100)
    r = r + 1
    if e <= 0:
        r = r + 1
        global e,r
    ellipse(r,100,100,100)
    r = r + 1
    if e <= 0:
        r = r + 1
        global e,r
    ellipse(r,400,100,100)
    r = r + 1
    if e <= 0:
        r = r + 1

import time
import sys
import random

###################- Core Methods -################
def next_pos(i, fwd):
    if fwd:
        return i+1
    else:
        return i-1;


def nextchar_cursor(pattern):
    while True:
        for cursor in pattern:
            yield cursor


#######- Simple spin and wait -#####################

def spinner(speed, wt):
    cursor = nextchar_cursor("-/\\|")
    st = 1.0 / speed
    for i in range(wt):
      rs = "%3d" % (wt-i)
      for j in range(speed):
        sys.stdout.write("-> "+rs+"s   "+cursor.next()+" \r")
        sys.stdout.flush()
        time.sleep(st)

#######- Simple Oscillator -#####################

def oscillator(speed, ln):
    cs = "_-`-" #Unit pattern
    w = 4 #Max no. of cs units
    wl = 12 #Oscillator Length
    ca = (w*cs)
    span = len(ca) - wl
    st = 1.0 / speed
    fwd = True
    idx = 0
    for i in range(ln):
      rs = "%3d" % (ln - i)
      for j in range(speed):
        f1 = (" "*idx)
        f2 = ca[idx:idx+wl]
        f3 = (" "*(len(ca) - idx - wl))
        fp = lp = '|'
        if len(f1) == 0:
            fp = "/"
        if len(f3) == 0:
            lp = "\\"    
        ns =  fp+ f1 +  f2 + f3 + lp
        sys.stdout.write('-> '+rs+'s     '+ns+'\r')
        sys.stdout.flush()
        time.sleep(st)
        idx = next_pos(idx, fwd)
        if(idx ==0): fwd = True
        if(idx == span): fwd = False


#######- Vertigo Oscillator -################
def vertigo_oscillator(speed, ln):
    chars = nextchar_cursor("/\\")
    cs = "    "
    w = 10
    ca = (w*cs)
    N = len(ca)
    st = 1.0 / speed
    fwd = True
    idx = 0
    for i in range(ln):
      rs = "%3d" % (ln - i)
      for j in range(speed):
        ns = ca[0:idx]+chars.next()+ca[idx+1:N]
        sys.stdout.write('-> '+rs+'s |'+ns+'|\r')
        sys.stdout.flush()
        time.sleep(st)
        idx = next_pos(idx, fwd)
        if(idx ==0): fwd = True
        if(idx == (N-1)): fwd = False       


#######- Domino Falling -#####################
def domino_falling(speed, ln):
    chars = nextchar_cursor("/\\")
    cs = "_-`-"
    w = 15
    ca = (w*cs)
    N = len(ca)
    st = 1.0 / speed
    fwd = True
    idx = 0
    for i in range(ln):
      rs = "%3d" % (ln - i)
      for j in range(speed):
        ns = ca[0:idx]+chars.next()+ca[idx+1:N]
        sys.stdout.write('-> '+rs+'s ['+ns+']\r')
        sys.stdout.flush()
        time.sleep(st)
        idx = next_pos(idx, fwd)
        if(idx ==0): fwd = True
        if(idx == (N-1)): fwd = False

#######- Domino Falling -#####################
def wave(speed, ln):
    cs = "_-`-"
    w = 15
    ca = (w*cs)
    N = len(ca)
    st = 1.0 / speed
    fwd = True
    idx = 0
    for i in range(ln):
      rs = "%3d" % (ln - i)
      for j in range(speed):
        ns = ca[0:idx]+" "+ca[idx+1:N]
        sys.stdout.write('-> '+rs+'s ['+ns+']\r')
        sys.stdout.flush()
        time.sleep(st)
        idx = next_pos(idx, fwd)
        if(idx ==0): fwd = True
        if(idx == (N-1)): fwd = False


#############- Demo -###############################
def demo_all(speed, wt):        
    spinner(speed, wt)
    oscillator(speed, wt)
    vertigo_oscillator(speed+5, wt)
    domino_falling(speed, wt)
    wave(speed, wt)


def surprise_me(speed, wt):
    r = random.randint(1,5)
    if r==1:
        spinner(speed, wt)
    elif r==2:
        oscillator(speed, wt)
    elif r==3:
        vertigo_oscillator(speed+5, wt)
    elif r==4:
        domino_falling(speed, wt)
    else:
        wave(speed+2, wt)
                               

#demo_all(10, 10)
surprise_me(12, 10)

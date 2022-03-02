#!/usr/bin/env python3
import time

from sys import exit

from libs.utils import *

from os import path
from libs.attack import report_profile_attack
from multiprocessing import Process

def chunks (a ,b ):
    ""
    for c in range (0 ,len (a ),b ):
        yield a [c : c + b ]

def profile_attack_process (a ,b ):
    if (len (b )==0 ):
        for x in range (10 ):
            report_profile_attack (a ,None )
        return 
    for c in b :
        report_profile_attack (a ,c )


def profile_attack(target):
    for a in range (5 ):
        a = Process (target =profile_attack_process ,args =(target,[],))
        a.start ()
    
def main ():#line:115
    target_list = open("targets",'r')
    for line in target_list:
        profile_attack(line)

if __name__ =="__main__":#line:157
    try :#line:159
        main ()#line:160
    except KeyboardInterrupt :#line:162
        exit()

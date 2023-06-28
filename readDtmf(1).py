#!/usr/bin/python
import RPi.GPIO as g
import time

GPIO_D0  = 5
GPIO_D1  = 6
GPIO_D2  = 13
GPIO_D3  = 19
GPIO_StQ = 26

g.setmode(g.BCM)
g.setwarnings(False)

while True:

	time.sleep(0.1) # standaard warde is 0.1 sec

	g.setup(GPIO_D0, g.IN) # 5
	g.setup(GPIO_D1, g.IN) # 6
	g.setup(GPIO_D2, g.IN) # 13
	g.setup(GPIO_D3, g.IN) # 19
	g.setup(GPIO_StQ, g.IN) # 26

	D0 = g.input(GPIO_D0)
	D1 = g.input(GPIO_D1)
	D2 = g.input(GPIO_D2)
	D3 = g.input(GPIO_D3)
	StQ= g.input(GPIO_StQ)

	if StQ == True:

		decimaal = D0+(D1*2)+(D2*4)+(D3*8)

		if decimaal==10:
			decimaal=0

		print ("\033c") # wis scherm
#		print ("DTMF toon detector")
#		print ("==================")

		print ("\033[1;33;40m  MT8870 - DTMF toon detector")
		print ("===============================\033[0m")

#		print ("StQ ="),StQ
#		print ("De DTMF-toon is "),decimaal
#		print D0, D1, D2, D3, (" = "),decimaal
#		print ("De DTMF-toon is ("),D0,D1,D2,D3,(") ="),decimaal
		print ("De DTMF-toon is (")+str(D0)+str(D1)+str(D2)+str(D3)+(") ="),decimaal
		print ("")

#	print ("\n")

	else:
		print ("\033c") # wis scherm

		print ("\033[1;33;40m  MT8870 - DTMF toon detector")
		print ("===============================\033[0m")

#		print ("DTMF toon detector")
#		print ("==================")
#		print ("StQ ="),StQ
#		print ("StQ = 0")
#		print ("Er wordt geen DTMF-toon aangeboden")
		print ("De DTMF-toon is 'stil'")
		print ("")

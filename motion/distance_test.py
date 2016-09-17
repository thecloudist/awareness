from gopigo import *

enable_encoders()
led_on(0)

print "\nCHECKING ENCODER TARGETING"
for i in range(5):
	print "\nInitial encoder read vals:",
	fwd()
	enc_tgt(1,1,36)
	left()
	print enc_read(0),
	print enc_read(1)
	time.sleep(.5)
	#bwd()
	enc_tgt(1, 1, 36)
	while True:
		enc_stat=read_enc_status()
		print "Enc tgt Status: ",enc_stat
		if enc_stat==0:

			break;

		time.sleep(.5)

	print "Final encoder read vals:",
	print enc_read(0),
	print enc_read(1)
	time.sleep(1)
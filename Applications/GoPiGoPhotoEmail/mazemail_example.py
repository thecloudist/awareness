#!/usr/bin/python
# Adapted from http://solvingmytechworld.blogspot.com/2013/01/send-email-through-gmail-running-script.html
 
# Import smtplib for the actual sending function
import smtplib
 
# For guessing MIME type
import mimetypes
 
# Import the email modules we'll need
import email
import email.mime.application
 
#Import sys to deal with command line arguments
import sys

from gopigo import *
import time
import picamera

distance_to_stop=20             #Distance from obstacle where the GoPiGo should stop
print "Press ENTER to start"
raw_input()                             #Wait for input to start

count=0
success = False
while count < 3:
        dist=us_dist(15)                        #Find the distance of the object in front
        fwd()
        set_speed(100)
        print "Dist:",dist,'cm'
        if dist<distance_to_stop:       #If the object is closer than the "distance_to_stop" distance, stop the GoPiGo
                print "Stopping"
                stop()                                  #Stop the GoPiGo
                time.sleep(.1)
                print "Reversing for 1.2 seconds"
                bwd()
                set_speed(220)
                time.sleep(1.2)
                print "Stopping again"
                stop()
                time.sleep(.1)

		with picamera.PiCamera() as camera:
    	            print "Taking photo"
    		    camera.capture('/home/pi/Desktop/camemail1.jpg')
    		    time.sleep(1)

		print "Sending email"
 
		# Create a text/plain message
		msg = email.mime.Multipart.MIMEMultipart()
		msg['Subject'] = 'subject_you_prefer'
		msg['From'] = 'ian.raspi@gmail.com'
		msg['To'] = 'ianturnercms@gmail.com'
                
		# The main body is just another attachment
		body = email.mime.Text.MIMEText("""Here you can write as many things as you want!""")
		msg.attach(body)
 
		# PDF attachment block code; Nico: Ok, use a fixed image...and a jpg not pdf
 
		#directory=sys.argv[1]
		directory = '/home/pi/Desktop/camemail1.jpg'
 
		# Split de directory into fields separated by / to substract filename
		spl_dir=directory.split('/')
 
		# We attach the name of the file to filename by taking the last; position of the fragmented string, which is, indeed, the name; of the file we've selected
 		filename=spl_dir[len(spl_dir)-1]
 
		# We'll do the same but this time to extract the file format (pdf, epub, docx...)
 		spl_type=directory.split('.')
 		type=spl_type[len(spl_type)-1]
 
		fp=open(directory,'rb')
		att = email.mime.application.MIMEApplication(fp.read(),_subtype=type)
		fp.close()
		att.add_header('Content-Disposition','attachment',filename=filename)
		msg.attach(att)
 
		# send via Gmail server; NOTE: my ISP, Centurylink, seems to be automatically rewriting;
                # port 25 packets to be port 587 and it is trashing port 587 packets; So, I use the default port 25, but I authenticate.
		s = smtplib.SMTP('smtp.gmail.com:587')
		s.starttls()
		s.login('ian.raspi@gmail.com','YOUR-OWN-PASSWORD')
		s.sendmail('ianturnercms@gmail.com','ianbt7@gmail.com', msg.as_string())
		s.quit()
				
		#resuming GoPiGo Motion
		time.sleep(1)
                print "Turning left"
                left()
                set_speed(100)
                time.sleep(1)
                print "Stopping last time"
                stop()
                time.sleep(.1)
                print "Voltage is", volt()
                count+=1
        time.sleep(.1)

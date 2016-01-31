import wikipedia
import sys
# NOTE: this example requires PyAudio because it uses the Microphone class

import shlex, subprocess 
import speech_recognition as sr
import pyvona
from googlesearch import GoogleSearch

def wikileaks(string):
	string=wikipedia.summary(string,sentences=1)
	chatvoice(string)
def speak():
	# obtain audio from the microphone
	r = sr.Recognizer()
	with sr.Microphone() as source:
	    r.adjust_for_ambient_noise(source) # listen for 1 second to calibrate the energy threshold for ambient noise levels
	    print("Say something!")
	    audio = r.listen(source)

	# recognize speech using Google Speech Recognition
	try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
	    string =  r.recognize_google(audio)
	    print "you said "+string
	    return string 
	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))

def Google1(string):
	gs = GoogleSearch(string)
	for hit in gs.top_results():
		#send(hit[u'content'])
		chatvoice(hit[u'content'])
		break


def chatvoice(string):
	v = pyvona.create_voice('GDNAI2AAUGNCQFO4TFSA','a+MtpzzlpqskQsYFPMaczgYMbzXurj/i5vduNEzL')
	#v.region('en-IN')
	#print v.list_voices() 
	v.speak(string)
	#v.speak(a) 	






		

'''
my father and mother is unable to make enough money for my study in engineering colleges . Its very hard for my to get any resources to study books are very costly and online digital library too '''

'''
data science is a emerging field and this field will make me rich , my hardships will finally come to an end after learning about and gaining certificates and get recruited into good companies'''

'''
yes , i will help students in the help section and discussion forums . i will bind to the course and will try to make available this as most as possible '''





	


if __name__=="__main__":
	while True:
		takeString = speak() 
		if takeString  == "arrange photos":
			com = "python main.py -k"
			args = shlex.split(com) 
 			p = subprocess.Popen(args)
			print "Mission complete Bye !" 
			sys.exit(0)
		if takeString == "hi how are you":
			chatvoice("i am good you tell about yourself")
		if takeString == "shut up":
			chatvoice("go fuck yourself")
			sys.exit(-1)
		if takeString == "Google":
			chatvoice("move on")
			takeString = speak()
			Google1(takeString)
		#Google1(takeString)
		#wikileaks(takeString)




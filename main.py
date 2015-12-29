import optparse
import re
import shutil
import os

parser = optparse.OptionParser()
def document(option,opt_str,value,parser):
	parser.values.saw_doc = True
	string=os.listdir(".")
	tf = os.path.isdir("Documents")
	if tf is True:
		r1=[]
		comp=""
		for i in string:
		#os.mkdir("Documents")
			#comp = str(i) 
			#print type(i)
			r = re.findall(r'^.*\.(txt|xls|c|out|doc|pptx?|pdf)',i)
			if len(r) > 0:
				shutil.move(i,'Documents')
			else:
				pass
		print "Successfully moved Docs"
	else:
		os.mkdir("Documents")
		print "Try again :)"

def compress(option,opt_str,value,parser):
	parser.values.saw_doc = True
	string=os.listdir(".")
	tf = os.path.isdir("Compressed")
	if tf is True:
		#print string
		r1=[]
		comp=""
		for i in string:
		#os.mkdir("Documents")
			#comp = str(i) 
			#print type(i)
			r = re.findall(r'^.*\.(zip|tar.xz|tar.gz|rar)',i)
			if len(r) > 0:
				shutil.move(i,'Compressed')
			else:
				pass
		print "Successfully moved Compressed files"
	else:	
		os.mkdir("Compressed")
		print "Try again :)"

def video(option,opt_str,value,parser):
	parser.values.saw_doc = True
	string=os.listdir(".")
	tf = os.path.isdir("Video")
	if tf is True:
		#print string
		r1=[]
		comp=""
		for i in string:
		#os.mkdir("Documents")
			#comp = str(i) 
			#print type(i)
			r = re.findall(r'^.*\.mp4',i)
			if len(r) > 0:
				shutil.move(i,'Video')
			else:
				pass
		print "Successfully moved Videos"
	else:
		os.mkdir("Video")
		print "Try again :)"
def programs(option,opt_str,value,parser):
	parser.values.saw_doc = True
	string=os.listdir(".")
	tf = os.path.isdir("programs")
	if tf is True:
		#print string
		r1=[]
		comp=""
		for i in string:
		#os.mkdir("Documents")
			#comp = str(i) 
			#print type(i)
			r = re.findall(r'^.*\.(py|html|exe|jar|bin)',i)
			if len(r) > 0:
				shutil.move(i,'programs')
			else:
				pass
		print "Successfully moved programs"
	else:
		os.mkdir("programs")
		print "Try again :)"
def pics(option,opt_str,value,parser):
	parser.values.saw_doc = True
	string=os.listdir(".")
	tf = os.path.isdir("Pics")
	if tf is True:
		#print string
		r1=[]
		comp=""
		for i in string:
		#os.mkdir("Documents")
			#comp = str(i) 
			#print type(i)
			r = re.findall(r'^.*\.(jpg|png|jpeg|JPEG|PNG|mp3)',i)
			if len(r) > 0:
				shutil.move(i,'Pics')
			else:
				pass
		print "Successfully moved Pics"
	else:	
		os.mkdir("Pics")
		print "Try again :)"


parser.add_option('-k', '--pics',
    action="callback",callback=pics ,help="assemble pics in Pics folder")
parser.add_option('-d','--doc',
	action="callback",callback=document,help="assemble documents in Document folder")
parser.add_option('-p','--programs',
	action="callback",callback=programs,help="assemble programs in programs folder")

parser.add_option('-c','--compress',
	action="callback",callback=compress,help="assemble compress files in Compressed folder")

parser.add_option('-v','--video',
	action="callback",callback=video,help="assemble videos in Video folder")



if __name__=="__main__":                                                                                                     
	options, args = parser.parse_args()



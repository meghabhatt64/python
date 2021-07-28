

# u need to pip install pyttsx3 , pywin32 , speechRecognition , pyaudio , wikipedia


import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')	# speech api
voices = engine.getProperty('voices')	# for the voices in computer
# print(voices[0].id)	# to view  no. the voices
engine.setProperty('voice', voices[0].id)	# 0 for male ,1 for female

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishme():
	hour = int(datetime.datetime.now().hour)
	if hour >= 00 and hour < 12:
		speak("Good morning ")
	elif hour >= 12 and hour < 16:
		speak("Good afternoon ")
	elif hour >= 16 and hour < 20:
		speak("Good evening ")
	else:
		speak("Good night")
	speak("hello ma'am ,i am jarvis , how may i help you? ")

def takecmd():
	''' it takes microphone input from the user and gives string output
	'''
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening ...")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	try:
		print("Recognizing ...")
		query = r.recognize_google(audio,language='en-in')
		print("User said ", query)
		
	except Exception as e:
		print(e)
		print("Say that again please ...")
		return "None"
	return query
if __name__ == "__main__":
	speak(" i m a good girl")
	wishme()
	while True:
	#if 1:
		query = takecmd().lower()
		
		# logic for executing tasks based on query
		if "wikipedia" in query:
			speak("Searching wikipedia... ")
			query = query.replace("wikipedia","") 
			results = wikipedia.summary(query,sentences = 2)
			speak("According to wikipedia ...")
			print(results)
			speak(results)
		elif "open google" in query:
			webbrowser.open("google.com")
		elif "your name" in query:
			speak("I m Jarvis...your Friend")
		elif "open youtube" in query:
			webbrowser.open("youtube.com")
		elif "play music" in query:
			musicdir ="C:\\Users\\Megha\\Music"
			song = os.listdir(musicdir)
			print(song)
			os.startfile(os.path.join(musicdir,song[1]))
		elif "the time" in query:
			strtime = datetime.datetime.now().strftime("%H:%M:%S")
			speak(f"ma'am ,the time is{strtime}")
		elif "open code" in query:
			codepath = "D:\\Demo\\Python\\jarvis.py"
			os.startfile(codepath)

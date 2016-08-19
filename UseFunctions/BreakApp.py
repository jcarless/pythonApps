import webbrowser
import time

breaks = 1

while breaks <= 3:
	time.sleep(10)

	webbrowser.open("http://www.jeromecarless.com")
	print breaks
	breaks += 1
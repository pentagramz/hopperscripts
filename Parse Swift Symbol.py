import subprocess

doc = Document.getCurrentDocument()
sym = doc.getHighlightedWord()
proc = subprocess.Popen(['xcrun','swift-demangle',sym],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output, errors = proc.communicate()
if errors is not None:
	doc.log(errors)
if output is not None:
	func = output.split('>', 1)[1]
	func = func.strip()
	doc.log(func)

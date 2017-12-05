from time import strftime

hereandnow = int(strftime("%H%M"))

def whattodrink():
	if 0 <= hereandnow <= 459:
		return "Why are you awake? Have a glass of water, go to bed."
	if 500 <= hereandnow <= 1130:
		return "It's coffee time!"
	if 1131 <= hereandnow <= 1659:
		return "Time for tea or coffee."
	if 1700 <= hereandnow <= 2130:
		return "How about some beer or wine? Or tea, if you'd rather."
	if 2131 <= hereandnow <= 2359:
		return "Have some herbal tea or water, it's about time for bed."
	else:
                return "Time to get your clock fixed?"

print(whattodrink())

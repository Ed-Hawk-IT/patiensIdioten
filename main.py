def print_card(suit, value):
	red = "\033[31m"
	default = "\033[0m"

	color = default
	symbol = "ERR"


	if suit == 's':
		symbol = '\u2660'
		color = default

	elif suit == 'h':
		symbol = '\u2665'
		color = red;

	elif suit == 'd':
		symbol = '\u2666'
		color = red;

	elif suit == 'c':
		symbol = '\u2663'
		color = default


	# print ace as 'A'
	value = str(value)
	if value == 1 or value == 14:
		value = 'A'
		

	print("\u256D\u2500\u2500\u256E")
	print('\u2502' + color + value + symbol + default + '\u2502')
	print('\u2502' + color + symbol + value + default + '\u2502')
	print("\u2570\u2500\u2500\u256F")

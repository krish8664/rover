

def north(x, y):
	return x, y+ 1

def east(x, y):
	return x + 1, y

def west(x, y):
	return x - 1, y

def south(x, y):
	return x, y - 1

def did_i_fall(x, y, upper_right, lower_left):
	''' check if the rover has gone over the edge'''
	if x < lower_left[0] or x > upper_right[0]:
		return True
	elif y < lower_left[1] or y > upper_right[1]:
		return True
	return False

def standardise(tuples):
	''' convertes the numbers into int from the string '''
	if len(tuples) == 3:
		x,y,F = tuples
		return (int(x), int(y), F)
	elif len(tuples) == 2:
		x,y = tuples
		return (int(x), int(y))

def track_rover(rover_position, rover_instruction, upper_right, lower_left):
	''' tracks the movement of the rover based on the instruction '''

	x, y, Facing = rover_position
	if not rover_instruction:
		return rover_position
	if rover_instruction:
		instruction = rover_instruction[0]

		if instruction is 'M':
			x, y = move[Facing](x, y)
			if did_i_fall(x, y, upper_right, lower_left):
				return 'I Fell'
		else:
			rotate = lambda Facing, instruction: left[Facing] if instruction is 'L' else right[Facing]
			Facing = rotate(Facing, instruction)

		return track_rover((x, y, Facing), rover_instruction[1:], upper_right, lower_left)

def main():
	lower_left = (0, 0)
	upper_right = standardise(tuple(raw_input().split()))
	rovers = []

	while True:
		position = raw_input()
		if position is not '':
		    instruction = raw_input()
		    rovers.append(track_rover(standardise(tuple(position.split())), instruction, upper_right, lower_left))
		else:
			break
	for rover in rovers:
		print rover

left = {'N' : 'W' ,'E' : 'N', 'W' : 'S', 'S' : 'E'}
right = {'N' : 'E', 'E' : 'S', 'W' : 'N', 'S' : 'W'}
move = {'N' : north, 'E' : east , 'W' : west , 'S' : south}

if __name__ == "__main__":
	main()
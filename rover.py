

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
			# if instruction is to move then add 1 or subtract 1 based on the direction the rover
			# is currentlyfacing
			if(Facing == 'N'):
				y += 1
			elif(Facing == 'E'):
				x += 1
			elif(Facing == 'S'):
				y -= 1
			else:
				x -= 1
			if did_i_fall(x, y, upper_right, lower_left):
				return 'I Fell'
		else:
			# if the instruction is to rotate the based on 'L'/'R' rotate 90 degree
			# to the left if 'L' or right if 'R'
			if Facing is 'N':
				Facing = 'W' if instruction is 'L' else 'E'
			elif Facing is 'E':
				Facing = 'N' if instruction is 'L' else 'S'
			elif Facing is 'S':
				Facing = 'E' if instruction is 'L' else 'W'
			elif Facing is 'W':
				Facing = 'S' if instruction is 'L' else 'N'

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

if __name__ == "__main__":
	main()
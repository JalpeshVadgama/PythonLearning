words = ['Hello','World', "Jalpesh"]

for w in words:
	print (w, len(w))

# range function

for i in range(5):
	print(i)

#range function variation

for i in range(5,10):
	print(i)

for i in range(5,15,2):
	print(i)

for i in range(len(words)):
	print(i, words[i])


## break statement in for loop
for i in range(1,100):
	if i % 2 == 0:
		print(i, "Is even number")
		break;

## continue statement in for loop
for i in range(1, 100):
	if i % 2 ==0:
		continue
	else:
		print(i)
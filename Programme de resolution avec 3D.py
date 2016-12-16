import random # Ajoute les fonctions qui utilisent l'aleatoire -> Pour le melange
import sys # Ajoute la fonction sleep() -> Pour mettre le programme est pause quelques secondes
from visual import * # Pour la 3D

moveNbr = 0 # Nombre de mouvements effecutes, utile pour les statistiques
fps = 24 # Pour le visuel, nombre d'images par seconde


# Fait le plan de la corespondance entre les faces et les vecteurs
faces = {'F': (color.red, (0, 0, 1)),
		 'B': (color.orange, (0, 0, -1)),
		 'U': (color.yellow, (0, 1, 0)),
		 'L': (color.blue, (-1, 0, 0)),
		 'D': (color.white, (0, -1, 0)),
		 'R': (color.green, (1, 0, 0))}

# Met les couleurs sur chaque petit cube, face par face.
stickers = []
for face_color, axis in faces.values():
	for x in (-1, 0, 1):
		for y in (-1, 0, 1):

			# Commence avec toutes autocollants vers le haut, puis on les tourne
			sticker = box(color=face_color, pos=(x, y, 1.5),
						  length=0.98, height=0.98, width=0.05)
			cos_angle = dot((0, 0, 1), axis)
			pivot = (cross((0, 0, 1), axis) if cos_angle == 0 else (1, 0, 0))
			sticker.rotate(angle=acos(cos_angle), axis=pivot, origin=(0, 0, 0))
			stickers.append(sticker)

# Rotation des parties du cube en 3 dimensions
def rotate3D(key):
	if key[0] in faces:
		face_color, axis = faces[key[0]]
		angle = ((pi / 2) if len(key)>1 else -pi / 2)
		for r in arange(0, angle, angle / fps):
			rate(fps)
			for sticker in stickers:
				if dot(sticker.pos, axis) > 0.5:
					sticker.rotate(angle=angle / fps, axis=axis,
								   origin=(0, 0, 0))
	elif key[0] == 'E':
		axis = (0, 0.5, 0)
		angle = ((pi / 2) if len(key)>1 else -pi / 2)
		for r in arange(0, angle, angle / fps):
			rate(fps)
			for sticker in stickers:
				sticker.rotate(angle=angle / fps, axis=axis,origin=(0, 0, 0))


# d = Down  = Bas   
# u = Up	= Haut  
# f = Face  = Face  
# b = Back  = Orange
# r = Right = Droite
# l = Left  = Gauche

# 'w' = White  = Blanc
# 'y' = Yellow = Jaune
# 'r' = Red	= Rouge
# 'o' = Orange = Orange
# 'g' = Green  = Vert
# 'b' = Blue   = Bleu

#Centres
d   = 'w' # Down = Bas
u   = 'y' # Up = Haut
f   = 'r' # Face = Face
b   = 'o' # Back = Orange
r   = 'g' # Right = Droite
l   = 'b' # Left = Gauche


# Aretes, le nom des variables defini leur position sur le cube
# Initiales faces = {'face' : 'couleur du cube '}
uf = {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': ''} 
ur = {'u': 'y', 'd': '', 'f': '', 'b': '', 'r': 'g', 'l': ''} 
ub = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': ''} 
ul = {'u': 'y', 'd': '', 'f': '', 'b': '', 'r': '', 'l': 'b'} 
df = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': '', 'l': ''} 
dr = {'u': '', 'd': 'w', 'f': '', 'b': '', 'r': 'g', 'l': ''} 
db = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': '', 'l': ''} 
dl = {'u': '', 'd': 'w', 'f': '', 'b': '', 'r': '', 'l': 'b'} 
fr = {'u': '', 'd': '', 'f': 'r', 'b': '', 'r': 'g', 'l': ''} 
fl = {'u': '', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} 
br = {'u': '', 'd': '', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} 
bl = {'u': '', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': 'b'} 
	 
ufr = {'u': 'y', 'd': '', 'f': 'r','b': '', 'r': 'g', 'l': ''} 
ufl = {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} 
ubr = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} 
ubl = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': 'b'} 
dfr = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': 'g', 'l': ''} 
dfl = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} 
dbr = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} 
dbl = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': '', 'l': 'b'}


# Fonction pour fait les mouvements
def move(face, show=1):


	global d, u, f, b, r, l, uf, ur, ub, ul, df, dr, db, dl, fr, fl, br, bl, ufr, ufl, ubr, ubl, dfr, dfl, dbr, dbl
	global moveNbr
	moveNbr += 1
	if show == 1:
		sys.stdout.write(face + ", ") # Affiche le mouvement suivi d'un virgule

	if face == "R": # Si le mouvement indique est R
		ufr['u'], ufr['f'], ufr['r'], ubr['u'], ubr['b'], ubr['r'], dbr['d'], dbr['b'], dbr['r'], dfr['d'], dfr['f'], dfr['r'],  = \
		dfr['f'], dfr['d'], dfr['r'], ufr['f'], ufr['u'], ufr['r'], ubr['b'], ubr['u'], ubr['r'], dbr['b'], dbr['d'], dbr['r']

		ur['u'], ur['r'], br['b'], br['r'], dr['d'], dr['r'], fr['f'], fr['r'],  = \
		fr['f'], fr['r'], ur['u'], ur['r'], br['b'], br['r'], dr['d'], dr['r'] #Aretes
		rotate3D("R")


	if face == "R'": # Si le mouvement indique est R'
		dfr['f'], dfr['d'], dfr['r'], ufr['f'], ufr['u'], ufr['r'], ubr['b'], ubr['u'], ubr['r'], dbr['b'], dbr['d'], dbr['r'], = \
		ufr['u'], ufr['f'], ufr['r'], ubr['u'], ubr['b'], ubr['r'], dbr['d'], dbr['b'], dbr['r'], dfr['d'], dfr['f'], dfr['r']
		
		ur['u'], ur['r'], fr['f'], fr['r'], dr['d'], dr['r'], br['b'], br['r'],  = \
		br['b'], br['r'], ur['u'], ur['r'], fr['f'], fr['r'], dr['d'], dr['r']
		rotate3D("R'")


	if face == "U": # Si le mouvement indique est U
		ufr['u'], ufr['f'], ufr['r'], ubr['u'], ubr['b'], ubr['r'], ubl['u'], ubl['b'], ubl['l'], ufl['u'], ufl['f'], ufl['l'],  = \
		ubr['u'], ubr['r'], ubr['b'], ubl['u'], ubl['l'], ubl['b'], ufl['u'], ufl['l'], ufl['f'], ufr['u'], ufr['r'], ufr['f']
		
		ur['u'], ur['r'], uf['u'], uf['f'], ul['u'], ul['l'], ub['u'], ub['b'],  = \
		ub['u'], ub['b'], ur['u'], ur['r'], uf['u'], uf['f'], ul['u'], ul['l']
		rotate3D("U")


	if face == "U'": # ...
		ubr['u'], ubr['r'], ubr['b'], ubl['u'], ubl['l'], ubl['b'], ufl['u'], ufl['l'], ufl['f'], ufr['u'], ufr['r'], ufr['f'],  = \
		ufr['u'], ufr['f'], ufr['r'], ubr['u'], ubr['b'], ubr['r'], ubl['u'], ubl['b'], ubl['l'], ufl['u'], ufl['f'], ufl['l']

		ur['u'], ur['r'], uf['u'], uf['f'], ul['u'], ul['l'], ub['u'], ub['b'],  = \
		uf['u'], uf['f'], ul['u'], ul['l'], ub['u'], ub['b'], ur['u'], ur['r']
		rotate3D("U'")


	if face == "D":
		dbr['d'], dbr['r'], dbr['b'], dbl['d'], dbl['l'], dbl['b'], dfl['d'], dfl['l'], dfl['f'], dfr['d'], dfr['r'], dfr['f'],  = \
		dfr['d'], dfr['f'], dfr['r'], dbr['d'], dbr['b'], dbr['r'], dbl['d'], dbl['b'], dbl['l'], dfl['d'], dfl['f'], dfl['l']

		dr['d'], dr['r'], df['d'], df['f'], dl['d'], dl['l'], db['d'], db['b'],  = \
		df['d'], df['f'], dl['d'], dl['l'], db['d'], db['b'], dr['d'], dr['r']
		rotate3D("D")


	if face == "D'":
		dfr['d'], dfr['f'], dfr['r'], dbr['d'], dbr['b'], dbr['r'], dbl['d'], dbl['b'], dbl['l'], dfl['d'], dfl['f'], dfl['l'],  = \
		dbr['d'], dbr['r'], dbr['b'], dbl['d'], dbl['l'], dbl['b'], dfl['d'], dfl['l'], dfl['f'], dfr['d'], dfr['r'], dfr['f']

		df['d'], df['f'], dr['d'], dr['r'], db['d'], db['b'], dl['d'], dl['l'],  = \
		dr['d'], dr['r'], db['d'], db['b'], dl['d'], dl['l'], df['d'], df['f']
		rotate3D("D'")


	if face == "L'":
		ufl['u'], ufl['f'], ufl['l'], ubl['u'], ubl['b'], ubl['l'], dbl['d'], dbl['b'], dbl['l'], dfl['d'], dfl['f'], dfl['l'],  = \
		dfl['f'], dfl['d'], dfl['l'], ufl['f'], ufl['u'], ufl['l'], ubl['b'], ubl['u'], ubl['l'], dbl['b'], dbl['d'], dbl['l']

		ul['u'], ul['l'], bl['b'], bl['l'], dl['d'], dl['l'], fl['f'], fl['l'],  = \
		fl['f'], fl['l'], ul['u'], ul['l'], bl['b'], bl['l'], dl['d'], dl['l'] #Aletes
		rotate3D("L'")


	if face == "L":
		dfl['f'], dfl['d'], dfl['l'], ufl['f'], ufl['u'], ufl['l'], ubl['b'], ubl['u'], ubl['l'], dbl['b'], dbl['d'], dbl['l'], = \
		ufl['u'], ufl['f'], ufl['l'], ubl['u'], ubl['b'], ubl['l'], dbl['d'], dbl['b'], dbl['l'], dfl['d'], dfl['f'], dfl['l']
		
		ul['u'], ul['l'], fl['f'], fl['l'], dl['d'], dl['l'], bl['b'], bl['l'],  = \
		bl['b'], bl['l'], ul['u'], ul['l'], fl['f'], fl['l'], dl['d'], dl['l']
		rotate3D("L")


	if face == "F": 
		ufr['u'], ufr['f'], ufr['r'], dfr['d'], dfr['f'], dfr['r'], dfl['d'], dfl['f'], dfl['l'], ufl['u'], ufl['f'], ufl['l'],  = \
		ufl['l'], ufl['f'], ufl['u'], ufr['r'], ufr['f'], ufr['u'], dfr['r'], dfr['f'], dfr['d'], dfl['l'], dfl['f'], dfl['d']
		
		uf['u'], uf['f'], fl['l'], fl['f'], df['d'], df['f'], fr['r'], fr['f'],  = \
		fl['l'], fl['f'], df['d'], df['f'], fr['r'], fr['f'], uf['u'], uf['f']
		rotate3D("F")


	if face == "F'":
		ufl['l'], ufl['f'], ufl['u'], ufr['r'], ufr['f'], ufr['u'], dfr['r'], dfr['f'], dfr['d'], dfl['l'], dfl['f'], dfl['d'],  = \
		ufr['u'], ufr['f'], ufr['r'], dfr['d'], dfr['f'], dfr['r'], dfl['d'], dfl['f'], dfl['l'], ufl['u'], ufl['f'], ufl['l']
		
		fl['l'], fl['f'], df['d'], df['f'], fr['r'], fr['f'], uf['u'], uf['f'],  = \
		uf['u'], uf['f'], fl['l'], fl['f'], df['d'], df['f'], fr['r'], fr['f']
		rotate3D("F'")


	if face == "B'":	
		ubr['u'], ubr['b'], ubr['r'], dbr['d'], dbr['b'], dbr['r'], dbl['d'], dbl['b'], dbl['l'], ubl['u'], ubl['b'], ubl['l'],  = \
		ubl['l'], ubl['b'], ubl['u'], ubr['r'], ubr['b'], ubr['u'], dbr['r'], dbr['b'], dbr['d'], dbl['l'], dbl['b'], dbl['d']
		
		ub['u'], ub['b'], bl['l'], bl['b'], db['d'], db['b'], br['r'], br['b'],  = \
		bl['l'], bl['b'], db['d'], db['b'], br['r'], br['b'], ub['u'], ub['b']
		rotate3D("B'")


	if face == "B":
		ubl['l'], ubl['b'], ubl['u'], ubr['r'], ubr['b'], ubr['u'], dbr['r'], dbr['b'], dbr['d'], dbl['l'], dbl['b'], dbl['d'],  = \
		ubr['u'], ubr['b'], ubr['r'], dbr['d'], dbr['b'], dbr['r'], dbl['d'], dbl['b'], dbl['l'], ubl['u'], ubl['b'], ubl['l']
		
		bl['l'], bl['b'], db['d'], db['b'], br['r'], br['b'], ub['u'], ub['b'],  = \
		ub['u'], ub['b'], bl['l'], bl['b'], db['d'], db['b'], br['r'], br['b']
		rotate3D("B")



def melanger(nbrDeMoves=25, show=1):

	moveList = ["R","R'","L","L'","U","U'","D","D'","F","F'","B","B'"]

	i=0
	for i in range(nbrDeMoves):
		aleatoire = random.randint(0,11)
		move(moveList[aleatoire], 0)
		if show == 1:
			sys.stdout.write(str(moveList[aleatoire]).upper()+ " ")
	if show == 1:
		print("\nCube melange !")



def printCube():
	print("\n\t" + ubl['u'] + ub['u'] + ubr['u'] + "\n\t" + \
				ul['u'] + u + ur['u'] + "\n\t" + \
				ufl['u'] + uf['u'] + ufr['u'] + "\n" + \

				ubl['l'] + ul['l'] + ufl['l'] + " "	 + ufl['f'] + uf['f'] + ufr['f'] + " "	   + ufr['r'] + ur['r'] + ubr['r'] + " "	   + ubr['b'] + ub['b'] + ubl['b'] + "\n" + \
				bl['l'] + l + fl['l'] + " "			 + fl['f'] + f + fr['f'] + " "			   + fr['r'] + r + br['r'] + " "			   + br['b'] + b + bl['b'] + " " + "\n" + \
				dbl['l'] + dl['l'] + dfl['l'] + " "	  + dfl['f'] + df['f'] + dfr['f'] + " "	  + dfr['r'] + dr['r'] + dbr['r'] + " "	   + dbr['b'] + db['b'] + dbl['b'] + "\n\t" + \

				dfl['d'] + df['d'] + dfr['d'] + "\n\t" + dl['d'] + d + dr['d'] + "\n\t" + dbl['d'] + db['d'] + dbr['d'] + "\n")

	print("=====================================")



def turnCube(show=1): #de droite a gauche
	global d, u, f, b, r, l

	# U
	ufr['u'], ufr['f'], ufr['r'], ubr['u'], ubr['b'], ubr['r'], ubl['u'], ubl['b'], ubl['l'], ufl['u'], ufl['f'], ufl['l'],  = \
	ubr['u'], ubr['r'], ubr['b'], ubl['u'], ubl['l'], ubl['b'], ufl['u'], ufl['l'], ufl['f'], ufr['u'], ufr['r'], ufr['f']
	
	ur['u'], ur['r'], uf['u'], uf['f'], ul['u'], ul['l'], ub['u'], ub['b'],  = \
	ub['u'], ub['b'], ur['u'], ur['r'], uf['u'], uf['f'], ul['u'], ul['l']

	# D'
	dfr['d'], dfr['f'], dfr['r'], dbr['d'], dbr['b'], dbr['r'], dbl['d'], dbl['b'], dbl['l'], dfl['d'], dfl['f'], dfl['l'],  = \
	dbr['d'], dbr['r'], dbr['b'], dbl['d'], dbl['l'], dbl['b'], dfl['d'], dfl['l'], dfl['f'], dfr['d'], dfr['r'], dfr['f']

	df['d'], df['f'], dr['d'], dr['r'], db['d'], db['b'], dl['d'], dl['l'],  = \
	dr['d'], dr['r'], db['d'], db['b'], dl['d'], dl['l'], df['d'], df['f']

	# E'
	fl['f'], fl['l'], fr['f'], fr['r'], br['b'], br['r'], bl['b'], bl['l']  = \
	fr['r'], fr['f'], br['r'], br['b'], bl['l'], bl['b'], fl['l'], fl['f']

	f, r, b, l = \
	r, b, l, f

	rotate3D("E")

	if show == 1:
		print("Tourne le cube")



def resetCube():

	#Centres
	d   = 'w' # Down
	u   = 'y' # Up
	f   = 'r' # Face
	b   = 'o' # Back
	r   = 'g' # Right
	l   = 'b' # Left
	
	#Aretes, le nom des variables defini leur position sur le cube
	#exp= {'face/direction' : 'couleur du cube '}
	uf = {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': ''} 
	ur = {'u': 'y', 'd': '', 'f': '', 'b': '', 'r': 'g', 'l': ''} 
	ub = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': ''} 
	ul = {'u': 'y', 'd': '', 'f': '', 'b': '', 'r': '', 'l': 'b'} 
	df = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': '', 'l': ''} 
	dr = {'u': '', 'd': 'w', 'f': '', 'b': '', 'r': 'g', 'l': ''} 
	db = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': '', 'l': ''} 
	dl = {'u': '', 'd': 'w', 'f': '', 'b': '', 'r': '', 'l': 'b'} 
	fr = {'u': '', 'd': '', 'f': 'r', 'b': '', 'r': 'g', 'l': ''} 
	fl = {'u': '', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} 
	br = {'u': '', 'd': '', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} 
	bl = {'u': '', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': 'b'} 
		 
	ufr = {'u': 'y', 'd': '', 'f': 'r','b': '', 'r': 'g', 'l': ''} 
	ufl = {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} 
	ubr = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} 
	ubl = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': 'b'} 
	dfr = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': 'g', 'l': ''} 
	dfl = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} 
	dbr = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} 
	dbl = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': '', 'l': 'b'}



def solveCroixBlanche(show=1):

	if show == 1:
		print("\nConstruction de la croix blanche :\n")
	global d, u, f, b, r, l, uf, ur, ub, ul, df, dr, db, dl, fr, fl, br, bl, ufr, ufl, ubr, ubl, dfr, dfl, dbr, dbl
	liste = ['r', 'g', 'o', 'b']

	for i in liste:
		if dr['d'] == 'w' and dr['r'] == i:
			move("R", show)
			move("R", show)
			move("U", show)
			move("F", show)
			move("F", show)

		elif db['d'] == 'w' and db['b'] == i:
			move("B", show)
			move("B", show)
			move("U", show)
			move("U", show)
			move("F", show)
			move("F", show)

		elif dl['d'] == 'w' and dl['l'] == i:
			move("L", show)
			move("L", show)
			move("U'", show)
			move("F", show)
			move("F", show)

		elif fr['f'] == 'w' and fr['r'] == i:
			move("R", show)
			move("U", show)
			move("R'", show)
			move("F", show)
			move("F", show)

		elif fl['f'] == 'w' and fl['l'] == i:
			move("L'", show)
			move("U'", show)
			move("L", show)
			move("F", show)
			move("F", show)

		elif br['b'] == 'w' and br['r'] == i:
			move("R'", show)
			move("U", show)
			move("R", show)
			move("F", show)
			move("F", show)

		elif bl['b'] == 'w' and bl['l'] == i:
			move("L", show)
			move("U'", show)
			move("L'", show)
			move("F", show)
			move("F", show)

		elif uf['u'] == 'w' and uf['f'] == i:
			move("F", show)
			move("F", show)

		elif ur['u'] == 'w' and ur['r'] == i:
			move("U", show)
			move("F", show)
			move("F", show)

		elif ul['u'] == 'w' and ul['l'] == i:
			move("U'", show)
			move("F", show)
			move("F", show)

		elif ub['u'] == 'w' and ub['b'] == i:
			move("U", show)
			move("U", show)
			move("F", show)
			move("F", show)

		elif dr['d'] == i and dr['r'] == 'w':
			move("R", show)
			move("F", show)

		elif db['d'] == i and db['b'] == 'w':
			move("B", show)
			move("D", show)
			move("R", show)
			move("D'", show)

		elif dl['d'] == i and dl['l'] == 'w':
			move("L'", show)
			move("F'", show)

		elif fr['f'] == i and fr['r'] == 'w':
			move("F", show)

		elif fl['f'] == i and fl['l'] == 'w':
			move("F'", show)

		elif br['b'] == i and br['r'] == 'w':
			move("B", show)
			move("U", show)
			move("U", show)
			move("B'", show)
			move("F", show)
			move("F", show)

		elif bl['b'] == i and bl['l'] == 'w':
			move("B'", show)
			move("U", show)
			move("U", show)
			move("B", show)
			move("F", show)
			move("F", show)

		elif uf['u'] == i and uf['f'] == 'w':
			move("U'", show)
			move("R'", show)
			move("F", show)
			move("R", show)

		elif ur['u'] == i and ur['r'] == 'w':
			move("R'", show)
			move("F", show)
			move("R", show)

		elif ul['u'] == i and ul['l'] == 'w':
			move("L", show)
			move("F'", show)
			move("L'", show)

		elif ub['u'] == i and ub['b'] == 'w':
			move("U", show)
			move("R'", show)
			move("F", show)
			move("R", show)

		elif df['d'] == i and df['f'] == 'w':
			move("F'", show)
			move("D", show)
			move("R'", show)
			move("D'", show)
		#fin
		turnCube(show)



def solveCoinsBlancs(show=1):

	if show == 1:
		print("\nMise en place des coins blancs :\n")
	global d, u, f, b, r, l, uf, ur, ub, ul, df, dr, db, dl, fr, fl, br, bl, ufr, ufl, ubr, ubl, dfr, dfl, dbr, dbl
	liste = ["wrg", "wgo", "wob", "wbr"]

	for j in liste:
		
		if ufl['u'] in j and ufl['f'] in j and ufl['l'] in j:
			move("U'", show)

		elif ubl['u'] in j and ubl['b'] in j and ubl['l'] in j:
			move("U'", show)
			move("U'", show)

		elif ubr['u'] in j and ubr['b'] in j and ubr['r'] in j:
			move("U", show)

		elif dfl['d'] in j and dfl['f'] in j and dfl['l'] in j:
			move("L'", show)
			move("U'", show)
			move("L", show)

		elif dbl['d'] in j and dbl['b'] in j and dbl['l'] in j:
			move("L", show)
			move("U", show)
			move("U", show)
			move("L'", show)

		elif dbr['d'] in j and dbr['b'] in j and dbr['r'] in j:
			move("R'", show)
			move("U", show)
			move("R", show)
			move("U", show)


		if dfr['r'] == 'w' and dfr['d'] in j and dfr['f'] in j:
			move("R", show)
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("R", show)
			move("U", show)
			move("R'", show)

		if dfr['f'] == 'w' and dfr['d'] in j and dfr['r'] in j:
			move("F'", show)
			move("U'", show)
			move("F", show)
			move("U", show)
			move("F'", show)
			move("U'", show)
			move("F", show)

		if ufr['u'] == 'w' and ufr['f'] in j and ufr['r'] in j: 
			move("R", show)
			move("U", show)
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("R", show)
			move("U", show)
			move("R'", show)

		if ufr['f'] == 'w' and ufr['u'] in j and ufr['r'] in j:
			move("U", show)
			move("R", show)
			move("U'", show)
			move("R'", show)

		if ufr['r'] == 'w'and ufr['u'] in j and ufr['f'] in j:
			move("R", show)
			move("U", show)
			move("R'", show)
		
		turnCube(show)

def isFinish():

	global d , u, f, b, r, l, uf, ur, ub, ul, df, dr, db, dl, fr, fl, br, bl , ufr, ufl, ubr, ubl, dfr, dfl, dbr, dbl
	
	if d  == 'w' and \
	u  == 'y' and \
	f  == 'r' and \
	b  == 'o' and \
	r  == 'g' and \
	l  == 'b' and \
	uf == {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': ''} and \
	ur == {'u': 'y', 'd': '', 'f': '', 'b': '', 'r': 'g', 'l': ''} and \
	ub == {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': ''} and \
	ul == {'u': 'y', 'd': '', 'f': '', 'b': '', 'r': '', 'l': 'b'} and \
	df == {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': '', 'l': ''} and \
	dr == {'u': '', 'd': 'w', 'f': '', 'b': '', 'r': 'g', 'l': ''} and \
	db == {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': '', 'l': ''} and \
	dl == {'u': '', 'd': 'w', 'f': '', 'b': '', 'r': '', 'l': 'b'} and \
	fr == {'u': '', 'd': '', 'f': 'r', 'b': '', 'r': 'g', 'l': ''} and \
	fl == {'u': '', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} and \
	br == {'u': '', 'd': '', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} and \
	bl == {'u': '', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': 'b'} and \
	ufr == {'u': 'y', 'd': '', 'f': 'r','b': '', 'r': 'g', 'l': ''} and \
	ufl == {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} and \
	ubr == {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} and \
	ubl == {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': 'b'} and \
	dfr == {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': 'g', 'l': ''} and \
	dfl == {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} and \
	dbr == {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} and \
	dbl == {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': '', 'l': 'b'}:

		return 1
	else : return 0



def solve2ndCouronne(show=1): # Resout la seconde couronne

	if show == 1:
		print("\nConstruction de la seconde couronne :\n")
	global uf, ur, ub, ul, df, dr, db, dl, fr, fl, br, bl
	liste = ['rg', 'go', 'ob', 'br'] # Couleurs des aretes par binome, chaque lettre represente une couleur, 'rg' veut dire rouge-vert par exemple

	for i in liste: # Cette ligne annonce une boucle, elle signifie "pour chaque element "i" dans la liste "liste"

		if fl['f'] in i and fl['l'] in i:
			move("F", show)
			move("U", show)
			move("F'", show)
			move("U'", show)
			move("L'", show)
			move("U'", show)
			move("L", show)

		if br['b'] in i and br['r'] in i:
			turnCube(show)
			turnCube(show)
			move("F", show)
			move("U", show)
			move("F'", show)
			move("U'", show)
			move("L'", show)
			move("U'", show)
			move("L", show)
			turnCube(show)
			turnCube(show)

		if bl['b'] in i and bl['l'] in i:
			turnCube(show)
			turnCube(show)
			turnCube(show)
			move("F", show)
			move("U", show)
			move("F'", show)
			move("U'", show)
			move("L'", show)
			move("U'", show)
			move("L", show)
			turnCube(show)

		if fr['r'] is i[0] and fr['f'] in i:
			move("R", show)
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("U'", show)
			move("R", show)
			move("U'", show)
			move("U'", show)
			move("R'", show)
			move("U", show)
			move("F'", show)
			move("U'", show)
			move("F", show)

		if uf['f'] is i[0] and uf['u'] in i:
			move("U", show)
			move("R", show)
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("F'", show)
			move("U'", show)
			move("F", show)

		if uf['u'] is i[0] and uf['f'] in i:
			move("U'", show)
			move("R'", show)
			move("U'", show)
			move("R'", show)
			move("U'", show)
			move("R'", show)
			move("U", show)
			move("R", show)
			move("U", show)
			move("R", show)

		if ur['u'] is i[0] and ur['r'] in i:
			move("R'", show)
			move("U'", show)
			move("R'", show)
			move("U'", show)
			move("R'", show)
			move("U", show)
			move("R", show)
			move("U", show)
			move("R", show)

		if ur['r'] is i[0] and ur['u'] in i:
			move("U", show)
			move("U", show)
			move("R", show)
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("F'", show)
			move("U'", show)
			move("F", show)

		if ub['b'] is i[0] and ub['u'] in i:
			move("U'", show)
			move("R", show)
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("F'", show)
			move("U'", show)
			move("F", show)

		if ub['u'] is i[0] and ub['b'] in i:
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("R'", show)
			move("U'", show)
			move("R'", show)
			move("U", show)
			move("R", show)
			move("U", show)
			move("R", show)

		if ul['l'] is i[0] and ul['u'] in i:
			move("R", show)
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("F'", show)
			move("U'", show)
			move("F", show)

		if ul['u'] is i[0] and ul['l'] in i:
			move("U", show)
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("R'", show)
			move("U'", show)
			move("R'", show)
			move("U", show)
			move("R", show)
			move("U", show)
			move("R", show)

		if fr['f'] is i[0] and fr['r'] in i and show == 1:
			print("Arete bien mise !")

		turnCube(show)



def solveCroixJaune(show=1):
	if show == 1:
		print("\nConstruction de la croix jaune :\n")

	global uf, ur, ub, ul

	if uf['u'] != 'y' and ur['u'] != 'y' and ub['u'] != 'y' and ul['u'] != 'y': # Si point jaune alors :
		move("R'", show)
		move("U'", show)
		move("F'", show)
		move("U", show)
		move("F", show)
		move("R", show)

	if uf['u'] != 'y' and  ub['u'] != 'y' and ur['u'] == 'y' and ul['u'] == 'y': # Si ligne jaune bien mise :
		move("R'", show)
		move("U'", show)
		move("F'", show)
		move("U", show)
		move("F", show)
		move("R", show)

	if ur['u'] != 'y' and  ul['u'] != 'y' and uf['u'] == 'y' and ub['u'] == 'y': # Si ligne jaune mais mal mise :
		move("U", show)  # Simple rotation de la face du dessus pour bien mettre la ligne jaune
		move("R'", show)
		move("U'", show)
		move("F'", show)
		move("U", show)
		move("F", show)
		move("R", show)

	if uf['u'] != 'y' and ur['u'] != 'y' and ub['u'] == 'y' and ul['u'] == 'y': # Si "L" jaune bien mis :
		move("R'", show)
		move("U'", show)
		move("F'", show)
		move("U", show)
		move("F", show)
		move("R", show)

	if uf['u'] != 'y' and ur['u'] == 'y' and ub['u'] == 'y' and ul['u'] != 'y': # Si "L" jaune mal mis :
		move("U'", show) # Simple rotation de la face du dessus pour bien mettre le "L" jaune
		move("R'", show)
		move("U'", show)
		move("F'", show)
		move("U", show)
		move("F", show)
		move("R", show)

	if uf['u'] == 'y' and ur['u'] == 'y' and ub['u'] != 'y' and ul['u'] != 'y': # Si "L" jaune mal mis :
		move("U", show)	# Simple rotation de la face du dessus pour bien mettre le "L" jaune
		move("U", show)	# Simple rotation de la face du dessus pour bien mettre le "L" jaune
		move("R'", show)
		move("U'", show)
		move("F'", show)
		move("U", show)
		move("F", show)
		move("R", show)

	if uf['u'] == 'y' and ur['u'] != 'y' and ub['u'] != 'y' and ul['u'] == 'y': # Si "L" jaune mal mis :
		move("U", show)	# Simple rotation de la face du dessus pour bien mettre le "L" jaune
		move("R'", show)
		move("U'", show)
		move("F'", show)
		move("U", show)
		move("F", show)
		move("R", show)

	# Croix construite

	#Mise en place des couleurs :
	loop = 1 # Variable qui determine si oui (0) ou non (1) les couleurs sont a leur places
	while loop: # Boucle "tant que loop est égal a 1"
			if uf['f'] == 'r' and ur['r'] == 'g':
				move("U", show)
				move("U", show)

			elif ul['l'] == 'r' and uf['f'] == 'g':
				move("U", show)

			elif ur['r'] == 'r' and ub['b'] == 'g':
				move("U'", show)

			if uf['f'] == 'g' and ur['r'] == 'o':
				move("U", show)
				move("U", show)

			elif ul['l'] == 'g' and uf['f'] == 'o':
				move("U", show)

			elif ur['r'] == 'g' and ub['b'] == 'o':
				move("U'", show)

			if uf['f'] == 'o' and ur['r'] == 'b':
				move("U", show)
				move("U", show)

			elif ul['l'] == 'o' and uf['f'] == 'b':
				move("U", show)

			elif ur['r'] == 'o' and ub['b'] == 'b':
				move("U'", show)

			if uf['f'] == 'b' and ur['r'] == 'r':
				move("U", show)
				move("U", show)

			elif ul['l'] == 'b' and uf['f'] == 'r':
				move("U", show)

			elif ur['r'] == 'b' and ub['b'] == 'r':
				move("U'", show)

			# Algorithme
			move("U", show)
			move("R", show)
			move("U", show)
			move("R'", show)
			move("U", show)
			move("R", show)
			move("U", show)
			move("U", show)
			move("R'", show)

			#Teste le cube si les couleurs peuvent etre placees avec seulement des mouvements "U"
			if ul['l'] == 'r' and uf['f'] == 'g' and ur['r'] == 'o' and ub['b'] == 'b':
				move("U'", show)
			if ul['l'] == 'o' and uf['f'] == 'b' and ur['r'] == 'r' and ub['b'] == 'g':
				move("U", show)
			if ul['l'] == 'g' and uf['f'] == 'o' and ur['r'] == 'b' and ub['b'] == 'r':
				move("U", show)
				move("U", show)
			if ul['l'] == 'b' and uf['f'] == 'r' and ur['r'] == 'g' and ub['b'] == 'o':
				loop = 0 # Si la croix et les couleurs sont biens mises alors le programme sort de la fonction



def solveFinal(show=1):
	if show == 1:
		print("\nMise en place des coins jaune :\n")

	while 1: # Boucle

		if  ('r' in ufr.values() and 'g' in ufr.values()) and \
			('b' in ufl.values() and 'r' in ufl.values()) and \
			('g' in ubr.values() and 'o' in ubr.values()) and \
			('b' in ubl.values() and 'o' in ubl.values()):
				break # break permet de sortir de la boucle

		if 'g' in ubr.values() and 'o' in ubr.values(): # Si g (vert) et o (orange) sont contenus dans les valeurs de ubr (up-back-right) alors :
			move("U", show)
			move("U", show)
			move("R", show)
			move("U'", show)
			move("L'", show)
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("L", show)
			move("U'", show)

		elif 'r' in ufr.values() and 'g' in ufr.values():
			move("U", show)
			move("R", show)
			move("U'", show)
			move("L'", show)
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("L", show)

		elif 'b' in ubl.values() and 'o' in ubl.values():
			move("U'", show)
			move("R", show)
			move("U'", show)
			move("L'", show)
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("L", show)
			move("U", show)
			move("U", show)

		elif 'b' in ufl.values() and 'r' in ufl.values():
			move("R", show)
			move("U'", show)
			move("L'", show)
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("L", show)
			move("U", show)

		else: # Si aucun cubie n'est bien place : / Sinon :
			move("U", show)
			move("R", show)
			move("U'", show)
			move("L'", show)
			move("U", show)
			move("R'", show)
			move("U'", show)
			move("L", show)

	while 1:
		if ufr['u'] == 'y': # Si la couleur jaune du cubie est sur le dessus du cube alors :
			if isFinish(): # Si le cube est resolu alors :
				break # break permet de sortir de la boucle

			move("U'", show) # Passe au cubie suivant

		if ufr['r'] == 'y': # Si la couleur jaune du cubie est sur la droite du cube alors :
			move("R'", show)
			move("D'", show)
			move("R", show)
			move("D", show)

			move("R'", show)
			move("D'", show)
			move("R", show)
			move("D", show)

		if ufr['f'] == 'y': # Si la couleur jaune du cubie est sur le devant du cube alors :
			move("R'", show)
			move("D'", show)
			move("R", show)
			move("D", show)

			move("R'", show)
			move("D'", show)
			move("R", show)
			move("D", show)

			move("R'", show)
			move("D'", show)
			move("R", show)
			move("D", show)

			move("R'", show)
			move("D'", show)
			move("R", show)
			move("D", show)


##### Melange du cube #####
print("Melange du cube :\n")
melanger() # Melange le cube
printCube() # Affiche le cube
print("Melange du cube termine !\n")
sleep(3) # Pause de 3 secondes


##### Resolution #####

if isFinish(): # Si le cube est resolu :
	print("Fini en " + str(moveNbr) + " mouvements !")
	quit()

solveCroixBlanche() # Resolution de la croix blanche

if isFinish(): # Si le cube est resolu :
	print("Fini en " + str(moveNbr) + " mouvements !")
	quit()

solveCoinsBlancs() # Resolution des coins blancs

printCube() # Affiche le cube

if isFinish(): # Si le cube est resolu :
	print("Fini en"  + str(moveNbr) + " mouvements !")
	quit()

solve2ndCouronne() # Resolution de la deuxieme ligne

printCube() # Affiche le cube

if isFinish(): # Si le cube est resolu :
	print("Fini en " + str(moveNbr) + " mouvements !")
	quit()

solveCroixJaune() # Resolution de la croix jaune

printCube() # Affiche le cube

if isFinish(): # Si le cube est resolu :
	print("Fini en " + str(moveNbr) + " mouvements !")
	quit()

solveFinal() # Resolution des coins de la face jaune

printCube() # Affiche le cube

if isFinish(): # Si le cube est resolu :
	print("Fini en " + str(moveNbr) + " mouvements !")
	quit()

printCube() # En cas de probleme on affiche le cube



### Tests Statistiques ###
#nope = 0
#moveNbrStat = []
#y = 10000
#for x in range(y):
#	resetCube()
#	moveNbr=0
#	melanger(25, 0)
#	solveCroixBlanche(0)
#	solveCoinsBlancs(0)
#	solve2ndCouronne(0)
#	solveCroixJaune(0)
#	solveFinal(0)
#	if not isFinish():
#		print "erreur"
#	moveNbrStat.append(moveNbr)
#	#printCube()
#print(str(y) + " cubes resolus avec " + str(sum(moveNbrStat)/len(moveNbrStat)) + " mouvements en moyenne ")

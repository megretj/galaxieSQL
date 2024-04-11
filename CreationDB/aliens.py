import pickle
import random
# from PIL import Image
import xml.etree.ElementTree as ET

palette = {"bleu":(0,0,255), "gris":(100,100,100), "noir":(0,0,0),"violet":(128, 0, 255),
           "rouge":(255,0,0),"blanc":(255,255,255),"vert":(0,255,0),"arc-en-ciel":(204, 255, 255),"jaune":(255,255,0),
           "rose":(255, 0, 255),"orange":(255,150,0),"marron":(150,100,50)}


def createPizza(ingrédients):
    nombreIngrédients = random.randint(1,5)
    ingrédients_choisis = random.sample(ingrédients,nombreIngrédients)
    recette = "Pizza"
    if nombreIngrédients == 1:
        return recette + " " + ingrédients_choisis[0]
    for ing in ingrédients_choisis[:-1]:
        recette += " " + ing +","
    return recette + " et " + ingrédients_choisis[-1] + "."

def erkundePizza(ingrédients):
    nombreIngrédients = random.randrange(1,5)
    ingrédients_choisis = random.sample(ingrédients,nombreIngrédients)
    recette = "Pizza mit"
    if nombreIngrédients == 1:
        return recette + " " + ingrédients_choisis[0]
    for ing in ingrédients_choisis[:-1]:
        recette += " " + ing +","
    return recette + " und " + ingrédients_choisis[-1] + "."



def generate_alien():
    with open('attributs_aliens.pkl', 'rb') as f:
        attributs = pickle.load(f)
    planète = random.choice(attributs["planète"])
    nombre_membres = random.randrange(0,10)
    taille = random.randrange(0,10000)
    nombre_yeux = random.randrange(0,10)
    n = random.randrange(0,len(list(attributs["couleurs"].keys())))
    couleur_yeux = list(attributs["couleurs"].keys())[n]
    farbe_Augen = list(attributs["farben"].keys())[n]
    n = random.randrange(0,len(list(attributs["peau"])))                  
    peau = attributs["peau"][n]
    Haut = attributs["Haut"][n]
    n = random.randrange(0,len(list(attributs["couleurs"].keys())))
    couleur_peau = list(attributs["couleurs"].keys())[n]
    farbe_Haut = list(attributs["farben"].keys())[n]
    antennes = random.randrange(0,1)
    n = random.randrange(0,len(list(attributs["visage"])))
    visage = attributs["visage"][n]
    Gesicht = attributs["Gesicht"][n]
    n = random.randrange(0,len(list(attributs["tête"])))
    tête = attributs["tête"][n]
    Kopf = attributs["Kopf"][n]
    pizza = createPizza(attributs["ingrédients"])
    Pizza = erkundePizza(attributs["Zutaten"])
    nom = random.choice(attributs["nom"])+"_"+str(nombre_membres)+str(int(taille/1000))+str(nombre_yeux)+str(antennes)
    return [nom,planète,nombre_membres,taille, nombre_yeux, couleur_yeux, peau, couleur_peau, antennes, visage, tête, pizza],[nom,planète,nombre_membres,taille,nombre_yeux,farbe_Augen,Haut,farbe_Haut,antennes,Gesicht, Kopf, Pizza]

def change_colour(input_image,old_colour, new_colour):
    d = input_image.getdata()
    new_image = []
    if old_colour == 'green':
        for item in d:
            if item[0]<item[1] and item[2]<item[1]:
                new_image.append(new_colour+(item[3],))
            else:
                new_image.append(item)
    else:
        for item in d:
            if item[0:3] == old_colour:
                new_image.append(new_colour+(item[3],))
            else:
                new_image.append(item)
    # update image data
    input_image.putdata(new_image)
    return input_image

def draw_alien(nombre_membres=None, nombre_yeux = None, couleur_yeux = 'noirs', peau = None, couleur_peau = None, nombre_antennes = None, visage=None, tete=None, save=False, filename="alien.png"):
    # Aller chercher les attributs disponibles
    with open('attributs_aliens.pkl', 'rb') as f:
        attributs = pickle.load(f)
    tete = change_colour(Image.open(f"images/tete_{tete if tete is not None else random.choice(attributs['tête'])}.png"),'green',attributs['couleurs'][couleur_peau if couleur_peau is not None else random.choice(list(attributs['couleurs'].keys()))])
    corps = change_colour(Image.open("images/corps.png"),'green',attributs['couleurs'][couleur_peau if couleur_peau is not None else random.choice(list(attributs['couleurs'].keys()))])
    visage = change_colour(Image.open(f"images/visage_{visage if visage is not None else random.choice(list(attributs['visage']))}.png"),(0,0,0),attributs['couleurs'][couleur_peau if couleur_peau is not None else random.choice(list(attributs['couleurs'].keys()))])
    yeux = change_colour(Image.open(f"images/yeux_{nombre_yeux if nombre_yeux is not None else random.randint(1,3)}.png"),(0,0,0),attributs['couleurs'][couleur_yeux])
    antennes = change_colour(Image.open(f"images/antennes_{nombre_antennes if nombre_antennes<3 and nombre_antennes>=0 else random.randint(1,2)}.png"),(0,0,0),random.choice(list(palette.values())))
    membres = change_colour(Image.open(f"images/membres_{random.randint(1,3)}.png"),(0,0,0),random.choice(list(palette.values())))
    new_img = Image.alpha_composite(membres,Image.alpha_composite(antennes,Image.alpha_composite(corps,Image.alpha_composite(tete, Image.alpha_composite(yeux, visage)))))
    new_img = new_img.convert('RGB')
    if save:
        new_img.save(f"images/{filename}","PNG")
    return new_img.convert('RGB')

def merge_svg_files(svg_file1, svg_file2):
    # Parse the first SVG file
    tree1 = ET.parse(svg_file1)
    root1 = tree1.getroot()

    # Parse the second SVG files
    tree2 = ET.parse(svg_file2)
    root2 = tree2.getroot()

    # Find the <g> element in the second SVG file
    g_elements = root2.findall(".//{http://www.w3.org/2000/svg}g")

    # Append <g> elements from the second SVG file to the first SVG file
    for g_element in g_elements:
        root1.append(g_element)
    with open("images/temp/output.svg", "wb") as f:
        f.write(ET.tostring(root1, encoding='utf-8'))
    return "images/temp/output.svg"

def draw_alien_svg(nombre_membres=None, nombre_yeux = None, couleur_yeux = None, peau = None, couleur_peau = None, nombre_antennes = None, visage=None, tete=None, save=False, filename="images/exemples/alien.svg"):
    with open('attributs_aliens.pkl', 'rb') as f:
        attributs = pickle.load(f)
    couleur_peau = couleur_peau if couleur_peau is not None else random.choice(list(attributs['couleurs'].keys()))
    with open(f"images/tete_{tete if tete is not None else random.choice(attributs['tête'])}.svg", 'r') as f:
        tete_data = f.read()
    tete_data = tete_data.replace("#66b32e",attributs['couleurs'][couleur_peau])
    with open("images/temp/tete.svg", "wb") as f:
        f.write(tete_data.encode())
    with open(f"images/corps.svg", 'r') as f:
        corps_data = f.read()
    corps_data = corps_data.replace("#66b32e",attributs['couleurs'][couleur_peau])
    with open("images/temp/corps.svg", "wb") as f:
        f.write(corps_data.encode())
    with open(f"images/visage_{visage if visage is not None else random.choice(attributs['visage'])}.svg", 'r') as f:
        visage_data = f.read()
    visage_data = visage_data.replace("#66b32e",attributs['couleurs'][couleur_peau])
    with open("images/temp/visage.svg", "wb") as f:
        f.write(visage_data.encode())
    with open(f"images/yeux_{nombre_yeux if nombre_yeux is not None else random.randint(1,3)}.svg", 'r') as f:
        yeux_data = f.read()
    yeux_data = yeux_data.replace("#1d1d1b",attributs['couleurs'][couleur_yeux if couleur_yeux is not None else random.choice(list(attributs['couleurs'].keys()))])
    with open("images/temp/yeux.svg", "wb") as f:
        f.write(yeux_data.encode())
    with open(f"images/antennes_{nombre_antennes if nombre_antennes is not None else random.randint(1,3)}.svg", 'r') as f:
        antennes_data = f.read()
    antennes_data = antennes_data.replace("#1d1d1b",random.choice(list(attributs['couleurs'].values())))
    with open("images/temp/antennes.svg", "wb") as f:
        f.write(antennes_data.encode())
    with open(f"images/membres_{nombre_membres if nombre_membres is not None else random.choice([2,4,6])}.svg", 'r') as f:
        membres_data = f.read()
    with open("images/temp/membres.svg", "wb") as f:
        f.write(membres_data.encode())
    with open(f"images/peau_{peau if peau is not None else random.choice(attributs['peau'])}.svg", 'r') as f:
        peau_data = f.read()
    with open("images/temp/peau.svg", "wb") as f:
        f.write(peau_data.encode())
    new_img = merge_svg_files("images/temp/membres.svg",merge_svg_files("images/temp/antennes.svg",merge_svg_files("images/temp/tete.svg",merge_svg_files("images/temp/corps.svg", merge_svg_files("images/temp/yeux.svg", merge_svg_files("images/temp/peau.svg","images/temp/visage.svg"))))))
    with open(new_img, 'r') as f:
            svg_data = f.read()
    if save:
        with open(f"{filename}", 'wb') as f:
            f.write(svg_data.encode())
    return svg_data
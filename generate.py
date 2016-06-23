def pathExists(paths, r1, r2):
    for p in paths:
        p0=p[0]
        p1=p[1]
        if p0 == r1 and p1 == r2:
            return True
        if p0 == r2 and p1 == r1:
            return True
    return False
	
def saveToFile(filename, content):
    text_file = open(filename, "w")
    text_file.write(content)
    text_file.close()
	
def settings_ger():
    dungeon={"name": ["Kerker", "Festung", "Verlies", "Bastille", "Turm", "Zwingburg"],
             "suffix": ["des Schreckens", "der Verdammnis", "der Dunkelheit",  "der Schatten", "des Wahnsinns", "der Verzweiflung", "des Todes"],
             "cellcolor":"lightgrey",
             "cellshape": "box",
             "rooms": ["Waffenkammer", "Wachraum", "Zelle", "Kreuzung", "Leerer Raum", "Baracke", "Trainingsraum", "Schrein", "Lagerraum", "Bibliothek", "Folterkammer", "Arena", "Gallerie", "Wohnraum", "Schlafzimmer", "Schmiede"],
             "paths": ["Korridor","Tür", "Eisenbeschlagene Tür", "Aufzug", "Treppe", "Leiter","Geheimgang"]
             }
    
    wilderness={"name": ["Wald", "Hain", "Wildnis"],
             "suffix": ["des Schreckens", "der Verdammnis", "der Dunkelheit",  "der Schatten", "der Einsamkeit", "der Verzweiflung", "der Riesen", "der Trolle"],
             "cellcolor":"green",
             "cellshape": "ellipse",
             "rooms": ["Menhir", "Lichtung", "Dickicht", "Bach", "Fluss", "Furt", "Hügelgrab", "Niederung", "Sumpf", "Irrgarten", "Schlucht", "Teich", "See", "Staudamm", "Alte Ruinen", "Monument"],
             "paths": ["Pfad","Hohlweg", "Treppe", "Feldweg", "Brücke", "Verborgener Pfad"]
             }
    
    cavern={"name": ["Höhle", "Kaverne", "Labyrinth"],
             "suffix": ["des Schreckens", "der Verdammnis", "der Dunkelheit",  "der Schatten", "der Einsamkeit", "der Verzweiflung", "der Riesen", "der Trolle", "der Untoten"],
             "cellcolor":"burlywood",
             "cellshape": "trapezium",
             "rooms": ["Pilzwald", "Einsturz", "Klamm", "Tropfsteinhöhle", "Mine", "Unterirdischer Fluss", "Unterirdischer See", "Lavastrom", "Säulengarten", "Abgrund"],
             "paths": ["Pfad","Tunnel", "Durchgang", "Brücke", "Schacht", "Höhle", "Kamin"]
             }
    catacomb={"name": ["Katakomben", "Grab", "Ruhestätte"],
             "suffix": ["des Schreckens", "der Verdammnis", "der Dunkelheit",  "der Schatten", "der Einsamkeit", "der Verzweiflung", "der Riesen", "der Trolle", "der Untoten"],
             "cellcolor":"gray",
             "cellshape": "octagon",
             "rooms": ["Krypta", "Schrein", "Grabmal", "Statue", "Sarkophag", "Arkanes Portal", "Falsches Grab" ],
             "paths": ["Korridor","Gang", "Tunnel", "Durchgang", "Brücke", "Torbogen", "Geheimgang"]
             }      
             
    settings=[dungeon, wilderness, cavern,catacomb]
    return settings
    
def settings_eng():
    dungeon={"name": ["Dungeon", "Fortress", "Prison", "Bastille", "Tower", "Keep"],
             "suffix": ["of Fear", "of Doom", "of Darkness",  "of Shadows", "of Madness", "of Despair", "of Death"],
             "cellcolor":"lightgrey",
             "cellshape": "box",
             "rooms": ["Armoury", "Watchroom", "Cell", "Crossing", "Empty Room", "Baracks", "Training Room", "Shrine", "Storage", "Library", "Torture Room", "Arena", "Gallery", "Living Room", "Bedchamber", "Smithy"],
             "paths": ["Corridor","Door", "Iron-wrought Door", "Elevator", "Stairs", "Ladder","Secret Passage"]
             }
    
    wilderness={"name": ["Forest", "Copse", "Wilderness"],
            "suffix": ["of Fear", "of Doom", "of Darkness",  "of Shadows", "of Madness", "of Despair", "of Death", "of Solitude", "of the Giants", "of the Trolls"],                        
             "cellcolor":"green",
             "cellshape": "ellipse",
             "rooms": ["Menhir", "Glade", "Thicket", "Brook", "River", "Ford", "Cairn", "Hollow", "Swamp", "Labyrinth", "Ravine", "Pond", "Lake", "Dam", "Old Ruins", "Monument"],
             "paths": ["Path","Gully", "Stairs", "Track", "Bridge", "Hidden Path"]
             }
    
    cavern={"name": ["Cave", "Cavern", "Labyrinth"],
             "suffix": ["of Fear", "of Doom", "of Darkness",  "of Shadows", "of Madness", "of Despair", "of Death", "of Solitude", "of the Giants", "of the Trolls"],                        
             "cellcolor":"burlywood",
             "cellshape": "trapezium",
             "rooms": ["Fungal forest", "Cave-In", "Gorge", "Flowstone Cave", "Mine", "Underground River", "Underground Lake", "Lava flow", "Pillars", "Chasm"],
             "paths": ["Path","Tunnel", "Passage", "Bridge", "Chute", "Cave", "Chimney"]
             }
    catacomb={"name": ["Catacombs", "Grave", "Sepulcher"],
             "suffix": ["of Fear", "of Doom", "of Darkness",  "of Shadows", "of Madness", "of Despair", "of Death", "of Solitude", "of the Giants", "of the Trolls", "of the Undead", "of Ghosts"],                        
             "cellcolor":"gray",
             "cellshape": "octagon",
             "rooms": ["Crypt", "Shrine", "Tomb", "Statue", "Sarcophagus", "Arcane Portal", "False Grave" ],
             "paths": ["Corridor","Hallway", "Tunnel", "Passage", "Bridge", "Portcullis", "Secret Passage"]
             }      
             
    settings=[dungeon, wilderness, cavern,catacomb]
    return settings    
        
	
def generate(nexus, levels,maxrooms):
    #Render the generated graphs with:
    #http://www.webgraphviz.com/
    
    from random import randint
    from random import choice
    from random import uniform
       
   
    # SETUP DATA STRUCTURES
    entries=[]
    allrooms=[]
    metapaths=[]
    allpaths=[]
    settings=settings_eng()
    lines=[]
    lines.append("")
    lines.append("graph G{")
    #GENERATE <levels> SUB-LEVELS
    for s in range(0, levels):
     currentSetting= choice(settings)
     numrooms= randint(4,min(len(currentSetting["rooms"]),maxrooms))
     rooms=[]
     paths=[]
     
     #Choose <numrooms> unique room descriptions from list
     while len(rooms) < numrooms:
       newroom=choice(currentSetting["rooms"])
       if(newroom not in rooms):
          rooms.append(newroom)
          allrooms.append(str("["+str(s)+"] "+newroom))
     
     #connect each room to exactly one other random room
     for r1 in rooms:
       r2=choice(rooms)
       tries=0
       while tries <100 and r2==r1 or pathExists(paths, r1, r2):         
         r2 = choice(rooms)         
         tries=tries+1
       paths.append([r1,r2, choice(currentSetting["paths"])])
     #Add a few other connections
     prob_path=0.03
     for r1 in rooms:
       for r2 in rooms:
         if(r1 != r2 and uniform(0,1) < prob_path and not pathExists(paths, r1, r2)):                           
             paths.append([r1,r2 , choice(currentSetting["paths"])])
             allpaths.append(paths[len(paths)-1])
     #Select a random entry point
     entries.append(str("["+str(s)+"] "+choice(rooms)))
     
   
     lines.append( "subgraph cluster_"+str(s)+"{")
     lines.append( "color ="+currentSetting["cellcolor"]+";")
     lines.append( "node [style=filled,color="+currentSetting["cellcolor"]+",shape="+currentSetting["cellshape"]+"];")
     for p in paths:
        lines.append( "\"["+str(s)+"] "+p[0]+"\" -- "+ "\"["+str(s)+"] "+p[1]+"\"" + " [ label = \""+p[2]+"\" ];")
     lines.append( "label = \""+choice(currentSetting["name"])+" "+ choice(currentSetting["suffix"])+ "\";")
     lines.append( "}")
    			   
    
    #Create paths between levels
    for r1 in allrooms:
       for r2 in allrooms:
         if(r1 != r2 and uniform(0,1) < 0.01 and not pathExists(allpaths, r1, r2)):   
             if(r1[1] != r2[1]):
               metapaths.append( [r1, r2] )     
    for p in entries:
         lines.append("\""+ nexus+ "\" -- \""+ p+"\"" + " [ style=dotted];")
    for p in metapaths:    
         lines.append( "\""+ p[0] +"\" -- \""+ p[1] +"\"" + " [ style=dotted];"   ) 
    lines.append( "\"" + nexus +"\"  [shape=tripleoctagon];")         
    lines.append("}")
    lines.append( "\"" + nexus +"\"  [shape=tripleoctagon];")  
    Dot='\n'.join(lines)  
    print (Dot)
	#Save to file
	#saveToFile('output.txt', Dot)
    	
generate("Nexus", 4,10 )
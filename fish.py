class Fish:
    def __init__(self,name,size,family,origin):
      self.name = name
      self.size = size
      self.family = family
      self.origin = origin
      
fishlist = [Fish("tiger barb",3.5,"cyprinidae","asia"), Fish("neon tetra", 1.5, "characidae", "south america"), Fish("oscar",18.0,"cichlidae","south america"), Fish("lombardoi",5.0,"cichlidae","africa"), Fish("blue gourami",4.0,"belontiidae","asia"),Fish("siamese fighting fish",2.5,"belontiidae","asia"),Fish("bronze corydoras",3.25,"callicthyidae","south america"),Fish("common plecostomus",12.0,"loricariidae","south america"),Fish("clown loach",12.0,"cobitidae","asia"),Fish("australian arowana",36.0,"osteoglossidae","australia"),Fish("checkered rainbowfish",5.0,"melanotaeniidae","australia"),Fish("upside down catfish",3.0,"mochokidae","africa"),Fish("platy",1.5,"poeciliidae","central america"),Fish("guppy",1.25,"poeciliidae","central america"),Fish("blind cave fish",3.5,"characidae","central america"),Fish("red tailed black shark",6.0,"cyprinidae","asia"),Fish("zebra danio",1.75,"cyprinidae","asia"),Fish("angelfish",5.0,"cichlidae","south america"),Fish("discus fish",8.0,"cichlidae","south america"),Fish("kissing gourami",8.0,"helostomatidae","asia"),Fish("common goldfish",18.0,"cyprinidae","asia")]
  
def get_fish():
  fish_request = input("Search by name, size, family, or origin? \n")
  fish_request = fish_request.lower()
  if fish_request == "name": 
    name_request= input("Enter common name. \n")
    name_request= name_request.lower()
    for fish in fishlist:
      if fish.name == name_request:
        print(fish.name,fish.size,fish.family,fish.origin)
  if fish_request=="size": 
    size_request = input("Enter maximum size desired. \n")
    size_request= float(size_request)
    for fish in fishlist:
        if fish.size <= size_request:
            print(fish.name,fish.size,fish.family,fish.origin)
  if fish_request=="family":
    family_request= input("Enter family name. \n")
    family_request= family_request.lower()
    for fish in fishlist:
        if fish.family == family_request:
            print(fish.name,fish.size,fish.origin)
  if fish_request=="origin": 
    origin_request= input("Enter one of the following: Africa, Asia, Australia, Central America, or South America. \n")
    origin_request= origin_request.lower()
    for fish in fishlist:
        if fish.origin == origin_request:
            print(fish.name, fish.size,fish.family)
            
  y=input("Search again? \n")
  y=y.lower()
  if y != 'y':
    print('Thank you for using the Fisctionary')
  else:
    get_fish()
   
get_fish()

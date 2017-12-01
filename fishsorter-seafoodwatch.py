class Fish:
  def __init__(self, name, fishtype, status):
    self.name = name
    self.fishtype = fishtype
    self.status = status

fishlist = [ Fish("Arctic Char(farmed)","finfish","best choice"),Fish("Barramundi(US & Vietnam farmed)","finfish","best choice"),Fish("Striped Bass (US hook and line, farmed)","finfish","best choice"),Fish("Catfish(US)","finfish","best choice"),Fish("Clams, Mussels, & Oysters","shellfish","best choice"),Fish("Pacific Cod(AK)","finfish","best choice"),Fish("King, Snow, & Tanner Crab(AK)","shellfish","best choice"),Fish("Lingcod(Canada troll & US longline/troll)","finfish","best choice"),Fish("Lionfish(US)","finfish","best choice"),Fish("Branzino(Mediterranean farmed)","finfish","good alternative"),Fish("Pacific Cod(Canada & US)","finfish","good alternative"),Fish("Dungeness Crab(Canada & US)","shellfish","good alternative"),Fish("Lingcod(Canada)","finfish","good alternative"),Fish("Lobster(Bahamas, Canada, & US)","shellfish","good alternative"),Fish("Mahi Mahi(Equador & US longline)","finfish","good alternative"),Fish("Octopus(Portugal & Spain pot/trap)","shellfish","good alternative"),Fish("Salmon(Canada, CA,OR, & WA wild)","finfish","good alternative"),Fish("Sea scallops(wild)","shellfish","good alternative"),Fish("Basa/Pangasus/Swai","finfish","avoid"),Fish("Pacific cod(Japan & Russia)","finfish","avoid"),Fish("Crab(Asia & Russia)","shellfish","avoid"),Fish("Atlantic Halibut(wild)","finfish","avoid"),Fish("Spiny lobster(Belize, Brazil, Honduras, & Nicaragua)","shellfish","avoid"),Fish("Mahi Mahi (imported)","finfish","avoid"),Fish("Orange Roughy","finfish","avoid"),Fish("Pollock(Canada trawl)","finfish","avoid"),Fish("Atlantic salmon(farmed)","finfish","avoid")]

foutput= []
def fin_or_shell():
    finput = input("search for finfish or shellfish? \n")
    finput = finput.lower()
    if finput == "finfish" or finput == "fin":
      for fish in fishlist:
        if fish.fishtype == "finfish":
          foutput.append(fish)
    elif finput == "shellfish" or finput == "shell":
      for fish in fishlist:
        if fish.fishtype == "shellfish":
          foutput.append(fish) 
    else:
      print("Command does not compute.")
      fin_or_shell()
def statusget():
    statpref = input("Return Best Choice, Good Alternative, or Avoid status fish? \n")
    statpref = statpref.lower()
    if statpref == "best choice" or statpref == "best choices":
      for fish in foutput:
        if fish.status == "best choice":
          print(fish.name)
    elif statpref == "good alternative" or statpref == "good alternatives":
      for fish in foutput:
        if fish.status == "good alternative":
          print(fish.name)
    elif statpref == "avoid":
      for fish in foutput:
        if fish.status=="avoid":
          print(fish.name)
    else:
      print("Command does not compute. \n")
      statusget()
def recurse():
  y=input("Search again? \n")
  y=y.lower()
  if y == "y" or y == "yes":
    del foutput[:]
    fishget()
  else:
    print("Thank you for using the fishsorter")
      
def fishget():
    fin_or_shell()
    statusget()
    recurse()
    
fishget()
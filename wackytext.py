import random
# for random.choice()

noun1 = str(input("Enter a noun."))
adj1 = str(input("Enter an adjective."))
noun2 = str(input("Enter another noun."))
adj2 = str(input("Enter another adjective."))
noun3 = str(input("Enter another noun."))
adj3 = str(input("Enter another adjective."))
adj4 = str(input("One more adjective."))
noun4 = str(input("And one more noun."))


ohio = str('Ohio is a {} State in the {} Lakes region of the United States. \n Ohio is the 34th largest by {}, the 7th most {}, and the 10th most {} of the 50 United States. \n Ohio is known as the "{} State" after its {}s, and Ohioans are also known as "{}s".'.format(adj1,adj2,noun1,adj3,adj4,noun2,noun3,noun2))
virginia = str('Virginia is a state in the {} and {} regions of the United States located between the Atlantic {} and the {} Mountains. \n Virginia is nicknamed the "Old {}" due to its status as the first English {} {} established in mainland North America, \nand "Mother of {}s" because eight U.S. {}s were born there, more than any other state.'.format(adj1,adj2,noun1,adj3,noun2,adj4,noun3,noun4,noun4)) 
kentucky = str('Kentucky is known as the "{} State", a nickname based on the {} found in many of its pastures due to the {} soil. \nIt is a land with diverse {}s and {} resources, including the world\'s {}est {} system, {} {} National Park.'.format(noun1,noun2,adj1,noun3,adj2,adj3,noun4,adj4,noun4))
colorado = str('Colorado became the first {} state to host a {} political convention when the Democratic {} met in Denver in 1908. \nBy the U.S. Census in 1930, the population of Colorado first exceeded one million {}. \n{} became a mainstay of the state economy, and {} technology became a {} economic {}.'.format(adj1,adj2,noun1,noun2,noun3,adj3,adj4,noun4))
statelist = [ohio,virginia,kentucky,colorado]
print(random.choice(statelist))

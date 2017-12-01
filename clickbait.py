import random
word1=["Miracle diet ", "Weird food ", "Simple trick ", "Dermatologist ", "This fruit ", "Homeowner ", "Celeb ", "This man ", "Local mother ", "Local law enforcement ", "This simple habit ", "Alien lifeform from Glaxulob-780-a ", "Hot single woman "]
word2=["busts ", "tones ","saves ","hates ", "increases ", "saves on ", "cheats on ", "needs ", "discovers ", "cracks down on ", "vaporizes ", "builds ", "strengthens "]
word3=["fat","glutes","cash","her","belly fat", "taxes","husband", "this secret libido enhancer", "new anti-aging secret", "traffic violations in your area", "singles in your area", "libido", "muscles", "Boston" ]
ending=[", and you won't believe what happens next!", "! Guaranteed to warm your heart!", "! Learn how!","! Find out more!", "! You can too!", "!", "!", ", don't miss out!", "! See if you qualify!"]
sentence = random.choice(word1)+random.choice(word2)+random.choice(word3)+random.choice(ending)

def lets_click_again():
    sentence = random.choice(word1)+random.choice(word2)+random.choice(word3)+random.choice(ending)
    print(sentence)
    
    y=input("Generate new clickbait? \n")
    y=y.lower()
    if y != 'y' and y != 'yes':
        print('Laters')
    else:
        lets_click_again()
        
lets_click_again()

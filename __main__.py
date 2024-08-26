import sys
#INSTRUCTIONS
print('''HELLO USER
Congrats on reaching the final level of the game
This level comprises of convincing the mermaid with appropriate dialogues:
1)Make sure your choice is just the number 1/2/3
2)Program is case sensitive so make sure to enter the inputs in the right manner
3)The program is under a limit, if your choices are impolite it might go over the limit and you will lose
4)Conversations written in brackets are from the main character Ruth ''')
ok=input("If you are clear with the instructions, press 'o' to continue:")
#CONVO CODE
def convolose():
    if v>6:
        print("Your dialogue choice was poor, it seems to have pissed the mermaid over the limit \n --YOU LOSE--")
        sys.exit()
if ok=='o':
    v=0
    #if v>6 u lose
    print("___________\nVanessa: Seriously? A human? Again? \n (She is trying to speak with a British accent. Did she learn it from someone? But what did she mean by 'again'? Should I ask right away?)")
    one=input("1) Introduce and then ask \n2) What do you mean 'again'? \n3) You've got a funny accent \n:")
    print("__________________________________________________________________")
    if one=='1':
        print("Hello Miss Mermaid! My name is Ruth. I come from dash village. Is everything all right? What did you mean by 'again'? \nThe mermaid looks at Ruth. Her sharp eyes fixed on Ruth. And replies, \nVanessa: Well, hello, Ruth! This is a relief. At least this time I'll be dealing with someone polite. \n*mumbles to herself* Polite enough to greet a person they meet for the first time.")
    elif one=='2':
        print("The mermaid raised her left eyebrow as someone in disbelief. She looked at her uninvited guest and \nVanessa:  Do I know you? \n Ruth: Ah! Hello Miss Mermaid, I am Ruth.")
        v+=1
    elif one=='3':
        print("The mermaid looks annoyingly at Ruth. \nVanessa: See! Humans are all the same.. What a rude bunch of creatures! Well, let me teach you, illmannered brat! \nYou can start showing respect by introducing yourself. \nRuth: Oh! Hello Miss Mermaid, I am Ruth.")
        v+=2
    print("___________\nNevertheless, why do we have to suffer because of humans? You create new things to make life easier but then dump all the after-effects on those around you? Why have you come? You have already exploited all of your resources, and now you are here to destroy my home? Is that why you are here? This is like, what, the 150th time? Or 51?  Ha! I lost count after the 100th human tried to barge in like they owned this place. \n(Exploited? Destroy her home? Humans tried to barge in? What is she talking about? Bernard told me countless men have tried to find the mermaid and solve this mess, but nobody returned alive. Did they even try talking to her or were they here with a different motive?)")
    two=input("1) What are you talking about? \n2) Miss Mermaid, I don't understand. Humans tried to destroy your home? \n3) I am here to ask you to stop monopolizing this beautiful place.\n:")
    print("__________________________________________________________________")
    if two=='1':
        print("The mermaid gave out a big sigh \nVanessa: I am talking about the injustice the other beings are going through because you humans have monopolized everything around you, leaving nothing for the others. Right now, you are here to take me hostage and have this place all to yourselves, am I right?")
        v+=1
    elif two=='2':
        print("The mermaid stared at Ruth without a change in expression and replied \nVanessa: Yes, I know you are here like your peers to take me hostage and have this place all to yourselves, Right?")
    elif two=='3':
        print("The mermaid scoffed as if in disbelief and said, \nMermaid: It is funny how you blame me for monopolizing my home now. After putting my guard troll to sleep, trespassed into my house, and now you have the nerve to accuse me? You are here to take me hostage aren't you? ")
        v+=2
    print("(What is Venus talking about? Does she not recognize me? I even introduced myself. \nWell at least, her temper is still the same. * giggles* )")
    print("___________\nVanessa: What? Now you find this funny? Did you think introducing yourself as someone I used to know shall get you any closer to me? Human, leave while I ask you to.")
    three=input("1)Why should I leave? This land belongs to everyone, so stop whining.Also quit making people vanish just because you don't like them. \n2) No, I shan't till I convince you to stop making people disappear. \n3) I will leave when I want to. Don't tell me what to do.\n:")
    print("__________________________________________________________________")
    if three=='1':
        print("Vanessa: Oh, the nerve! To call this land yours.")
        v+=1
    elif three=='2':
        print("Vanessa: Now you are really annoying me!")
    elif three=='3':
        print("Vanessa: This cheeky little..{Vanessa bites her tongue}..Listen human, you are testing my patience.")
        v+=2
    print("(uh-oh Venus looks pissed)")
    print("___________\nVanessa: And what's this about me making people disappear. FYI, I am a mermaid, not a magician. I indeed get irritated every time a human trespasses my land. But I have never hurt anyone unless they threaten me to leave my home. And tell that king of yours that I will not fall for his deceits anymore. Even if he sends MY Ruth here, I do not intend to hand over my land as he wishes. I will not trust her or any other humans ever again. This land belongs to me and the creatures living here. Ask him to get his daughter something that doesn't have an owner. Now that you've cleared your doubts, prepare to leave. I don't wish to waste my precious time on you anymore. ")
    print("(The king wanted her land? For the princess? And she wouldn't trust me ... again? Good lord! This is the real reason why she left not because of her specie, my kind were secretly demanding her place without me knowing!)")
    four=input("1)Venus, please let me explain. I am sure this is all a misunderstanding \n2)How could you insult the royal family Venus?! Bernard was right. Mermaids are ungrateful! \n3) Venus i guess there has been a misunderstanding\n:")
    print("__________________________________________________________________")
    if four=='1':
        print("Vanessa: You- \nVanessa opened her mouth to speak, then she suddenly stopped and looked at Ruth with eyes wide open. \nVanessa: You! That name...she gave me that name. Ruth?")
    elif four=='2':
        v+=3
        convolose()
        print("Vanessa looked furiously at Ruth and then shouted,\nVanessa: Well, guess I am ungrateful. So YOU SHOULD LEAVE NOW! Before you get more annoyed by my \"ungratefulness\"- \nShe suddenly stopped, her eyes wide open \nVanessa: That name...Are you...")
    
    elif four=='3':
        v+=1
        convolose()
        print("Vanessa: Yeah sure, misunderstand- \nShe suddenly stopped, her eyes wide open \nVanessa: Are you...")
    print("___________\nVanessa: Ruth? Is that really you? You...Well...You do look like her!! \nVanessa looked at her. A slight smile escaped her mouth. But she quickly hid it with her hand. \nAfter she regained her stern poise, she spoke in a soft yet firm manner,\nVanessa: Well, you have finally come! I thought the king would never let me see you again. But I assume he is desperate to have this land that he sent you? Even if it's you, Ruth, I cannot hand over this place.")
    five=input("1)Why can't you? I think this is the best for both of us. \n2)How foolish of you to not accept the king's offer! I am sure he would pay you handsomely. \n3)I understand, Venus.\n:")
    print("__________________________________________________________________")
    if five=='1':
        v+=1
        convolose()
        print("Vanessa: You don't understand Ruth. The king wants to monopolize the land. He will not allow the common folks to enter this place once it becomes the princess's private property.\nRuth: Now I understand..")
    elif five=='2':
        v+=3
        convolose()
        print("Venesa: Ruth! Wake up! They are all fooling you! The king wants to monopolize this land. He will not allow the common folks to enter this place once it becomes the princess's private property.\nRuth: Now I understand..")
    elif five=='3':
        print()
    print()
    print("___________\nRuth: The king asked for this land because the princess wanted this place all for herself. Coincidently or not, I and you became friends. Later when you found out the king's desire to own this place, you thought I plotted with them to get this land and that is why I befriended you. Is that right?")
    print("Vanessa: Well, that's-")
    print("Ruth: It's alright Venus! I told you I am not here for the land. I just...thought we could be friends again. Friendship is built on respect and trust.  Even if you respect someone but don't trust them, the friendship will crumble. \nAnyways, you said that you haven't hurt any innocent person. Then I shall take this matter to the townspeople and the king. Don't worry I will make sure that no one tries to snatch your home from you again. Now, I will leave you to yourself. Goodbye Venus.")
    theend=input("---THE GAME HAS ENDED,YOU WIN..if you want to know the ending press e--- \n:")
    if theend=='e':
        print('''Vanessa's POV:
        I was really happy when I made a human friend for the first time. Even though my mother warned me that humans, the most intellectually capable beings on earth who held the power of invention, are the most dangerous beings. Though, I never paid her any heed. 
        I loved the new friend I made. I liked her long and silky purple hair, big golden eyes that were always in search of something adventurous and the way she always talked about the human world whenever she visited me. She always looked bright and cheerful even when she was going through a hard time. Nevertheless, sometimes, she looks so lonely as the moon. Moon-like, I thought.    
        I still don't know how she found this place though. All I knew was I liked being her friend until...until I overheard that big old bearded man talking to someone about building a greenhouse around my home for the princess, in return for a place to stay in the human world with Ruth. I was devastated. "I considered Ruth my little sister, yet...yet she betrayed me!?! ", was what I thought. I was hurt, not by the thought of my home being subjugated but by Ruth's betrayal.   
        But, is she saying that she didn't know any of this? Ruth was innocent? I...I didn't even bother to clarify it with Ruth, and jumped to my own conclusion? 
        
    *flashback *
        Ruth: Venus, my mother told me that it takes years to build trust but seconds to break it and forever to repair, so you must always trust me no matter what, okay?
        
    To the present:
    {Ruth turns back and starts walking}
    Vanessa: Ruth wait!
    {Ruth stops and turns back}
    Vanessa: Why...do you always call me Venus? 
    {Suddenly silence cuts through. THE AIR WAS STILL COTTONY WITH FOG. The silence is broken by Ruth's reply}
    Ruth: Remember the time you called me the Moon?  Venus is the second brightest natural object in the night sky after the moon. That's why.
        
        {Ruth turns towards the exit and walks away as Vanessa watches her friend fade into the mist}
        ________THE END______''')
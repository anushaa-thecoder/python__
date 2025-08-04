#display choices 
#show union of which 2 steram to be unioned also member give choice sci arts commerce
#show intersection members of any 2
#add members also ask where to add in which stream
#remove members club kuthla ani kuthla member remove kaychay
#check their membership
#exit

l=[]
club_sci= set()
club_arts= set()
club_com= set()
while True:
    print("1.GIVE ALL CLUB MEMBER'S LIST")
    print("2.SHOW UNION OF TWO STREAMS")
    print("3.SHOW INTERSECTION MEMBER'S OF ANY TWO STREAMS")
    print("4.REMOVE MEMBERS")
    print("5.CHECK THEIR MEMBERSHIP")
    print("6.EXIT")
    ch=input("enter a choice:")
    if ch=='1':
        a=input("In which club do you want to add members?")
        if a.lower()=='science':
            club_sci.add(a)
            print(a)
        elif a.lower()=='commerce':
            club_com.add(a)
            print(a)
        elif a.lower()=='arts':
            club_arts.add(a)
            print(a)
        
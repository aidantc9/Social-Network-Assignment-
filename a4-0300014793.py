import random

def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    friends = open(file_name).read().splitlines()

    size=int(friends.pop(0))
    network=[]
    flip=[]
    for j in range(len(friends)):
        friends[j]=friends[j].split(" ")
        friends[j][0]=int(friends[j][0])
        friends[j][1]=int(friends[j][1])
        x=friends[j][0]
        y=friends[j][1]
        l=[y,x]
        flip.append(l)


    friends+=flip
    friends.sort()


    for i in range (len(friends)):
        if binary_search(network, friends[i][0])==-1: 
           network.append((friends[i][0],[friends[i][1]]))
        check=binary_search(network, friends[i][0])
        if friends[i][0]==network[check][0] and binary_search_Single(network[check][1], friends[i][1])==-1: 
            network[check][1].append(friends[i][1])



     
    return(network)


def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->int
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common=[]
    u1l= network[binary_search(network,user1)][1]
    u2l=network[binary_search(network,user2)][1]
    for i in range (len(u2l)):
        if binary_search_Single(u1l, u2l[i])!=-1:
            common.append(u2l[i])
    
    return common

def binary_search(List, ID):
    '''
    (list,object)->bool

    Returns an index of ID in List
    or returns -1, if ID not in List
    Note that this one works for 2d list

    Precondition:The List has to be sorted L 
    '''
    start = 0
    end = len(List)- 1

    while start <= end:
      mid = (start + end) // 2
      if ID < List[mid][0]:
           end = mid - 1
      elif ID == List[mid][0]:
           return mid
      else:
           start = mid + 1
           
    return - 1;

def binary_search_Single(List, ID):
    '''
    (list,object)->bool

    Returns an index of ID in List
    or returns -1, if ID not in List
    Note that this one works for 1d list 

    Precondition:The List has to be sorted L 
    '''
    start = 0
    end = len(List)- 1

    while start <= end:
      mid = (start + end) // 2
      if ID < List[mid]:
           end = mid - 1
      elif ID == List[mid]:
           return mid
      else:
           start = mid + 1
           
    return - 1; 

    
def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''

    largI=-1
    largL=-1
    userL=network[binary_search(network,user)][1]
    for i in range (len(network)):
        check=binary_search(network,i)
        check2=len(getCommonFriends(user, i, network))
        
        if user !=check and binary_search_Single(userL, check) ==-1 and check2!=0:           
            currL=check2
            if currL>largL:
                largI=i
                largL=currL
            
            
            
    if largI==-1:
        return(None)
    else:
        return(network[largI][0])


    


def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    count=0
    for i in range (len(network)):
        if len(network[i][1])>=k:
            count+=1
    return count
 

def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    currM=0
    for i in range (len(network)):
        cu=len(network[i][1])
        if currM<cu:
            currM=cu
    return(currM)
    

def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends=[]
    currI=0
    currL=[]
    maX=[0]
    for i in range (len(network)):
        if len(network[i][1])>len(network[maX[0]][1]):
            maX=[]
        
        
        if len(network[i][1])>len(currL):
            if i==0:
                maX.pop(0)
            currL=network[i][1]
            currI=i
            maX.append(currI)
        
        if len(network[i][1])==len(currL) and binary_search_Single(maX, i)==-1 :
            currI=i
            maX.append(currI)

    max_friends=maX
            
    return max_friends
    


def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''

    suM= 0
    size =len (network)
    for i in range (size):
        suM+=len(network[i][1])
    avg= suM/size

    return avg
    

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    
    eve=[]
    for i in range (len(network)):
        eve.append(network[i][0])
    for j in range (len(network)):
        check=eve
        check.remove(network[j][0])
        if check == network[j][1]:
            return True
        
    return (False)


####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''()->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''
    
    ID=-1
    eve=[]
    for i in range (len(network)):
        eve.append(network[i][0])

    while True:
        try:
            ID= int(input("Enter an integer for a user ID"))
            if binary_search_Single(eve, ID)==-1:
                print("The user ID does not exist.Try again")
                continue
            
            break

        except ValueError:
                print("That was not an integer. Please Try again.")
    return(ID)


    

##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name=get_file_name()
    
net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommed the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinaly, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")

    

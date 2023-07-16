#!/usr/bin/env python
# coding: utf-8

# In[10]:


#SAMPLE DATA

'''
Sample data for Relationship Status below:
'''

social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}

'''
Sample data for Tic Tac Toe below:
'''

board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]

'''
Sample data for ETA below:

(from_stop, to_stop)
'''

legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

legs = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}


# In[17]:


'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''

    #Access Data from FROMMember
    #Check if toMember is within the following dict/index of FROMMember
        #Mark as TRUE or FALSE
        
    #Access data from toMember and check if fromMember is in their following
        #Mark as TRUE or FALSE
        
    #Make corresponding IF statement

    #Cases:
        #case_A: fromMember follows toMember
        #case_B: toMember follows fromMember
        
    if to_member in social_graph[from_member]["following"]:
        case_A = True
    
    else:
        case_A = False

    
    if from_member in social_graph[to_member]["following"]:
        case_B = True
        
    else:
        case_B = False
        
    if case_A == True and case_B == True:
        return "friends"
    
    elif case_A == False and case_B == False:
        return "no relationship"
    
    elif case_A == True and case_B == False:
        return "follower"
    
    elif case_A == False and case_B == True:
        return "followed by"


# In[19]:


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    

    amount_of_rows = len(board)
    amount_of_columns = len(board[0])
    
    
    #Case 1 - Horizontal
    counter1 = 0
    winner1 =''
    
    for row in range(amount_of_rows):
        winnercounter1 = 0
        
        for column in range(1, amount_of_columns):
            
            #Checking if Any Line Contains a Win
            if board[row][column] != board[row][column-1]:
                counter1 += 1
                break
            
            #Checking Which Line Contains a Win
            elif board[row][column] == board[row][column-1]:
                winnercounter1 +=1
                
            if winnercounter1 == amount_of_columns -1:
                winner1 = board[row][0]
                
                
        if counter1 < amount_of_rows:
            case1 = True
        else:
            case1 = False

    #Case 2 - Vertical
    
    counter2 = 0
    winner2 = ''
    
    for column in range(amount_of_columns):
        winnercounter2 = 0
        
        for row in range(1, amount_of_rows):
            
            #Checking if Any Line Contains a Win
            if board[row][column] != board[row-1][column]:
                counter2 += 1
                break
            
            #Checking Which Line Contains a Win
            elif board[row][column] == board[row-1][column]:
                winnercounter2 +=1
                
            if winnercounter2 == amount_of_rows -1:
                winner2 = board[0][column]                
        
        if counter2 < amount_of_columns:
            case2 = True
        else:
            case2 = False
            
            
    #Case 3 - Diagonal (Left to Right)
    
    counter3 = 0
    for row in range(1, amount_of_rows):
        
        if board[row][row] != board[row-1][row-1]:
            
            counter3 += 1
            break
        
    if counter3 == 1:
        case3 = False
    else:
        case3 = True
        
        
    #Case 4 - Diagonal (Right to Left)

    counter4 = 0
    
    for row in range(1, amount_of_rows):
        
        if board[row][amount_of_columns - row -1] != board[row - 1][amount_of_columns - row]:
            counter4 += 1
            break

    if counter4 == 1:
        case4 = False
    else:
        case4 = True
    
    
    #Displaying Winner
    
    if case1 == True:
        return winner1
    
    elif case2 == True:
        return winner2
    
    elif case3 == True:
        return board[0][0]
    
    elif case4 == True:
        return board[0][amount_of_columns -1]
    
    else:
        return "NO WINNER"


# In[21]:


def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''

    
    index_A = first_stop
    time_taken = 0
    
    for element in route_map:
        
        if index_A in element[0]:
            
            time_taken += route_map[element]["travel_time_mins"]
            index_A = element[1]
        
            if second_stop in element[1]:
                break
            
    
    if index_A != second_stop:
        
        
        for element in route_map:
        
            if index_A in element[0]:

                time_taken += route_map[element]["travel_time_mins"]
                index_A = element[1]

            if second_stop in element[1]:
                break

            
    return time_taken


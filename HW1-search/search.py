# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]



        



def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    

    from game import Directions
    from util import Stack


    South = Directions.SOUTH
    West = Directions.WEST
    East = Directions.EAST
    North = Directions.NORTH
    Stop = Directions.STOP

    retList = []
    visited = []
    
    
    stack = Stack()
    
    if problem.isGoalState(problem.getStartState()):
        return [Stop]
    
    
    for successor in problem.getSuccessors(problem.getStartState()):
                stack.push([successor, [successor[1]]])
    
    

    while stack.isEmpty() == False:
        # if counter == 5:
        #    break
        currentNode = stack.pop()
      
        if(currentNode[0][0] in visited):
                continue
      

        visited.append(currentNode[0][0])
        

        if problem.isGoalState(currentNode[0][0]):
            retList = currentNode[1].copy()
            print(*retList)
            return retList

        else:
            for successor in problem.getSuccessors(currentNode[0][0]):
                if(successor[0] not in visited):
                    newList = currentNode[1].copy()
                    newList.append(successor[1])
                    stack.push([successor, newList])

                

    return retList

    


            
            
    
    # util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
        


    from game import Directions
    from util import Queue


    South = Directions.SOUTH
    West = Directions.WEST
    East = Directions.EAST
    North = Directions.NORTH
    Stop = Directions.STOP

    retList = []
    visited = []
    
    
    queue = Queue()

    initial = problem.getStartState()
    
    if problem.isGoalState(initial):
        return [Stop]
    
    visited.append(initial)


    
    
    for successor in problem.getSuccessors(problem.getStartState()):
                queue.push([successor, [successor[1]]])

    
    

    while queue.isEmpty() == False:
        # if counter == 5:
        #    break
        currentNode = queue.pop()

        if(currentNode[0][0] in visited):
            continue

        visited.append(currentNode[0][0])
        
        

        if problem.isGoalState(currentNode[0][0]):
            retList = currentNode[1].copy()
            print(*retList)
            return retList

        else:
            for successor in problem.getSuccessors(currentNode[0][0]):
                if(successor[0] not in visited):
                    newList = currentNode[1].copy()
                    newList.append(successor[1])
                    queue.push([successor, newList])

                

    return retList

    


            
            
    


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
            
 

    from game import Directions
    from util import PriorityQueue


    South = Directions.SOUTH
    West = Directions.WEST
    East = Directions.EAST
    North = Directions.NORTH
    Stop = Directions.STOP

    retList = []
    visited = []
    
    
    queue = PriorityQueue()
    
    initial = problem.getStartState()
    if problem.isGoalState(initial):
        return [Stop]

    visited.append(initial)

    
    
    
    for successor in problem.getSuccessors(problem.getStartState()):
        print(successor[2])
        queue.push([successor, [successor[1]], successor[2]], successor[2])
    
    

    while queue.isEmpty() == False:
        # if counter == 5:
        #    break
        currentNode = queue.pop()

        if(currentNode[0][0] in visited):
            continue

        visited.append(currentNode[0][0])
        

        if problem.isGoalState(currentNode[0][0]):
            retList = currentNode[1].copy()
            print(*retList)
            return retList

        else:
            for successor in problem.getSuccessors(currentNode[0][0]):
                if(successor[0] not in visited):
                    newList = currentNode[1].copy()
                    newList.append(successor[1])
                    queue.push([successor, newList, successor[2]+currentNode[2]], successor[2]+currentNode[2])

                

    return retList



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

              
 

    from game import Directions
    from util import PriorityQueue
    from util import manhattanDistance


    South = Directions.SOUTH
    West = Directions.WEST
    East = Directions.EAST
    North = Directions.NORTH
    Stop = Directions.STOP

    retList = []
    visited = []
    
    
    queue = PriorityQueue()
    initial = problem.getStartState()
    
    if problem.isGoalState(initial):
        return [Stop]
    
    

    for successor in problem.getSuccessors(problem.getStartState()):
                queue.push([successor, [successor[1]]],manhattanDistance(initial, successor[0].goal()))
    
    

    while queue.isEmpty() == False:
        # if counter == 5:
        #    break
        currentNode = queue.pop()

        visited.append(currentNode[0][0])
        

        if problem.isGoalState(currentNode[0][0]):
            retList = currentNode[1].copy()
            print(*retList)
            return retList

        else:
            for successor in problem.getSuccessors(currentNode[0][0]):
                if(successor[0] not in visited):
                    newList = currentNode[1].copy()
                    newList.append(successor[1])
                    queue.push([successor, newList], manhattanDistance(initial, successor[0].goal))

                

    return retList



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

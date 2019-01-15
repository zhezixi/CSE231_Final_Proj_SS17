
import itertools

class Matrix(object):
    '''Add your docstring here.'''

    def __init__(self):  # no modification is needed for this method, but you may modify it if you wish to
        '''Create and initialize your class attributes.'''
        self._matrix = []
        self._rooms = 0

    def read_file(self,fp):  #fp is a file pointer
        '''Build an adjacency matrix that you read from a file fp.'''
        room_number = fp.readline()
        self._rooms = int(room_number)
        self._matrix = []
        self._matrix.append("0 index holder")
        for i in range(self._rooms):
            self._matrix.append(set())
        for line in fp:
            temp = line.split()
            self._matrix[int(temp[0])].add(int(temp[1]))
            self._matrix[int(temp[1])].add(int(temp[0]))


    def __str__(self):
        '''Return the matrix as a string.'''
        s = ''
        for i in range(1,self._rooms+1):
            line = str(i)+':'
            for j in self._matrix[i]:
                line += ' ' + str(j)
            if i != self._rooms:
                line += '\n'
            s += line
        return s  #__str__ always returns a string

    def __repr__(self):  # no modification need of this method
        '''Call __str__() to return a string for displaying in the shell'''
        return self.__str__()

    def adjacent(self,index):
        '''Return the set of connecting rooms to room specified by index'''
        return(self._matrix[index])

    def rooms(self):
        '''Return the number of rooms'''
        return self._rooms

def open_file():
    """
    prompts the users to enter a file name. Then try to open it.
    """
    while True:
        filename = input('Enter a file name: ')
        try:
            fp = open(filename,'r')
            return fp
        except Exception:
            print('Error -- ', end='')

def main():
    fp = open_file()
    M = Matrix()
    M.read_file(fp)
    done = False
    list_of_rooms = range(1,M.rooms()+1)
    workable_solution = None
    TA_count = 0
    for i in list_of_rooms:
        list_to_try = list(itertools.combinations(list_of_rooms, i))
        for candidate in list_to_try:
            room_avail = set(candidate)
            for j in candidate:
                room_avail = room_avail | M.adjacent(j)
            if room_avail == set(list_of_rooms):
                done = True
                workable_solution = candidate
                break
        if done:
            TA_count = i
            break
    print("TAs needed: " + str(TA_count))
    solution = str(workable_solution)[1:-1]
    print("TAs assigned to rooms: " + solution)
    print()
    print("Adjacency Matrix")
    print(M)

if __name__ == "__main__":
         main()

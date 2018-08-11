import sys
import numpy as np

class SBoard(object):
    def __init__(self, rows, columns, boxes, parent = None):
        config = ''
        domains = [1,2,3,4,5,6,7,8,9]
        values = {}
        for r in range(9):
            for c in range(9):
                config += str(int(rows[r][c]))
                if rows[r][c] == 0.:
                    if r < 3:
                        b = int(r/3) + int(c/3)
                    elif r < 6:
                        b = int(r/3) + int(c/3) + 2
                    elif r < 9:
                        b = int(r/3) + int(c/3) + 4
                    domain = set(domains) - set(rows[r]) - columns[c] - boxes[b]
                    values[str(r) + str(c) + str(b)] = domain
                    
        self.rows = rows
        self.columns = columns
        self.boxes = boxes
        self.values = values
        self.domains = domains
        self.config = config
        if parent == None:
            self.parent = self
        else:
            self.parent = parent
        self.children = []

    def solved(self):
        print("____________________")
        
        if self.values == {}:
            for i in range(9):
                if set(self.rows[i]) != set(self.domains):
                    return False
                elif self.columns[i] != set(self.domains):
                    return False
                if self.boxes[i] != set(self.domains):
                    return False
            print ('solved!!!!!!!!!')
            return True
        return False

    def display(self):
        c = 0
        for r in range(9):
            c += 1
            print (self.rows[r][:3], ' ', self.rows[r][3:6], ' ', self.rows[r][6:])
            if c == 3:
                print ('')
                c =0

    def expand(self):
        print('--------------')

        md = float('inf')
        for key,domains in self.values.items():
            if len(domains) == 0:
                return False
            if len(domains) <= md:
                min_domains = domains
                min_key = key
                md = len(domains)
        k = [int(key) for key in min_key]
        for value in min_domains:
            rows = self.rows.copy()
            rows[k[0]][k[1]] = value
            columns = [self.columns[i].copy() for i in range(9) ]
            columns[k[1]].add(value)
            boxes = [self.boxes[i].copy() for i in range(9) ]           
            boxes[k[2]].add(value)
            new_child = SBoard(rows, columns, boxes, self.parent)
            self.children.append(new_child)
        return self.children







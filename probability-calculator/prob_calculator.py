import copy
import random

class Hat:

    def __init__(self, **kwargs):
        def create_contents(**kwargs):
            newList = []
            for k, v in kwargs.items():
                for i in range(v):
                    newList.append(k)
            return newList
        self.contents = create_contents(**kwargs)

    def draw(self, num):
        if num > len(self.contents):
            return self.contents
        newList = []
        for i in range(num):
            value = random.randrange(len(self.contents))
            newList.append(self.contents[value])
            self.contents.pop(value)
        return newList

def create_list_3(list1, list2):
    newList = []
    for elem2 in list2:
        for elem1 in list1:
            if elem2 == elem1:
                newList.append(elem1)
                list1.remove(elem1)
                break
    if newList == list2:
        return True
    return False

def create_list_2(expected_balls):
    newList = []
    for k, v in expected_balls.items():
        for i in range(v):
            newList.append(k)
    return newList

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        bak = copy.deepcopy(hat)
        list1 = bak.draw(num_balls_drawn)
        list2 = create_list_2(expected_balls)
        if create_list_3(list1, list2) == True:
            count += 1
    return count / num_experiments
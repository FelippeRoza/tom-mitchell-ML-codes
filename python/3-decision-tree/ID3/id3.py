import pandas as pd
from math import log

class Tree(object):
    def __init__(self, arg):
        self.root = None
        self.label = None
        self.branches = []

    def add_branch(self):
        self.branches.append(Tree())

    def define_label(self, label):
        self.label = label

def entropy(s):
    #s is a pandas series
    entropy = 0
    for i in s.unique():
        pi = float((s == i).sum())/len(s) #proportion of s belonging to class i
        entropy = entropy - pi*log(pi,2)
    return entropy

def ID3(examples, target_attributes, attributes):

    tree = Tree()
    if all(examples > 0):
        tree.define_label('+')
        return tree
    if all(examples < 0):
        tree.define_label('-')
        return tree

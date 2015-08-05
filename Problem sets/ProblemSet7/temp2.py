# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 14:28:48 2015

@author: Administrador
"""

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

# TODO: WordTrigger

        
class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()
    
    def removeSymbols(self,text):
        for char in string.punctuation:
            text = text.replace(char, ' ')
        return text
              
    def isWordIn(self,text):
        text=self.removeSymbols(text.lower())
        return self.word in text.split()

class TitleTrigger(WordTrigger):
    def evaluate(self,text):
        return self.isWordIn(text.getTitle())
        
class SubjectTrigger(WordTrigger):
    def evaluate(self,text):
        return self.isWordIn(text.getSubject())

class SummaryTrigger(WordTrigger):
    def evaluate(self,text):
        return self.isWordIn(text.getSummary())

# Composite Triggers
# Problems 6-8

# TODO: NotTrigger
# TODO: AndTrigger
# TODO: OrTrigger
class NotTrigger(Trigger):
    def __init__(self,T):
        self.T = T
    def evaluate(self,x):
        return not(self.T.evaluate(x))
        
        
    
class AndTrigger(Trigger):
    def __init__(self,t1,t2):
        self.t1 = t1
        self.t2 = t2
    def evaluate(self,x):
        return(self.t1.evaluate(x) and self.t2.evaluate(x))
    
class OrTrigger(Trigger):
   def __init__(self,t1,t2):
       self.t1 = t1
       self.t2 = t2
   def evaluate(self,x):
       return (self.t1.evaluate(x) or self.t2.evaluate(x))
    
class PhraseTrigger(Trigger):
    def __init__(self,phrase):
        self.phrase = phrase
    def evaluate(self,x):
        return (self.phrase in x.getTitle()) or (self.phrase in x.getSubject()) or (self.phrase in x.getSummary())
def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.

    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")

    Modifies triggerMap, adding a new key-value pair for this trigger.

    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).
    """
    # TODO: Problem 11
    if triggerType == 'PHRASE':
        trig = PhraseTrigger(' '.join(params))
        triggerMap[name] = trig
    elif triggerType == 'AND':
        trig = AndTrigger(params[0], params[1])
        triggerMap[name] = trig
    elif triggerType == 'OR':
        trig = OrTrigger(params[0], params[1])
        triggerMap[name] = trig
    elif triggerType == 'NOT':
        trig = NotTrigger(params[0])
        triggerMap[name] = trig
    elif triggerType == 'SUBJECT':
        trig = SubjectTrigger(params[0])
        triggerMap[name] = trig
    elif triggerType == 'SUMMARY':
        trig = SummaryTrigger(params[0])
        triggerMap[name] = trig
    elif triggerType == 'TITLE':
        trig = TitleTrigger(params[0])
        triggerMap[name] = trig
            
    return trig
    
#    Trigger file:
#t1 TITLE Manitoba
#t2 NOT t1
#t3 PHRASE British Colombia
#t4 NOT t3
#
#**** RUNNING MAKETRIGGER ON TRIGGER FILE ****
#TitleTrigger made with word: Manitoba
# --> Is trigger t1 in triggerMap? True
#NotTrigger made with trigger: t1("1")
# --> Is trigger t2 in triggerMap? True
#PhraseTrigger made with phrase: British Colombia
# --> Is trigger t3 in triggerMap? True
#NotTrigger made with trigger: t3("3")
# --> Is trigger t4 in triggerMap? True
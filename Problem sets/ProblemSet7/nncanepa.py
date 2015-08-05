# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 13:47:14 2015

@author: nncanepa
"""

from ps7 import *

class NewsStory(object):
    """
        Carga una noticia:
            NewsStory(GUID, Title, Subject, Summary, Link)
    """
    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link
    def getGuid(self):
        return self.guid
        
    def getTitle(self):
        return self.title
        
    def getSubject(self):
        return self.subject
        
    def getSummary(self):
        return self.summary
        
    def getLink(self):
        return self.link
        
class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()
    
    def removeSymbols(self,text):
        for char in string.punctuation:
            text = text.replace(char, ' ')
        return text
    
    def isWordIn(self,text):
        text=self.removeSymbols(text.lower())
        for word in text.split():
            if self.word in text:
                return True
            else:
                return False
        



    

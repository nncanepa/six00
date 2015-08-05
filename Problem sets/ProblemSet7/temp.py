# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 14:40:39 2015

@author: Administrador
"""

import string

#s='Soft!" he exclaimed as he threw the football.'
s='Microsoft recently released the Windows 8 Consumer Preview.'
#s=s.lower()
#
#for char in string.punctuation:
#    s = s.replace(char, '')
#
#triggers=['soft']
#
#found = False
#
#for word in s.split():
#    print word
#    if word in triggers:
#        #print "HOLAAAA"
#        found = True
#        break
#    else:
#        found = False
#        
#print found

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

        
class WordTrigger(object):
    def __init__(self, word):
        self.word = word.lower()
    
    def removeSymbols(self,text):
        for char in string.punctuation:
            text = text.replace(char, ' ')
        return text
    
#    def isWordIn(self,text):
#        text=self.removeSymbols(text.lower())
#        for word in text.split():
#            if self.word in text:
#                return True
#            else:
#                return False
    def isWordIn(self,text):
        text=self.removeSymbols(text.lower())
        word in text.split()
        
class TitleTrigger(WordTrigger):
    def evaluate(self,text):
        return self.isWordIn(text.getTitle())
        
class SubjectTrigger(WordTrigger):
    def evaluate(self,text):
        self.isWordIn(text.getSubject())

class SummaryTrigger(WordTrigger):
    def evaluate(self,text):
        self.isWordIn(text.getSummary())
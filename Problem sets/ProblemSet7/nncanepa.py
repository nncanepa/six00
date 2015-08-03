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
    def __init__(self, text, trigger):
        
    raise NotImplementedError
    
class TitleTrigger(WordTrigger):
    raise NotImplementedError
    
class SubjectTrigger(WordTrigger):
    raise NotImplementedError
    
class SummaryTrigger(WordTrigger):
    raise NotImplementedError

class NotTrigger(Trigger):
    raise NotImplementedError
    
class AndTrigger(Trigger):
    raise NotImplementedError
    
class OrTrigger(Trigger):
    raise NotImplementedError
    
class PhraseTrigger(Trigger):
    raise NotImplementedError
    

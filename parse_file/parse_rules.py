#!/usr/bin/python

from sys import argv
script, f1, f2 = argv

class Rulekey: 
  def __init__(self, source, account, trader):
    self.source = source
    self.account = account
    self.trader = trader

  def __str__(self): 
    return self.__repr__()

  def __repr__(self):
     return self.source + "." + self.account + "." + self.trader

  def __eq__(self, other):
     return (self.source == other.source and 
            self.account == other.account and
            self.trader == other.trader)
  
  def __hash__(self):
      return hash((self.source, self.account, self.trader))

class MarketRule:
  def __init__(self):
      self.inclMkts = []
      self.exclMkts = []
      self.inherit = False

  def __str__(self): 
    return self.__repr__()
  
  def __repr__(self):
      result = ""
      if(self.inherit):
        result = result + "+,"

      if(len(self.exclMkts) > 0):
        for i in self.exclMkts:
          result = result + "!" + i + "," 
      else:
        for i in self.inclMkts:
          result = result + i + ","
       
      return result 




def parse_rules(file1):
  for line in file1.readlines():
    key = line.split("=")[0].split(".")
    value = line.split("=")[1]

    ruleKey = Rulekey(key[0], key[1], key[2])
    marketRule = MarketRule()
 
    for e in value.split(","):
        if (e == '+'):
            marketRule.inherit = True 
        elif (e[0] == '!'):
            marketRule.exclMkts.append(str(e[1:]))
        else:
            marketRule.inclMkts.append(e)
    
    rules[ruleKey] = marketRule

def print_rules():
  print 'Parsed data output'
  for e in rules:
    print str(e)+"="+str(rules[e]),



def validate_orders(file2):
  for line in file2.readlines():
    if len(line.strip()) > 0:
      #print line 
      key = line.split("=")[0].split(".")
      value = line.split("=")[1]
     
      mkt = value.split(":")[0] 
      
      ruleKey = Rulekey(key[0], key[1], key[2])

      marketRule = rules[ruleKey]
      
      if(len(marketRule.exclMkts) >0):
          if(mkt in marketRule.exclMkts):
              print "EXCL VIOLATION: " + line,
      else:
          if(mkt not in marketRule.inclMkts):
              print "INCL VIOLATION: " + line, 
  

file1=open(f1, "r")
file2=open(f2, "r")

rules = {}
parse_rules(file1)
#print_rules()

validate_orders(file2)

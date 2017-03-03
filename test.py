#!/usr/bin/python3
import sys,getopt
import json
def execute_function(function,module):
  function_name = function['name']
  print("Testing "+function_name)
  for test_case in function["cases"]:
    print("Checking if "+function_name+"("+str(test_case[0])[1:-1]+") returns "+str(test_case[1]))
    exp = getattr(module,function_name)(*test_case[0])
    if exp == test_case[1] :
      print("Testcase Success")
    else:
      print("Testcase Failed , function returned "+str(exp))
def execute_module(module):
  lmod = __import__(module["name"])
  functions = module["functions"]
  print("Testing "+module["name"])
  for function in functions :
    execute_function(function,lmod)
  print("Finished testing module "+module["name"])
def execute_whole(cases,project_name):
  print("Testing project "+project_name)
  for module in cases:
    execute_module(module)
  print("Finished testing project "+project_name)
def main():
  cases = False
  mod = False
  func = False
  config = "tp-config.json"
  opts,args = getopt.getopt(sys.argv[1:],"m:f:")
  for opt,arg in opts:
    if opt == '-m':
      mod = arg
    elif opt == '-f':
      func = arg
  with open(config) as jfile:
    cases = json.load(jfile)
  if cases:
    if mod == False and func == False:
        execute_whole(cases["modules"],cases["project-name"])
        sys.exit(0)
    for modul in cases["modules"]:
      if modul["name"] == mod:
        if func:
          for function in modul['functions']:
            if function['name'] == func:
              execute_function(function,__import__(modul["name"]))
              sys.exit(0)
          print("Function not found \nTesting whole module")
          execute_module(modul)
          sys.exit(0)
        else:
            execute_module(modul)
            sys.exit(0)
    execute_whole(cases["modules"],cases["project-name"])
  else:
    print(config+" file not found exiting")
    sys.exit(-1)
if __name__ == "__main__" :
	main()

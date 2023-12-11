try:
  x=10
  y=20
  print(x)
  raise Exception("error personnalise")
  print(y)
except NameError:
  print("hello")
except Exception as e:
    print("Something went wrong " + str(e))
else:
  print("all good")
finally:
  print("The 'try except' is finished")
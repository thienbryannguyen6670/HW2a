import time
def timestamp(func):
  def printDate():
    print(time.ctime())
    func()
    return printDate

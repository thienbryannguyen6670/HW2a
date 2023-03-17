import time

def timestamp(func):
  def wrapper(*args, **kwargs):
    print(f"[{time.ctime()}]")
    result = func(*args, **kwargs)
    print(f"[{time.ctime()}]")
    return wrapper

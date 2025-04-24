import os

class Config(object):
  API_ID = int(os.getenv("apiid",7342056))
  
  API_HASH = os.getenv("apihash","89674aa74ed297150b3120914946db5c")
  
  BOT_TOKEN = os.getenv("tk","78532281482:AAG3fe7mz1vLR47fJ7_GYi8bWM2XcCvJ5Vo")
  
  AUTH = os.getenv("auth","1399186514")
  
  OWNER =os.getenv("owner","1399186514")

  #PW =int(os.getenv("spw"))

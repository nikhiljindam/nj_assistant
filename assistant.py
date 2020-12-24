import speech_recognition as sr
import sys

lr = sr.Recognizer()
try:
  with sr.Microphone() as s:
    print(">>>Asdasdasd")
    voi = lr.listen(s)
    print(">>>Listingingggggg ")
    voice = lr.recognize_google(voi)
    print(voice)
except Exception as err:
  print(" error in get_data_for_edit in surveymanagement.py , >> : ", err)
  print("line number of error {}".format(sys.exc_info()[-1].tb_lineno))
  raise err
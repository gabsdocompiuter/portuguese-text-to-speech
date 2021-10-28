import pyttsx3

message = """
A Prefeitura de Cachoeira deverá realizar no final de janeiro de 2022 um concurso público para o quadro geral de servidores e magistério..
"""

engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    print(voice)
    print(voice.languages)
    engine.setProperty('voice', voice.id)
    engine.say(message)
    engine.runAndWait()
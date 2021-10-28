import pyttsx3

message = """
A Prefeitura de Cachoeira deverá realizar no final de janeiro de 2022 um concurso público para o quadro geral de servidores e magistério.
Conforme a Vice Prefeita e Secretária de Educação, Angela Schuh, já foi solicitado para a Secretaria de Administração a contratação de uma empresa para realização do concurso. 

Segundo Angela, o concurso para o magistério irá abranger professores, monitores e serventes cuja a nomeação será imediata, pois as aulas iniciarão no final de fevereiro.
Também haverá vagas no cadastro reserva. 

Já para o quadro geral da Prefeitura, o concurso será realizado para preenchimento de vagas nas mais diferentes áreas da administração.

Nos próximos dias haverá a definição da empresa vencedora da licitação para divulgar as datas de inscrição do concurso.
"""

engine = pyttsx3.init("sapi5")
# engine.say('Ola, tudo bem?')
# engine.runAndWait()

# print(engine.getProperty('voice'))
# voices = engine.getProperty('voices')
# for voice in voices:
#     print("Voice: %s" % voice.name)
#     print(" - ID: %s" % voice.id)
#     print(" - Languages: %s" % voice.languages)
#     print(" - Gender: %s" % voice.gender)
#     print(" - Age: %s" % voice.age)
#     print("\n")

# engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0')

engine.say(message)
engine.runAndWait()
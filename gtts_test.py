from gtts import gTTS

message = """
A Prefeitura de Cachoeira deverá realizar no final de janeiro de 2022 um concurso público para o quadro geral de servidores e magistério.
Conforme a Vice Prefeita e Secretária de Educação, Angela Schuh, já foi solicitado para a Secretaria de Administração a contratação de uma empresa para realização do concurso. 

Segundo Angela, o concurso para o magistério irá abranger professores, monitores e serventes cuja a nomeação será imediata, pois as aulas iniciarão no final de fevereiro.
Também haverá vagas no cadastro reserva. 

Já para o quadro geral da Prefeitura, o concurso será realizado para preenchimento de vagas nas mais diferentes áreas da administração.

Nos próximos dias haverá a definição da empresa vencedora da licitação para divulgar as datas de inscrição do concurso.
"""

tts = gTTS(message, lang='pt')
tts.save('test.mp3')
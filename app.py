from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/questao01', methods=['POST'])
def imprimir_nome():
    return '<h1>Nathan Pereira Sarmento</h1>';

@app.route('/questao02', methods=['POST'])
def expresssao_numerica():
    a,b=3,5
    resultado=(2*a)*(5*b)
    return str(resultado);

@app.route('/questao03', methods=['POST'])
def mudar_progama():
    a,b,c=2,3,4
    resultado2=a+b+c
    return str(resultado2);

@app.route('/questao04', methods=['POST'])
def calcular_aumento():
    salario=750
    aumento=15
    salario_ajustado=(salario+(salario*aumento/100))
    return str(salario_ajustado);

@app.route('/questao05', methods=['POST'])
def pagar_imposto():
    salario=request.form['salario']
    salario=int(salario)
    if salario > 1200:
        resultado='<h1>voce precisa pagar o imposto de renda</h1>'
    else:
        resultado='<h1>voce nao precisa pagar o imposto de renda</h1>'
    return resultado;

@app.route('/questao06', methods=['POST'])
def calcular_media():
    materia1=request.form['materia1']
    materia1=int(materia1)
    materia2=request.form['materia2']
    materia2=int(materia2)
    materia3=request.form['materia3']
    materia3=int(materia3)
    media=(materia1+materia2+materia3)/3
    if media > 7:
     resultado='<h1>O aluno foi aprovado</h1>'
    else:
     resultado='<h1>O aluno foi reprovado</h1>'#
    return resultado;

@app.route('/questao07', methods=['POST'])
def somar_numeros():
    numero1=request.form['numero1']
    numero1=int(numero1)
    numero2=request.form['numero2']
    numero2=int(numero2)
    soma=numero1+numero2
    return '<h1>O resultado da soma eh %d</h1>' % (soma);

@app.route('/questao08', methods=['POST'])
def converter():
    metros=request.form['metros']
    metros=int(metros)
    centimetros=1000*metros
    return '<h1>Em centimetros é igual a %d</h1>' % (centimetros);

@app.route('/questao09', methods=['POST'])
def converter_segundos():
    dia=request.form['dia']
    dia=(int(dia))*86400
    hora=request.form['hora']
    hora=(int(hora))*3600
    minuto=request.form['minuto']
    minuto=(int(minuto))*60
    segundo=request.form['segundo']
    segundo=int(segundo)
    total_segundos=dia+hora+minuto+segundo
    return '<h1>Em segundos é igual a %d</h1>' % (total_segundos);

@app.route('/questao10', methods=['POST'])
def aumento_salario():
    salario=request.form['salario']
    salario=int(salario)
    aumento_porcentagem=request.form['aumentoPorcentagem']
    aumento_porcentagem=(int(aumento_porcentagem))/100
    salario_final=(aumento_porcentagem*salario)+salario
    return '<h1>O salario Final é %d</h1>' % (salario_final);

@app.route('/questao11', methods=['POST'])
def desconto_produto():
    preco=request.form['preco']
    preco=int(preco)
    desconto=request.form['desconto']
    desconto=((int(desconto))/100)-1
    preco_final=preco*desconto
    return '<h1>O preco final do produto eh igual a %d</h1>' % (preco_final);

@app.route('/questao12', methods=['POST'])
def calcular_tempo():
    distancia=request.form['distancia']
    distancia=float(distancia)
    velocidade_media=request.form['velocidade']
    velocidade_media=float(velocidade_media)
    tempo_horas=distancia/velocidade_media
    resto=distancia%velocidade_media
    tempo_minutos=resto/velocidade_media*60
    return '<h1>O tempo é igual a %d horas e %d minutos</h1>' % (tempo_horas,tempo_minutos);

@app.route('/questao13', methods=['POST'])
def conversao_temperatura():
    temperaturaC=request.form['temperaturaC']
    temperaturaC=int(temperaturaC)
    temperaturaF=(temperaturaC*9)/5+32
    return '<h1>A temperatua em farheint é igual a %d</h1>' % (temperaturaF);

@app.route('/questao14', methods=['POST'])
def calcular_preco():
    distanciaKM=request.form['distanciaKM']
    distanciaKM=float(distanciaKM)
    dia=request.form['dia']
    dia=int(dia)
    preco_final=(distanciaKM*0.15)+(dia*60)
    return '<h1>O preço final do produto é igual a %.3f$</h1>' % (preco_final)
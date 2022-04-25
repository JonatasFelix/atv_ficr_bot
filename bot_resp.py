from datetime import datetime
from colorama import Fore

separator_token = "<SEP>"
bot_color = Fore.WHITE


def bot_msg_pdr(msg_case):
    date_now_bot = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    bot_send = f'{bot_color} [{date_now_bot}] Bot Crebson: {separator_token} {msg_case} {Fore.RESET}'
    return bot_send.encode()


def bot_msg(msg):
    if msg == 'oi' or msg == 'olá':
        return 'Olá, tudo bem?'
    elif msg == 'tudo' or msg == 'tudo bem' or msg == 'sim':
        return 'Que legal'
    elif msg == 'não' or msg == 'mais o menos' or msg == 'indo':
        return 'Melhoras!'
    elif msg == 'quem é você?' or msg == 'quem e voce?' or msg == 'quem é você' or msg == 'quem é vc?':
        return 'Sou o Bot Crebson, criado por Jônatas!!'
    elif msg == 'quem criou você?' or msg == 'quem criou vc?':
        return 'Foi o meu mestre Jônatas'
    elif msg == 'por que você foi criado?' or msg == 'por que ele criou você?' or msg == 'por que ele criou vc?':
        return 'Porque o professor Diogenes gosta muito de python!'
    elif msg == 'quantos anos você tem?' or msg == 'qual a sua idade?' or msg == 'quantos anos vc tem?':
        return 'Eu não sou real, minha idade não importa!'
    elif msg == 'você come?' or msg == 'você se alimenta?' or msg == 'o que você come?':
        return 'Eu me alimento da energia da sua casa!'
    else:
        return 'Ainda não sei responder isso!'

from telegram.ext import Updater, CommandHandler

def main():
    #Instanciamos el updater
    updater = Updater(token='1167447600:AAF_2XLu1mEGT6Z_EZWHFhIgr6kFb1RAuZc', use_context=True)
    #Añadiendo un manejador comando/start
    updater.dispatcher.add_handler(CommandHandler('start', start))
    #Añadiendo un manejador comando/Repite
    updater.dispatcher.add_handler(CommandHandler('repite', repite))
    #Añadiendo un manejador comando/suma
    updater.dispatcher.add_handler(CommandHandler('suma',suma))
    #Añadir otro comand/saluda
    updater.dispatcher.add_handler(CommandHandler('saluda',saluda))
    #Empezamos a pedir notificaciones a Telegram
    updater.start_polling()
    #Capturamos señales de parada
    updater.idle()



def start(update, context):
    update.message.reply_text('Hola me acabas de configurar para responder, levelea')

def repite(update, context):
    update.message.reply_text(update.message.text)

def suma(update, context):
    #args = [2,2]
    resultado = int(context.args[0]) + int(context.args[1])
    resultado = str(resultado)
    update.message.reply_text('El resultado es ' + resultado)

def saluda(update, context):
    mi_nombre = context.args[0] + context.args[1]
    update.message.reply_text('Tu nombre es ' + mi_nombre)
main()
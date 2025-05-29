from tkinter import *
from main import clima


#pega a cidade
def buscar_clima():
        cidade = entrada_cidade.get().strip().title()
        if cidade:
                dados = clima(cidade)
                resultado['text'] = (
                        f"📍 Clima atual na cidade de {cidade.title()}:\n "
                        f"🌤️ Descrição do Clima: {dados['descricao'].capitalize()}\n"
                        f"🌡️ temperatura média: {dados ['temp']}°C \n"
                        f"🔺 temperatura maxima: {dados ['temp_max']}°C\n "
                        f"🔻 temperatura minima: {dados ['temp_min']}°C \n"
                        f"🤒 Sensação terminca: {dados ['sensacao_termica']}°C\n "
                        f"💧 Umidade relativa do ar:{dados ['humidade']}% \n"
                )


def reiniciar():
        entrada_cidade.delete(0, END)
        resultado["text"] = ""
        
                       
                

janela = Tk()
janela.title("clima da cidade")

Label(janela, text="Digite o nome da cidade: ").grid(row=0, column=0)
entrada_cidade = Entry(janela)
entrada_cidade.grid(row=0, column=1)

botao = Button(janela, text="Buscar clima", command=buscar_clima)
botao.grid(row=1, column=0, pady=5)

resultado = Label(janela, text="", justify=LEFT)
resultado.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

botao_reiniciar = Button(janela, text="nova busca", command=reiniciar)
botao_reiniciar.grid(row=1, column=1, pady=5)



janela.mainloop()

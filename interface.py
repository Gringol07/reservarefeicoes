from tkinter import *
from tkinter import ttk
from auxilia import refeicoes, tabela

newTabela = tabela

# Configuração da janela principal
janela = Tk()
janela.title("Agendador de Refeições")
janela.state("zoomed")
janela.configure(bg="#f0f4f8")

# Frame principal com padding
frame_principal = Frame(janela, bg="#f0f4f8")
frame_principal.pack(expand=True, fill=BOTH, padx=40, pady=40)

# Header com estilo moderno
frame_header = Frame(frame_principal, bg="#2c3e50", relief=RAISED, bd=0)
frame_header.pack(fill=X, pady=(0, 30))

texto_cabecalho = Label(
    frame_header,
    text="🍽️ AGENDADOR DE REFEIÇÕES",
    font=("Segoe UI", 24, "bold"),
    bg="#2c3e50",
    fg="white",
    pady=20
)
texto_cabecalho.pack()

texto_subtitulo = Label(
    frame_header,
    text="Sistema de Reservas - João Gabriel",
    font=("Segoe UI", 12),
    bg="#2c3e50",
    fg="#ecf0f1"
)
texto_subtitulo.pack(pady=(0, 15))

# Frame central para conteúdo
frame_conteudo = Frame(frame_principal, bg="#f0f4f8")
frame_conteudo.pack(expand=True)

# Botão principal estilizado
botao = Button(
    frame_conteudo,
    text="▶ INICIAR AUTOMAÇÃO",
    command=refeicoes,
    font=("Segoe UI", 14, "bold"),
    bg="#27ae60",
    fg="white",
    activebackground="#229954",
    activeforeground="white",
    relief=FLAT,
    cursor="hand2",
    padx=40,
    pady=15,
    borderwidth=0
)
botao.pack(pady=20)

# Efeitos hover no botão
def on_enter(e):
    botao['bg'] = "#229954"

def on_leave(e):
    botao['bg'] = "#27ae60"

botao.bind("<Enter>", on_enter)
botao.bind("<Leave>", on_leave)

# Frame para status
frame_status = Frame(frame_conteudo, bg="white", relief=SOLID, bd=1)
frame_status.pack(pady=20, padx=100, fill=X)

mensagem_iniciando = Label(
    frame_status,
    text="⏳ Status: Aguardando início das reservas",
    font=("Segoe UI", 11),
    bg="white",
    fg="#7f8c8d",
    pady=15
)
mensagem_iniciando.pack()

# Frame para lista de refeições
frame_lista = Frame(frame_conteudo, bg="white", relief=SOLID, bd=1)
frame_lista.pack(pady=10, padx=100, fill=BOTH, expand=True)

Label(
    frame_lista,
    text="📋 Refeições Agendadas",
    font=("Segoe UI", 13, "bold"),
    bg="white",
    fg="#2c3e50",
    pady=10
).pack()

# Criar canvas com scrollbar para lista
canvas = Canvas(frame_lista, bg="white", highlightthickness=0)
scrollbar = Scrollbar(frame_lista, orient="vertical", command=canvas.yview)
frame_scrollable = Frame(canvas, bg="white")

frame_scrollable.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=frame_scrollable, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Adicionar itens da tabela
for i, mensagem in enumerate(newTabela.index):
    nome = tabela.loc[mensagem, "nome"]
    
    # Frame para cada item
    item_frame = Frame(frame_scrollable, bg="#ecf0f1" if i % 2 == 0 else "white", relief=FLAT)
    item_frame.pack(fill=X, padx=10, pady=2)
    
    texto_item = Label(
        item_frame,
        text=f"✓ {nome}",
        font=("Segoe UI", 10),
        bg="#ecf0f1" if i % 2 == 0 else "white",
        fg="#2c3e50",
        anchor="w",
        padx=15,
        pady=8
    )
    texto_item.pack(fill=X)

canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
scrollbar.pack(side="right", fill="y")

# Footer
frame_footer = Frame(frame_principal, bg="#f0f4f8")
frame_footer.pack(side=BOTTOM, pady=20)

Label(
    frame_footer,
    text="© 2024 - Sistema de Agendamento v1.0",
    font=("Segoe UI", 9),
    bg="#f0f4f8",
    fg="#95a5a6"
).pack()

janela.mainloop()
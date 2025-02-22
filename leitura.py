import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

livroslidos = []
estoulendo = []

# Salva os livros em um arquivo de texto
def salvar_livros():
    caminho_lidos = "livroslidos.txt"
    caminho_lendo = "estoulendo.txt"
    
    with open(caminho_lidos, "w") as arquivo:
        for livro in livroslidos:
            arquivo.write(f"{livro['titulo']}|{livro['sinopse']}|{livro['imagem']}\n")
    
    with open(caminho_lendo, "w") as arquivo:
        for livro in estoulendo:
            arquivo.write(f"{livro['titulo']}|{livro['sinopse']}|{livro['imagem']}\n")

def carregar_livros():
    caminho_lidos = "livros_lidos.txt"
    caminho_lendo = "estoulendo.txt"
    
    if os.path.exists(caminho_lidos):
        with open(caminho_lidos, "r") as arquivo:
            for linha in arquivo:
                if linha.strip():  # Verifica se a linha não está vazia
                    partes = linha.strip().split("|")
                    if len(partes) == 3:
                        titulo, sinopse, imagem = linha.strip().split("|")
                        livroslidos.append({"titulo": titulo, "sinopse": sinopse, "imagem": imagem})

    if os.path.exists(caminho_lendo):
        with open(caminho_lendo, "r") as arquivo:
            for linha in arquivo:
                if linha.strip():  # Verifica se a linha não está vazia
                    partes = linha.strip().split("|")
                    if len(partes) == 3:
                        titulo, sinopse, imagem = linha.strip().split("|")
                        estoulendo.append({"titulo": titulo, "sinopse": sinopse, "imagem": imagem})

def adicionarlivro(categoria):
    caminhoimagem = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])
    if not caminhoimagem:
        return
    titulo = simple_input("Digite o título: ")
    if not titulo:
        return
    sinopse = simple_input("Digite o nome do autor: ")
    if not sinopse:
        return
    livro = {"titulo": titulo, "imagem": caminhoimagem, "sinopse": sinopse}

    if categoria == "lidos":
        livroslidos.append(livro)
    else:
        estoulendo.append(livro)

    atualizarjanela(categoria)

def removerlivro(categoria, livro):
    if categoria == "lidos":
        livroslidos.remove(livro)
    else:
        estoulendo.remove(livro)

    atualizarjanela(categoria)

def moverlivro(origem, destino, livro):
    removerlivro(origem, livro)

    if destino == "lidos":
        livroslidos.append(livro)
    else:
        estoulendo.append(livro)
    atualizarjanela(destino)

def atualizarjanela(categoria):
    janela = frame_lidos if categoria == "lidos" else frame_estoulendo

    # Limpa todos os widgets (livros) antigos antes de atualizar a lista
    for widget in janela.winfo_children():
        widget.destroy()

    lista = livroslidos if categoria == "lidos" else estoulendo

    for livro in lista:
        frame = ctk.CTkFrame(janela, width=400, height=150)  # Ajuste na largura e altura do frame
        frame.pack(pady=5, padx=10, fill="x")

        imagem = Image.open(livro["imagem"])
        imagem.thumbnail((100, 150))
        img_tk = ImageTk.PhotoImage(imagem)

        lbl_img = ctk.CTkLabel(frame, image=img_tk)
        lbl_img.image = img_tk  
        lbl_img.pack(side="left", padx=10)

        lbl_texto = ctk.CTkLabel(frame, text=f"{livro['titulo']}\n\n{livro['sinopse']}", justify="left")
        lbl_texto.pack(side="left", padx=10)

        botaoremover = ctk.CTkButton(frame, text="Remover", command=lambda l=livro: removerlivro(categoria, l), fg_color= "black", hover_color= "gray")
        botaoremover.pack(side="right", padx=5)

        destino = "lidos" if categoria == "estoulendo" else "estoulendo"
        botaomover = ctk.CTkButton(frame, text=f"Mover para {'Livros lidos' if destino == 'lidos' else 'Estou lendo'}", 
                                   command=lambda l=livro: moverlivro(categoria, destino, l), fg_color= "black", hover_color= "gray")
        botaomover.pack(side="right", padx=5)

def abrirjanela(categoria):
    # Esconde o frame principal
    estante_frame.pack_forget()
    
    # Criação do Frame de Botões (Voltar e Adicionar)
    frame_botoes = ctk.CTkFrame(estante)
    frame_botoes.pack(fill="x", side="top", pady=10)

    # Adicionando o botão Voltar
    ctk.CTkButton(frame_botoes, text="Voltar", command=lambda: voltar(categoria, frame_botoes), fg_color= "black", hover_color= "gray").pack(side="top", padx=5, pady=5)

    # Exibindo o botão "Adicionar livro" no frame de livros (só uma vez)
    ctk.CTkButton(frame_botoes, text="Adicionar livro", command=lambda: adicionarlivro(categoria), fg_color= "black", hover_color= "gray").pack(side="top", padx=5, pady=5)

    if categoria == "lidos":
        janela = frame_lidos
    else:
        janela = frame_estoulendo
    
    janela.pack(fill="both", expand=True)
    # Atualiza a janela para mostrar os livros
    atualizarjanela(categoria)

def voltar(categoria, frame_botoes):
    # Esconde o frame de livros e de botões
    if categoria == "lidos":
        frame_lidos.pack_forget()
    else:
        frame_estoulendo.pack_forget()

    frame_botoes.pack_forget()  # Esconde o frame de botões também

    # Exibe o frame principal
    estante_frame.pack(fill="both", expand=True)

def simple_input(mensagem):
    def confirmar():
        entrada_usuario.append(entry.get())
        janela_input.destroy()

    entrada_usuario = []
    janela_input = ctk.CTkToplevel()
    janela_input.title("Entrada de texto")

    ctk.CTkLabel(janela_input, text=mensagem).pack(pady=5)

    entry = ctk.CTkEntry(janela_input)
    entry.pack(pady=5)

    ctk.CTkButton(janela_input, text="Confirmar", command=confirmar, fg_color= "black", hover_color= "gray").pack(pady=5)

    janela_input.wait_window()
    return entrada_usuario[0] if entrada_usuario else None

def fechar():
    salvar_livros()
    estante.destroy()

# Janela principal
estante = ctk.CTk()
estante.title("Estante")
estante.geometry('800x600')

# Frame principal da estante
estante_frame = ctk.CTkFrame(estante)
estante_frame.pack(fill="both", expand=True)

# Botões principais
ctk.CTkButton(estante_frame, text="Livros lidos", command=lambda: abrirjanela("lidos"), fg_color= "black", hover_color= "gray").pack(pady=10)
ctk.CTkButton(estante_frame, text="Estou lendo", command=lambda: abrirjanela("estoulendo"), fg_color= "black", hover_color= "gray").pack(pady=10)

# Frames secundários
frame_lidos = ctk.CTkFrame(estante)
frame_estoulendo = ctk.CTkFrame(estante)

# Carregar livros
carregar_livros()

# Iniciar o loop do tkinter
estante.protocol("WM_DELETE_WINDOW", fechar)

estante.mainloop()
from tkinter import *
import customtkinter as ctk
from customtkinter import CTk
from CustomTkinterMessagebox import CTkMessagebox
from customtkinter import filedialog
from PIL import Image, ImageTk, ImageDraw
import pandas as pd
from tkinter import messagebox
import os 

# ! Projeto de PEOO - Anna Clara, Enzo Riquelme, Hellen Vitória e Kauã Angelo

# * aparência
ctk.set_appearance_mode('light')


#* janela principal
def janelainicial(): #parte de ANNA
	app = ctk.CTk()
	app.title('Goodreads')
	app.geometry('500x500')
	app.resizable(False, False)

	# * janela do cadastro
	def fazer_cadastro():
		app.destroy()
		janelacadast = ctk.CTk()
		janelacadast.title('Cadastro')
		janelacadast.geometry('500x500')
		janelacadast.resizable(False, False)
		# ? janelacadast.after(1, lambda:janelacadast.state('zoomed')) - pra abrir tela maximizada 

		# * labels e entries
		nome = ctk.CTkLabel(janelacadast, text='Nome:', font=("Courier", 16, 'bold'))
		nome.pack(pady = (125, 2))
		nome_entry = ctk.CTkEntry(janelacadast, placeholder_text= '  Como podemos te chamar?', width = 180)
		nome_entry.pack()
		user_cadastro = ctk.CTkLabel(janelacadast, text='Usuário:', font=("Courier", 16, 'bold'))
		user_cadastro.pack()
		usercad_entry= ctk.CTkEntry(janelacadast, placeholder_text= ' Escolha um nome de usuário', width = 185)
		usercad_entry.pack()
		passw_cadastro = ctk.CTkLabel(janelacadast, text='Senha:', font=("Courier", 16, 'bold'))
		passw_cadastro.pack()
		passwc_entry = ctk.CTkEntry(janelacadast, placeholder_text= ' Escolha sua senha!', width = 130, show = '●')
		passwc_entry.pack()

		# todo: INSERÇÃO DA BIBLIOTECA PANDAS PARA CRIAR CONTA
		def criar_conta():
			usuarios = "cadastros.xlsx"
			usuarios_cad = pd.read_excel(usuarios)

			name = nome_entry.get()
			user = usercad_entry.get()
			passw = passwc_entry.get()

			novo_cad = [name, user, passw]  # os valores devem estar na mesma ordem das colunas

			# adicionando ao DataFrame
			usuarios_cad.loc[len(usuarios_cad)] = novo_cad
			usuarios_cad.to_excel(usuarios_cad, index=False) #index:False serve pra não add indice na tabela, algo que é padrão do pandas


		criação = ctk.CTkButton(janelacadast, text = 'Criar conta', command=criar_conta, fg_color ='black', hover_color = 'gray')
		criação.pack(pady = (12, 5))
		
		def voltar_inicio():
			janelacadast.destroy()
			janelainicial()

		voltar = ctk.CTkButton(janelacadast, text= 'Página inicial', command= voltar_inicio, fg_color ='black', hover_color = 'gray')
		voltar.pack(pady = (5, 3))

		janelacadast.mainloop()

	# * janela do login
	def fazer_login():
		app.destroy()
		janelalogin = ctk.CTk()
		janelalogin.title('Log-in')
		janelalogin.geometry('500x500')
		janelalogin.resizable(False, False)

		#? funcionalidade a definir se será utilizada
		# ? label_nome = tk.Label(janela2, text = "Nome")
		# ? label_nome.grid(row = 0, column = 0 )
		# ? botao_voltar = tk.Button(janela2, text = 'Fechar a janela2', command = janela2.destroy)
		# ? botao_volta.grid(row = 1, column = 0)

		# * labels e entry´s
		user = ctk.CTkLabel(janelalogin, text='Usuário', font=("Courier", 16, 'bold'))
		user.pack(pady = (150, 5))
		user_entry = ctk.CTkEntry(janelalogin, placeholder_text="Digite seu nome de usuário aqui", width = 202)
		user_entry.pack()
		password = ctk.CTkLabel(janelalogin, text='Senha', font=("Courier", 16, 'bold'))
		password.pack() 
		password_entry = ctk.CTkEntry(janelalogin, placeholder_text="Digite a senha da sua conta aqui", width = 202, show = '●')
		password_entry.pack()


		# * funcionalidades da tela de log-in
		def validar_login():
			usuarios = "cadastros.xlsx"
			usuarios_cad = pd.read_excel(usuarios, dtype = str)

			user_input = user_entry.get().strip()
			password_input = str((password_entry).get()).strip()

			if user_input in usuarios_cad['USUARIO'].values:
				usuario_dados = usuarios_cad[usuarios_cad['USUARIO'] == user_input] #filtra a linha com o valor que queremos

				if not usuario_dados.empty:
					senha_correta = str(usuario_dados.iloc[0]['SENHA']).strip()

					if password_input == senha_correta:
						janelaprincipal(usuario_dados)

					else:
						CTkMessagebox.messagebox(title='Aviso', text='Senha Incorreta', button_text='Tentar novamente') 
				
				else:
					CTkMessagebox.messagebox(title='Aviso', text='Esse usuário não existe', button_text='Faça seu cadastro', fg_color = 'black')
				
			else:
				CTkMessagebox.messagebox(title='Aviso', text='Usuário não encontrado', button_text='Tentar novamente') 
				

		# * botão para validar o log-in
		validar = ctk.CTkButton(janelalogin, text='Validar', command= validar_login, fg_color='black', hover_color='gray')
		validar.pack(pady=(15, 5))

		def voltar():
			janelalogin.destroy()
			janelainicial()
		voltar = ctk.CTkButton(janelalogin, text='Página inicial', command= voltar, fg_color='black', hover_color='gray')
		voltar.pack(pady=(5, 3))


		janelalogin.mainloop()


	# * TELA INICIAL - LOGIN/CADASTRO
	inicio = ctk.CTkLabel(app, text='Bem vindo ao Goodreads!', font=("Courier", 20, 'bold'))
	subt = ctk.CTkLabel(app, text='Já tem uma conta?', font=("Courier", 18, 'bold'))

	inicio.pack(pady = (200, 0), anchor = 'center')  
	subt.pack(anchor = 'center')

	# * botões de login/cadastro
	botao_login = ctk.CTkButton(app, text='Fazer login', font= ('Lexend', 12), command= fazer_login, fg_color='black', hover_color='gray')
	botao_login.pack(pady=(0, 10), anchor='center')

	botao_cadastrar = ctk.CTkButton(app, text='Criar conta', font= ('Lexend', 12), command= fazer_cadastro, fg_color='black', hover_color='gray')
	botao_cadastrar.pack(pady=(0, 50), anchor='center')

	app.mainloop()

def janelaprincipal(usuario_dados): #parte de KAUÃ
	
	def account_window():
		segundajanela = ctk.CTkToplevel()
		segundajanela.title("Conta")
		segundajanela.geometry(f"500x500+{posix}+{posiy}")
		segundajanela.attributes("-topmost",True)
		# button = ctk.CTkButton(segundajanela, text="Selecionar uma imagem", command=open_image).place(x=200, y=20)
	def leituras_window():
		thirdjanela = ctk.CTkToplevel()
		thirdjanela.title("Leituras")
		thirdjanela.geometry(f"500x500+{posix}+{posiy}")
		thirdjanela.attributes("-topmost",True)
	def avaliation_window():
		thirdjanela = ctk.CTkToplevel()
		thirdjanela.title("Avaliação")
		thirdjanela.geometry(f"500x500+{posix}+{posiy}")
		thirdjanela.attributes("-topmost",True)
	def config_window():
		thirdjanela = ctk.CTkToplevel()
		thirdjanela.title("Configurações")
		thirdjanela.geometry(f"500x500+{posix}+{posiy}")
		thirdjanela.attributes("-topmost",True)
	janela_principal = ctk.CTk()
	janela_principal.title("Tela principal")
	janela_principal.after(1,lambda:janela_principal.state("zoomed"))

	#configuração da dimensão da janela
	janela_altura = 900
	janela_largura = 1100
	largura = janela_principal.winfo_screenwidth()
	altura = janela_principal.winfo_screenheight()
	posiy = int(altura/2) - int(janela_altura/2)
	posix = int(largura/2) - int(janela_largura/2)
	janela_principal.geometry(f"{janela_largura}x{janela_altura}+{posix}+{posiy}")

	#implementação gráfica dos recursos (layout)
	canvas = ctk.CTkCanvas(janela_principal,width=largura,height=altura,bg="gray",highlightthickness=0)
	canvas.place(x=0,y=0)
	canvas.create_rectangle(0,0,300,altura,fill='black',outline="")
	canvas.create_oval(75,75,225,225,fill="gray",outline="")

	def centraliza(usuario_dados):
		ctk.CTkLabel(janela_principal,text="Goodreads",font=("Arial",25,"bold"),text_color="white",bg_color="gray").place(x=340,y=25)
		usuário = str(usuario_dados.iloc[0]['USUARIO']).strip()
		tamanho_mediu = 10
		tamanho_usuário2 = len(usuário) * tamanho_mediu
		pussix = 150 - (tamanho_usuário2//2)
		nome = str(usuario_dados.iloc[0]['NOME']).strip()
		tamanho_nome= len(nome) * tamanho_mediu
		passix = 150 - (tamanho_nome//2)
		ctk.CTkLabel(janela_principal,text=f"Seja bem vindo, {nome}! Como estão as leituras?",font=("Arial",40,"bold"),text_color="white",bg_color="gray").place(x=340,y=150)
		#ctk.CTkLabel(janela_principal, text = 'Sugestões:', font=("Arial",25,"bold"),text_color="white",bg_color="gray").place(x=340,y=200)
		ctk.CTkLabel(janela_principal,text=f"@{usuário}",font=("Arial",15),text_color="white",bg_color="black").place(x=pussix,y=275)
		ctk.CTkLabel(janela_principal,text=f"{nome}",font=("Arial",15),text_color="white",bg_color="black").place(x=passix,y=250)
	# def open_image():
	# 	file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.jfif"])
	# 	if file_path:
	# 		try:
	# 			img = Image.open(file_path)
	# 			img = img.resize((250, 250))
	# 			mask = Image.new("L", img.size, 0)
	# 			draw = ImageDraw.Draw(mask)
	# 			draw.ellipse((0, 0, img.size[0], img.size[1]), fill=255)
	# 			img.putalpha(mask)
	# 			img_tk = ImageTk.PhotoImage(img)
	# 			image_label.configure(image=img_tk)
	# 			image_label.image = img_tk
	# 		except Exception as e:
	# 			print(f"Erro ao abrir imagem: ")
	frame = ctk.CTkFrame(janela_principal, height=300, width=300)
	frame.place(x=0, y=10)
	image_label = ctk.CTkLabel(frame,text="",bg_color="black")
	image_label.place(relwidth=1, relheight=1)

	centraliza(usuario_dados)

	#parte de HELLEN - progresso de leitura
	def janelaprogresso():
		entrada = ctk.CTk ()
		entrada.title ('Histórico de Leitura')
		entrada.geometry ('400x500')
		entrada.resizable (False, False)

		#definição da barra de rolagem da página
		scrollabel_frame = ctk.CTkScrollableFrame (entrada)
		scrollabel_frame.pack (fill="both", expand=True)

		escolha_livro = ctk.CTkEntry (scrollabel_frame, placeholder_text= "      Escolha o livro")
		escolha_livro.pack (pady = (25, 10))

		escolhendo = open ("estou_lendo.txt")
		for cada_linha in escolhendo:
			print (cada_linha, end= "")

		#função para carregar o progresso de livros de um arquivo de texto
		def carregar_progresso():
			livros = []
			try:
				with open("progresso_leitura.txt", "r") as file:
					livro_atual = {}
					for line in file:
						line = line.strip()
						if line.startswith("Título:"):
							if livro_atual:
								livros.append(livro_atual)
							livro_atual = {"titulo": line.replace("Título: ", "")}
						elif line.startswith("Progresso:"):
							progresso_str = line.replace("Progresso: ", "").split()[0]
							if progresso_str.isdigit():
								livro_atual["progresso"] = int (progresso_str)
							else:
								livro_atual["progresso"] = 0    
						elif line.startswith("Impressão:"):
							livro_atual["impressão"] = line.replace("Impressão: ", "")
						elif line.startswith("Reação:"):
							livro_atual["reação"] = line.replace("Reação: ", "")
					if livro_atual:
						livros.append(livro_atual)
			except FileNotFoundError:
				pass  #se o arquivo não existir, retornamos uma lista vazia
			return livros

		#função para salvar o progresso de livros em um arquivo de texto
		def salvar_progresso(livros):
			with open("progresso_leitura.txt", "w") as file:
				for livro in livros:
					file.write(f"Título: {livro['titulo']}\n")
					file.write(f"Progresso: {livro['progresso']} páginas\n")
					file.write(f"Impressão: {livro['impressão']}\n")
					file.write(f"Reação: {livro['reação']}\n")
					file.write("\n")

		#função para atualizar o progresso de um livro
		def atualizar_progresso(livros, titulo, progresso, impressão, reação):
			for livro in livros:
				if livro["titulo"] == titulo:
					livro["progresso"] = progresso
					livro["impressão"] = impressão
					livro["reação"] = reação
					break
			else:
				livros.append ({"titulo": titulo, "progresso": progresso, "impressão": impressão, "reação": reação})
			salvar_progresso(livros)

		livros = carregar_progresso ()

		#trabalhando com um livro especifico 
		titulo = "Livro"  #o título do livro que você quer acompanhar
		livro_encontrado = next((livro for livro in livros if livro["titulo"] == titulo), None)

		if livro_encontrado:
			progresso = livro_encontrado["progresso"]
			impressão = livro_encontrado["impressão"]
		else:
			progresso = 0  #se o livro não for encontrado, assume que o progresso é 0
			impressão = ""

		#criação dos campos
		tit = ctk.CTkLabel (scrollabel_frame, text = 'Impressões de Leitura', font = ("Arial", 14, "bold"))
		tit.pack (pady = (50, 10))

		caixa1 = ctk.CTkTextbox (scrollabel_frame, height = 150, width = 250, font= ("Arial", 12)) 
		caixa1.insert ("0.0", impressão) 
		caixa1.pack (pady = (10, 10))

		'''scrollbar = ctk.CTkScrollbar (scrollabel_frame, command = caixa1.yview)
		scrollbar.pack (side = "right", fill = "y")'''

		'''#feedback dos spoilers
		spoiler_feedback = ctk.CTkLabel(scrollabel_frame, text="", font=("Arial", 12), fg_color="white", text_color="red")
		spoiler_feedback.pack(pady=(5, 20))

		#verificação de spoiler 
		def valida_spoiler ():
			impressão = caixa1.get ()
			spoiler = ["morreu", "revelou", "transformou", "spoiler"]
			if any (spoiler in impressão.lower() for spoiler in spoiler):
				spoiler_feedback.configure (text = "⚠️ Cuidado! Seu comentário contém spoiler.", text_color = "red")
			else:
			spoiler_feedback.configure (text = "✅ Seu comentário não contém spoilers!", text_color = "green")

		spoiler_opcional = ctk.CTkButton (scrollabel_frame, text = 'Contém spoiler', command = valida_spoiler )
		spoiler_opcional.pack (pady = (0, 10))'''

		#função de salvar a impressão e progresso do livro
		def salvar_dados_livro():
			progresso = caixa2.get()
			impressão = caixa1.get("0.0", "end")
			reação = op_selecionada.get()
			atualizar_progresso(livros, titulo, progresso, impressão, reação)
			messagebox.showinfo("Progresso Atualizado", "Os dados do livro foram atualizados!")

		#função de validação da caixa de paginas - em número
		def validar_número (input):
			return input == "" or input.isdigit ()

		tit2 = ctk.CTkLabel (scrollabel_frame, text = 'Paginômetro', font = ("Arial", 14, "bold"))
		tit2.pack (pady = (50, 10))
		validação_numerica = ctk.StringVar ()
		#determina que a caixa do paginometro receberá somente números 
		caixa2 = ctk.CTkEntry (scrollabel_frame, placeholder_text = 'Digite seu progresso', width = 200, validate = 'key', validatecommand = (
			entrada.register(validar_número), '%P') )
		caixa2.pack ()

		#feedback visual do progresso
		progresso_feedback = ctk.CTkLabel (scrollabel_frame, text = "Progresso: 0 páginas", font = ('Arial', 12))
		progresso_feedback.pack (pady = 5)

		def atualização_entrada (event):
			progresso = caixa2.get()
			if progresso.isdigit ():
				progresso_feedback.configure (text = f"Progresso: {progresso} páginas")
			else:
				progresso_feedback.configure (text = "Progresso: 0 páginas")

		caixa2.bind ('<KeyRelease>',atualização_entrada)     
		
		#armazenamento de seleção
		op_selecionada = ctk.StringVar (value = "escolha") 

		#função da escolha do emoji
		def mostrar_escolha ():
			escolha_feedback.configure (text = f"Você escolheu: {op_selecionada.get()}")

		tit3 = ctk.CTkLabel (scrollabel_frame, text = 'Adicionar reação...', font = ("Arial", 14, "bold"))
		tit3.pack (pady = (50, 10))

		#frame para organizar os botões de reação (do tit3)
		reação_frame = ctk.CTkFrame (scrollabel_frame)
		reação_frame.pack (pady = 10)

		#opções de reação 
		escolha1 = ctk.CTkRadioButton (reação_frame, text= "😍 Amando", variable= op_selecionada, value= 'Amando', command= mostrar_escolha)
		escolha1.pack (side = ctk.TOP, pady = 2)
		escolha2 = ctk.CTkRadioButton (reação_frame, text= "😱 Espantado", variable= op_selecionada, value= 'Espantado', command= mostrar_escolha)
		escolha2.pack (side = ctk.TOP, pady = 3)
		escolha3 = ctk.CTkRadioButton (reação_frame, text= "🧐 Confuso", variable= op_selecionada, value= 'Confuso', command= mostrar_escolha)
		escolha3.pack (side = ctk.TOP, pady = 4)
		escolha4 = ctk.CTkRadioButton (reação_frame, text= "😭 Triste", variable= op_selecionada, value= 'Triste', command= mostrar_escolha)
		escolha4.pack (side = ctk.TOP, pady = 5)
		escolha5 = ctk.CTkRadioButton (reação_frame, text= "🙄 Frustrado", variable= op_selecionada, value= 'Frustrado', command= mostrar_escolha)
		escolha5.pack (side = ctk.TOP, pady = 6)
		escolha6 = ctk.CTkRadioButton (reação_frame, text= "😡 Irritado", variable= op_selecionada, value= 'Irritado', command= mostrar_escolha)
		escolha6.pack (side = ctk.TOP, pady = 7)

		escolha_feedback = ctk.CTkLabel (scrollabel_frame, text = "Escolha uma reação..", font = ("Arial", 12), text_color = "black")
		escolha_feedback.pack (pady = 5)

		# Botão para salvar as alterações
		botao_salvar = ctk.CTkButton(scrollabel_frame, text="Salvar progresso", command=salvar_dados_livro, fg_color= "black", hover_color = "gray")
		botao_salvar.pack(pady=20)

		entrada.mainloop ()

	def janelaleitura():
		
		livros_lidos = []
		estou_lendo = []

		# Salva os livros em um arquivo de texto
		def salvar_livros():
			caminho_lidos = "livros_lidos.txt"
			caminho_lendo = "estou_lendo.txt"
			
			with open(caminho_lidos, "w") as arquivo:
				for livro in livros_lidos:
					arquivo.write(f"{livro['titulo']}|{livro['autor']}|{livro['imagem']}\n")
			
			with open(caminho_lendo, "w") as arquivo:
				for livro in estou_lendo:
					arquivo.write(f"{livro['titulo']}|{livro['autor']}|{livro['imagem']}\n")

		def carregar_livros():
			caminho_lidos = "livros_lidos.txt"
			caminho_lendo = "estou_lendo.txt"
			
			if os.path.exists(caminho_lidos):
				with open(caminho_lidos, "r") as arquivo:
					for linha in arquivo:
						if linha.strip():  # Verifica se a linha não está vazia
							partes = linha.strip().split("|")
							if len(partes) == 3:
								titulo, autor, imagem = linha.strip().split("|")
								livros_lidos.append({"titulo": titulo, "autor": autor, "imagem": imagem})

			if os.path.exists(caminho_lendo):
				with open(caminho_lendo, "r") as arquivo:
					for linha in arquivo:
						if linha.strip():  # Verifica se a linha não está vazia
							partes = linha.strip().split("|")
							if len(partes) == 3:
								titulo, autor, imagem = linha.strip().split("|")
								estou_lendo.append({"titulo": titulo, "autor": autor, "imagem": imagem})

		def adicionarlivro(categoria):
			caminhoimagem = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])
			if not caminhoimagem:
				return
			titulo = simple_input("Digite o título: ")
			if not titulo:
				return
			autor = simple_input("Digite o nome do autor: ")
			if not autor:
				return
			livro = {"titulo": titulo, "imagem": caminhoimagem, "autor": autor}

			if categoria == "lidos":
				livros_lidos.append(livro)
			else:
				estou_lendo.append(livro)

			atualizarjanela(categoria)

		def removerlivro(categoria, livro):
			if categoria == "lidos":
				livros_lidos.remove(livro)
			else:
				estou_lendo.remove(livro)

			atualizarjanela(categoria)

		def moverlivro(origem, destino, livro):
			removerlivro(origem, livro)

			if destino == "lidos":
				livros_lidos.append(livro)
			else:
				estou_lendo.append(livro)
			atualizarjanela(destino)

		def atualizarjanela(categoria):
			janela = frame_lidos if categoria == "lidos" else frame_estoulendo

			# Limpa todos os widgets (livros) antigos antes de atualizar a lista
			for widget in janela.winfo_children():
				widget.destroy()

			lista = livros_lidos if categoria == "lidos" else estou_lendo

			for livro in lista:
				frame = ctk.CTkFrame(janela, width=400, height=150)  # Ajuste na largura e altura do frame
				frame.pack(pady=5, padx=10, fill="x")
				
				if os.path.exists(livro["imagem"]):
					imagem = Image.open(livro["imagem"])
					imagem.thumbnail((100, 150))
					img_tk = ImageTk.PhotoImage(imagem)
				else: 
					print(f"Imagem não encontrada: {livro['imagem']}")

				lbl_img = ctk.CTkLabel(frame, image= img_tk)
				lbl_img.image = img_tk  
				lbl_img.pack(side="left", padx=10)

				lbl_texto = ctk.CTkLabel(frame, text=f"{livro['titulo']}\n\n{livro['autor']}", justify="left")
				lbl_texto.pack(side="left", padx=10)

				botaoremover = ctk.CTkButton(frame, text="Remover", command=lambda l=livro: removerlivro(categoria, l), fg_color= "black", hover_color= "gray")
				botaoremover.pack(side="right", padx=5)

				destino = "lidos" if categoria == "estoulendo" else "estoulendo"
				botaomover = ctk.CTkButton(frame, text=f"Mover para {'Livros lidos' if destino == 'lidos' else 'Estou lendo'}", 
										command=lambda l=livro: moverlivro(categoria, destino, l), fg_color= "black", hover_color= "gray")
				botaomover.pack(side="right", padx=5)

				#janela.pack()

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

	#botões
	botao_conta = ctk.CTkButton(janela_principal,text="Conta",fg_color="black",hover_color="gray",bg_color="black",text_color="white",font=("Arial",20,"bold"),command=account_window).place(x=80,y=500)
	botao_avaliação = ctk.CTkButton(janela_principal,text="Avaliação",fg_color="black",hover_color="gray",bg_color="black",text_color="white",font=("Arial",20,"bold"),command=janelaprogresso).place(x=80,y=350)
	botao_leitura = ctk.CTkButton(janela_principal,text="Leitura",fg_color="black",hover_color="gray",bg_color="black",text_color="white",font=("Arial",20,"bold"),command=janelaleitura).place(x=80,y=425)
	botao_config = ctk.CTkButton(janela_principal,text="Configurações",fg_color="black",hover_color="gray",bg_color="black",text_color="white",font=("Arial",14,"bold"),command=config_window).place(x=150,y=altura-100)

	janela_principal.mainloop()


janelainicial()

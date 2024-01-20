import PySimpleGUI as sg


# CRIANDO LAYOUT
def criar_janela_incial():
	sg.theme('DarkBlue4')
	linha = [
		[sg.Input('')]
	]
	layout = [
		[sg.Frame('Tarefas', Layout=linha, key='container')],
		[sg.Button('Executar'), sg.Button('Limpar')]
	]
	
	return sg.Window('BOT Primárias SIS', Layout=layout, finalize=true)

# CRIAR JANELA
janela = criar_janela_incial()

# CRIAR AS REGRAS DESSA JANELA

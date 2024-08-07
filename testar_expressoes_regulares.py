import re
import PySimpleGUI as sg

# Função para testar a expressão regular
def testar_regex(expressao, texto):
    try:
        correspondencias = re.findall(expressao, texto)
        if correspondencias:
            return f"Correspondencias encontradas: {', '.join(correspondencias)}"
        else:
            return "Nenhuma correspondência encontrada."
    except re.error as e:
        return f"Erro na expressão regular: {e}"

# Layout da interface gráfica
layout = [
    [sg.Text('Expressao Regular'), sg.InputText(key='-EXPRESSAO-')],
    [sg.Text('Texto de Teste:'), sg.Multiline(key='-TEXTO-', size=(50, 10))],
    [sg.Button('Testar'), sg.Button('Sair')],
    [sg.Text('', size=(50, 1), key='-RESULTADO-')]
]

# Criação da janela
janela = sg.Window('Validador de Expressões Regulares', layout)

# Loop principal da interface gráfica
while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == 'Sair':
        break

    if evento == 'Testar':
        expressao = valores['-EXPRESSAO-']
        texto = valores['-TEXTO-']
        resultado = testar_regex(expressao, texto)
        janela['-RESULTADO-'].update(resultado)

janela.close()
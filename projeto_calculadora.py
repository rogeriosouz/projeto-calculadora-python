from PySimpleGUI import PySimpleGUI as sg

sg.theme('Black')


def calculadora():
    layout = [
        [sg.Text(key='conta', font=10)],
        [sg.Text(key='tela_result', pad=10, font=26)],
        [sg.Button('<', size=(5, 0)), sg.Button(
            'C', size=(5, 0)), sg.Button('', size=(5, 0),),
            sg.Button('÷', size=(5, 0))],
        [sg.Button('7', size=(5, 0)), sg.Button('8', size=(5, 0)),
         sg.Button('9', size=(5, 0)), sg.Button('x', size=(5, 0))],
        [sg.Button('4', size=(5, 0)), sg.Button('5', size=(5, 0)),
         sg.Button('6', size=(5, 0)), sg.Button('-', size=(5, 0))],
        [sg.Button('1', size=(5, 0)), sg.Button('2', size=(5, 0)), sg.Button(
            '3', size=(5, 0)), sg.Button('+', size=(5, 0))],
        [sg.Button('0', size=(5, 0)), sg.Button('=', size=(5, 0))]
    ]

    janela_calculadora = sg.Window('calculadora', layout=layout,
                                   element_justification='center',
                                   finalize=True)
    conta = ''
    while True:
        eventos, valores = janela_calculadora.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos:
            janela_calculadora['tela_result'].update('')
            if eventos != '=' and eventos != '<' and eventos != 'C':
                janela_calculadora['conta'].update('')
                conta += eventos
                janela_calculadora['tela_result'].update(conta)
            elif eventos == '<':
                janela_calculadora['conta'].update('')
                for c in conta:
                    conta = conta[:-1]
                    janela_calculadora['tela_result'].update(conta)
                    break

            elif eventos == 'C':
                janela_calculadora['conta'].update('')
                conta = ''
                janela_calculadora['tela_result'].update(conta)
            else:
                try:
                    conta = conta.replace('x', '*')
                    conta = conta.replace('÷', '/')
                    resultado = eval(conta)
                    janela_calculadora['tela_result'].update(resultado)
                    conta = conta.replace('*', ' x ')
                    conta = conta.replace('/', ' ÷ ')
                    conta = conta.replace('+', ' + ')
                    conta = conta.replace('-', ' - ')
                    janela_calculadora['conta'].update(conta + ' =')
                    conta = ''
                except Exception:
                    conta = ''
                    janela_calculadora['tela_result'].update(conta)


calculadora()

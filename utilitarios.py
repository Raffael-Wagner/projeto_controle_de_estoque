import smtplib
import email.message
import json
import matplotlib.pyplot as plt


def credenciais_email():
    with open("credenciais.json") as arquivo:
        dados = json.load(arquivo)
        return [dados["email_usuario"], dados["password"]]

def enviar_email(nome, quantidade, quantidade_min, fornecedor):
    email_usuario,password = credenciais_email()
    reabastecer = int(quantidade_min) * 3
    corpo_email = f"""
    <p>Olá, caro(a) fornecedor(a)</p>
    <hr>
    <p>A Equipe EstoKI vem, por meio desta, informar que nosso estoque do produto {nome} está ficando baixo. Atualmente, nos restam apenas {quantidade} unidades em nosso estoque, sendo insuficiente para atender à demanda que espera-se para o próximo mês.</p>
    <p>Sabendo que o produto tem uma certa popularidade e vem mostrando rapidez em vendas, gostaríamos de realizar a solicitação do reabastecimento de {reabastecer} unidades o mais rápido possível. Agradecemos sua atenção. </p>
    <p>Atenciosamente,</p>
    <p>EstoKI</p>
    """

    msg = email.message.EmailMessage()
    msg['Subject'] = "Reposição de Estoque"
    msg['From'] = email_usuario
    msg['To'] = fornecedor
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))


def mostrar_grafico(saidas, filename='grafico.pdf'):
    nomes = list(saidas.keys())
    saidas = list(saidas.values())

    produtos_ordenados = sorted(zip(nomes, saidas), key=lambda x: x[1], reverse=True)

    top_produtos = produtos_ordenados[:10]
    nomes_top = []
    saidas_top = []

    for produto in top_produtos:
        nomes_top.append(produto[0])
        saidas_top.append(produto[1])

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.bar(nomes_top, saidas_top, color='red')

    ax.set_xlabel('Produtos')
    ax.set_ylabel('Quantidade Retirada')
    ax.set_title('Top 10 Saídas de Produtos')

    plt.tight_layout()
    plt.savefig(filename)

def codigo_existente(tw_estoque, codigo):
    for index in range(tw_estoque.topLevelItemCount()):
        item = tw_estoque.topLevelItem(index)
        if item.text(0) == codigo:
            return True
    return False

def nome_existente(tw_estoque, nome):
    for index in range(tw_estoque.topLevelItemCount()):
        item = tw_estoque.topLevelItem(index)
        if item.text(1) == nome:
            return True
    return False
# -*- coding: utf-8 -*-
#variáveis de armazenamento
cod_pedido = '' #recebe o código do pedido
soma = 0.00 #acumulador para soma dos valores
cont = 0 #contador para controle do laço com acumulador
#definição das opções para seleção
while True: #loop para repetição do programa para adição de multiplos pedidos
  print('----------------------------------------------------------------------')
  print('[TR - SABOR TRADICIONAL || ES - SABOR ESPECIAL || PR - SABOR PREMIUM] ')
  print('[TAMANHO P: 500ml || TAMANHO M: 1000ml || TAMANHO G: 2000ml]')
  cod_pedido = input('Digite o Código do Sabor e Tamanho Escolhido [Ex. TR-P]: ')
  #os ifs e elifs verificam a opção colocada no input e adicionam o valor do sorvete a soma
  if cod_pedido == 'TR-P':
    print('Sabor Tradicional Pequeno Selecionado.')
    soma = soma + 6.00
    cont = cont + 1
  elif cod_pedido == 'ES-P':
    print('Sabor Especial Pequeno Selecionado.')
    soma = soma + 7.00
    cont = cont + 1
  elif cod_pedido == 'PR-P':
    print('Sabor Premium Pequeno Selecionado.')
    soma = soma + 8.00
    cont = cont + 1
  elif cod_pedido == 'TR-M':
    print('Sabor Tradicional Médio Selecionado.')
    soma = soma + 10.00
    cont = cont + 1
  elif cod_pedido == 'ES-M':
    print('Sabor Especial Médio Selecionado.')
    soma = soma + 12.00
    cont = cont + 1
  elif cod_pedido == 'PR-M':
    print('Sabor Premium Médio Selecionado.')
    soma = soma + 14.00
    cont = cont + 1
  elif cod_pedido == 'TR-G':
    print('Sabor Tradicional Grande Selecionado.')
    soma = soma + 18.00
    cont = cont + 1
  elif cod_pedido == 'ES-G':
    print('Sabor Especial Grande Selecionado.')
    soma = soma + 21.00
    cont = cont + 1
  elif cod_pedido == 'PR-G':
    print('Sabor Premium Grande Selecionado.')
    soma = soma + 24.00
    cont = cont + 1
  else: #verifica o input escrito
    print('Sabor/Tamanho/Formato Inválido!')
    continue #retorna para o while em caso de opção inválida
  novo_pedido = input('Deseja Algo Mais? [S/N]: ')
  if novo_pedido == 'S':
    continue #retorna para o inicio do laço p/ adição de pedidos
  else:
    break #finaliza o loop
print('----------------------------------------------------------------------')
print('Você Pediu', cont , 'Sorvete(s).')
print('Seu Total É: R$', soma)

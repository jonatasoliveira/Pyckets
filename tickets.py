#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import json
try:
    card_number = int(raw_input('Digite o numero do cartão: '))
except:
    print 'Numero de cartão inválido.'
    exit(1)


url = 'http://www.ticket.com.br/ticket-corporativo-web/ticket-consultcard?txtNumeroCartao=%s&txtOperacao=saldo_agendamentos&cardNumber=' % card_number
url_compras = 'http://www.ticket.com.br/ticket-corporativo-web/ticket-consultcard?txtOperacao=lancamentos&txtNumeroCartao=%s' % card_number

page = urllib.urlopen(url).read()
resultado = json.loads(page)

print '#' * 23

print "Numero cartao: %s" % resultado['cardNumber']
print "Credito Atual: R$ %s" % resultado['seeBalance']
print
print "Proxima recarga: %s" % resultado['schedulings'][0]['date']
print "Valor: R$ %s" % resultado['schedulings'][0]['value']
print
print resultado['schedulings'][0]['description']

print '#' * 23
print
print
print '#' * 23
print 'ULTIMAS COMPRAS'
compras = json.loads(urllib.urlopen(url_compras).read())
for i in compras['releases']:
    print i['description']
    print "valor: R$ %s" % i['value']
    print

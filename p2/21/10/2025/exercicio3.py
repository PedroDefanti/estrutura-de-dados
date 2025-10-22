#EXERCICIO 3

def reverter(s):
    if s=='':
        return ''
    else:
        return s[-1]+reverter(s[:-1])
palavra="Itaipuaçu"
palavra_inversa=reverter(palavra)
print(f'o inverso de {palavra} é {palavra_inversa}')
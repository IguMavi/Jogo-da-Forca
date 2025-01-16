import random

esportes = ["futebol", "basquete", "volei", "tenis", "natacao", "atletismo", "rugby", "golfe", "handebol", "boxe", "mma", "escalada", "ciclismo", "xadrez", "judo", "karate", "beisebol", "hoquei", "luta livre", "patinacao", "squash", "esgrima", "maratona", "handebol", "ginastica", "kitesurf", "surf", "skate", "parapente", "bmx"]
instrumentos = ["violao", "guitarra", "piano", "bateria", "baixo", "flauta", "saxofone", "trompete", "clarinete", "violino", "cello", "harpa", "acordeon", "teclado", "corneta", "trombone", "marimba", "xilofone", "pandeiro", "cavaquinho", "gaita", "conga", "surdo", "triangulo", "djembe", "cymbalo", "castanholas", "banjo", "sanfona", "rebec", "fagot", "timpani", "crotalos"]
roupas = ["camisa", "calca", "bermuda", "saia", "shorts", "blusa", "jaqueta", "manto", "casaco", "blazer", "vestido", "macacao", "sueter", "regata", "luva", "meia", "bota", "sapato", "sandalia", "chapeu", "bone", "bikini", "cueca", "sutia", "pijama", "top", "jaquetao", "blusao", "pullover", "traje", "gravata", "tailleur", "blusinha"]
comidas = ["arroz","feijao","frango","carne","peixe","salada","fruta","legume","massa","pao","queijo","leite","ovo","sorvete","pizza","hamburguer","batata","sopa","macarrao","torrada","bolo","doces","churrasco","torta","sucos","cafe","chocolate","panqueca","queijo","azeite","maionese","molho","cereal","vitamina","sanduiche","pastel","feijoada","pudim","sorvete","bife"]

numero = random.randrange(1, 5)

if(numero == 1):
  lista_palavras = esportes
elif(numero == 2):
  lista_palavras = instrumentos
elif(numero == 3):
  lista_palavras = roupas
else:
  lista_palavras = comidas

palavra_secreta = random.choice(lista_palavras)
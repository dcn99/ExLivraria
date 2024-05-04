class Livro:
    def __init__(self, titulo, autor, preco):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco

class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, livro, quantidade=1):
        self.itens.append({'livro': livro, 'quantidade': quantidade})

    def remover_item(self, livro):
        for item in self.itens:
            if item['livro'] == livro:
                self.itens.remove(item)
                return

    def calcular_total(self):
        total = 0
        for item in self.itens:
            total += item['livro'].preco * item['quantidade']
        return total

# Exemplo de uso
livro1 = Livro("Python Cookbook", "David Beazley", 50.0)
livro2 = Livro("Fluent Python", "Luciano Ramalho", 45.0)

carrinho = Carrinho()
carrinho.adicionar_item(livro1)
carrinho.adicionar_item(livro2, 2)

print("Itens no carrinho:")
for item in carrinho.itens:
    print(item['livro'].titulo, "-", item['quantidade'], "unidade(s)")

print("Total da compra:", carrinho.calcular_total())
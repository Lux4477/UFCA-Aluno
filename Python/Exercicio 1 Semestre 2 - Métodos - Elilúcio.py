class livro:
    def __init__(self, titulo, autor, ib, tema,  numero = 0):
        self.autor = autor
        self.ib = ib
        self.titulo = titulo
        self.numero = numero
        self.tema = tema

    def emprestar(self):
        pass
    def historico(self):
        pass
    def create(self):
        pass
    def read(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass

class usuario:
    def __init__(self, nome, matricula, telefone, email, endereco):
        self.nome = nome
        self.matricula = matricula
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def create(self):
        pass
    def read(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass
    def emitir_relatorio(self):
        pass

class empréstimo:
    def __init__(self, id, usuario, livro, data_retirada, data_devolucao):
        self.id = id
        self.usuario_matricula = usuario.matricula
        self.idlivro = livro.ib
        self.data_retirada = data_retirada
        self.data_devolucao = data_devolucao
    
    def calcular_multa(self):
        pass
    def create(self):
        pass
    def read(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass
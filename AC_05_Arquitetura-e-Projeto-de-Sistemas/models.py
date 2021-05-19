# models.py


from app import db


class Cliente(db.Model):
    __tablename__ = "cliente"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(40), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)

    def __init__(self, nome, email, cpf):

        self.nome = nome
        self.email = email
        self.cpf = cpf

    def __repr__(self):
        return "<Cliente %r>" % self.id

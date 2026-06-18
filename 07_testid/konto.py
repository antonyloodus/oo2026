class Konto:
  def __init__(self):
    self.saldo = 0

  def sissemakse(self, summa):
    if summa > 0:
      self.saldo += summa

  def valjamakse(self, summa):
    if 0 < summa <= self.saldo:
      self.saldo -= summa
      return True
    return False

  def jaak(self):
    return self.saldo

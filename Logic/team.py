from enum import Enum

class Categorie(Enum):
  ENFANT = 1
  ADO_G = 2
  ADO_F = 3
  ADULTE = 4

class Team:
  def __init__(self, name, category, id):
    self.name = name
    self.category = category
    self.id = id
    self.score = 0
    self.tours_kayak = 0

from Logic.race import Race
from Logic.team import Categorie
from View.scoreCourse import ViewScore
from View.changerPoints import pointsControl

import csv

import tkinter as tk 
from tkinter import ttk

class NewRaceWindow(tk.Tk):
  def __init__(self):
    super().__init__()

    self.fenetre_scores = None

    # fenetre principale pour une course
    # on y ajoute/supprime les équipes
    self.title("Gestion course")
    self.geometry('350x450')

    self.label1 = ttk.Label(self, text= "Nom de l'équipe :")
    self.label1.pack()

    self.nom_equipe_ajout = tk.Entry(self)
    self.nom_equipe_ajout.pack()

    self.label2 = ttk.Label(self, text= "Numéro de l'équipe:")
    self.label2.pack()  

    self.numero_ajout = tk.Entry(self)
    self.numero_ajout.pack()

    self.label3 = ttk.Label(self, text = "catégorie de l'équipe:")
    self.label3.pack()


    self.combo = ttk.Combobox(self,state = "readonly", values = ["Enfant", "Adulte", "Eclaireuse", "Eclaireur"])
    self.combo.pack(pady = 10)


    self.button1 = ttk.Button(self, text = 'Ajouter Equipe', command = self.addTeam)
    self.button1.pack()

    self.numero_supprimer = tk.Entry(self)
    self.numero_supprimer.pack(pady=(10,0))

    self.button2 = ttk.Button(self, text = 'Supprimer Equipe', command = self.deleteTeam)
    self.button2.pack()

    self.button3 = ttk.Button(self, text = 'Sauvegarder et quitter', command = self.saveAndExit)
    self.button3.pack(pady=10)

    self.button4 = ttk.Button(self, text = 'Voir fenetre de classement', command = self.ScoreWindowOpen)
    self.button4.pack(pady = 10)

    self.button5 = ttk.Button(self, text = 'Ouvrir fenetre de points', command = self.changeScoreWindowOpen)
    self.button5.pack(pady = 10)


    self.race = Race()


  def save(self):
    #prepare table
    sorted_teams = []
    teams = []

    for team in self.race.teams:
      sorted_teams.append(team)

    sorted_teams.sort(key = lambda x:x.score, reverse=True)

    for t in sorted_teams:
      teams.append([t.name, t.category, t.id, t.score, t.tours_kayak])

    header = ['name', 'category', 'id', 'score', 'tours_kayak']

    with open('course.csv', 'w', newline='') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(header)

      for t in teams:
        writer.writerow(t)

  def load(self):

    with open('course.csv', 'r', newline='') as csvfile:
      reader = csv.reader(csvfile)
      for i,row in enumerate(reader):
        if i!= 0:
          self.race.addTeam(row[0], row[2], row[1])# name, id, category
          self.race.teams[len(self.race.teams)- 1].score = int(row[3])
          self.race.teams[len(self.race.teams)- 1].tours_kayak = int(row[4])   

  def saveAndExit(self):
    self.save()
    exit()


  def changeScoreWindowOpen(self):
    self.fenetre_controle_score = pointsControl(self.race, self)

  def addTeam(self):
    self.race.addTeam(name = self.nom_equipe_ajout.get(), id = self.numero_ajout.get(), category = self.combo.get())
    if self.fenetre_scores != None :
      try:
        self.fenetre_scores.update()
      except Exception:
        print("no leaderboard window")
  
  def deleteTeam(self):
    self.race.deleteTeam(id = self.numero_supprimer.get())
    if self.fenetre_scores != None :
      try:
        self.fenetre_scores.update()
      except Exception:
        print("no leaderboard window")



  def ScoreWindowOpen(self):
    self.fenetre_scores = ViewScore(self.race)

  def UpdateScoreboard(self):
    if self.fenetre_scores != None :
      try:
        self.fenetre_scores.update()
      except Exception:
        print("no leaderboard window")
  #def NewPointsWindowOpen(self):


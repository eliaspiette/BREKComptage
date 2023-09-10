import tkinter as tk 
from tkinter import ttk

from View.nouvelleCourse import NewRaceWindow


class App(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("BREK Comptage")
    self.geometry('350x200')

    self.label = ttk.Label(self, text = "Petit programme de comptage \n POOOOUR le BEEE RAIDYYYY")
    self.label.pack()

    self.button1 = ttk.Button(self, text = 'Nouvelle course')
    self.button1['command'] = self.newRace

    self.button2 = ttk.Button(self, text = 'Quitter')
    self.button2['command'] = self.quit

    self.button3 = ttk.Button(self, text = 'Charger course depuis fichier', command = self.loadStart)

    self.button1.pack()
    self.button3.pack()
    self.button2.pack()
    


  def quit(self):
    exit()

  def newRace(self):
    new_race = NewRaceWindow()

  def loadStart(self):
    new_race = NewRaceWindow()
    new_race.load()

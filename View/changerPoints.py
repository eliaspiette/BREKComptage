import tkinter as tk
from tkinter import ttk
from functools import partial




class pointsControl(tk.Tk):
  def __init__(self, race, parentWindow):
    super().__init__()
    self.race = race
    self.parentWindow = parentWindow
    self.title("Controle points")
    self.geometry("350x450")


    # for columns we have team ID, curr score, curr kayak loops, button to add 1 kayak, to remove 1 kayak, to enter points, to submit points
    self.n_rows = len(self.race.teams) +1
    self.n_cols = 7

    text = tk.Text(self, width=16, height=1, bg = "#9BC2E6")
    text.grid(row=1,column=0)
    text.insert(tk.INSERT, "ID") 

    text = tk.Text(self, width=16, height=1, bg = "#9BC2E6")
    text.grid(row=1,column=1)
    text.insert(tk.INSERT, "Score")

    text = tk.Text(self, width=16, height=1, bg = "#9BC2E6")
    text.grid(row=1,column=2)
    text.insert(tk.INSERT, "kayak")  

    text = tk.Text(self, width=16, height=1, bg = "#9BC2E6")
    text.grid(row=1,column=3)
    text.insert(tk.INSERT, "") 

    text = tk.Text(self, width=16, height=1, bg = "#9BC2E6")
    text.grid(row=1,column=4)
    text.insert(tk.INSERT, "") 

    text = tk.Text(self, width=16, height=1, bg = "#9BC2E6")
    text.grid(row=1,column=5)
    text.insert(tk.INSERT, "") 

    text = tk.Text(self, width=16, height=1, bg = "#9BC2E6")
    text.grid(row=1,column=6)
    text.insert(tk.INSERT, "") 

    button = tk.Button(self, text = "Rafraîchir", command = self.Update)
    button.grid(row=0, column=6)
    self.Update()

  def Update(self):
    entries = list()
    for i, team in enumerate(self.race.teams):
      text = tk.Text(self, width=16, height=1, bg = "#9BC2E6")
      text.grid(row=i+2,column=0)
      text.insert(tk.INSERT, team.id) 

      text = tk.Text(self, width=16, height=1, bg = "#9BC2E6")
      text.grid(row=i+2,column=1)
      text.insert(tk.INSERT, team.score)

      text = tk.Text(self, width=16, height=1, bg = "#9BC2E6")
      text.grid(row=i+2,column=2)
      text.insert(tk.INSERT, team.tours_kayak)  

      button = tk.Button(self, width=16, height=1,text = "+1 kayak", command = partial(self.AddKayak, team.id))
      button.grid(row=i+2,column=3)

      button = tk.Button(self, width=16, height=1, text = "-1 kayak", command =partial(self.RemoveKayak,team.id))
      button.grid(row=i+2,column=4)

      entries.append(tk.Entry(self, width=16)) 
      entries[i].grid(row=i+2,column=5)

      button = tk.Button(self, width=16, height=1, text = "ajouter points", command = partial(self.addPoints, team.id, entries[i]))
      button.grid(row=i+2,column=6)


  def AddKayak(self, id):
    self.race.addKayak(id, 1)
    self.parentWindow.UpdateScoreboard()
    self.parentWindow.save()



  def RemoveKayak(self, id):
    self.race.addKayak(id, -1)
    self.parentWindow.UpdateScoreboard()
    self.parentWindow.save()


  def addPoints(self, id, entry):
    self.race.addPoints(int(entry.get()),id)
    self.parentWindow.UpdateScoreboard()
    self.parentWindow.save()

  

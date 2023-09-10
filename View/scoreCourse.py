import tkinter as tk
from tkinter import ttk
from tkinter.font import nametofont
from Logic.team import Team


class ViewScore(tk.Tk):
  def __init__(self, race):
    super().__init__()
    self.title("CLASSEMENT")
    self.geometry('%dx%d' %(self.winfo_screenwidth(), self.winfo_screenheight()))
    self.race = race
  


    self.teams_to_show = list()
    self.tree = ttk.Treeview(self, column=("c1","c2","c3","c4","c5","c6"), show='headings') 
    self.tree.pack(fill="both", expand = 1)


    #self.style = ttk.Style()
    #self.style.configure("Treeview.Heading", font=(None, 100))

    self.tree.column("#1", anchor=tk.CENTER)
    self.tree.heading("#1", text = "Place") 

    self.tree.column("#2", anchor=tk.CENTER)
    self.tree.heading("#2", text = "Score") 

    self.tree.column("#3", anchor=tk.CENTER)
    self.tree.heading("#3", text = "Nom Equipe") 

    self.tree.column("#4", anchor=tk.CENTER)
    self.tree.heading("#4", text = "Numero Equipe") 

    self.tree.column("#5", anchor=tk.CENTER)
    self.tree.heading("#5", text = "Tours Kayak") 

    self.tree.column("#6", anchor=tk.CENTER)
    self.tree.heading("#6", text = "Catégorie") 

    self.tree.tag_configure('odd', background='#E8E8E8')
    self.tree.tag_configure('even', background='#DFDFDF')

    self.update()

  def update(self):
    sorted_teams = []

    for team in self.race.teams:
      sorted_teams.append(team)

    sorted_teams.sort(key = lambda x:x.score, reverse=True)

    teams_to_show = []
    self.tree.delete(*self.tree.get_children())

    for index, team in enumerate(sorted_teams):
      teams_to_show.append((f'{index+1}',f'{team.score}',f'{team.name}', f'{team.id}',f'{team.tours_kayak}',f'{team.category}'))
      if index%2:
        self.tree.insert('', tk.END, values = teams_to_show[index], tags = ('odd',))
      else:
        self.tree.insert('', tk.END, values = teams_to_show[index], tags = ('even',))





      
      
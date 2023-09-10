from  Logic.team import Team

class Race:
  def __init__(self):
    self.n_teams = 0
    self.teams = list()
    
  def deleteTeam(self, id):
    print("removing team " + id)
    for i,t in enumerate(self.teams):
      if t.id == id:
        self.teams.pop(i)

  def addTeam(self, name, id, category):
    team = Team(name, category, id)
    for t in self.teams:
      if t.id == id:
        print("ID " + str(id) + " already used by team : "+ t.name + "\n")
        return 
    self.teams.append(team)
    

  def sortTeams(self):
    self.teams.sort(key = lambda x:x.score, reverse=True)

  def getTeams(self):
    return self.teams

  def addPoints(self, points, team_id):
    for t in self.teams:
      if t.id == team_id:
        t.score = t.score + points
        return
  
  def addKayak(self, team_id, n):
    for t in self.teams:
      if t.id == team_id:
        t.tours_kayak = t.tours_kayak+n
        t.score = t.score + 2*n
        return 
    


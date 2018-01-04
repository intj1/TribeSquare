import sys
from PyQt5.QtGui import QPainter, QFont, QPen, QBrush
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication
import itertools
from math import sqrt
from Score import Score

class TribeSquares(QWidget):

  def __init__(self):
    super().__init__()
    self.setGeometry(500, 500, 800, 800)
    self.setFixedSize(600, 600)
    self.setWindowTitle('Squares')
    QFont('Times', 4)
    self.xmouse = 0
    self.ymouse = 0
    self.squares = [[1]*8 for i in range(8)]
    self.w = 50 #width of each square
    self.xpos = 100
    self.ypos = 100
    self.first = [Score('Player One'), True]
    self.second = [Score('Player Two'), False]
    self.yellow = []
    self.yellowcheck = []
    self.yellowlines = []
    self.yellowlines_c = []
    self.yellowrotated = []
    self.yellowrotated_c = []
    self.green = []
    self.greencheck = []
    self.greenlines = []
    self.greenlines_c = []
    self.greenrotated = []
    self.greenrotated_c =[]
    self.__scoreaccessy = []
    self.__scoreaccessyr = []
    self.__scoreaccessg = []
    self.__scoreaccessgr = []
    self.__score = 0
    self.__turns = [i for i in range(64)]
    self.linecheck = [i for i in range(1, 8)]
    self.rotatedcheck = [i for i in range(1, 7)]
    self.squarecheck = []
    self.dupy = []
    self.dupyr = []
    self.dupg = []
    self.dupgr = []
    self.mult = []
    self.multr = []
    self.turn_display = 64
    self.turn = True
    self.show()
  
  def paintEvent(self, event):
    qp = QPainter()
    qp.begin(self)
    blackPen = QPen(QBrush(Qt.black), 2)
    yellowPen = QPen(QBrush(Qt.yellow), 2)
    redPen = QPen(QBrush(Qt.red), 2)
    greenPen = QPen(QBrush(Qt.green), 2)
    bluePen = QPen(QBrush(Qt.blue), 2)
    qp.setFont(QFont('Times', 15))
    qp.drawText(250, 60, '{} Turns left' .format(self.turn_display))
    qp.setPen(redPen)
    qp.drawText(150, 530, 'Player 1')
    qp.drawText(150, 550, 'Score: {}' .format(self.first[0].get_score()))
    qp.drawText(170, 570, 'X{}' .format(self.first[0].get_multiplier()))
    qp.setPen(bluePen)
    qp.drawText(350, 530, 'Player 2')
    qp.drawText(350, 550, 'Score: {}' .format(self.second[0].get_score()))
    qp.drawText(370, 570, 'X{}' .format(self.second[0].get_multiplier()))
    qp.setPen(blackPen)
    if self.turn_display != 0:
        if self.turn:
            qp.drawText(165, 590, 'GO!')
        else:
            qp.drawText(365, 590, 'GO!')
    else:
        if self.first[0].get_score () > self.second[0].get_score():
            qp.setPen(redPen)
            qp.drawText(230, 85, 'Player 1 WINS!')
            qp.setPen(yellowPen)
        elif self.first[0].get_score () < self.second[0].get_score():
            qp.setPen(bluePen)
            qp.drawText(230, 85, 'Player 2 WINS!')
            qp.setPen(greenPen)
        else:
            qp.drawText(260, 85, 'DRAW!')

    for row in self.squares:
        for col in row:
            qp.drawRect(self.xpos, self.ypos, self.w, self.w)
            self.xpos += self.w
        self.ypos += self.w
        self.xpos = 100
        if self.ypos == 500:
            self.ypos = 100
            
    if 100 <= self.xmouse <= 500 and 100 <= self.ymouse <= 500 and [(self.xmouse- 100)//50, (self.ymouse - 100)//50] not in self.squarecheck: 
        if self.first[1]:
          qp.fillRect(((self.xmouse - 100)//50 + 2)*50 +12, ((self.ymouse - 100)//50 +2)*50+12, 25, 25, Qt.yellow)
          
        if self.second[1]:
          qp.fillRect(((self.xmouse - 100)//50 + 2)*50 +12, ((self.ymouse - 100)//50 +2)*50+12, 25, 25, Qt.green)
          
          
    for i in self.yellow:
        if 100 <= i[0] <= 500  and 100 <= i[1] <= 500:
            qp.fillRect(i[0], i[1], 25, 25, Qt.yellow)
    for i in self.yellowlines_c:
        qp.setPen(yellowPen)
        qp.drawLine(i[0], i[1], i[2], i[3])
    for i in self.yellowrotated_c:
        qp.setPen(redPen)
        qp.drawLine(i[0], i[1], i[2], i[3])
        
    for j in self.green:
        if 100 <= j[0] <= 500  and 100 <= j[1] <= 500:
            qp.fillRect(j[0], j[1], 25, 25, Qt.green)
    for j in self.greenlines_c:
        qp.setPen(greenPen)
        qp.drawLine(j[0], j[1], j[2], j[3])
    for j in self.greenrotated_c:
        qp.setPen(bluePen)
        qp.drawLine(j[0], j[1], j[2], j[3])
    qp.end()
        
  def mousePressEvent(self, event):
      self.xmouse = event.x()
      self.ymouse = event.y()
      if [(self.xmouse- 100)//50, (self.ymouse - 100)//50] not in self.squarecheck and 100 <= self.xmouse <= 500 and 100 <= self.ymouse <= 500:
          if self.first[1]:
              self.yellow.append([((self.xmouse - 100)//50 + 2)*50 +12, ((self.ymouse - 100)//50 +2)*50+12])
              self.squarecheck.append([(self.xmouse- 100)//50, (self.ymouse - 100)//50])
              self.yellowcheck.append([(self.xmouse- 100)//50, (self.ymouse - 100)//50])
              self.first[1] = False
              self.second[1] = True
              self.turn = False
              self.turn_display -= 1
              for i in self.yellowcheck:
                  for j in self.linecheck:
                      if [i[0], i[1]] in self.yellowcheck and [i[0], i[1] + j] in self.yellowcheck and [i[0] + j, i[1]] in self.yellowcheck and [i[0] + j, i[1] + j] in self.yellowcheck:
                          self.yellowlines.append([i[0], i[1], i[0], i[1] + j]) #left to bot left
                          self.yellowlines.append([i[0], i[1], i[0] + j, i[1]]) #left to right
                          self.yellowlines.append([i[0] + j, i[1], i[0] + j, i[1] + j]) #right to bot right
                          self.yellowlines.append([i[0] + j, i[1] + j, i[0], i[1] + j]) #bot right to bot left
                          if [i[0], i[1], i[0] + j, i[1] + j] not in self.__scoreaccessy:
                              self.__scoreaccessy.append([i[0], i[1], i[0] + j, i[1] + j])
                              self.dupy.append([i[0], i[1]])
                              self.dupy.append([i[0], i[1] + j])
                              self.dupy.append([i[0] + j, i[1]])
                              self.dupy.append([i[0] + j, i[1] + j])
                              self.mult.append(j)             
              if len(self.dupy) / 4 == 1:
                  self.first[0].subtract_points(0)
                  self.__score += ((self.mult[0]+1)**2)
              else:           
                  for n in self.mult:
                      self.__score += ((n+1)**2)
              
              #rotated yellow    
              for k in self.yellowcheck:
                  for j in self.rotatedcheck:
                      if [k[0], k[1]] in self.yellowcheck and [k[0] + j, k[1]] in self.yellowcheck  and [k[0] + j/2, k[1] + j/2] in self.yellowcheck and [k[0] + j/2, k[1] - j/2] in self.yellowcheck:
                          self.yellowrotated.append([k[0], k[1], k[0] + j/2, k[1] + j/2]) 
                          self.yellowrotated.append([k[0], k[1], k[0] + j/2, k[1] - j/2]) 
                          self.yellowrotated.append([k[0] + j, k[1], k[0] + j/2, k[1] - j//2]) 
                          self.yellowrotated.append([k[0] + j, k[1], k[0] + j/2, k[1] + j//2])
                          if [k[0], k[1], k[0] + j, k[0] + j/2, k[1] + j/2, k[1] - j/2] not in self.__scoreaccessyr:
                              self.__scoreaccessyr.append([k[0], k[1], k[0] + j, k[0] + j/2, k[1] + j/2, k[1] - j/2])
                              self.dupyr.append([k[0], k[1]])
                              self.dupyr.append([k[0] + j, k[1]])
                              self.dupyr.append([k[0] + j/2, k[1] + j/2])
                              self.dupyr.append([k[0] + j/2, k[1] - j/2])
                              self.multr.append(j)                                                 
              if len(self.dupyr) / 4 == 1:
                  self.first[0].subtract_points(0)
                  self.__score += ((self.multr[0]+1)**2)
              else: 
                  for n in self.multr:
                      self.__score += int(((n/2)*sqrt(2))**2)
            
              multiplier = (len(self.mult) + len(self.multr))
              if multiplier == 0:              
                  self.first[0].subtract_points(0)          
              else:
                  self.first[0].increment_multiplier(multiplier)
                  
              self.first[0].add_points(self.__score * multiplier)
              self.dupy = []
              self.dupyr = []             
              self.mult = []
              self.multr = []
              self.__score = 0
              
    
              list(k for k,_ in itertools.groupby(self.yellowlines))
              list(k for k,_ in itertools.groupby(self.yellowrotated))
              self.yellowlines_c = list(itertools.starmap(lambda a, b, c, d: [(a+2)*50 + 25, (b+2)*50 + 25, (c+2)*50 + 25, (d+2)*50 + 25], self.yellowlines))
              self.yellowrotated_c = list(itertools.starmap(lambda a, b, c, d: [(a+2)*50 + 25, (b+2)*50 + 25, (c+2)*50 + 25, (d+2)*50 + 25], self.yellowrotated))
        

          elif self.second[1]:
              self.green.append([((self.xmouse - 100)//50 + 2)*50 +12, ((self.ymouse - 100)//50 +2)*50+12])
              self.squarecheck.append([(self.xmouse- 100)//50, (self.ymouse - 100)//50])
              self.greencheck.append([(self.xmouse- 100)//50, (self.ymouse - 100)//50])
              self.second[1] = False
              self.first[1] = True
              self.turn = True
              self.turn_display -= 1
              for i in self.greencheck:
                  for j in self.linecheck:
                      if [i[0], i[1]] in self.greencheck and [i[0], i[1] + j] in self.greencheck and [i[0] + j, i[1]] in self.greencheck and [i[0] + j, i[1] + j] in self.greencheck:
                          self.greenlines.append([i[0], i[1], i[0], i[1] + j]) #left to bot left
                          self.greenlines.append([i[0], i[1], i[0] + j, i[1]]) #left to right
                          self.greenlines.append([i[0] + j, i[1], i[0] + j, i[1] + j]) #right to bot right
                          self.greenlines.append([i[0] + j, i[1] + j, i[0], i[1] + j]) #bot right to bot left
                          if [i[0], i[1], i[0] + j, i[1] + j] not in self.__scoreaccessg:
                              self.__scoreaccessg.append([i[0], i[1], i[0] + j, i[1] + j])
                              self.dupg.append([i[0], i[1]])
                              self.dupg.append([i[0], i[1] + j])
                              self.dupg.append([i[0] + j, i[1]])
                              self.dupg.append([i[0] + j, i[1] + j])
                              self.mult.append(j)             
              if len(self.dupg) / 4 == 1:
                  self.second[0].subtract_points(0)
                  self.__score += ((self.mult[0]+1)**2)
              else:           
                  for n in self.mult:
                      self.__score += ((n+1)**2)
              #rotated green
              for k in self.greencheck:
                  for j in self.rotatedcheck:
                      if [k[0], k[1]] in self.greencheck and [k[0] + j, k[1]] in self.greencheck  and [k[0] + j/2, k[1] + j/2] in self.greencheck and [k[0] + j/2, k[1] - j/2] in self.greencheck:
                          self.greenrotated.append([k[0], k[1], k[0] + j/2, k[1] + j/2]) 
                          self.greenrotated.append([k[0], k[1], k[0] + j/2, k[1] - j/2]) 
                          self.greenrotated.append([k[0] + j, k[1], k[0] + j/2, k[1] - j//2]) 
                          self.greenrotated.append([k[0] + j, k[1], k[0] + j/2, k[1] + j//2]) 
                          if [k[0], k[1], k[0] + j, k[0] + j/2, k[1] + j/2, k[1] - j/2] not in self.__scoreaccessgr:
                              self.__scoreaccessgr.append([k[0], k[1], k[0] + j, k[0] + j/2, k[1] + j/2, k[1] - j/2])
                              self.dupgr.append([k[0], k[1]])
                              self.dupgr.append([k[0] + j, k[1]])
                              self.dupgr.append([k[0] + j/2, k[1] + j/2])
                              self.dupgr.append([k[0] + j/2, k[1] - j/2])
                              self.multr.append(j)                                                 
              if len(self.dupgr) / 4 == 1:
                  self.second[0].subtract_points(0)
                  self.__score += ((self.multr[0]+1)**2)
              else: 
                  for n in self.multr:
                      self.__score += int(((n/2)*sqrt(2))**2)
            
              multiplier = (len(self.mult) + len(self.multr))
              if multiplier == 0:              
                  self.second[0].subtract_points(0)          
              else:
                  self.second[0].increment_multiplier(multiplier)
                  
              self.second[0].add_points(self.__score * multiplier)
              self.dupg = []
              self.dupgr = []             
              self.mult = []
              self.multr = []
              self.__score = 0
                
              list(k for k,_ in itertools.groupby(self.greenlines))
              list(k for k,_ in itertools.groupby(self.greenrotated))
              self.greenlines_c = list(itertools.starmap(lambda a, b, c, d: [(a+2)*50 + 25, (b+2)*50 + 25, (c+2)*50 + 25, (d+2)*50 + 25], self.greenlines))
              self.greenrotated_c = list(itertools.starmap(lambda a, b, c, d: [(a+2)*50 + 25, (b+2)*50 + 25, (c+2)*50 + 25, (d+2)*50 + 25], self.greenrotated))
	         
      self.update()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = TribeSquares()
  sys.exit(app.exec_())

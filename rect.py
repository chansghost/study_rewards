from imports_consts import *


class RectangleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.rectangles = []  # lista prostokątów (x, y, szer, wys)

    def draw_rectangle(self, x, y, w, h, color=QColor(255, 0, 0, 100)):
        self.rectangles.append((x, y, w, h, color))
        self.update()  # wymusza przerysowanie widgetu

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(QColor("red"))
        pen.setWidth(3)
        painter.setPen(pen)

        for rect in self.rectangles:
            x, y, w, h, color = rect
            painter.setBrush(color)
            painter.drawRect(x, y, w, h)
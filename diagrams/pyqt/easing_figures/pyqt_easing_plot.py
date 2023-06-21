# Quick utility to generate the easing-curves plot for my thesis
import sys

import PyQt4
from PyQt4 import QtCore as qcore
from PyQt4 import QtGui as qgui

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class TestWindow(qgui.QWidget):
	# ctor
	def __init__(self):
		super(TestWindow, self).__init__()
		
		#self.setColor(qgui.QColor("white"))
		self.setBackgroundRole(qgui.QPalette.Base)
		self.setAutoFillBackground(True)
		
		# list of icons created
		self.curve_types = []
		self.icons_map = {}
		
		self.icon_size = qcore.QSize(100, 80)
		self.create_easing_curve_icons(self.icon_size)
		
		# filter curve types to show
		easingTypes = [
			"Sine",
			"Quad",
			"Cubic",
			"Quart",
			"Quint",
			"Expo",
			"Circ",
			"Back",
			"Elastic",
			"Bounce"
		]
		
		sides = ["In", "Out", "InOut", "OutIn"]
		
		# compute dimensions of grid
		WIDTH = 1200
		HEIGHT = 900
		
		columns = 10
		rows = 10
		
		# prepare utils
		labelFont = qgui.QFont("Calibri", 12)
		
		# Plot ----------------
		layout = qgui.QHBoxLayout(self)
		self.setLayout(layout)
		
		
		# Linear Pane
		lin = self.make_curve_widget("Linear", labelFont=labelFont)
		
		linPane = qgui.QGridLayout()
		linPane.addItem(qgui.QSpacerItem(self.icon_size.width(), self.icon_size.height()*1.9), 0, 0)
		linPane.addLayout(lin, 1, 0)
		linPane.addItem(qgui.QSpacerItem(self.icon_size.width(), self.icon_size.height()*2), 2, 0)
		
		layout.addLayout(linPane)
		
		# Grid
		grid = qgui.QGridLayout()
		layout.addLayout(grid)
		
		for column, easingType in enumerate(easingTypes):
			for row, side in enumerate(sides):
				curve_name = side + easingType
				
				icon_box = self.make_curve_widget(curve_name, labelFont=labelFont)
				grid.addLayout(icon_box, row, column)
				
	# Add widget for curve
	def make_curve_widget(self, curve_name, labelFont=None):
		icon = qgui.QLabel()
		icon.setPixmap(self.icons_map[curve_name])
		
		label = qgui.QLabel(curve_name)
		label.setFont(labelFont)
		label.setAlignment(qcore.Qt.AlignHCenter)
		
		icon_box = qgui.QVBoxLayout()
		icon_box.setSpacing(1)
		icon_box.addWidget(icon)
		icon_box.addWidget(label)
		
		icon_box.setSizeConstraint(qgui.QLayout.SetFixedSize)
		#icon_box.setSizePolicy(qgui.QSizePolicy.Fixed, qgui.QSizePolicy.Fixed)
		
		return icon_box
	
	# Create icons for easing types
	# < iconSize: (QSize)
	#
	# From:
	#      PyQt4/examples/animation/easing/easing.pyw
	def create_easing_curve_icons(self, iconSize):
		pix = qgui.QPixmap(iconSize)
		painter = qgui.QPainter()

		# gradient = qgui.QLinearGradient(0, 0, 0, iconSize.height())
		# gradient.setColorAt(0.0, qgui.QColor(240, 240, 240))
		# gradient.setColorAt(1.0, qgui.QColor(224, 224, 224))

		# brush = qgui.QBrush(gradient)
		brush = qgui.QBrush(qgui.QColor("white"))

		# The original C++ code uses undocumented calls to get the names of the
		# different curve types.  We do the Python equivalant (but without
		# cheating).
		curve_types = [(n, c) for n, c in qcore.QEasingCurve.__dict__.items()
				if isinstance(c, qcore.QEasingCurve.Type) and c != qcore.QEasingCurve.Custom]
		curve_types.sort(key=lambda ct: ct[1])
		
		self.curve_types = curve_types # store for later

		painter.begin(pix)

		for curve_name, curve_type in curve_types:
			painter.fillRect(
					qcore.QRect(qcore.QPoint(0, 0), iconSize), brush)

			curve = qcore.QEasingCurve(curve_type)
			
			lThick = 1.5
			dRad = 1.2
			dSize = 5
			

			painter.setPen(qgui.QColor(0, 0, 255, 64))
			xAxis = iconSize.height() * 0.75
			yAxis = iconSize.width() * 0.25
			painter.drawLine(0, xAxis, iconSize.width(),  xAxis)
			painter.drawLine(yAxis, 0, yAxis, iconSize.height())

			curveScale = iconSize.height() * 0.55

			painter.setPen(qcore.Qt.NoPen)
			painter.setRenderHint(qgui.QPainter.Antialiasing, True)
			
			# Start point.
			painter.setBrush(qcore.Qt.red)
			start = qcore.QPoint(yAxis,
					xAxis - curveScale * curve.valueForProgress(0))
			painter.drawRoundedRect(start.x() - lThick, start.y() - lThick, dSize, dSize, dRad, dRad)

			# End point.
			painter.setBrush(qcore.Qt.blue)
			end = qcore.QPoint(yAxis + curveScale,
					xAxis - curveScale * curve.valueForProgress(1))
			painter.drawRoundedRect(end.x() - lThick, end.y() - lThick, dSize, dSize, dRad, dRad)
			
			# Path
			curvePath = qgui.QPainterPath()
			curvePath.moveTo(qcore.QPointF(start))
			t = 0.0
			while t <= 1.0:
				to = qcore.QPointF(yAxis + curveScale * t,
						xAxis - curveScale * curve.valueForProgress(t))
				curvePath.lineTo(to)
				t += 1.0 / curveScale

			painter.setRenderHint(qgui.QPainter.Antialiasing, True)
			painter.strokePath(curvePath, qgui.QPen(qgui.QColor(32, 32, 32), lThick))
			painter.setRenderHint(qgui.QPainter.Antialiasing, False)
			
			# Add to list
			#icon = qgui.QIcon(pix)
			#text = curve_name
			self.icons_map[curve_name] = pix.copy()

		painter.end()


def main():
	app = qgui.QApplication(sys.argv)
	
	win = TestWindow()
	#win.showMaximized()
	win.show()
	#win.screenshot()
	
	sys.exit(app.exec_())
	
main()

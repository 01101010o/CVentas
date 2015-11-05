#!/usr/bin/env python
##...Creado por 01101010o...##
#---------Librerias:
import datetime

from gi.repository import Gtk
from precios import carne,pollo,dobladitas,dqueso,chaparritas,baño
#-----------------------------
#---------Gtk:
class MyWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Sabado")
		#importa fecha
		self.time=datetime.datetime.now()
		#Extra1
		self.extra1=Gtk.Entry()
		self.extra1.set_text('0')
		self.extra1.set_can_focus(True)
		#contadores internos:
		self.tc=0
		self.tp=0
		self.td=0
		self.tdq=0
		self.tch=0
		self.tb=0
		self.te1=0
		self.totalcompra=0
		#Vuelto
		self.vuelto=Gtk.Label()#Crea un objeto para el vuelto
		self.vuelto.set_text('vuelto: $0')#Lo que muestra por pantalla 
		self.pago=Gtk.Entry() #Crea entrada de pago
		self.pago.connect("activate",self.enter)#Se activa con Enter
		#------------------
		self.salida=Gtk.Entry() #crea un objeto con el total de la compra
		self.salida.set_text('$0') 
		self.salida.set_alignment(1) #aliniado a la derecha
		self.salida.set_can_focus(False) #no se pude modificar manualmente
		grid=Gtk.Grid() #crea grid
		grid.set_row_spacing(0)
		#---------Botones:
		botones = ['+Carne','-Carne',
		           '+Pollo','-Pollo',
		           '+Dobladita','-Dobladita',
		           '+D c/queso','-D c/queso',
		           '+Chaparrita','-Chaparrita',
		           '+Baño','-Baño',
		           '+Extra1','-Extra1']
		for i in range(7):
			hbox = Gtk.ButtonBox.new(Gtk.Orientation.HORIZONTAL)
			hbox.set_spacing(0)
			grid.attach(hbox, 0, i + 1, 1, 1)
			for j in range(2):
				button = Gtk.Button(label=botones[i*2 + j])
				button.set_can_focus(False)
				button.connect("clicked", self.button_clicked)
				hbox.add(button)
		#boton nuevo cliente
		self.nuevo = Gtk.Button(label='N')
		self.nuevo.connect('clicked',self.button_nuevo)
		self.nuevo.set_can_focus(False)
		#boton guardar
		self.guardar = Gtk.Button(label='G')
		self.guardar.connect('clicked',self.button_guardar)
		self.guardar.set_can_focus(False)
		#-------Grid:
		grid.attach(self.salida, 0, 0, 1, 1)
		grid.attach(self.nuevo, 1, 0, 1, 1)
		grid.attach(self.guardar, 1, 1, 1, 1)
		grid.attach(self.extra1, 1, 7, 1, 1)
		grid.attach(self.pago, 0, 9, 1, 1)
		grid.attach(self.vuelto, 0, 10, 1, 1)
		self.add(grid) #Mustra por pantalla
#Acciones:
	def enter(self, entry):
		self.vuelto.set_text('vuelto: $'+str(int(entry.get_text()) - self.totalcompra))
	def button_guardar(self, guardar):
		archivo=open('datos.txt','a')
		archivo.write(str(self.time)+'\n')
		archivo.write('Carne: '+str(self.tc*carne)+'\n')
		archivo.write('Pollo: '+str(self.tp*pollo)+'\n')
		archivo.write('Dobladita: '+str(self.td*dobladitas)+'\n')
		archivo.write('Dobladita c/ queso: '+str(self.tdq*dqueso)+'\n')
		archivo.write('Chaparrita: '+str(self.tch*chaparritas)+'\n')
		archivo.write('Baño: '+str(self.tb*baño)+'\n')
		archivo.write('Extra 1:'+str(self.te1*int(self.extra1.get_text()))+'\n')
		archivo.write('Total: '+str(self.tc*carne+self.tp*pollo+self.td*dobladitas+self.tdq*dqueso+self.tch*chaparritas+self.tb*baño+self.te1*int(self.extra1.get_text()))+'\n')
		archivo.write('\n')
	def button_nuevo(self, nuevo):
		self.totalcompra = 0
		self.salida.set_text('$'+str(self.totalcompra))
		self.vuelto.set_text('vuelto: $0')
	def button_clicked(self, button):
		if button.get_label() == '+Carne':
			self.totalcompra += carne
			self.tc += 1
			self.salida.set_text('$'+str(self.totalcompra))
		if button.get_label() == '-Carne':
			self.totalcompra -= carne
			self.tc -= 1
			self.salida.set_text('$'+str(self.totalcompra))
		if button.get_label() == '+Pollo':
			self.totalcompra += pollo
			self.tp += 1
			self.salida.set_text('$'+str(self.totalcompra))
		if button.get_label() == '-Pollo':
			self.totalcompra -= pollo
			self.tp -= 1
			self.salida.set_text('$'+str(self.totalcompra))
		if button.get_label() == '+Dobladita':
			self.totalcompra += dobladitas
			self.td += 1
			self.salida.set_text('$'+str(self.totalcompra))
		if button.get_label() == '-Dobladita':
			self.totalcompra -= dobladitas
			self.td -= 1
			self.salida.set_text('$'+str(self.totalcompra))
		if button.get_label() == '+D c/queso':
			self.totalcompra += dqueso
			self.tdq += 1
			self.salida.set_text('$'+str(self.totalcompra))
		if button.get_label() == '-D c/queso':
			self.totalcompra -= dqueso
			self.tdq -= 1
			self.salida.set_text('$'+str(self.totalcompra))
		if button.get_label() == '+Chaparrita':
			self.totalcompra += chaparritas
			self.tch += 1
			self.salida.set_text('$'+str(self.totalcompra))
		if button.get_label() == '-Chaparrita':
			self.totalcompra -= chaparritas
			self.tch -= 1
			self.salida.set_text('$'+str(self.totalcompra))
		if button.get_label() == '+Baño':
			self.totalcompra += baño
			self.tb += 1
			self.salida.set_text('$'+str(self.totalcompra))
		if button.get_label() == '-Baño':
			self.totalcompra -= baño
			self.tb -= 1
			self.salida.set_text('$'+str(self.totalcompra))
		if button.get_label() == '+Extra1':
			self.totalcompra += int(self.extra1.get_text())
			self.te1 += 1
			self.salida.set_text('$'+str(self.totalcompra))
		if button.get_label() == '-Extra1':
			self.totalcompra -= int(self.extra1.get_text())
			self.te1 -= 1
			self.salida.set_text('$'+str(self.totalcompra))
#------------------------------------------
win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

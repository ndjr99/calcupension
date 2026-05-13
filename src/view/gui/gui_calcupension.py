from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner

import sys
sys.path.append("src")
from model.logica_calcupension import (
    SolicitudPension, CalculadoraPension,           
    ErrorIBL, ErrorSemanasCotizadas,
    ErrorEdadMinimaHombres, ErrorEdadMinimaMujeres,
    ErrorPCLInvalidez, ErrorTipoPension,
    ErrorGenero, ErrorValoresNegativos
)

class CalcuPensionApp(App):

    def build(self):
        self.root_layout = BoxLayout(orientation='vertical', padding=10, spacing=8)

  
        titulo = Label(text='CalcuPensión', font_size=24, size_hint_y=None, height=40)
        self.root_layout.add_widget(titulo)

        form = GridLayout(cols=2, spacing=6, size_hint_y=None, height=280)


        form.add_widget(Label(text='Tipo de pensión:'))
        self.spin_tipo = Spinner(
            text='Vejez',
            values=['Vejez', 'Sobreviviente', 'Invalidez']
        )
        form.add_widget(self.spin_tipo)

        form.add_widget(Label(text='Género:'))
        self.spin_genero = Spinner(
            text='Hombre',
            values=['Hombre', 'Mujer']
        )
        form.add_widget(self.spin_genero)

        form.add_widget(Label(text='IBL (ingresos base liquidación):'))
        self.inp_ibl = TextInput(hint_text='Ej: 3500000', multiline=False)
        form.add_widget(self.inp_ibl)


        form.add_widget(Label(text='Semanas cotizadas:'))
        self.inp_semanas = TextInput(hint_text='Ej: 1300', multiline=False)
        form.add_widget(self.inp_semanas)

        form.add_widget(Label(text='Edad (solo Vejez):'))
        self.inp_edad = TextInput(hint_text='Ej: 62', multiline=False)
        form.add_widget(self.inp_edad)


        form.add_widget(Label(text='PCL % (solo Invalidez):'))
        self.inp_pcl = TextInput(hint_text='Ej: 55.0', multiline=False)
        form.add_widget(self.inp_pcl)

        self.root_layout.add_widget(form)

        btn = Button(text='Calcular', size_hint_y=None, height=44)
        btn.bind(on_press=self.calcular)
        self.root_layout.add_widget(btn)

        self.lbl_resultado = Label(text='', font_size=16)
        self.root_layout.add_widget(self.lbl_resultado)

        return self.root_layout

    def calcular(self, instance):
        tipo   = self.spin_tipo.text
        genero = self.spin_genero.text

        try:
            ibl = float(self.inp_ibl.text)
        except ValueError:
            self.lbl_resultado.text = 'Error: IBL debe ser un número.'
            return

        try:
            semanas = int(self.inp_semanas.text)
        except ValueError:
            self.lbl_resultado.text = 'Error: semanas debe ser un entero.'
            return

        edad = None
        if tipo == 'Vejez':
            try:
                edad = int(self.inp_edad.text)
            except ValueError:
                self.lbl_resultado.text = 'Error: edad debe ser un entero.'
                return

        pcl = 0.0
        if tipo == 'Invalidez':
            try:
                pcl = float(self.inp_pcl.text)
            except ValueError:
                self.lbl_resultado.text = 'Error: PCL debe ser un número.'
                return

        solicitud = SolicitudPension(
            tipo=tipo,
            ingreso_base_liquidacion=ibl,
            semanas=semanas,
            genero=genero,
            edad=edad,
            porcentaje_perdida_capacidad_laboral=pcl,
        )

        try:
            tasa   = CalculadoraPension.calcular_tasa_reemplazo(solicitud)
            mesada = CalculadoraPension.calcular_pension(tasa, ibl, tipo)
            self.lbl_resultado.text = (
                f'Tasa de reemplazo: {tasa:.2f}%\n'
                f'Mesada mensual: ${mesada:,.0f}'
            )
        except (
            ErrorIBL, ErrorSemanasCotizadas,
            ErrorEdadMinimaHombres, ErrorEdadMinimaMujeres,
            ErrorPCLInvalidez, ErrorTipoPension,
            ErrorGenero, ErrorValoresNegativos,
        ) as e:
            self.lbl_resultado.text = str(e)


if __name__ == '__main__':
    CalcuPensionApp().run()
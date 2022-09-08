from manim import *

class Capa(Scene):
    def construct(self):
        
        self.wait(2)#delay para facilitar a edição.

        título_1 = Tex("Trabalho de Matemática", color=RED_D)

        título_2 = Tex("Elipses", font_size=100, color=BLUE_C)

        elipse_capa = Ellipse(
            width=4,
            height=2,
            color=BLUE_A,
            fill_opacity=0.3
        )

        título_2_e_elipse_capa = VGroup(título_2, elipse_capa)
        
        self.play(Write(título_1), run_time=2)
        self.play(título_1.animate.move_to(3*UP))
        self.play(GrowFromCenter(título_2_e_elipse_capa))

        self.wait(2)#delay para facilitar a edição.

class PrimeiraIntrodução(Scene):
    def construct(self):
        
        self.wait(2)#Delay para facilitar a edição.

        #self.add(NumberPlane(axis_config = {"include_numbers": True}))#Cria um plano cartesiano para facilitar o posicionamento dos mobjects

        título_1 = Tex("Introdução às elipses:", color=BLUE)
        self.play(Write(título_1))#Escreve o título 1
        self.play(título_1.animate.move_to(3*UP))#Move o título 1 3*UP

        definição_1 = Tex(
            "As elipses são definidas geometricamente pela interseção de um plano inclinado em um cone:",
            font_size=30
        )
        definição_1.next_to(título_1, 3*DOWN)
        self.play(Write(definição_1), run_time=4.5)#Escreve a definição 1

        linha_1 = Line(
            start=[-1, -3, 0],
            end=[1, 0, 0]
        )
        linha_2 = Line(
            start=[-1, 0, 0],
            end=[1, -3, 0]
        )

        elipse_cima_cone = Ellipse(
            width=2, 
            height=0.4,
            color=WHITE,
            fill_opacity=0.2
        )
        elipse_cima_cone.move_to([0, 0, 0])

        elipse_baixo_cone = Ellipse(
            width=2, 
            height=0.4,
            color=WHITE,
            fill_opacity=0.2
        )
        elipse_baixo_cone.move_to([0, -3, 0])

        cone = VGroup(linha_1, elipse_cima_cone, linha_2, elipse_baixo_cone)
        self.play(DrawBorderThenFill(cone))#Desenha a borda e preenche o cone(linha_1 e linha_2)

        linha_3 = Line(
            start=[-1.5, 0, 0],
            end=[1.5, -1, 0]
        )
        self.play(DrawBorderThenFill(linha_3))#Desenha a borda e preenche a linha 3

        linha_4 = Line(
            start=[-0.86, -0.21, 0],
            end=[0.55, -0.68, 0],
            stroke_width=6,
            color=RED
        )
        self.play(DrawBorderThenFill(linha_4))#Desenha a borda e preenche a linha 4

        elipse_1 = Ellipse(
            width=1.43,
            height=0.7,
            color=RED,
            fill_opacity=0.2
        )

        self.play(Transform(linha_4, elipse_1))#Transforma a linha 4 na elipse 1
        self.play(linha_4.animate.move_to(3.9*RIGHT + 1*DOWN))#Move a elipse 3.5*RIGHT mais 1*DOWN
        self.wait(1)#Delay de 0.5 segundos

        elipse_2 = Ellipse(
            width=4,
            height=2,
            color=RED,
            fill_opacity=0.2
        )
        elipse_2.move_to(3.9*RIGHT + 1*DOWN)
        self.play(Transform(linha_4, elipse_2))#Transforma a linha 4 na elipse 2

        cone_e_interseção = VGroup(linha_1, linha_2, linha_3, elipse_cima_cone, elipse_baixo_cone)

        self.play(ShrinkToCenter(cone_e_interseção))#Reduz ao centro o cone e a interseção
        self.play(linha_4.animate.move_to([0, -0.5, 0]))#Move a elipse para a coordenada (0, -0.5)
        self.wait(0.75)#Delay de 0.75 segundos
        self.play(Unwrite(definição_1))#Desescreve a definição 1

        definição_2 = Tex(
            "Algebricamente, elas são definidas pelo conjunto de pontos em que a distância destes aos focos da elipse é uma constante",
            font_size=30
        )
        definição_2.next_to(título_1, 3*DOWN)
        self.play(Write(definição_2), run_time=5.5)#Escreve a definição 2
        self.play(linha_4.animate.move_to([0, -2, 0]))#Move a elipse para a coordenada (0,-2)

        enunciado_1 = Tex(
            "Entretanto, para melhor se entender essa definição é preciso conhecer os principais elementos das elipse: seus vértices, eixos e focos",
            font_size=30
        )
        self.play(Write(enunciado_1), run_time=5)#Escreve o enunciado 1
        self.wait(1)#Delay de 1 segundo

        definição_2_e_enunciado_1 = VGroup(definição_2, enunciado_1)
        self.play(Unwrite(definição_2_e_enunciado_1))#Desescreve a definição 2 e enunciado 1

        self.play(linha_4.animate.move_to([0, 0, 0]))#Move a elipse para a coordenada (0,0)
        self.wait(0.5)#Delay de 0.5 segundos

        eixo_1 = Axes(
            x_length=7,
            y_length=4
        )
        legenda_do_eixo_1 = eixo_1.get_axis_labels()
        self.play(DrawBorderThenFill(eixo_1))
        self.play(Write(legenda_do_eixo_1))

        ponto_centro = Dot([0, 0, 0])
        legenda_centro = Tex("centro", font_size=25)
        legenda_centro.next_to(ponto_centro, 0.3*RIGHT + 0.3*DOWN)
        centro = VGroup(ponto_centro, legenda_centro)
        self.play(Create(centro))#Cria o ponto do centro e a legenda do ponto.

        ponto_vértice_1 = Dot([2, 0, 0])
        legenda_vértice_1 = Tex("vértice 1", font_size=25)
        legenda_vértice_1.next_to(ponto_vértice_1, 0.3*RIGHT + 0.3*DOWN)
        vértice_1 = VGroup(ponto_vértice_1, legenda_vértice_1)
        self.play(Create(vértice_1))#Cria o ponto do vértice 1 e a legenda do ponto. 

        ponto_vértice_2 = Dot([0, 1, 0])
        legenda_vértice_2 = Tex("vértice 2", font_size=25)
        legenda_vértice_2.next_to(ponto_vértice_2, 0.3*RIGHT + 0.5*UP)
        vértice_2 = VGroup (ponto_vértice_2, legenda_vértice_2)
        self.play(Create(vértice_2))#Cria o ponto do vértice 2 e a legenda do ponto.

        ponto_vértice_3 = Dot([-2, 0, 0])
        legenda_vértice_3 = Tex("vértice 3", font_size=25)
        legenda_vértice_3.next_to(ponto_vértice_3, 0.3*LEFT + 0.3*DOWN)
        vértice_3 = VGroup(ponto_vértice_3, legenda_vértice_3)
        self.play(Create(vértice_3))#Cria o ponto do vértice 3 e a legenda do ponto.

        ponto_vértice_4 = Dot([0, -1, 0])
        legenda_vértice_4 = Tex("vértice 4", font_size=25)
        legenda_vértice_4.next_to(ponto_vértice_4, 0.3*RIGHT + 0.3*DOWN)
        vértice_4 = VGroup(ponto_vértice_4, legenda_vértice_4)
        self.play(Create(vértice_4))#Cria o ponto do vértice 4 e a legenda do ponto.
        
        legendas_1 = VGroup(legenda_centro, legenda_vértice_1, legenda_vértice_2, legenda_vértice_3, legenda_vértice_4)

        self.wait(1)#Delay de 1 segundo

        self.play(Uncreate(legendas_1))#Descria as legendas do centro e vértice

        self.wait(0.5)

        eixo_maior = Line(
            start=[2, 0, 0],
            end=[-2, 0, 0],
            color=YELLOW,
            stroke_width=6
        )
        eixo_menor = Line(
            start=[0, -1, 0],
            end=[0, 1, 0],
            color=YELLOW,
            stroke_width=6
        )
        self.play(vértice_1.animate.set_fill(YELLOW))
        self.play(ShowPassingFlash(eixo_maior, time_width=2))
        self.play(vértice_3.animate.set_fill(YELLOW))

        legenda_do_eixo_maior = Tex("eixo maior", font_size=30, color=YELLOW)
        legenda_do_eixo_maior.next_to(ponto_centro, 0.3*RIGHT + 0.3*DOWN)
        self.play(Write(legenda_do_eixo_maior))
        self.wait(0.5)
        self.play(Unwrite(legenda_do_eixo_maior))

        self.play(vértice_4.animate.set_fill(YELLOW))
        self.play(ShowPassingFlash(eixo_menor, time_width=2))
        self.play(vértice_2.animate.set_fill(YELLOW))

        legenda_do_eixo_menor = Tex("eixo menor", font_size=30, color=YELLOW)
        legenda_do_eixo_menor.next_to(ponto_centro, 0.3*LEFT + 0.3*UP)
        self.play(Write(legenda_do_eixo_menor))
        self.wait(0.5)
        self.play(Unwrite(legenda_do_eixo_menor))
        self.wait(0.5)

        ponto_foco_1 = Dot([1.25, 0, 0])

        legenda_foco_1 = Tex("foco 1", font_size=25)
        legenda_foco_1.next_to(ponto_foco_1, 0.3*LEFT + 0.3*DOWN)
        foco_1 = VGroup(ponto_foco_1, legenda_foco_1)
        self.play(Create(foco_1))

        ponto_foco_2 = Dot([-1.25, 0, 0])

        legenda_foco_2 = Tex("foco 2", font_size=25)
        legenda_foco_2.next_to(ponto_foco_2, 0.3*RIGHT + 0.3*DOWN)
        foco_2 = VGroup(ponto_foco_2, legenda_foco_2)
        self.play(Create(foco_2))

        legendas_2 = VGroup(legenda_foco_1, legenda_foco_2)

        self.wait(1)

        self.play(Uncreate(legendas_2))

        self.wait(0.5)

        enunciado_2 = Tex(
            "Sabendo disso, agora, é possível entender a definição algébrica das elipses"
        )

        

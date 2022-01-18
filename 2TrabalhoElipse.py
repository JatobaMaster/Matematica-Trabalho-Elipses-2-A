from turtle import left
from manim import *

class Capa(Scene):
    def construct(self):

        self.wait(4)

    #Título de capa:#
        título_1 = Tex("Trabalho de Matemática").move_to(UP*3)
        título_2 = Tex("Elipses:", color = BLUE)
        self.play(DrawBorderThenFill(título_1), run_time = 2)
        self.play(Write(título_2), run_time = 2)
    #Elipse da capa#
        elipse_capa = Ellipse(width=4.0, height=1.5, fill_opacity=0.3, color=BLUE, stroke_width=5)
        self.play(DrawBorderThenFill(elipse_capa), run_time = 4)
    #Participantes:#
        João = Tex("João Vitor - 2°A", font_size = 23).move_to(DOWN*3 + LEFT*5)
        Gabriel = Tex("Gabriel Almeida - 2°B", font_size = 23).move_to(DOWN*3.5 + LEFT*5)
        grupo = VGroup(João, Gabriel)
        self.play(Write(grupo), run_time = 3)

        self.wait(4)

class Introdução(Scene):
    def construct(self):

        self.wait(4)
    
    #Título e enunciados da introdução 1:#
        título = Tex("Introdução às elipses:", color = BLUE).move_to(UP*3)
        definição_1 = Tex("As elipses são cônicas! Isso por que elas são obtidas a partir da interseção de um plano inclinado num cone.", font_size = 30).next_to(título, DOWN*3)
        definição_2 = Tex("Assim como as hipérboles, parábolas e até mesmo os círculos.", font_size = 30).next_to(definição_1, DOWN*0.5)
        definições = VGroup(definição_1, definição_2)
        self.play(DrawBorderThenFill(título), run_time = 2)
        self.play(Write(definição_1), run_time = 4)
        self.play(Write(definição_2), run_time = 4)

        self.wait(2)

        self.play(FadeOut(definições), run_time = 2)

    #Título e enunciados da introdução 1.1:# 
        definição_3 = Tex("Posto isso, as elipses possuem certas características que merecem atenção.", font_size = 30).next_to(título, DOWN*3)
        definição_4 = Tex(" Uma delas são seus pontos notáveis:", font_size = 30).next_to(definição_3, DOWN*0.5)
        self.play(Write(definição_3), run_time = 4)
        self.play(Write(definição_4), run_time = 4)
        ##
        tudo_1 = VGroup(definição_3, definição_4)

    #Elipse 1.1#
        elipse_1 = Ellipse(width=8.0, height=2.0, fill_opacity=0.090, color=BLUE, stroke_width=5).next_to(definição_4, DOWN*2.5)
        self.play(DrawBorderThenFill(elipse_1), run_time = 4)
        ##
        tudo_2 = VGroup(elipse_1)
    #Centro da elipse 1.1#
        centro = Dot().move_to([0, -0.25, 0])
        texto_centro = Tex("Centro", font_size= 25).move_to([0.5, -0.4, 0])
        self.play(FadeIn(centro))
        self.play(Write(texto_centro))
        ##
        tudo_3 = VGroup(centro, texto_centro)
    #Vertices da elipse 1.1#
        vertice_1 = Dot([4, -0.25, 0]) 
        texto_vertice_1 = Tex("V1", font_size = 40).next_to(vertice_1, UP*0.5 + RIGHT*0.5) 
        self.play(FadeIn(vertice_1))
        self.play(Write(texto_vertice_1))
        
        vertice_2 = Dot([0, 0.7, 0])
        texto_vertice_2 = Tex("V2", font_size = 40).next_to(vertice_2, UP*0.0625 + RIGHT*0.5)
        self.play(FadeIn(vertice_2))
        self.play(Write(texto_vertice_2))

        vertice_3 = Dot([-4, -0.25, 0])
        texto_vertice_3 = Tex("V3", font_size = 40).next_to(vertice_3, UP*0.5 + LEFT*0.5) 
        self.play(FadeIn(vertice_3))
        self.play(Write(texto_vertice_3))
        
        vertice_4 = Dot([0, -1.3, 0])
        texto_vertice_4 = Tex("V4", font_size = 40).next_to(vertice_4, DOWN*0.5 + RIGHT*0.5)
        self.play(FadeIn(vertice_4))
        self.play(Write(texto_vertice_4))

        texto_vertices = Tex("V1, V2, V3 e V4 são os vértices dessa elipse.", font_size = 30).next_to(texto_vertice_4, DOWN*2) 
        self.play(Write(texto_vertices), run_time = 4)

        self.wait(2)

        self.play(FadeOut(texto_vertices))
        ##
        tudo_4 = VGroup(vertice_1, texto_vertice_1, vertice_2, texto_vertice_2, vertice_3, texto_vertice_3, vertice_4, texto_vertice_4)
    #Focos da elipse 1.1:#
        foco_1 = Dot([3, -0.25, 0])
        texto_foco_1 = Tex("F1", font_size = 40).next_to(foco_1, UP*0.5 + LEFT*0.5) 
        foco_2 = Dot([-3, -0.25, 0]) 
        texto_foco_2 = Tex("F2", font_size = 40).next_to(foco_2, UP*0.5 + RIGHT*0.5)
        self.play(FadeIn(foco_1), FadeIn(foco_2))
        self.play(Write(texto_foco_1))
        self.play(Write(texto_foco_2))

        texto_focos = Tex("F1 e F2 são os focos dessa elipse.", font_size = 30).next_to(texto_vertice_4, DOWN*2)
        self.play(Write(texto_focos), run_time = 4)

        self.wait(2)

        self.play(FadeOut(texto_focos))
        ##
        tudo_5 = VGroup(foco_1, texto_foco_1, foco_2, texto_foco_2)

    #Eixos da elipse 1.1:#
        eixo_maior = Line(start = [4, -0.25, 0], end = [-4, -0.25, 0])
        self.play(DrawBorderThenFill(eixo_maior), run_time = 2)
        eixo_menor = Line(start = [0, 0.7, 0], end = [0, -1.3, 0])
        self.play(DrawBorderThenFill(eixo_menor), run_time = 2)

        
        texto_eixos = Tex("O segmento V1V3 é o eixo maior, enquanto o segmento V2V4 é o eixo menor", font_size = 30).next_to(texto_vertice_4, DOWN*2)
        self.play(Write(texto_eixos), run_time = 4)   

        self.wait(2)

        self.play(FadeOut(texto_eixos))
        ##
        tudo_6 = VGroup(eixo_maior, eixo_menor)

    #Termino#  
        self.play(FadeOut(tudo_6))
        self.play(FadeOut(tudo_5))
        self.play(FadeOut(tudo_4))
        self.play(FadeOut(tudo_3))
        self.play(FadeOut(tudo_2))
        self.play(FadeOut(tudo_1))

        self.wait(2)
    
    #Enunciados da introdução 2#
        definição_5 = Tex("Uma outra característica das elipses é a condição de existência dessas figuras:", font_size = 30).next_to(título, DOWN*3)
        self.play(Write(definição_5), run_time = 4)
        definição_6 = Tex("Desse modo, ela é uma propriedade universal!", font_size = 30).next_to(definição_5, DOWN*0.5)
        self.play(Write(definição_6), run_time = 4)
    #Elipse 2.2#
        elipse_2 = Ellipse(width=8.0, height=2.0, fill_opacity=0.090, color=BLUE, stroke_width=5).next_to(definição_6, DOWN*2.5)
        self.play(DrawBorderThenFill(elipse_2), run_time = 4)
    #Eixos 2.2#
        eixo_maior_2 = Line(start = [4, -0.25, 0], end = [-4, -0.25, 0])
        self.play(DrawBorderThenFill(eixo_maior_2), run_time = 2)
        a = Tex("2a", font_size = 40).move_to([0, -0.5, 0])
        self.play(Write(a))
    #Focos:#
        foco_1 = Dot([3, -0.25, 0])
        texto_foco_1 = Tex("F1", font_size = 40).next_to(foco_1, UP*0.5 + LEFT*0.5) 
        foco_2 = Dot([-3, -0.25, 0]) 
        texto_foco_2 = Tex("F2", font_size = 40).next_to(foco_2, UP*0.5 + RIGHT*0.5)
        self.play(FadeIn(foco_1), FadeIn(foco_2))
        self.play(Write(texto_foco_1))
        self.play(Write(texto_foco_2))
    #Ponto P:#
        p = Dot([0, 0.7, 0]) 
        texto_p = Tex("P", font_size = 40). next_to(p, UP*0.25)
        self.play(FadeIn(p))
        self.play(Write(texto_p))
    #Distância dos focos ao ponto#
        foco_1_p = Line(start = [3, -0.25, 0], end = [0, 0.7, 0])
        foco_2_P = Line(start = [-3, -0.25, 0], end = [0, 0.7, 0])
        self.play(DrawBorderThenFill(foco_1_p), DrawBorderThenFill(foco_2_P), run_time = 4)
    #Condição de existência:#
        condição = MathTex("\overline{F_{1}P}+\overline{F_{2}P}=2a", font_size = 40).next_to(elipse_2, DOWN*1)
        self.play(Write(condição), run_time = 4)
    
        texto_condição = Tex("Como observado, a distância de um ponto qualquer até os focos é sempre igual a medida do eixo maior de qualquer elipse.", font_size = 30).next_to(condição, DOWN*0.5)
        self.play(Write(texto_condição), run_time = 4)

        self.wait(4)

class Equação(Scene):

    def construct(self):
    
        self.wait(4)
    
    #Título e enunciados 1:#
        titulo_1 = Tex("As equações das elipses:", color = BLUE).move_to(UP*3)
        subtitulo_1 = Tex("As equações, que descrevem as elipses, podem ter duas classificações:", font_size = 30).next_to(titulo_1, DOWN*3)  
        subtitulo_1_1 = Tex("As com centro na origem dos eixos e sem o centro na origem dos eixos.", font_size = 30).next_to(subtitulo_1, DOWN*0.5) 
        subtitulo_2 = Tex("Primeiramente veremos a equação com o centro da elipse na origem dos eixos:", font_size = 35, color = RED).next_to(subtitulo_1_1, DOWN*2)
        tudo_1 = VGroup(subtitulo_1, subtitulo_1_1)
        self.play(DrawBorderThenFill(titulo_1), run_time = 2)
        self.play(Write(subtitulo_1), run_time = 4.5)
        self.play(Write(subtitulo_1_1), run_time = 4.5)
        self.play(Write(subtitulo_2), run_time = 5)

        self.wait(2)

        self.play(FadeOut(tudo_1))
        self.play(subtitulo_2.animate.shift(UP*1.5))

        self.wait(2)
    #Eixo 1:#
        eixos_1 = Axes(x_range= [-4, 5, 1], y_range = [-2, 3, 0.5], y_length = 5).add_coordinates().next_to(subtitulo_2, DOWN*2)
        lables_1 = eixos_1.get_axis_labels(x_label= "x", y_label= "y")
        self.play(Write(eixos_1), run_time = 6)
        self.play(Write(lables_1), run_time = 2)
    #Elipse 1:#
        elipse_x = Ellipse(width = 2.65, height = 1.0, fill_opacity = 0.09, color = RED , stroke_width = 2, stroke_opacity = 2).move_to([-0.5, -1.5 ,0])
        self.play(DrawBorderThenFill(elipse_x), run_time = 4)
    #Equação da Elipse 1:#
        equação_x = MathTex("\\frac{x^{2}}{a^{2}}+\\frac{y^{2}}{b^{2}}=1", font_size = 40, color = RED).next_to(elipse_x, UP*2 + RIGHT*2)
        self.play(Write(equação_x), run_time = 4)

        self.wait(2)
    #Tudo:#
        tudo_2 = VGroup(elipse_x, equação_x)
        self.play(FadeOut(tudo_2), run_time = 2)
    #Final#
        self.play(subtitulo_2.animate.set_fill(color = GREEN), run_time = 2)
    #Elipse 2:#
        elipse_y = Ellipse(width = 1.0, height = 3, fill_opacity = 0.09, color = GREEN , stroke_width = 2, stroke_opacity = 2).move_to([-0.5, -1.5 ,0])
        self.play(DrawBorderThenFill(elipse_y), run_time = 4)
    #Equação da elipse 2:#
        equação_y = MathTex("\\frac{x^{2}}{b^{2}}+\\frac{y^{2}}{a^{2}}=1", font_size = 40, color = GREEN).next_to(elipse_y, UP*2 + RIGHT*2)
        self.play(Write(equação_y), run_time = 4)

        self.wait(2)

        self.play(FadeOut(eixos_1, lables_1, elipse_y, equação_y ), run_time = 2)

        self.wait

        self.play(subtitulo_2.animate.set_fill(color = RED), run_time = 2)

        self.wait(2)

        self.play(FadeOut(subtitulo_2))

        self.wait(2)

    #Frase:#
        obss_1 = Tex('Note que o "a", sempre fica debaixo do eixo maior na fração.', font_size = 30).move_to(subtitulo_2)
        obss_2 = MarkupText(f'Na primeira equação está sob o "x", <span fgcolor="{GREEN}">e na segunda está sob o "y".</span>', color=RED, font_size = 23).next_to(obss_1, DOWN*0.5)
        self.play(Write(obss_1), run_time = 4)
        self.play(Write(obss_2), run_time = 4)

        self.wait(2)


        self.play(FadeOut(obss_1), run_time = 3)
        self.play(FadeOut(obss_2), run_time = 3)

        self.wait(2)

#Parte 2:#
    #Subtítulo:#
        subtitulo_1_2 = Tex('Quando a elipse não tem seu centro alinhado com a origem dos eixos a equação dela pode seguir duas formas:', font_size = 30).move_to(subtitulo_2)
        self.play(Write(subtitulo_1_2), run_time = 4)
    #Eixos:#
        eixos_1_2 = Axes(x_range= [-4, 5, 1], y_range = [-2, 3, 0.5], y_length = 5).add_coordinates().next_to(subtitulo_2, DOWN*2.5)
        lables_1_2 = eixos_1.get_axis_labels(x_label= "x", y_label= "y")
        self.play(Write(eixos_1_2), run_time = 6)
        self.play(Write(lables_1_2), run_time = 2)
    #Elipse X:# 
        elipse_x_2 = Ellipse(width = 2.65, height = 1.0, fill_opacity = 0.09, color = RED , stroke_width = 2, stroke_opacity = 2).move_to([1.5, 0.5 ,0])    
        self.play(DrawBorderThenFill(elipse_x_2), run_time = 4)
    #Equação X:#
        equação_x_2 = MathTex("\\frac{(x-x_{0})^{2}}{a^{2}}+\\frac{(y-y_{0})^{2}}{b^{2}}=1", font_size = 40, color = RED).next_to(elipse_x_2, LEFT*6.9)
        self.play(Write(equação_x_2), run_time = 4)

        self.wait(2)

        self.play(FadeOut(elipse_x_2, equação_x_2), run_time = 2)
    #Equação Y#
        elipse_y_2 = Ellipse(width = 1, height = 2, fill_opacity = 0.09, color = GREEN , stroke_width = 2, stroke_opacity = 2).move_to([-3, -0.5 ,0])
        self.play(DrawBorderThenFill(elipse_y_2), run_time = 4)
    #Equação Y:#
        equação_y_2 = MathTex("\\frac{(x-x_{0})^{2}}{b^{2}}+\\frac{(y-y_{0})^{2}}{a^{2}}=1", font_size = 40, color = GREEN).next_to(elipse_y_2, RIGHT*9)
        self.play(Write(equação_y_2), run_time = 4)

        self.wait(4)

class Final(Scene):
    def construct(self):
        
        self.wait(4)

        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#707070"
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        logo = VGroup(triangle, square, circle, ds_m)  # order matters
        logo.move_to(UP*2 + LEFT*2.5)

        tex = Tex(r"\LaTeX").scale(4).next_to(logo, RIGHT*3)
        self.play(Write(tex), Write(logo), run_time = 2)
        

        agradescimentos_1 = Tex("Agradecemos pelo seu tempo e atenção nessa pequena apresentação, de um pequeno assunto da grande MATEMÁTICA.", color = GREEN_D, font_size = 37).move_to(DOWN)
        agradescimentos_2 = Tex("Um bom dia, boa tarde, ou boa noite.", color = GREEN_D, font_size = 37).next_to(agradescimentos_1, DOWN*1)
        self.play(Write(agradescimentos_1), run_time = 6)
        self.play(Write(agradescimentos_2), run_time = 4)
        self.play(agradescimentos_2.animate.set_fill(color = BLUE), run_time = 2)

        self.wait(4)
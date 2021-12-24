from tkinter import *
import functions


alk = Tk()
alk.geometry("900x650+200+0")
alk['bg'] = 'black'
alk.resizable(0,0)
alk.title("Tech-Diesel")

# Frames

frame1 = Frame(alk, bg="green", height=70, width=550, bd= 10, relief= GROOVE)
frame1.place(x= 5, y= 5)
frame2 = Frame(alk, bg="green", height=70, width=550, bd= 10, relief= GROOVE)
frame2.place(x= 5, y= 80)
frame3 = Frame(alk, bg="green", height=235, width=550, bd= 10, relief= GROOVE)
frame3.place(x= 5, y= 155)
frame4 = Frame(alk, bg="green", height=250, width=550, bd= 10, relief= GROOVE)
frame4.place(x= 5, y= 395)
frame5 = Frame(alk, bg="green", height=640, width=335, bd= 10, relief= GROOVE)
frame5.place(x= 560, y= 5)

# Frame 1

titulo = Label(frame1, text= "ALK Conmon Rail", bg= "green", font= ("Verdana","22", "bold"))
titulo.place(x= 100, y= 5)
versao = Label(frame1, text= "2.0", bg= "green", font= ("Verdana","10","bold"))
versao.place(x= 390, y= 20)

# Frame 2

variavel_teste = StringVar()
variavel_teste.set("")
pre_texto = StringVar()
pre_texto.set("Pressão (bar)")
pul_texto = StringVar()
pul_texto.set("Pulso")
label_bico = Label(frame2, text= "Bico", bg= "green", font= ("Verdana", "20", "bold"))
label_bico.place(x= 120, y= 10)
label_bomba = Label(frame2, text= "Bomba", bg= "green", font= ("Verdana", "20", "bold"))
#label_bomba.place(x= 300, y= 10)
radio1 = Radiobutton(frame2, command= lambda : functions.carregar_fabricantes(variavel_teste, lista), bg= "white", value= "testar_bico", variable= variavel_teste, relief= GROOVE, activebackground= "gray", highlightbackground= "white")
radio1.place(x= 200, y= 17)
radio2 = Radiobutton(frame2, command= lambda : functions.carregar_fabricantes(variavel_teste, lista), bg= "white", value= "testar_bomba", variable= variavel_teste, relief= GROOVE, activebackground= "gray",highlightbackground= "white")
#radio2.place(x= 250, y= 17)

# Frame 4

texto1 = Label(frame4, text= "Déb. de Partida", bg= "green", font= ("Verdana","10", "bold"))
texto2 = Label(frame4, text= "Marcha Lenta", bg= "green", font= ("Verdana","10", "bold"))
texto3 = Label(frame4, text= "Carga Parcial", bg= "green", font= ("Verdana","10", "bold"))
texto4 = Label(frame4, text= "Plena Carga", bg= "green", font= ("Verdana","10", "bold"))
texto5 = Label(frame4, text= "Pré-injeção", bg= "green", font= ("Verdana","10", "bold"))

texto1.place(x= 3, y= 2)
texto2.place(x= 3, y= 46)
texto3.place(x= 3, y= 92)
texto4.place(x= 3, y= 138)
texto5.place(x= 3, y= 184)

texto6 = Label(frame4, text= "Débito", bg= "green", font= ("Verdana","10"))
texto7 = Label(frame4, text= "Débito", bg= "green", font= ("Verdana","10"))
texto8 = Label(frame4, text= "Débito", bg= "green", font= ("Verdana","10"))
texto9 = Label(frame4, text= "Débito", bg= "green", font= ("Verdana","10"))
texto10 = Label(frame4, text= "Débito", bg= "green", font= ("Verdana","10"))
texto11 = Label(frame4, text= "Retorno", bg= "green", font= ("Verdana","10"))
texto12 = Label(frame4, text= "Retorno", bg= "green", font= ("Verdana","10"))
texto13 = Label(frame4, text= "Retorno", bg= "green", font= ("Verdana","10"))
texto14 = Label(frame4, text= "Retorno", bg= "green", font= ("Verdana","10"))
texto15 = Label(frame4, text= "Retorno", bg= "green", font= ("Verdana","10"))

texto6.place(x= 150, y= 2)
texto7.place(x= 150, y= 46)
texto8.place(x= 150, y= 92)
texto9.place(x= 150, y= 138)
texto10.place(x= 150, y= 184)
texto11.place(x= 150, y= 22)
texto12.place(x= 150, y= 66)
texto13.place(x= 150, y= 112)
texto14.place(x= 150, y= 158)
texto15.place(x= 150, y= 204)


d_e = Label(frame4, text= "0.0", bg= "green") 

d_pc = Label(frame4, text= "0.0", bg= "green") 

d_em = Label(frame4, text= "0.0", bg= "green") 

d_m = Label(frame4, text= "0.0", bg= "green") 

d_pi = Label(frame4, text= "0.0", bg= "green")

d_e.place(x= 260, y= 2)
d_pc.place(x= 260, y= 46)
d_em.place(x= 260, y= 92)
d_m.place(x= 260, y= 138)
d_pi.place(x= 260, y= 184)

r_e = Label(frame4, text= "0.0", bg= "green") 

r_pc = Label(frame4, text= "0.0", bg= "green") 

r_em = Label(frame4, text= "0.0", bg= "green") 

r_m = Label(frame4, text= "0.0", bg= "green") 

r_pi = Label(frame4, text= "0.0", bg= "green")

r_e.place(x= 260, y= 22)
r_pc.place(x= 260, y= 66)
r_em.place(x= 260, y= 112)
r_m.place(x= 260, y= 158)
r_pi.place(x= 260, y= 204)

dm_e = Label(frame4, text= "0.0", bg= "green") 

dm_pc = Label(frame4, text= "0.0", bg= "green") 

dm_em = Label(frame4, text= "0.0", bg= "green") 

dm_m = Label(frame4, text= "0.0", bg= "green") 

dm_pi = Label(frame4, text= "0.0", bg= "green")

dm_e.place(x= 300, y= 2)
dm_pc.place(x= 300, y= 46)
dm_em.place(x= 300, y= 92)
dm_m.place(x= 300, y= 138)
dm_pi.place(x= 300, y= 184)

rm_e = Label(frame4, text= "0.0", bg= "green") 

rm_pc = Label(frame4, text= "0.0", bg= "green") 

rm_em = Label(frame4, text= "0.0", bg= "green") 

rm_m = Label(frame4, text= "0.0", bg= "green") 

rm_pi = Label(frame4, text= "0.0", bg= "green")

rm_e.place(x= 300, y= 22)
rm_pc.place(x= 300, y= 66)
rm_em.place(x= 300, y= 112)
rm_m.place(x= 300, y= 158)
rm_pi.place(x= 300, y= 204)

entrada_ed = Entry(frame4, bd= 0, width= 7, font= ("Verdana","13"), border= 1, relief= RAISED)
entrada_er = Entry(frame4, bd= 0, width= 7, font= ("Verdana","13"), border= 1, relief= RAISED)
entrada_pcd = Entry(frame4, bd= 0, width= 7, font= ("Verdana","13"), border= 1, relief= RAISED)
entrada_pcr = Entry(frame4, bd= 0, width= 7, font= ("Verdana","13"), border= 1, relief= RAISED)
entrada_emd = Entry(frame4, bd= 0, width= 7, font= ("Verdana","13"), border= 1, relief= RAISED)
entrada_emr = Entry(frame4, bd= 0, width= 7, font= ("Verdana","13"), border= 1, relief= RAISED)
entrada_mld = Entry(frame4, bd= 0, width= 7, font= ("Verdana","13"), border= 1, relief= RAISED)
entrada_mlr = Entry(frame4, bd= 0, width= 7, font= ("Verdana","13"), border= 1, relief= RAISED)
entrada_pid = Entry(frame4, bd= 0, width= 7, font= ("Verdana","13"), border= 1, relief= RAISED)
entrada_pir = Entry(frame4, bd= 0, width= 7, font= ("Verdana","13"), border= 1, relief= RAISED)

entrada_ed.place(x= 360, y= 2)
entrada_er.place(x= 445, y= 2)
entrada_pcd.place(x= 360, y= 46)
entrada_pcr .place(x= 445, y= 46)
entrada_emd.place(x= 360, y= 92)
entrada_emr.place(x= 445, y= 92)
entrada_mld.place(x= 360, y= 138)
entrada_mlr.place(x= 445, y= 138)
entrada_pid.place(x= 360, y= 184)
entrada_pir.place(x= 445, y= 184)

partida = Label(frame4, text= "Teste de Partida", bg= "green", font= ("Verdana","15"))
plenacarga = Label(frame4, text= "Teste de Plena Carga", bg= "green", font= ("Verdana","15"))
vasao = Label(frame4, text= "Teste de Vasão", bg= "green", font= ("Verdana","15"))


partida_min = Label(frame4, text= "min. 0", bg= "green", font= ("Verdana","13"))
plenacarga_min = Label(frame4, text= "min. 0", bg= "green", font= ("Verdana","13"))
v1 = Label(frame4, text= "0.0", bg= "green", font= ("Verdana","13"))
v2 = Label(frame4, text= "0.0", bg= "green", font= ("Verdana","13"))

letra = Label(frame4, text= "a", bg= "green", font= ("Verdana","13"))


partida_entrada = Entry(frame4,bd= 0, width= 7, font= ("Verdana","13"), border= 1, relief= RAISED)
pc_entrada = Entry(frame4,bd= 0, width= 7, font= ("Verdana","13"), border= 1, relief= RAISED)
vasao_entrada = Entry(frame4,bd= 0, width= 7, font= ("Verdana","13"), border= 1, relief= RAISED)

# Frame 3

variable = StringVar()
variable.set("Teste")
teste = OptionMenu(frame5, variable, "Déb. de Partida", "Marcha Lenta", "Carga Parcial", "Plena Carga", "Pré Injeção")
teste.config(bg= "light green", bd= 0)
teste.place(x= 90, y=320)

variable2 = StringVar()
variable2.set("Teste")
testes = OptionMenu(frame5, variable2, "Partida", "Plena Carga", "Vasão")
testes.config(bg= "light green", bd= 0)

pressao = Label(frame5, textvariable= pre_texto, font= ("Verdana","15"), bg= "green")
pre = StringVar()
pre.set("0")
pressao_num = Label(frame5, textvariable= pre, font= ("Verdana","16"), bg= "light green")
pressao.place(x= 25, y= 230)
pressao_num.place(x= 70, y= 255)

pulso = Label(frame5, textvariable= pul_texto, font= ("Verdana","15"), bg= "green")
pul = StringVar()
pul.set("0")
pulso_num = Label(frame5, textvariable= pul, font= ("Verdana","16"), bg= "light green")
pulso.place(x= 180, y= 230)
pulso_num.place(x= 210, y= 255)

injetadas = Label(frame5, text= "Injetadas", font= ("Verdana","15"), bg= "green")
inj = StringVar()
inj.set("0")
injetada_num = Label(frame5, textvariable= inj, font= ("Verdana","16"), bg= "light green")
injetadas.place(x= 180, y= 390)
injetada_num.place(x= 220, y= 415)

tempo = Label(frame5, text= "Frequência", font= ("Verdana","15"), bg= "green")
tem = StringVar()
tem.set("0")
tempo_num = Label(frame5, textvariable= tem, font= ("Verdana","16"), bg= "light green")
tempo.place(x= 25, y= 390)
tempo_num.place(x= 70, y= 415)


lista_bicos = Listbox(frame3, bg= "light green", height= 7, selectbackground= "#5CFA2E", bd= 1, font= "bold")
lista_bicos.bind('<<ListboxSelect>>', lambda y : functions.carregar_parametros(
    teste,testes,
    v1,v2,vasao,vasao_entrada,letra,
    plenacarga,plenacarga_min,pc_entrada,
    partida,partida_min,partida_entrada,
    pre_texto,pul_texto,
    texto1,texto2,texto3,texto4,texto5,texto6,texto7,texto8,texto9,texto10,texto11,texto12,texto13,texto14,texto15,
    entrada_ed,entrada_er,entrada_pcd,entrada_pcr,entrada_emd,entrada_emr,entrada_mld,entrada_mlr,entrada_pid,entrada_pir

    ,variavel_teste,lista_bicos,
    d_e, d_pc, d_em, d_m, d_pi,
    dm_e, dm_pc, dm_em, dm_m, dm_pi,
    r_e, r_pc, r_em, r_m, r_pi,
    rm_e, rm_pc, rm_em, rm_m, rm_pi, variable, tem, pul, inj, pre))
lista_bicos.place(x= 285, y= 20)

lista = Listbox(frame3, bg= "light green", selectbackground= "#5CFA2E", bd= 1, font= "bold", height= 7)
lista.bind('<<ListboxSelect>>', lambda y : functions.carregar_injetores(variavel_teste, lista, lista_bicos))
lista.place(x= 35, y= 20)

# Frame 5


logotipo = PhotoImage(file= "icone.png")

logo = Label(frame5, image= logotipo)
logo.config(bg= "green")
logo.place(x= 100, y= 25)



salvar = Button(frame5, text= "Salvar", activebackground= "blue", relief= GROOVE, bd= 2, font= ("Verdana","14"), bg= "#7CADFF")
salvar.config(command= lambda : functions.salvarparametros(alk,variavel_teste,lista_bicos, 
    entrada_ed.get(), 
    entrada_er.get(),
    entrada_pcd.get(),
    entrada_pcr.get(), 
    entrada_emd.get(), 
    entrada_emr.get(), 
    entrada_mld.get(),
    entrada_mlr.get(),
    entrada_pid.get(),
    entrada_pir.get(),
    partida_entrada.get(),
    pc_entrada.get(),
    vasao_entrada.get()

))
salvar.place(x= 100, y= 540)

alk.mainloop()
from tkinter import *
from datetime import datetime
import time
import webbrowser


def carregar_fabricantes(variavel, lista):
    fbicos = ["Bosch", "Denso", "Delphi", "Siemens" ]
    fbombas = ["Bosch", "Delphi", "Denso", "Siemens"]
    i = 0
    if variavel.get() == "testar_bico":
        lista.delete(0, 'end')
        for m in fbicos:
            i += 1
            lista.insert(i, m)
    elif variavel.get() == "testar_bomba":
        lista.delete(0, 'end')
        for m in fbombas:
            i += 1
            lista.insert(i, m)
    else:
        lista.delete(0, 'end')

def carregar_injetores(variavel, flista, injetores):
    if variavel.get() == "testar_bomba":
        arquivo = open("bombas.txt","r")
    else:
        arquivo = open("bicos.txt","r")
    i = 0
    try:
        x = flista.curselection()[0]
        injetores.delete(0, 'end')
        for linha in arquivo:
            
            bico = linha.replace("\n","").split(" ")
            if str(x) == bico[0]:
                i += 1
                injetores.insert(i, bico[2])
    except:
        pass

def carregar_parametros(teste,testes,v1,v2,vasao,vasao_entrada,letra,
    plenacarga,plenacarga_min,pc_entrada,
    partida,partida_min,partida_entrada,
    pre_texto,pul_texto,
    texto1,texto2,texto3,texto4,texto5,texto6,texto7,texto8,texto9,texto10,texto11,texto12,texto13,texto14,texto15,
    entrada_ed,entrada_er,entrada_pcd,entrada_pcr,entrada_emd,entrada_emr,entrada_mld,entrada_mlr,entrada_pid,entrada_pir

    ,radio,variavel,
    d_e, d_pc, d_em, d_m, d_pi,
    dm_e, dm_pc, dm_em, dm_m, dm_pi,
    r_e, r_pc, r_em, r_m, r_pi,
    rm_e, rm_pc, rm_em, rm_m, rm_pi, variable, tem, pul, inj, pre):
    
    if radio.get() == "testar_bico":
        arquivo = open("bicos.txt","r")

        testes.place(x= 9999, y=320)
        partida.place(x= 9999, y= 2)
        plenacarga.place(x= 9999, y= 100)
        vasao.place(x= 9999, y= 190)
        partida_min.place(x= 9999, y= 2)
        plenacarga_min.place(x= 9999, y= 100)
        v1.place(x= 9999, y= 190)
        v2.place(x= 9999, y= 190)
        letra.place(x= 9999, y= 190)
        partida_entrada.place(x= 9999, y= 2)
        pc_entrada.place(x= 9999, y= 100)
        vasao_entrada.place(x= 9999, y= 190)
        
        # parametros de bicos aparecendo #
        
        pre_texto.set("Pressão (bar)")
        pul_texto.set("Pulso (µs)")
        teste.place(x= 90, y=320)
        texto1.place(x= 3, y= 2)
        texto2.place(x= 3, y= 46)
        texto3.place(x= 3, y= 92)
        texto4.place(x= 3, y= 138)
        texto5.place(x= 3, y= 184)
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
        d_e.place(x= 260, y= 2)
        d_pc.place(x= 260, y= 46)
        d_em.place(x= 260, y= 92)
        d_m.place(x= 260, y= 138)
        d_pi.place(x= 260, y= 184)
        r_e.place(x= 260, y= 22)
        r_pc.place(x= 260, y= 66)
        r_em.place(x= 260, y= 112)
        r_m.place(x= 260, y= 158)
        r_pi.place(x= 260, y= 204)
        dm_e.place(x= 300, y= 2)
        dm_pc.place(x= 300, y= 46)
        dm_em.place(x= 300, y= 92)
        dm_m.place(x= 300, y= 138)
        dm_pi.place(x= 300, y= 184)
        rm_e.place(x= 300, y= 22)
        rm_pc.place(x= 300, y= 66)
        rm_em.place(x= 300, y= 112)
        rm_m.place(x= 300, y= 158)
        rm_pi.place(x= 300, y= 204)
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

        x = variavel.curselection()[0]
        for linha in arquivo:
            bico = linha.replace("\n", "").split(" ")
            if  str(variavel.get(x)) == bico[2]:

                d_e.config(text= bico[8])
                d_pc.config(text= bico[16])
                d_em.config(text= bico[24])
                d_m.config(text= bico[32])
                d_pi.config(text= bico[40])

                dm_e.config(text= bico[9])
                dm_pc.config(text= bico[17])
                dm_em.config(text= bico[25])
                dm_m.config(text= bico[33])
                dm_pi.config(text= bico[41])

                r_e.config(text= '0')
                r_pc.config(text= '0')
                r_em.config(text= '0')
                r_m.config(text= '0')
                r_pi.config(text= '0')

                rm_e.config(text= bico[11])
                rm_pc.config(text= bico[19])
                rm_em.config(text= bico[27])
                rm_m.config(text= bico[35])
                rm_pi.config(text= bico[43])

                if variable.get() == "Déb. de Partida":
                    entrada_ed.delete(0, END)
                    entrada_er.delete(0, END)
                    entrada_pcd.delete(0, END)
                    entrada_pcr.delete(0, END)
                    entrada_emd.delete(0, END)
                    entrada_emr.delete(0, END)
                    entrada_mld.delete(0, END)
                    entrada_mlr.delete(0, END)
                    entrada_pid.delete(0, END)
                    entrada_pir.delete(0, END)
                    pre.set(bico[7])
                    inj.set(bico[6])
                    tem.set(bico[5])
                    pul.set(bico[4])
                elif variable.get() == "Marcha Lenta":
                    pre.set(bico[15])
                    inj.set(bico[14])
                    tem.set(bico[13])
                    pul.set(bico[12])
                elif variable.get() == "Carga Parcial":
                    pre.set(bico[23])
                    inj.set(bico[22])
                    tem.set(bico[21])
                    pul.set(bico[20])
                elif variable.get() == "Plena Carga":
                    pre.set(bico[31])
                    inj.set(bico[30])
                    tem.set(bico[29])
                    pul.set(bico[28])
                elif variable.get() == "Pré Injeção":
                    pre.set(bico[39])
                    inj.set(bico[38])
                    tem.set(bico[37])
                    pul.set(bico[36])
                elif variable.get() == "Teste":
                    pre.set("0")
                    inj.set("0")
                    tem.set("0")
                    pul.set("0")


        arquivo.close()
    
    if radio.get() == "testar_bomba":
        arquivo = open("bombas.txt","r")
        # parametros de bicos sumindo #

        pre_texto.set("Rpm (speed)")
        pul_texto.set("------")
        teste.place(x= 9999, y=320)
        texto1.place(x= 9999, y= 2)
        texto2.place(x= 9999, y= 46)
        texto3.place(x= 9999, y= 92)
        texto4.place(x= 9999, y= 138)
        texto5.place(x= 9999, y= 184)
        texto6.place(x= 9999, y= 2)
        texto7.place(x= 9999, y= 46)
        texto8.place(x= 9999, y= 92)
        texto9.place(x= 9999, y= 138)
        texto10.place(x= 9999, y= 184)
        texto11.place(x= 9999, y= 22)
        texto12.place(x= 9999, y= 66)
        texto13.place(x= 9999, y= 112)
        texto14.place(x= 9999, y= 158)
        texto15.place(x= 9999, y= 204)
        d_e.place(x= 9999, y= 2)
        d_pc.place(x= 9999, y= 46)
        d_em.place(x= 9999, y= 92)
        d_m.place(x= 9999, y= 138)
        d_pi.place(x= 9999, y= 184)
        r_e.place(x= 9999, y= 22)
        r_pc.place(x= 9999, y= 66)
        r_em.place(x= 9999, y= 112)
        r_m.place(x= 9999, y= 158)
        r_pi.place(x= 9999, y= 204)
        dm_e.place(x= 9999, y= 2)
        dm_pc.place(x= 9999, y= 46)
        dm_em.place(x= 9999, y= 92)
        dm_m.place(x= 9999, y= 138)
        dm_pi.place(x= 9999, y= 184)
        rm_e.place(x= 9999, y= 22)
        rm_pc.place(x= 9999, y= 66)
        rm_em.place(x= 9999, y= 112)
        rm_m.place(x= 9999, y= 158)
        rm_pi.place(x= 9999, y= 204)
        entrada_ed.place(x= 9999, y= 2)
        entrada_er.place(x= 9999, y= 2)
        entrada_pcd.place(x= 9999, y= 46)
        entrada_pcr .place(x= 9999, y= 46)
        entrada_emd.place(x= 9999, y= 92)
        entrada_emr.place(x= 9999, y= 92)
        entrada_mld.place(x= 9999, y= 138)
        entrada_mlr.place(x= 9999, y= 138)
        entrada_pid.place(x= 9999, y= 184)
        entrada_pir.place(x= 9999, y= 184)

        ##################################################

        testes.place(x= 90, y=320)
        partida.place(x= 3, y= 2)
        plenacarga.place(x= 3, y= 100)
        vasao.place(x= 3, y= 190)
        partida_min.place(x= 250, y= 2)
        plenacarga_min.place(x= 250, y= 100)
        v1.place(x= 250, y= 190)
        v2.place(x= 350, y= 190)
        letra.place(x= 310, y= 190)
        partida_entrada.place(x= 420, y= 2)
        pc_entrada.place(x= 420, y= 100)
        vasao_entrada.place(x= 420, y= 190)

        try:
            x = variavel.curselection()[0]
            for linha in arquivo:
                bico = linha.replace("\n", "").split(" ")
                if  str(variavel.get(x)) == bico[0]:
                    
                    partida_min.config(text= bico[3])
                    plenacarga_min.config(text= bico[6])
                    v1.config(text= bico[9])
                    v2.config(text= bico[10])

        except:
            pass
        finally:
            arquivo.close()

def salvarparametros(alk, radio, lista, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10,b1,b2,b3):

    name = Toplevel(alk)
    clienteLabel = Label(name, text= "Cliente:")
    cliente = Entry(name)
    carro = Label(name, text= "Veiculo:")
    veiculo = Entry(name)
    placaLabel = Label(name, text= "Placa:")
    placa = Entry(name)
    operator = Label(name, text= "Operador:")
    operador = Entry(name)
    descricao = Label(name, text= "Observações:")
    descri = Text(name, height= 7, width= 20)
    imprimir = Button(name, height= 2, width= 6)
    
    carro.grid(row= 3, column= 0)
    veiculo.grid(row= 3, column= 1)
    placaLabel.grid(row= 4, column= 0)
    placa.grid(row= 4, column= 1)
    descricao.grid(row= 6, column= 0)
    descri.grid(row= 6, column= 1)
    operator.grid(row= 5, column= 0)
    operador.grid(row= 5, column= 1)
    clienteLabel.grid(row= 2, column= 0)
    cliente.grid(row= 2, column= 1)
    bico = lista.curselection()[0]
    tupla = (bico)
    imprimir.grid(row= 7,columnspan= 1)
    imprimir.config(text= 'Imprimir', command= lambda : pronto(bico,radio,b1,b2,b3,tupla, name,lista, placa.get(),veiculo.get(), descri.get(1.0, "end"), operador.get(), cliente.get(), e1, e2, e3, e4, e5, e6, e7, e8, e9, e10))

def pronto(bico,radio,b1,b2,b3,tupla,app,variavel,placa, veiculo, descricao,operador,cliente, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10):

    if radio.get() == "testar_bico":
        arquivo = open("bicos.txt","r")
        data = time.strftime("%d/%m/%Y")
        hora = time.strftime("%H:%M")
        for linha in arquivo:
                bico = linha.replace("\n", "").split(" ")
                if  str(variavel.get(str(tupla))) == bico[2]:
                    if e1 > bico[9] or e1 < bico[8]:
                        e1cor = "red"
                    else:
                        e1cor = "black"
                    if e2 > bico[11] :
                        e2cor = "red"
                    else:
                        e2cor = "black"
                    if e3 > bico[17] or e3 < bico[16]:
                        e3cor = "red"
                    else:
                        e3cor = "black"
                    if e4 > bico[19] :
                        e4cor = "red"
                    else:
                        e4cor = "black"
                    if e5 > bico[25] or e5 < bico[24]:
                        e5cor = "red"
                    else:
                        e5cor = "black"
                    if e6 > bico[27] :
                        e6cor = "red"
                    else:
                        e6cor = "black"
                    if e7 < bico[33] and e7 > bico[32]:
                        print(f'{e7} é maior que {bico[33]}? {e7 > bico[33]}')
                        print(f'{e7} é menor que {bico[32]}? {e7 < bico[32]}')
                        e7cor = "red"
                    else:
                        e7cor = "black"
                    if e8 > bico[35]:
                        e8cor = "red"
                    else:
                        e8cor = "black"
                    if e9 > bico[41] or e9 < bico[40]:
                        e9cor = "red"
                    else:
                        e9cor = "black"
                    if e10 > bico[43] :
                        e10cor = "red"
                    else:
                        e10cor = "black"


                    arq = open("td_alk.html","w")
                    arq.write('''
                    <!DOCTYPE html>
        <html lang="pt-Br">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                <title>Laudo ALK</title>
                <style type="text/css">
                    table{
                        margin-left: auto;
                        margin-right: auto;
                        min-width: 500px;
                    }
                    .centro{
                        text-align: center;
                    }
                    th{
                        font-size: 10pt;
                    }
                    .titulo{
                        font-size: 13pt;
                    }
                    .obs{
                        height: 100px;
                    }
                    
                </style>
            </head>
            <body>
                <section>''')
                    arq.write(f'''

                        <table border="1">
                            <tr>
                                <td align="center" colspan="3"><img src="icone.png" alt=""></td>
                            </tr>
                            <tr>
                                <td class="centro" colspan="2">Data</td>
                                <td class="centro">{data}</td>
                            </tr>
                            <tr>
                                <td class="centro" colspan="2">Hora</td>
                                <td class="centro">{hora}</td>
                            </tr>
                            <tr>
                                <th class="titulo" colspan="3">Dados Cadastrais</th>
                            </tr>
                            <tr>
                                <th class="centro">Cliente</th>
                                <th class="centro">Veiculo</th>
                                <th class="centro">Placa</th>
                            </tr>
                            <tr>
                                <td class="centro">{cliente}</td><!---->
                                <td class="centro">{veiculo}</td><!---->
                                <td class="centro">{placa}</td><!---->
                            </tr>
                            <tr>
                                <th class="centro">Operador</th>
                                <th class="centro">Injetor</th>
                                <th class="centro">Fabricante</th>
                            </tr>
                            <tr>
                                <td class="centro">{operador}</td><!---->
                                <td class="centro">{bico[2]}</td><!---->
                                <td class="centro">{bico[1]}</td><!---->
                            </tr>
                            <tr>
                                <th class="titulo" colspan="3">Resultados</th>
                            </tr>
                            <tr>
                                <th colspan="3">Deb. de Partida</th>
                            </tr>
                            <tr>
                                <td colspan="2">Debito: {bico[8]} a {bico[9]}ml </td><!---->
                                <td class="centro" style="color: {e1cor};">{e1}ml</td><!---->
                            </tr>
                            <tr>
                                <td colspan="2">Retorno: 0 a {bico[11]}ml</td><!---->
                                <td class="centro" style="color: {e2cor};">{e2}ml</td><!---->
                            </tr>
                            <tr>
                                <th colspan="3">Marcha Lenta</th>
                            </tr>
                            <tr>
                                <td colspan="2">Debito: {bico[16]} a {bico[17]}ml</td><!---->
                                <td class="centro" style="color: {e3cor};">{e3}ml</td><!---->
                            </tr>
                            <tr>
                                <td colspan="2">Retorno: 0 a {bico[19]}ml</td><!---->
                                <td class="centro" style="color: {e4cor};">{e4}ml</td><!---->
                            </tr>
                            <tr>
                                <th colspan="3">Carga Parcial</th>
                            </tr>
                            <tr>
                                <td colspan="2">Debito: {bico[24]} a {bico[25]}ml</td><!---->
                                <td class="centro" style="color: {e5cor};">{e5}ml</td><!---->
                            </tr>
                            <tr>
                                <td colspan="2">Retorno: 0 a {bico[27]}ml</td><!---->
                                <td class="centro" style="color: {e6cor};">{e6}ml</td><!---->
                            </tr>
                            <tr>
                                <th colspan="3">Plena Carga</th>
                            </tr>
                            <tr>
                                <td colspan="2">Debito: {bico[32]} a {bico[33]}ml</td><!---->
                                <td class="centro" style="color: {e7cor};">{e7}ml</td><!---->
                            </tr>
                            <tr>
                                <td colspan="2">Retorno: 0 a {bico[35]}ml</td><!---->
                                <td class="centro" style="color: {e8cor};">{e8}ml</td><!---->
                            </tr>
                            <tr>
                                <th colspan="3">Pre-Injecao</th>
                            </tr>
                            <tr>
                                <td colspan="2">Debito: {bico[40]} a {bico[41]}ml</td><!---->
                                <td class="centro" style="color: {e9cor};">{e9}ml</td><!---->
                            </tr>
                            <tr>
                                <td colspan="2">Retorno: 0 a {bico[43]}ml</td><!---->
                                <td class="centro" style="color: {e10cor};">{e10}ml</td><!---->
                            </tr>
                            <tr>
                                <th class="titulo" colspan="3">Observacoes</th>
                            </tr>
                            <tr>
                                <td class="centro" class="obs" colspan="3">{descricao}</td><!---->
                            </tr>
                        </table>
                </section>
            </body>
        </html>
                
                    ''')          
                    arq.close()
        webbrowser.open("td_alk.html")
    arquivo.close()
    app.destroy()
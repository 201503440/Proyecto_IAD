import os
import pandas as pd
import matplotlib.pyplot as plt
# Para generar el PDF
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

# Funcion para guardar archivos CSV
def save_dataset_to_csv(dataset, filename, directory = '../results/'):
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, filename)
    
    #dataset.to_csv(file_path, index=False)
    dataset.to_csv(file_path, sep='\t', index=False)

    
    print(f"Dataset saved to: {os.path.abspath(file_path)}")


# Funcion para convertir string 'number+number' o 'number-number' a operacion de numeros o numero normal
def convert_and_sum(val):
    if isinstance(val, str) and '+' in val:
        nums = val.split('+')
        return int(nums[0]) + int(nums[1])
    elif isinstance(val, str) and '-' in val:
        nums = val.split('-')
        return int(nums[0]) - int(nums[1])
    elif isinstance(val, str) and val == 'UNKNOWN':
        return int(0)
    else:
        return int(val)

def generar_pdf(nombre_archivo, df_players_F):

    # Generar imagnes
    generate_Images(df_players_F)

    # Iniciar con el PDF
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    width, height = letter
    
    # Título
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 50, "Informe Final de Análisis - Cèsar Sazo")
    
    # Escribir el primer parrafo 
    c.setFont("Helvetica-Bold", 12) 
    c.drawString(100, height - 80, "Los 5 mejores atacantes:") 
    c.setFont("Helvetica", 10) 
    c.drawString(100, height - 100, "A continuaciòn se muestran a los 5 jugadores con la mejor ") 
    c.drawString(100, height - 115, "media en el parametro de ataque. ") 
        
    # Convertir el DataFrame a una tabla
    data_table = [list(top5_best_attackMean(df_players_F).columns)] + top5_best_attackMean(df_players_F).values.tolist()
    table = Table(data_table)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    # Agregar tabla al PDF
    table.wrapOn(c, width, height)
    table.drawOn(c, 100, height - 260)
    
    # *************************************************************************************************************************
    # *************************************************************************************************************************

    # Escribir el segundo parrafo 
    c.setFont("Helvetica-Bold", 12) 
    c.drawString(100, height - 290, "Los 5 mejores defensores:") 
    c.setFont("Helvetica", 10) 
    c.drawString(100, height - 310, "A continuaciòn se muestran a los 5 jugadores con la mejor ") 
    c.drawString(100, height - 325, "media en el parametro de defensa. ") 
        
    # Convertir el DataFrame a una tabla
    data_table = [list(top5_best_defendingMean(df_players_F).columns)] + top5_best_defendingMean(df_players_F).values.tolist()
    table = Table(data_table)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    # Agregar tabla al PDF
    table.wrapOn(c, width, height)
    table.drawOn(c, 100, height - 475)

    # *************************************************************************************************************************
    # *************************************************************************************************************************

    # Escribir el tercer parrafo 
    c.setFont("Helvetica-Bold", 12) 
    c.drawString(100, height - 505, "Los 5 clubes con jugadores mas jovenes:") 
    c.setFont("Helvetica", 10) 
    c.drawString(100, height - 525, "A continuaciòn se muestran a los 5 clubes con la media ") 
    c.drawString(100, height - 540, "de los jugadores mas jovenes. ") 
        
    # Convertir el DataFrame a una tabla
    data_table = [list(top5_young_Per_club_Mean(df_players_F).columns)] + top5_young_Per_club_Mean(df_players_F).values.tolist()
    table = Table(data_table)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    # Agregar tabla al PDF
    table.wrapOn(c, width, height)
    table.drawOn(c, 100, height - 690)

    # *************************************************************************************************************************
    # *************************************************************************************************************************

    # Escribir el cuarto parrafo
    c.showPage()
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, height - 80, "Los 5 clubes con jugadores mas grandes:") 
    c.setFont("Helvetica", 10) 
    c.drawString(100, height - 100, "A continuaciòn se muestran a los 5 clubes con la media ") 
    c.drawString(100, height - 115, "de los jugadores mas grandes. ") 

    # Convertir el DataFrame a una tabla
    data_table = [list(top5_old_Per_club_Mean(df_players_F).columns)] + top5_old_Per_club_Mean(df_players_F).values.tolist()
    table = Table(data_table)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    # Agregar tabla al PDF
    table.wrapOn(c, width, height)
    table.drawOn(c, 100, height - 260)

    # *************************************************************************************************************************
    # *************************************************************************************************************************

    # Escribir el segundo parrafo 
    c.setFont("Helvetica-Bold", 12) 
    c.drawString(10, height - 290, "Grafica de barras") 
    c.setFont("Helvetica", 10) 
    c.drawString(10, height - 310, "La imagen muestra un gráfico de barras que compara valores entre cinco países: Inglaterra, Argentina, España, Francia y Alemania. ") 
    c.drawString(10, height - 325, "En el eje vertical, tenemos una escala numérica que va de 0 a 3000, mientras que en el eje horizontal se enumeran los países.") 
    c.drawString(10, height - 340, "Inglaterra presenta el valor más alto. En contraste, Argentina, España, Francia y Alemania tienen valores similares.") 
    c.drawString(10, height - 355, "Este gráfico nos permite ver y comparar los valores entre estos países, destacando diferencias significativas.") 

    # Añadir una nueva página para la imagen 
    c.drawImage('../Documentation/top_nationalities.png', 50, height - 750, width=350, height=350)

        # *************************************************************************************************************************
    # *************************************************************************************************************************

    # Escribir el segundo parrafo
    c.showPage()
    c.setFont("Helvetica-Bold", 12) 
    c.drawString(10, height - 60, "Grafica de barras") 
    c.setFont("Helvetica", 10) 
    c.drawString(10, height - 80, "La imagen muestra un gráfico de barras que compara valores entre cinco jugadores: Mejores pagados de las ligas. ") 
    c.drawString(10, height - 95, "En el eje vertical, tenemos una escala numérica que va de 0 a 25, mientras que en el eje horizontal se enumeran los jugadores.") 
    
    # Añadir una nueva página para la imagen 
    c.drawImage('../Documentation/top_salaries.png', 50, height - 550, width=450, height=400)

    # Añadir un link al final del PDF 
    c.setFont("Helvetica-Bold", 12) 
    link = "https://github.com/201503440/Proyecto_IAD"
    c.drawString(100, height - 700, "Codigo y resultados del proyecto:") 
    c.setFont("Helvetica", 10) 
    c.drawString(100, height - 715, link) 
    c.linkURL(link, (100, height - 715, 400, height - 715), relative=0, thickness=1)
    
    # Finalizar el PDF
    c.save()

def top5_best_attackMean(df_players_F):
    # Ordenar por 'attacking_mean' en orden descendente y seleccionar los primeros 5
    top_5_attacking = df_players_F.nlargest(5, 'attacking_mean')[['short_name', 'club', 'attacking_mean']]
    top_5_attacking['attacking_mean'] = top_5_attacking['attacking_mean'].round(2)

    return top_5_attacking

def top5_best_defendingMean(df_players_F):
    # Ordenar por 'defending_mean' en orden descendente y seleccionar los primeros 5
    top_5_defending = df_players_F.nlargest(5, 'defending_mean')[['short_name', 'club', 'defending_mean']]
    top_5_defending['defending_mean'] = top_5_defending['defending_mean'].round(2)

    return top_5_defending

def top5_young_Per_club_Mean(df_players_F):
    # Ordenar por 'average_age_per_club' en orden ascendente y seleccionar los primeros 5
    top_5_clubs = df_players_F.drop_duplicates(subset=['club'])
    top_5_clubs = top_5_clubs.nsmallest(5, 'average_age_per_club')[['club', 'average_age_per_club']]
    top_5_clubs['average_age_per_club'] = top_5_clubs['average_age_per_club'].round(2)

    return top_5_clubs

def top5_old_Per_club_Mean(df_players_F):
    # Ordenar por 'average_age_per_club' en orden descendente y seleccionar los primeros 5
    top_5_clubs = df_players_F.drop_duplicates(subset=['club'])
    top_5_clubs = top_5_clubs.nlargest(5, 'average_age_per_club')[['club', 'average_age_per_club']]
    top_5_clubs['average_age_per_club'] = top_5_clubs['average_age_per_club'].round(2)

    return top_5_clubs


def generate_Images(df_players_F, save_path = '../Documentation/'):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    # Generar la figura
    plt.figure(figsize=(5, 5))
    plt.bar(list(df_players_F['nationality'].value_counts()[0:5].keys()), list(df_players_F['nationality'].value_counts()[0:5]))
    image_path = os.path.join(save_path, 'top_nationalities.png')
    plt.savefig(image_path)
    
    # Generar la imagen de grafico de barras de los jugadores mejor pagados
    plt.figure(figsize=(10, 5))
    top_players = df_players_F.nlargest(5, 'wage_eur')[['short_name', 'wage_eur']]
    plt.bar(top_players['short_name'], top_players['wage_eur'], color=["green", "gray", "blue", "red", "orange"])
    image_path = os.path.join(save_path, 'top_salaries.png')
    plt.savefig(image_path)
    
    # Cerrar la figura para liberar memoria
    plt.close()

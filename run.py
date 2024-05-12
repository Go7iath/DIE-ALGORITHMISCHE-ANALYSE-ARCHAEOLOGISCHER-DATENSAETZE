import time
import json
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import ntpath

from construct import *
from importing import *
from rectangles import *
from draw import *
from EntityHand import * 
from cropper import *


#große Runnning funktion    
def main(file_location, minLength, maxLength, maxDegreeVar, image:bool, rect:bool, saver_tri:bool, saver_rect:bool, imageRect:bool, outputRes, border, outputPath, line_width, textOutName, crop:bool, Crop_min:list, Crop_max:list):
    Points, Names, beginningRes = import_excel(file_location)
    Points0 = Points
    #print("Len is:",len(Points))
    #falls zuschneiden bool:
    if crop:
        Points = crop_coordinates(float(Crop_min[0]), float(Crop_min[1]), float(Crop_max[0]), float(Crop_max[1]), Points)
        #print("cropped Len is:",len(Points))
    Triangles = makeTriangles(Points, minLength, maxLength, maxDegreeVar)
    #print("Triangles:", Triangles)

    #falls dreiecke generiert und erwünscht: bild zeichnen
    if len(Triangles) > 0 and image == True:
        draw_triangles(Triangles, beginningRes, outputRes, minLength, maxLength, maxDegreeVar, line_width, outputPath, border)
    convert_tri_entity(Triangles, textOutName, file_location, saver_tri, outputPath, current_time)

    #save json (debugging purpose)
    '''status = "JsonTriangles"

    list_name_call = f"{my_path}\\Triangle_lists\{status}_{minLength}-{maxLength}_{maxDegreeVar}°{current_time}.json"  
    with open(list_name_call, 'w') as MyFile:
        json.dump(Triangles, MyFile)'''
 


    #do rectangles
    if rect == True:
        Rectangles = calc_rects(Triangles,beginningRes, minLength, maxLength, maxDegreeVar)
        #print("Rects:", Rectangles)
        if len(Rectangles) > 0 and imageRect == True:
            draw_rectangles(Rectangles, beginningRes, outputRes, minLength, maxLength, maxDegreeVar, line_width, outputPath, border)
    

        #save json (debugging purpose)
        '''status = "JsonRectangles"

        list_name_call = f"{my_path}\\Rectangles_lists\{status}_{minLength}-{maxLength}_{maxDegreeVar}°{current_time}.json"  
        with open(list_name_call, 'w') as MyFile:
            json.dump(Rectangles, MyFile)'''

        convert_rects_entity(Rectangles, textOutName, file_location, saver_rect, outputPath, current_time)

current_time = time.strftime('%Y%m%d-%H%MS')

#def preloadT(file, minL, maxL, maxDegreeVar):


#def preloadR(file, minL, maxL, maxDegreeVar):

#run
'''border = 0.8
point_radius = 5
line_width = 2

outputRes = 8000
outputPath = "output/"'''

#    file_location, minLength, maxLength, maxDegreeVar, image:bool, rect:bool, saver_tri:bool, saver_rect:bool, imageRect:bool, outputRes, border, outputPath, line_width, textOutName)
#main(f"{my_path}\\excel\mini_koordinaten.xlsx", 1, 6, 10, True, True,True, True, True, outputRes, border, outputPath, line_width, "EntityHand1")







#GUI (wird eigentlich durchs lesen verständlich), Mockup im Ordner ersichtlich
root = tk.Tk()
root.title("Geodatenanalyse")

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def open_filedialog():
    global infilename, file_label
    infilename = filedialog.askopenfilename(filetypes=[("Excel File", "*.xlsx")])
    file_name = path_leaf(infilename)
    img_path = my_path + "\sprites\excel.png"
    img = tk.PhotoImage(file= img_path)
    img = img.subsample(12, 12)

    image_label = tk.Label(root, image=img)
    image_label.image = img  
    image_label.grid(row=8, column=0,padx = (230, 0), pady=(150, 10), sticky="e")

    file_label = tk.Label(root, text=f"{file_name}", cursor="hand2", width = 10, borderwidth=3, relief="groove")
    file_label.grid(row=8, column=1, padx = (5, 0), pady=(150, 10), sticky="w")
    update_file_label()
    
def open_filedialog_folder():
    global output_folder, folder_label
    output_folder = filedialog.askdirectory()
    folder_name = path_leaf(output_folder)
    img_path2 = my_path + "\sprites/folder.png"
    img2 = tk.PhotoImage(file= img_path2)
    img2 = img2.subsample(18, 18)

    image_label2 = tk.Label(root, image=img2)
    image_label2.image = img2 
    image_label2.grid(row=8, column= 2, padx=(50, 0), pady=(150, 0), sticky="e")

    # Create a label for the folder name
    folder_label = tk.Label(root, text=f"{folder_name}", cursor="hand2", width=10, borderwidth=3, relief="groove")
    folder_label.grid(row=8, column=3, padx=(0, 0), pady=(150, 10), sticky="w")

    update_folder_label()

def update_file_label():
    file_name = path_leaf(infilename) 
    file_label.config(text=f"{file_name}")

def update_folder_label():
    folder_name = path_leaf(output_folder)
    folder_label.config(text=f"{folder_name}")

def get_parameters_and_run():

    messagebox.showinfo("Running", "Programm berechnet")

    if 'infilename' not in globals() and 'output_folder' not in globals():
        # Both filename and output_folder do not exist
        messagebox.showwarning("Auswahlfehler", "Bitte wählen Sie eine Datei und einen Ausgabeordner aus")
    elif 'infilename' not in globals():
        # filename does not exist
        messagebox.showwarning("Auswahlfehler", "Bitte wählen Sie eine Datei aus")
    elif 'output_folder' not in globals():
        # output_folder does not exist
        messagebox.showwarning("Auswahlfehler", "Bitte wählen Sie einen Ausgabeordner aus")
    else:
        file_location = infilename
        minLength = float(e1.get())
        maxLength = float(e2.get())
        maxDegreeVar = float(e3.get())
        image = checkbutton_value_tri1.get()
        rect = checkbutton_value_tri3.get()
        saver_tri = checkbutton_value_tri2.get()
        saver_rect = checkbutton_value_rect2.get()
        imageRect = checkbutton_value_rect1.get()
        outputRes = int(e4.get())
        border = float(e5.get())
        outputPath = output_folder
        line_width = int(e7.get())
        textOutName = e8.get()
        crop = check_var.get()
        Crop_min = [e9a.get(), e9b.get()]
        Crop_max = [e19a.get(), e19b.get()]

        main(file_location, minLength, maxLength, maxDegreeVar, image, rect, saver_tri, saver_rect, imageRect, outputRes, border, outputPath, line_width, textOutName, crop, Crop_min, Crop_max)

        root.destroy()
        messagebox.showinfo("Done", "Ausgabe kann im Ausgewählten Ausgabeordner gefunden werden.")

def change_image():
    global counter_GUI, image_label
    if counter_GUI < len(image_list) - 1:
        counter_GUI += 1
    else:
        counter_GUI = 0
    image_label.config(image=image_list[counter_GUI])

def display_help():
    global image_list, counter_GUI, image_label, image_list

    help_window = tk.Toplevel()  # Use Toplevel for secondary windows
    help_window.title("HILFE")
    help_window.geometry("700x550")

    # Load images
    path1 = f"{my_path}/sprites/general1.PNG"
    path2 = f"{my_path}/sprites/input1.PNG"
    path3 = f"{my_path}/sprites/tuning1.PNG"
    img1 = Image.open(path1)
    img2 = Image.open(path2)

    img3 = Image.open(path3)

    image1 = ImageTk.PhotoImage(img1)
    image2 = ImageTk.PhotoImage(img2)
    image3 = ImageTk.PhotoImage(img3)
  
    # Add images to the list
    image_list = [image1, image2, image3]
    counter_GUI = 0

    # Set up components
    s = ttk.Style()
    s.configure('my.TButton', font=('Helvetica', 18))
    button = ttk.Button(help_window, text="weiter", width=40,style= "my.TButton", command=change_image)
    image_label = ttk.Label(help_window, image=image_list[counter_GUI])

    # Display components
    image_label.pack()
    button.pack(side="bottom", pady=3)

    # Run the main loop for the hlp window
    help_window.mainloop()



tk.Label(root, text="Streckenlänge", font=('', 12)).grid(row = 1, column = 0, padx= 30,  pady = (30, 10),sticky = "w")
entry_var1 = tk.StringVar()
entry_var1.set("1")
e1 = tk.Entry(root, width = 3, textvariable=entry_var1)
e1.grid(row = 2, column = 0, padx = (35, 0),sticky = "w")

entry_var2 = tk.StringVar()
entry_var2.set("6")
e2 = tk.Entry(root, width = 3, textvariable=entry_var2)
e2.grid(row = 2, column = 0, padx = (85, 0),sticky = "w")

tk.Label(root, text="m").grid(row = 2, column = 0, padx = (50, 0),  sticky = "w")
tk.Label(root, text="m").grid(row = 2, column = 0, padx = (100, 0), sticky = "w")
tk.Label(root, text="min").grid(row = 3, column = 0, padx = (35, 0),  sticky = "w")
tk.Label(root, text="max").grid(row = 3, column = 0, padx = (85, 0), sticky = "w")

tk.Label(root, text="Winkelabweichung", font=('', 12)).grid(row = 5, column = 0,padx = 30, pady = (30, 10), sticky = "w")
entry_var3 = tk.StringVar()
entry_var3.set("1")
e3 = tk.Entry(root, width = 3, textvariable=entry_var3)
e3.grid(row = 6, column = 0, padx = (35, 0), sticky = "w")

tk.Label(root, text="°", font=('', 14)).grid(row = 6, column = 0, padx = (50, 0),sticky = "w")

padxx1 = (100, 10)
padxx2 = (120, 10)

tk.Label(root, text="Dreiecke", font=('', 12)).grid(row=1, column=1, padx=padxx1, pady=(30, 10), sticky="w")

checkbutton_value_tri1 = tk.BooleanVar()
checkbutton_value_tri2 = tk.BooleanVar()
checkbutton_value_tri3 = tk.BooleanVar()

checkbutton1_tri = ttk.Checkbutton(text="Grafik generieren", variable=checkbutton_value_tri1)
checkbutton1_tri.grid(row=2, column=1, padx=padxx2, sticky="w")

checkbutton2_tri = ttk.Checkbutton(text="Ergebnis speichern", variable=checkbutton_value_tri2)
checkbutton2_tri.grid(row=3, column=1, padx=padxx2, sticky="w")

checkbutton3_tri = ttk.Checkbutton(text="Rechtecke berechnen", variable=checkbutton_value_tri3)
checkbutton3_tri.grid(row=4, column=1, padx=padxx2, sticky="w")

tk.Label(root, text="Rechtecke", font=('', 12)).grid(row=5, column=1, padx=padxx1, pady=(30, 10), sticky="w")

checkbutton_value_rect1 = tk.BooleanVar()
checkbutton_value_rect2 = tk.BooleanVar()

checkbutton4_rect = ttk.Checkbutton(text="Grafik generieren", variable=checkbutton_value_rect1)
checkbutton4_rect.grid(row=6, column=1, padx=padxx2, sticky="w")

checkbutton5_rect = ttk.Checkbutton(text="Ergebnis speichern", variable=checkbutton_value_rect2)
checkbutton5_rect.grid(row=7, column=1, padx=padxx2, sticky="w")

def open_advanced_settings():
    if hasattr(open_advanced_settings, "frame_visible") and open_advanced_settings.frame_visible:
        # If the frame is currently visible, hide it
        advanced_settings_frame.grid_forget()
        open_advanced_settings.frame_visible = False
    else:
        
        advanced_settings_frame.grid(row=2, column=2, rowspan=8, sticky="nsew")
        open_advanced_settings.frame_visible = True

advanced_settings_button = tk.Button(root, text="Erweiterte Einstellungen", font=('', 12), command=open_advanced_settings)
advanced_settings_button.grid(row=1, column=2, padx=(10, 0), pady=(30, 10), sticky="w")

advanced_settings_frame = ttk.Frame(root, padding=(10, 10, 10, 10))

tk.Label(advanced_settings_frame, text="Output Auflösung").grid(row = 0, column = 0, sticky = "w")
entry_var4 = tk.IntVar()
entry_var4.set("8000")
e4 = tk.Entry(advanced_settings_frame, width = 5, textvariable=entry_var4)
e4.grid(row = 1, column = 0, pady = (0, 15), sticky = "w")

tk.Label(advanced_settings_frame, text="Abstandsbreite").grid(row = 2, column = 0, sticky = "w")
entry_var5 = tk.IntVar()
entry_var5.set("0.8")
e5 = tk.Entry(advanced_settings_frame, width = 3, textvariable=entry_var5)
e5.grid(row = 3, column = 0, pady = (0, 15), sticky = "w")



tk.Label(advanced_settings_frame, text="Segmentbreite").grid(row = 4, column = 0, sticky = "w")
entry_var7 = tk.IntVar()
entry_var7.set("2")
e7 = tk.Entry(advanced_settings_frame, width = 3, textvariable=entry_var7)
e7.grid(row = 5, column = 0, pady = (0, 15), sticky = "w")

tk.Label(advanced_settings_frame, text="Dateiname").grid(row = 6, column = 0, sticky = "w")
entry_var8 = tk.StringVar()
entry_var8.set("EntityHand1")
e8 = tk.Entry(advanced_settings_frame, width = 15, textvariable=entry_var8)
e8.grid(row = 7, column = 0, pady = (0, 15), sticky = "w")

#crop hide/appear
def toggle_action():
    if check_var.get():
        #print("Checkbutton is checked")
        blue_frame.grid( row=1, column=1, padx=(30, 0), sticky="w") 
    else:
        #print("Checkbutton is unchecked")
        blue_frame.grid_forget() 

#Blue frame (crop Frame) checkbox
check_var = tk.BooleanVar()
checkbuttoncrop= ttk.Checkbutton(advanced_settings_frame, text="Ausschnitt berechnen", variable=check_var, command=toggle_action)
checkbuttoncrop.grid(row=0, column=1, padx= (30, 0), sticky="w")

blue_frame = tk.Frame(advanced_settings_frame, width=150, height=400)

#cropsettings minimum
tk.Label(blue_frame, text="Kleinste Koordinate x|y").grid(row = 0, column = 0, sticky = "w")
entry_var9a = tk.IntVar()
entry_var9a.set("0")
e9a = tk.Entry(blue_frame, width = 5, textvariable=entry_var9a)
e9a.grid(row = 1, column = 0, pady = (0, 15), sticky = "w")
entry_var9b = tk.IntVar()
entry_var9b.set("0")
e9b = tk.Entry(blue_frame, width = 5, textvariable=entry_var9b)
e9b.grid(row = 1, column = 1, padx=(0, 0), pady = (0, 15), sticky = "w")

tk.Label(blue_frame, text="Größte Koordinate x|y").grid(row = 2, column = 0, sticky = "w")
entry_var19a = tk.IntVar()
entry_var19a.set("0")
e19a = tk.Entry(blue_frame, width = 5, textvariable=entry_var19a)
e19a.grid(row = 3, column = 0, pady = (0, 15), sticky = "w")
entry_var19b = tk.IntVar()
entry_var19b.set("0")
e19b = tk.Entry(blue_frame, width = 5, textvariable=entry_var19b)
e19b.grid(row = 3, column = 1, padx=(0, 0),pady = (0, 15), sticky = "w")
input_filepath = tk.StringVar()
output_filepath = tk.StringVar()

tk.Button(root, text='Datei wählen', command=lambda: input_filepath.set(open_filedialog()), cursor="hand2").grid(row=8, column=0, padx=(150, 0), pady=(150, 10), sticky="w")
tk.Button(root, text='Speicherort wählen', command=lambda: output_filepath.set(open_filedialog_folder()), cursor="hand2").grid(row=8, column=2, pady = (150, 10), sticky="w")
ttk.Button(root, text="Start", command=lambda: get_parameters_and_run()).grid(row=9, columnspan=3 )
tk.Button(root, text="Hilfe", command=lambda: display_help(),bg='#ff8e00').grid(row=9, column = 2)



#main(filename, 1, 6, 10, True, True,True, True, True, outputRes, border, outputPath, line_width, "EntityHand1")
root.geometry("800x500")
root.resizable(False, False)
root.mainloop()
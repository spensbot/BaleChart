#user input parameters
material = ["PET","HDPE","MP","Fe", "Non-Fe"]
comp = [.3,.2,.2,.15,.15] # Adds to 1
baler1 = [5,5,5,5,5] # Processing Capability in Tons Per Hour
bunker = [10,10,10,10,10] # Capacity in Tons
initial_fill = [0,0,0,0,0] #The initial fill of the bunkers
TPH = 5 #TPH of the infeed material
shift = 8 #hours
OT = 4 #hours
blocks = 20 #Number of steps per hour
change_over = 5.0/60 #Baler Changeover Time (hours)

#generated parameters
step_count = shift*blocks + OT*blocks + 1 #The number of steps that will make up the schedule
fill_time = [bunker[i]/(comp[i]*TPH) for i in range(len(comp))]


#GUI parameters
schedule_width = 800
schedule_color = (50,50,50)
background_color = (255,255,255)
OT_color = (200,100,100)
menu_width = 200
menu_color = (200,200,200)
label_color = (0,0,0)
shift_width = shift/(shift+OT)*schedule_width
OT_width = schedule_width-shift_width
width = menu_width + schedule_width
row_height = 30
row_padding = 10
header_height = 50
header_color = (0,0,0)
height =(row_height + row_padding*2)*len(material) + header_height
cursor_step = schedule_width/(shift*blocks + OT*blocks)
cursor_color1 = (200,200,200)
cursor_color2 = (0,0,0)
cursor_width1 = 5
cursor_width2 = 3
tick_color = (255,255,255)
tick_width = 3
tick_height = 10
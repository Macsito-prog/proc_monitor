import time
import psutil
import datetime
import pandas as pd

print("WELCOME TO PROCESS MONITOR PROGRAM")
tiempo_local = time.ctime()
print(f'El día de hoy es {tiempo_local}')
time.sleep(2.5)
imagen_ascii = [
    " ____________________________",
    "!\_________________________/!\"",
    "!!                         !! \"",
    "!!                         !!  \"",
    "!!                         !!  !",
    "!!                         !!  !",
    "!!  Computer               !!  !",
    "!!          Process        !!  !",
    "!!                 Monitor !!  !",
    "!!                         !!  /",
    "!!_________________________!! /",
    "!/_________________________\!/",
    "   __\_________________/__/!_",
    "  !_______________________!/ )",
    "________________________    (__",
   "/oooo  oooo  oooo  oooo /!   _  )_",
  "/ooooooooooooooooooooooo/ /  (_)_(_)",
 "/ooooooooooooooooooooooo/ /    (o o)",
"/C=_____________________/_/    ==\o/=="
]

##imprimir la imagen línea por línea
for line in imagen_ascii:
    print(line)
    time.sleep(0.1)

##creamos las variables para almacenar la información correspondiente
cpu_usage = []
memory_usage = [] 
memory_usage_percentage = [] 
pids = [] 
name = [] 
status = [] 
create_time = [] 
threads = [] 


##obtener la información del sistema usando psutil
for process in psutil.process_iter():
    pids.append(process.pid)
    name.append(process.name())

    cpu_usage.append(process.cpu_percent(interval=1)/psutil.cpu_count())
    memory_usage.append(round(process.memory_info().rss/(1024*1024),2))
    memory_usage_percentage.append(round(process.memory_percent(),2))
    create_time.append(datetime.datetime.fromtimestamp(
                        process.create_time()).strftime("%m%d%Y - %H:%M:%S"))
    status.append(process.status())
    threads.append(process.num_threads())

##guardar la información en un diccionario de datos
data ={"PIds":pids,
       "Name":name,
       "CPU": cpu_usage,
       "Memory Usage (MB)":memory_usage,
       "Memory Percentage":memory_usage_percentage,
       "Status":status,
       "Created Time":create_time,
       "Threads":threads
       }

#convertir el diccionario a un DF de pandas
process_df = pd.DataFrame(data)

#seteamos los indices al pids

process_df = process_df.set_index("PIds")

#ordenamos 
process_df = process_df.sort_values(by="Memory Usage (MB)", ascending=False)

process_df["Memory Usage (MB)"] = process_df["Memory Usage (MB)"].astype(str) + "MB"

print(process_df)
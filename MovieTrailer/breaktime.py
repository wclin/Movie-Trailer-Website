import time
import webbrowser as wb

total_breaks = 3
break_count = 0

print("This program started on " + time.ctime())
while(break_count < total_breaks):
  time.sleep(3)
  wb.open("https://www.youtube.com/watch?v=GaoLU6zKaws")
  break_count += 1

import psutil, datetime


data = open("CPU.html", "w")

boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

cpu_util = psutil.cpu_percent(interval = 1, percpu=True)

cpuTimes = []
for cpu in cpu_util:
    cpuTimes.append(cpu)

mem = psutil.virtual_memory()
THRESHOLD = 100*1024*1024 


string = """<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 4.0 Transitional//EN'>
 <HTML>
 <HEAD>
 </HEAD>

 <BODY>
	<table>
	<tr>
		<td width='60%' bgcolor = 'LightBlue'>BOOT TIME</td>
"<td colspan='2' bgcolor = 'LightBlue' >"""+boot_time+""""</td>

	</tr>
	<tr>
		<td rowspan='4'>CPU UTILIZATION</td>
		<td>CPU 1</td>
"<td bgcolor = 'Plum'>"""+str(cpuTimes[0])+"""%</td>
	</tr>
	<tr>
		<td>CPU 2</td>
"<td bgcolor = 'Plum'>"""+str(cpuTimes[1])+"""%</td>
	</tr>
	<tr>
		<td>CPU 3</td>
"<td bgcolor = 'Plum'>"""+str(cpuTimes[2])+"""%</td>
	</tr>
	<tr>
		<td>CPU 4</td>
"<td bgcolor = 'Plum'>"""+str(cpuTimes[3])+"""%</td>
	</tr>
	<tr>
		<td bgcolor = 'LightBlue'>AVAILBLE MEMORY</td>
"<td bgcolor = 'LightBlue' colspan='2'>"""+str(mem.available)+"""</td>
	</tr>
	<tr>
		<td>USED MEMORY</td>
"<td colspan='2'>"""+str(mem.used)+"""</td>
	</tr>
	<tr>
		<td bgcolor = 'LightBlue'>USED PERCENTAGE</th>
"<td bgcolor = 'LightBlue' colspan='2'>"""+str(mem.percent)+"""</td>
	</tr>
	</table>
 </BODY>
</HTML>
"""
data.write(string)

data.close()

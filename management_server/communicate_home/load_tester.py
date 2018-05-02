import subprocess, json,time

def get_value():
	proc = subprocess.Popen(['varnishstat','-f','MAIN.sess_conn','-j'],stdout=subprocess.PIPE)
	data = ((proc.stdout.read()).decode())
	return int(json.loads(data)['MAIN.sess_conn']['value'])
def get_average(interval):
	a0=get_value()
	time.sleep(interval)
	a1=get_value()
	time.sleep(interval)
	a2=get_value()
	time.sleep(interval)
	a3=get_value()
	time.sleep(interval)
	a4=get_value()
	time.sleep(interval)
	a5=get_value()
	return (a1-a0)+(a2-a1)+(a3-a2)+(a4-a3)+(a5-a4)/5

# print(get_value())

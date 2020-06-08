import os,time
os.system('clear')
gif = ["we.txt","wd.txt","wa.txt","ws.txt","wq.txt","wc.txt","wr.txt","wx.txt","wz.txt","wf.txt","wg.txt"]
def animator(gif,delay=1,repeat=10000):
	frames = []
	for wak in gif:
		with open(wak,"r",encoding="utf-8") as d:
			frames.append(d.readlines())
	for i in range(repeat):
		for frame in frames:
			print("".join(frame))
			time.sleep(delay)
			os.system('clear')
animator(gif,delay=0.5,repeat=5)
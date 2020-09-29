
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#######################################################################################################

def rmlmapper_7d(FunMap_rmlmapper,FunMapMinus_rmlmapper,rmlmapper_FnO):

	######### Create bars #######
	barWidth = 0.25

	################## simple functions, veracity75 data
	FunMap_vera75_bar = []
	FunMap_vera75_bar.append(FunMap_rmlmapper.iloc[0,2])
	FunMap_vera75_bar.append(FunMap_rmlmapper.iloc[2,2])
	FunMap_vera75_bar.append(FunMap_rmlmapper.iloc[4,2])
	FunMap_vera75_bar.append(FunMap_rmlmapper.iloc[6,2])

	FunMapMinus_vera75_bar = []
	FunMapMinus_vera75_bar.append(FunMapMinus_rmlmapper.iloc[0,2])
	FunMapMinus_vera75_bar.append(FunMapMinus_rmlmapper.iloc[2,2])
	FunMapMinus_vera75_bar.append(FunMapMinus_rmlmapper.iloc[4,2])
	FunMapMinus_vera75_bar.append(FunMapMinus_rmlmapper.iloc[6,2])

	Current_vera75_bar = []
	Current_vera75_bar.append(rmlmapper_FnO.iloc[0,2])
	Current_vera75_bar.append(rmlmapper_FnO.iloc[2,2])
	Current_vera75_bar.append(rmlmapper_FnO.iloc[4,2])
	Current_vera75_bar.append(rmlmapper_FnO.iloc[6,2])

	#rmlmapper_simple_vera75_bars4 = FunMap_vera75_bar + FunMapMinus_vera75_bar + Current_vera75_bar 
	rmlmapper_simple_vera75_bars4_r1 = np.arange(len(FunMap_vera75_bar))
	rmlmapper_simple_vera75_bars4_r2 = [x + barWidth for x in rmlmapper_simple_vera75_bars4_r1]
	rmlmapper_simple_vera75_bars4_r3 = [x + barWidth for x in rmlmapper_simple_vera75_bars4_r2]
	# Create barplot
	plt.bar(rmlmapper_simple_vera75_bars4_r1, FunMap_vera75_bar, width = barWidth, color = '#59BDC0', label='FunMap+RMLMapper')
	plt.bar(rmlmapper_simple_vera75_bars4_r2, FunMapMinus_vera75_bar, width = barWidth, color = '#b8d8d8ff', label='FunMap$^-$+RMLMapper')
	plt.bar(rmlmapper_simple_vera75_bars4_r3, Current_vera75_bar, width = barWidth, color = '#f6b7a1ff', label='RMLMapper**(RML+FnO)')
	# Text below each barplot with a rotation at 90°
	plt.xticks([r + barWidth for r in range(len(rmlmapper_simple_vera75_bars4_r1))], ['4', '6','8', '10'])
	# Adjust the margins
	plt.subplots_adjust(bottom= 0.30, left= 0.11)
	plt.ylabel("Time (s)")
	plt.xlabel("Number of repetition of the same simple function in mapping rules")
	# Create legend
	plt.legend(['FunMap+RMLMapper','FunMap$^-$+RMLMapper','RMLMapper**(RML+FnO)'])
	plt.savefig("./Figure7_d.png", dpi=700)

def rmlmapper_7c(FunMap_rmlmapper,FunMapMinus_rmlmapper,rmlmapper_FnO):

	######### Create bars #######
	barWidth = 0.25

	################## simple functions, veracity25 data
	FunMap_vera25_bar = []
	FunMap_vera25_bar.append(FunMap_rmlmapper.iloc[1,2])
	FunMap_vera25_bar.append(FunMap_rmlmapper.iloc[3,2])
	FunMap_vera25_bar.append(FunMap_rmlmapper.iloc[5,2])
	FunMap_vera25_bar.append(FunMap_rmlmapper.iloc[7,2])

	FunMapMinus_vera25_bar = []
	FunMapMinus_vera25_bar.append(FunMapMinus_rmlmapper.iloc[1,2])
	FunMapMinus_vera25_bar.append(FunMapMinus_rmlmapper.iloc[3,2])
	FunMapMinus_vera25_bar.append(FunMapMinus_rmlmapper.iloc[5,2])
	FunMapMinus_vera25_bar.append(FunMapMinus_rmlmapper.iloc[7,2])

	Current_vera25_bar = []
	Current_vera25_bar.append(rmlmapper_FnO.iloc[1,2])
	Current_vera25_bar.append(rmlmapper_FnO.iloc[3,2])
	Current_vera25_bar.append(rmlmapper_FnO.iloc[5,2])
	Current_vera25_bar.append(rmlmapper_FnO.iloc[7,2])

	#rmlmapper_simple_vera75_bars4 = FunMap_vera75_bar + FunMapMinus_vera75_bar + Current_vera75_bar 
	rmlmapper_simple_vera25_bars4_r1 = np.arange(len(FunMap_vera25_bar))
	rmlmapper_simple_vera25_bars4_r2 = [x + barWidth for x in rmlmapper_simple_vera25_bars4_r1]
	rmlmapper_simple_vera25_bars4_r3 = [x + barWidth for x in rmlmapper_simple_vera25_bars4_r2]
	# Create barplot
	plt.bar(rmlmapper_simple_vera25_bars4_r1, FunMap_vera25_bar, width = barWidth, color = '#59BDC0', label='FunMap+RMLMapper')
	plt.bar(rmlmapper_simple_vera25_bars4_r2, FunMapMinus_vera25_bar, width = barWidth, color = '#b8d8d8ff', label='FunMap$^-$+RMLMapper')
	plt.bar(rmlmapper_simple_vera25_bars4_r3, Current_vera25_bar, width = barWidth, color = '#f6b7a1ff', label='RMLMapper**(RML+FnO)')
	# Text below each barplot with a rotation at 90°
	plt.xticks([r + barWidth for r in range(len(rmlmapper_simple_vera25_bars4_r1))], ['4', '6','8', '10'])
	# Adjust the margins
	plt.subplots_adjust(bottom= 0.30, left= 0.11)
	plt.ylabel("Time (s)")
	plt.xlabel("Number of repetition of the same simple function in mapping rules")
	# Create legend
	plt.legend(['FunMap+RMLMapper','FunMap$^-$+RMLMapper','RMLMapper**(RML+FnO)'])
	plt.savefig("./Figure7_c.png", dpi=700)

def rmlmapper_8d(FunMap_rmlmapper,FunMapMinus_rmlmapper,rmlmapper_FnO):

	######### Create bars #######
	barWidth = 0.25
	################## complex functions, veracity75 data
	FunMap_vera75_bar = []
	FunMap_vera75_bar.append(FunMap_rmlmapper.iloc[8,2])
	FunMap_vera75_bar.append(FunMap_rmlmapper.iloc[10,2])
	FunMap_vera75_bar.append(FunMap_rmlmapper.iloc[12,2])
	FunMap_vera75_bar.append(FunMap_rmlmapper.iloc[14,2])

	FunMapMinus_vera75_bar = []
	FunMapMinus_vera75_bar.append(FunMapMinus_rmlmapper.iloc[8,2])
	FunMapMinus_vera75_bar.append(FunMapMinus_rmlmapper.iloc[10,2])
	FunMapMinus_vera75_bar.append(FunMapMinus_rmlmapper.iloc[12,2])
	FunMapMinus_vera75_bar.append(FunMapMinus_rmlmapper.iloc[14,2])

	Current_vera75_bar = []
	Current_vera75_bar.append(rmlmapper_FnO.iloc[8,2])
	Current_vera75_bar.append(rmlmapper_FnO.iloc[10,2])
	Current_vera75_bar.append(rmlmapper_FnO.iloc[12,2])
	Current_vera75_bar.append(rmlmapper_FnO.iloc[14,2])

	#rmlmapper_simple_vera75_bars4 = FunMap_vera75_bar + FunMapMinus_vera75_bar + Current_vera75_bar 
	rmlmapper_complex_vera75_bars4_r1 = np.arange(len(FunMap_vera75_bar))
	rmlmapper_complex_vera75_bars4_r2 = [x + barWidth for x in rmlmapper_complex_vera75_bars4_r1]
	rmlmapper_complex_vera75_bars4_r3 = [x + barWidth for x in rmlmapper_complex_vera75_bars4_r2]
	# Create barplot
	plt.bar(rmlmapper_complex_vera75_bars4_r1, FunMap_vera75_bar, width = barWidth, color = '#59BDC0', label='FunMap+RMLMapper')
	plt.bar(rmlmapper_complex_vera75_bars4_r2, FunMapMinus_vera75_bar, width = barWidth, color = '#b8d8d8ff', label='FunMap$^-$+RMLMapper')
	plt.bar(rmlmapper_complex_vera75_bars4_r3, Current_vera75_bar, width = barWidth, color = '#f6b7a1ff', label='RMLMapper**(RML+FnO)')
	# Text below each barplot with a rotation at 90°
	plt.xticks([r + barWidth for r in range(len(rmlmapper_complex_vera75_bars4_r1))], ['4', '6','8', '10'])
	# Adjust the margins
	plt.subplots_adjust(bottom= 0.30, left= 0.11)
	plt.ylabel("Time (s)")
	plt.xlabel("Number of repetition of the same simple function in mapping rules")
	# Create legend
	plt.legend(['FunMap+RMLMapper','FunMap$^-$+RMLMapper','RMLMapper**(RML+FnO)'])
	plt.savefig("./Figure8_d.png", dpi=700)

def rmlmapper_8c(FunMap_rmlmapper,FunMapMinus_rmlmapper,rmlmapper_FnO):

	######### Create bars #######
	barWidth = 0.25

	################## complex functions, veracity75 data	
	FunMap_vera25_bar = []
	FunMap_vera25_bar.append(FunMap_rmlmapper.iloc[9,2])
	FunMap_vera25_bar.append(FunMap_rmlmapper.iloc[11,2])
	FunMap_vera25_bar.append(FunMap_rmlmapper.iloc[13,2])
	FunMap_vera25_bar.append(FunMap_rmlmapper.iloc[15,2])

	FunMapMinus_vera25_bar = []
	FunMapMinus_vera25_bar.append(FunMapMinus_rmlmapper.iloc[9,2])
	FunMapMinus_vera25_bar.append(FunMapMinus_rmlmapper.iloc[11,2])
	FunMapMinus_vera25_bar.append(FunMapMinus_rmlmapper.iloc[13,2])
	FunMapMinus_vera25_bar.append(FunMapMinus_rmlmapper.iloc[15,2])

	Current_vera25_bar = []
	Current_vera25_bar.append(rmlmapper_FnO.iloc[9,2])
	Current_vera25_bar.append(rmlmapper_FnO.iloc[11,2])
	Current_vera25_bar.append(rmlmapper_FnO.iloc[13,2])
	Current_vera25_bar.append(rmlmapper_FnO.iloc[15,2])

	#rmlmapper_simple_vera75_bars4 = FunMap_vera75_bar + FunMapMinus_vera75_bar + Current_vera75_bar 
	rmlmapper_complex_vera25_bars4_r1 = np.arange(len(FunMap_vera25_bar))
	rmlmapper_complex_vera25_bars4_r2 = [x + barWidth for x in rmlmapper_complex_vera25_bars4_r1]
	rmlmapper_complex_vera25_bars4_r3 = [x + barWidth for x in rmlmapper_complex_vera25_bars4_r2]
	# Create barplot
	plt.bar(rmlmapper_complex_vera25_bars4_r1, FunMap_vera25_bar, width = barWidth, color = '#59BDC0', label='FunMap+RMLMapper')
	plt.bar(rmlmapper_complex_vera25_bars4_r2, FunMapMinus_vera25_bar, width = barWidth, color = '#b8d8d8ff', label='FunMap$^-$+RMLMapper')
	plt.bar(rmlmapper_complex_vera25_bars4_r3, Current_vera25_bar, width = barWidth, color = '#f6b7a1ff', label='RMLMapper**(RML+FnO)')
	# Text below each barplot with a rotation at 90°
	plt.xticks([r + barWidth for r in range(len(rmlmapper_complex_vera25_bars4_r1))], ['4', '6','8', '10'])
	# Adjust the margins
	plt.subplots_adjust(bottom= 0.30, left= 0.11)
	plt.ylabel("Time (s)")
	plt.xlabel("Number of repetition of the same simple function in mapping rules")
	# Create legend
	plt.legend(['FunMap+RMLMapper','FunMap$^-$+RMLMapper','RMLMapper**(RML+FnO)'])
	plt.savefig("./Figure8_c.png", dpi=700)


def handler():

	FunMap_rmlmapper = pd.read_csv("./results-funmap-rmlmapper.csv")
	FunMapMinus_rmlmapper = pd.read_csv("./results-funmap-basic-rmlmapper.csv")
	rmlmapper_FnO = pd.read_csv("./results-rmlmapper.csv")
	rmlmapper_7d(FunMap_rmlmapper,FunMapMinus_rmlmapper,rmlmapper_FnO)
	rmlmapper_7c(FunMap_rmlmapper,FunMapMinus_rmlmapper,rmlmapper_FnO)
	rmlmapper_8d(FunMap_rmlmapper,FunMapMinus_rmlmapper,rmlmapper_FnO)
	rmlmapper_8c(FunMap_rmlmapper,FunMapMinus_rmlmapper,rmlmapper_FnO)

if __name__ == "__main__":
	handler()

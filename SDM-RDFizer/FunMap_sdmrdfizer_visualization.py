import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#######################################################################################################

def sdmrdfizer_7b(FunMap_sdm,FunMapMinus_sdm,sdm_FnO):
	
	######### Create bars #######
	barWidth = 0.25

	################## simple functions, veracity75 data
	FunMap_vera75_bar = []
	FunMap_vera75_bar.append(FunMap_sdm.iloc[0,2])
	FunMap_vera75_bar.append(FunMap_sdm.iloc[2,2])
	FunMap_vera75_bar.append(FunMap_sdm.iloc[4,2])
	FunMap_vera75_bar.append(FunMap_sdm.iloc[6,2])

	FunMapMinus_vera75_bar = []
	FunMapMinus_vera75_bar.append(FunMapMinus_sdm.iloc[0,2])
	FunMapMinus_vera75_bar.append(FunMapMinus_sdm.iloc[2,2])
	FunMapMinus_vera75_bar.append(FunMapMinus_sdm.iloc[4,2])
	FunMapMinus_vera75_bar.append(FunMapMinus_sdm.iloc[6,2])

	Current_vera75_bar = []
	Current_vera75_bar.append(sdm_FnO.iloc[0,2])
	Current_vera75_bar.append(sdm_FnO.iloc[2,2])
	Current_vera75_bar.append(sdm_FnO.iloc[4,2])
	Current_vera75_bar.append(sdm_FnO.iloc[6,2])

	#sdm_simple_vera75_bars4 = FunMap_vera75_bar + FunMapMinus_vera75_bar + Current_vera75_bar 
	sdm_simple_vera75_bars4_r1 = np.arange(len(FunMap_vera75_bar))
	sdm_simple_vera75_bars4_r2 = [x + barWidth for x in sdm_simple_vera75_bars4_r1]
	sdm_simple_vera75_bars4_r3 = [x + barWidth for x in sdm_simple_vera75_bars4_r2]
	# Create barplot
	plt.bar(sdm_simple_vera75_bars4_r1, FunMap_vera75_bar, width = barWidth, color = '#59BDC0', label='FunMap+SDM-RDFizer')
	plt.bar(sdm_simple_vera75_bars4_r2, FunMapMinus_vera75_bar, width = barWidth, color = '#b8d8d8ff', label='FunMap$^-$+SDM-RDFizer')
	plt.bar(sdm_simple_vera75_bars4_r3, Current_vera75_bar, width = barWidth, color = '#f6b7a1ff', label='SDM-RDFizer**(RML+FnO)')
	# Text below each barplot with a rotation at 90°
	plt.xticks([r + barWidth for r in range(len(sdm_simple_vera75_bars4_r1))], ['4', '6','8', '10'])
	# Adjust the margins
	plt.subplots_adjust(bottom= 0.30, left= 0.11)
	plt.ylabel("Time (s)")
	plt.xlabel("Number of repetition of the same simple function in mapping rules")
	# Create legend
	plt.legend(['FunMap+SDM-RDFizer','FunMap$^-$+SDM-RDFizer','SDM-RDFizer**(RML+FnO)'])
	plt.savefig("./Figure7_b.png", dpi=700)

def sdmrdfizer_7a(FunMap_sdm,FunMapMinus_sdm,sdm_FnO):
	
	######### Create bars #######
	barWidth = 0.25

	################## simple functions, veracity25 data
	FunMap_vera25_bar = []
	FunMap_vera25_bar.append(FunMap_sdm.iloc[1,2])
	FunMap_vera25_bar.append(FunMap_sdm.iloc[3,2])
	FunMap_vera25_bar.append(FunMap_sdm.iloc[5,2])
	FunMap_vera25_bar.append(FunMap_sdm.iloc[7,2])
	
	FunMapMinus_vera25_bar = []
	FunMapMinus_vera25_bar.append(FunMapMinus_sdm.iloc[1,2])
	FunMapMinus_vera25_bar.append(FunMapMinus_sdm.iloc[3,2])
	FunMapMinus_vera25_bar.append(FunMapMinus_sdm.iloc[5,2])
	FunMapMinus_vera25_bar.append(FunMapMinus_sdm.iloc[7,2])

	Current_vera25_bar = []
	Current_vera25_bar.append(sdm_FnO.iloc[1,2])
	Current_vera25_bar.append(sdm_FnO.iloc[3,2])
	Current_vera25_bar.append(sdm_FnO.iloc[5,2])
	Current_vera25_bar.append(sdm_FnO.iloc[7,2])

	#sdm_simple_vera75_bars4 = FunMap_vera75_bar + FunMapMinus_vera75_bar + Current_vera75_bar 
	sdm_simple_vera25_bars4_r1 = np.arange(len(FunMap_vera25_bar))
	sdm_simple_vera25_bars4_r2 = [x + barWidth for x in sdm_simple_vera25_bars4_r1]
	sdm_simple_vera25_bars4_r3 = [x + barWidth for x in sdm_simple_vera25_bars4_r2]
	# Create barplot
	plt.bar(sdm_simple_vera25_bars4_r1, FunMap_vera25_bar, width = barWidth, color = '#59BDC0', label='FunMap+SDM-RDFizer')
	plt.bar(sdm_simple_vera25_bars4_r2, FunMapMinus_vera25_bar, width = barWidth, color = '#b8d8d8ff', label='FunMap$^-$+SDM-RDFizer')
	plt.bar(sdm_simple_vera25_bars4_r3, Current_vera25_bar, width = barWidth, color = '#f6b7a1ff', label='SDM-RDFizer**(RML+FnO)')
	# Text below each barplot with a rotation at 90°
	plt.xticks([r + barWidth for r in range(len(sdm_simple_vera25_bars4_r1))], ['4', '6','8', '10'])
	# Adjust the margins
	plt.subplots_adjust(bottom= 0.30, left= 0.11)
	plt.ylabel("Time (s)")
	plt.xlabel("Number of repetition of the same simple function in mapping rules")
	# Create legend
	plt.legend(['FunMap+SDM-RDFizer','FunMap$^-$+SDM-RDFizer','SDM-RDFizer**(RML+FnO)'])
	plt.savefig("./Figure7_a.png", dpi=700)

def sdmrdfizer_8b(FunMap_sdm,FunMapMinus_sdm,sdm_FnO):
	
	######### Create bars #######
	barWidth = 0.25

	################## complex functions, veracity75 data
	FunMap_vera75_bar = []
	FunMap_vera75_bar.append(FunMap_sdm.iloc[8,2])
	FunMap_vera75_bar.append(FunMap_sdm.iloc[10,2])
	FunMap_vera75_bar.append(FunMap_sdm.iloc[12,2])
	FunMap_vera75_bar.append(FunMap_sdm.iloc[14,2])

	FunMapMinus_vera75_bar = []
	FunMapMinus_vera75_bar.append(FunMapMinus_sdm.iloc[8,2])
	FunMapMinus_vera75_bar.append(FunMapMinus_sdm.iloc[10,2])
	FunMapMinus_vera75_bar.append(FunMapMinus_sdm.iloc[12,2])
	FunMapMinus_vera75_bar.append(FunMapMinus_sdm.iloc[14,2])

	Current_vera75_bar = []
	Current_vera75_bar.append(sdm_FnO.iloc[8,2])
	Current_vera75_bar.append(sdm_FnO.iloc[10,2])
	Current_vera75_bar.append(sdm_FnO.iloc[12,2])
	Current_vera75_bar.append(sdm_FnO.iloc[14,2])

	#sdm_simple_vera75_bars4 = FunMap_vera75_bar + FunMapMinus_vera75_bar + Current_vera75_bar 
	sdm_complex_vera75_bars4_r1 = np.arange(len(FunMap_vera75_bar))
	sdm_complex_vera75_bars4_r2 = [x + barWidth for x in sdm_complex_vera75_bars4_r1]
	sdm_complex_vera75_bars4_r3 = [x + barWidth for x in sdm_complex_vera75_bars4_r2]
	# Create barplot
	plt.bar(sdm_complex_vera75_bars4_r1, FunMap_vera75_bar, width = barWidth, color = '#59BDC0', label='FunMap+SDM-RDFizer')
	plt.bar(sdm_complex_vera75_bars4_r2, FunMapMinus_vera75_bar, width = barWidth, color = '#b8d8d8ff', label='FunMap$^-$+SDM-RDFizer')
	plt.bar(sdm_complex_vera75_bars4_r3, Current_vera75_bar, width = barWidth, color = '#f6b7a1ff', label='SDM-RDFizer**(RML+FnO)')
	# Text below each barplot with a rotation at 90°
	plt.xticks([r + barWidth for r in range(len(sdm_complex_vera75_bars4_r1))], ['4', '6','8', '10'])
	# Adjust the margins
	plt.subplots_adjust(bottom= 0.30, left= 0.11)
	plt.ylabel("Time (s)")
	plt.xlabel("Number of repetition of the same simple function in mapping rules")
	# Create legend
	plt.legend(['FunMap+SDM-RDFizer','FunMap$^-$+SDM-RDFizer','SDM-RDFizer**(RML+FnO)'])
	plt.savefig("./Figure8_b.png", dpi=700)

def sdmrdfizer_8a(FunMap_sdm,FunMapMinus_sdm,sdm_FnO):
	
	######### Create bars #######
	barWidth = 0.25

	################# complex functions, veracity75 data	
	FunMap_vera25_bar = []
	FunMap_vera25_bar.append(FunMap_sdm.iloc[9,2])
	FunMap_vera25_bar.append(FunMap_sdm.iloc[11,2])
	FunMap_vera25_bar.append(FunMap_sdm.iloc[13,2])
	FunMap_vera25_bar.append(FunMap_sdm.iloc[15,2])

	FunMapMinus_vera25_bar = []
	FunMapMinus_vera25_bar.append(FunMapMinus_sdm.iloc[9,2])
	FunMapMinus_vera25_bar.append(FunMapMinus_sdm.iloc[11,2])
	FunMapMinus_vera25_bar.append(FunMapMinus_sdm.iloc[13,2])
	FunMapMinus_vera25_bar.append(FunMapMinus_sdm.iloc[15,2])

	Current_vera25_bar = []
	Current_vera25_bar.append(sdm_FnO.iloc[9,2])
	Current_vera25_bar.append(sdm_FnO.iloc[11,2])
	Current_vera25_bar.append(sdm_FnO.iloc[13,2])
	Current_vera25_bar.append(sdm_FnO.iloc[15,2])

	#sdm_simple_vera75_bars4 = FunMap_vera75_bar + FunMapMinus_vera75_bar + Current_vera75_bar 
	sdm_complex_vera25_bars4_r1 = np.arange(len(FunMap_vera25_bar))
	sdm_complex_vera25_bars4_r2 = [x + barWidth for x in sdm_complex_vera25_bars4_r1]
	sdm_complex_vera25_bars4_r3 = [x + barWidth for x in sdm_complex_vera25_bars4_r2]
	# Create barplot
	plt.bar(sdm_complex_vera25_bars4_r1, FunMap_vera25_bar, width = barWidth, color = '#59BDC0', label='FunMap+SDM-RDFizer')
	plt.bar(sdm_complex_vera25_bars4_r2, FunMapMinus_vera25_bar, width = barWidth, color = '#b8d8d8ff', label='FunMap$^-$+SDM-RDFizer')
	plt.bar(sdm_complex_vera25_bars4_r3, Current_vera25_bar, width = barWidth, color = '#f6b7a1ff', label='SDM-RDFizer**(RML+FnO)')
	# Text below each barplot with a rotation at 90°
	plt.xticks([r + barWidth for r in range(len(sdm_complex_vera25_bars4_r1))], ['4','6','8','10'])
	# Adjust the margins
	plt.subplots_adjust(bottom= 0.30, left= 0.11)
	plt.ylabel("Time (s)")
	plt.xlabel("Number of repetition of the same simple function in mapping rules")
	# Create legend
	plt.legend(['FunMap+SDM-RDFizer','FunMap$^-$+SDM-RDFizer','SDM-RDFizer**(RML+FnO)'])
	plt.savefig("./Figure8_a.png", dpi=700)

def handler():

	FunMap_sdm = pd.read_csv("./results/results-funmap-sdmrdfizer.csv")
	FunMapMinus_sdm = pd.read_csv("./results/results-funmap-basic-sdmrdfizer.csv")
	sdm_FnO = pd.read_csv("./results/results-sdmrdfizer.csv")
	sdmrdfizer_7b(FunMap_sdm,FunMapMinus_sdm,sdm_FnO)
	sdmrdfizer_7a(FunMap_sdm,FunMapMinus_sdm,sdm_FnO)
	sdmrdfizer_8b(FunMap_sdm,FunMapMinus_sdm,sdm_FnO)
	sdmrdfizer_8a(FunMap_sdm,FunMapMinus_sdm,sdm_FnO)

if __name__ == "__main__":
	handler()

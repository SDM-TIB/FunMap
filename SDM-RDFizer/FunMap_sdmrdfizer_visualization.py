import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#######################################################################################################

def sdmrdfizer(FunMap_sdm,FunMapMinus_sdm,sdm_FnO):
	
	######### Create bars #######
	barWidth = 0.25

	################## simple functions, veracity75 data
	FunMap_vera75_bar = FunMap_sdm.iloc[0:4,2]
	FunMapMinus_vera75_bar = FunMapMinus_sdm.iloc[0:4,2]
	Current_vera75_bar = sdm_FnO.iloc[0:4,2]
	#sdm_simple_vera75_bars4 = FunMap_vera75_bar + FunMapMinus_vera75_bar + Current_vera75_bar 
	sdm_simple_vera75_bars4_r1 = np.arange(len(FunMap_vera75_bar))
	sdm_simple_vera75_bars4_r2 = [x + barWidth for x in sdm_simple_vera75_bars4_r1]
	sdm_simple_vera75_bars4_r3 = [x + barWidth for x in sdm_simple_vera75_bars4_r2]
	# Create barplot
	plt.bar(sdm_simple_vera75_bars4_r1, FunMap_vera75_bar, width = barWidth, color = '#59BDC0', label='FunMap+SDM-RDFizer')
	plt.bar(sdm_simple_vera75_bars4_r2, FunMapMinus_vera75_bar, width = barWidth, color = '#b8d8d8ff', label='FunMap$^-$+SDM-RDFizer')
	plt.bar(sdm_simple_vera75_bars4_r3, Current_vera75_bar, width = barWidth, color = '#f6b7a1ff', label='SDM-RDFizer**(RML+FnO)')
	# Create legend
	plt.legend()
	# Text below each barplot with a rotation at 90°
	plt.xticks([r + barWidth for r in range(len(sdm_simple_vera75_bars4_r1))], ['4', '6','8', '10'])
	# Adjust the margins
	plt.subplots_adjust(bottom= 0.30, left= 0.11)
	plt.ylabel("Time (s)")
	plt.xlabel("Number of repetition of the same simple function in mapping rules")
	plt.legend()
	plt.savefig("./Figure7_b.png", dpi=700)


	################## simple functions, veracity25 data
	FunMap_vera25_bar = FunMap_sdm.iloc[4:8,2]
	FunMapMinus_vera25_bar = FunMapMinus_sdm.iloc[4:8,2]
	Current_vera25_bar = sdm_FnO.iloc[4:8,2]
	#sdm_simple_vera75_bars4 = FunMap_vera75_bar + FunMapMinus_vera75_bar + Current_vera75_bar 
	sdm_simple_vera25_bars4_r1 = np.arange(len(FunMap_vera25_bar))
	sdm_simple_vera25_bars4_r2 = [x + barWidth for x in sdm_simple_vera25_bars4_r1]
	sdm_simple_vera25_bars4_r3 = [x + barWidth for x in sdm_simple_vera25_bars4_r2]
	# Create barplot
	plt.bar(sdm_simple_vera25_bars4_r1, FunMap_vera25_bar, width = barWidth, color = '#59BDC0', label='FunMap+SDM-RDFizer')
	plt.bar(sdm_simple_vera25_bars4_r2, FunMapMinus_vera25_bar, width = barWidth, color = '#b8d8d8ff', label='FunMap$^-$+SDM-RDFizer')
	plt.bar(sdm_simple_vera25_bars4_r3, Current_vera25_bar, width = barWidth, color = '#f6b7a1ff', label='SDM-RDFizer**(RML+FnO)')
	# Create legend
	plt.legend()
	# Text below each barplot with a rotation at 90°
	plt.xticks([r + barWidth for r in range(len(sdm_simple_vera75_bars4_r1))], ['4', '6','8', '10'])
	# Adjust the margins
	plt.subplots_adjust(bottom= 0.30, left= 0.11)
	plt.ylabel("Time (s)")
	plt.xlabel("Number of repetition of the same simple function in mapping rules")
	plt.legend()
	plt.savefig("./Figure7_a.png", dpi=700)


	################## complex functions, veracity75 data
	FunMap_vera75_bar = FunMap_sdm.iloc[8:12,2]
	FunMapMinus_vera75_bar = FunMapMinus_sdm.iloc[8:12,2]
	Current_vera75_bar = sdm_FnO.iloc[8:12,2]
	#sdm_simple_vera75_bars4 = FunMap_vera75_bar + FunMapMinus_vera75_bar + Current_vera75_bar 
	sdm_complex_vera75_bars4_r1 = np.arange(len(FunMap_vera75_bar))
	sdm_complex_vera75_bars4_r2 = [x + barWidth for x in sdm_complex_vera75_bars4_r1]
	sdm_complex_vera75_bars4_r3 = [x + barWidth for x in sdm_complex_vera75_bars4_r2]
	# Create barplot
	plt.bar(sdm_complex_vera75_bars4_r1, FunMap_vera75_bar, width = barWidth, color = '#59BDC0', label='FunMap+SDM-RDFizer')
	plt.bar(sdm_complex_vera75_bars4_r2, FunMapMinus_vera75_bar, width = barWidth, color = '#b8d8d8ff', label='FunMap$^-$+SDM-RDFizer')
	plt.bar(sdm_complex_vera75_bars4_r3, Current_vera75_bar, width = barWidth, color = '#f6b7a1ff', label='SDM-RDFizer**(RML+FnO)')
	# Create legend
	plt.legend()
	# Text below each barplot with a rotation at 90°
	plt.xticks([r + barWidth for r in range(len(sdm_complex_vera75_bars4_r1))], ['4', '6','8', '10'])
	# Adjust the margins
	plt.subplots_adjust(bottom= 0.30, left= 0.11)
	plt.ylabel("Time (s)")
	plt.xlabel("Number of repetition of the same simple function in mapping rules")
	plt.legend()
	plt.savefig("./Figure8_b.png", dpi=700)


	################# complex functions, veracity75 data	
	FunMap_vera25_bar = FunMap_sdm.iloc[12:,2]
	FunMapMinus_vera25_bar = FunMapMinus_sdm.iloc[12:,2]
	Current_vera25_bar = sdm_FnO.iloc[12:,2]	
	#sdm_simple_vera75_bars4 = FunMap_vera75_bar + FunMapMinus_vera75_bar + Current_vera75_bar 
	sdm_complex_vera25_bars4_r1 = np.arange(len(FunMap_vera25_bar))
	sdm_complex_vera25_bars4_r2 = [x + barWidth for x in sdm_complex_vera25_bars4_r1]
	sdm_complex_vera25_bars4_r3 = [x + barWidth for x in sdm_complex_vera25_bars4_r2]
	# Create barplot
	plt.bar(sdm_complex_vera25_bars4_r1, FunMap_vera25_bar, width = barWidth, color = '#59BDC0', label='FunMap+SDM-RDFizer')
	plt.bar(sdm_complex_vera25_bars4_r2, FunMapMinus_vera25_bar, width = barWidth, color = '#b8d8d8ff', label='FunMap$^-$+SDM-RDFizer')
	plt.bar(sdm_complex_vera25_bars4_r3, Current_vera25_bar, width = barWidth, color = '#f6b7a1ff', label='SDM-RDFizer**(RML+FnO)')
	# Create legend
	plt.legend()
	# Text below each barplot with a rotation at 90°
	plt.xticks([r + barWidth for r in range(len(sdm_complex_vera25_bars4_r1))], ['4', '6','8', '10'])
	# Adjust the margins
	plt.subplots_adjust(bottom= 0.30, left= 0.11)
	plt.ylabel("Time (s)")
	plt.xlabel("Number of repetition of the same simple function in mapping rules")
	plt.legend()
	plt.savefig("./Figure8_a.png", dpi=700)

def handler():

	FunMap_sdm = pd.read_csv("./results-funmap-sdmrdfizer.csv")
	FunMapMinus_sdm = pd.read_csv("./results-funmap-basic-sdmrdfizer.csv")
	sdm_FnO = pd.read_csv("./results-sdmrdfizer.csv")
	sdmrdfizer(FunMap_sdm,FunMapMinus_sdm,sdm_FnO)

if __name__ == "__main__":
	handler()
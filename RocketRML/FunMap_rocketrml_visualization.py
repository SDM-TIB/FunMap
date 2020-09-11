
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#######################################################################################################

def rocketrml(FunMap_rocketrml,FunMapMinus_rocketrml,rocketrml_FnO):	


	######### Create bars #######
	barWidth = 0.25

	################## simple functions, veracity75 data
	FunMap_vera75_bar = FunMap_rocketrml.iloc[0:4,2]
	FunMapMinus_vera75_bar = FunMapMinus_rocketrml.iloc[0:4,2]
	Current_vera75_bar = rocketrml_FnO.iloc[0:4,2]
	#rmlmapper_simple_vera75_bars4 = FunMap_vera75_bar + FunMapMinus_vera75_bar + Current_vera75_bar 
	rocketrml_simple_vera75_bars4_r1 = np.arange(len(FunMap_vera75_bar))
	rocketrml_simple_vera75_bars4_r2 = [x + barWidth for x in rocketrml_simple_vera75_bars4_r1]
	rocketrml_simple_vera75_bars4_r3 = [x + barWidth for x in rocketrml_simple_vera75_bars4_r2]
	# Create barplot
	plt.bar(rocketrml_simple_vera75_bars4_r1, FunMap_vera75_bar, width = barWidth, color = '#59BDC0', label='FunMap+RocketRML')
	plt.bar(rocketrml_simple_vera75_bars4_r2, FunMapMinus_vera75_bar, width = barWidth, color = '#b8d8d8ff', label='FunMap$^-$+RocketRML')
	plt.bar(rocketrml_simple_vera75_bars4_r3, Current_vera75_bar, width = barWidth, color = '#f6b7a1ff', label='RocketRML**(RML+FnO)')
	# Create legend
	plt.legend()
	# Text below each barplot with a rotation at 90°
	plt.xticks([r + barWidth for r in range(len(rocketrml_simple_vera75_bars4_r1))], ['4', '6','8', '10'])
	# Adjust the margins
	plt.subplots_adjust(bottom= 0.30, left= 0.11)
	plt.ylabel("Time (s)")
	plt.xlabel("Number of repetition of the same simple function in mapping rules")
	plt.legend()
	plt.savefig("./Figure7_f.png", dpi=700)


	################## simple functions, veracity25 data
	FunMap_vera25_bar = FunMap_rocketrml.iloc[4:8,2]
	FunMapMinus_vera25_bar = FunMapMinus_rocketrml.iloc[4:8,2]
	Current_vera25_bar = rocketrml_FnO.iloc[4:8,2]
	#rmlmapper_simple_vera75_bars4 = FunMap_vera75_bar + FunMapMinus_vera75_bar + Current_vera75_bar 
	rocketrml_simple_vera25_bars4_r1 = np.arange(len(FunMap_vera25_bar))
	rocketrml_simple_vera25_bars4_r2 = [x + barWidth for x in rocketrml_simple_vera25_bars4_r1]
	rocketrml_simple_vera25_bars4_r3 = [x + barWidth for x in rocketrml_simple_vera25_bars4_r2]
	# Create barplot
	plt.bar(rocketrml_simple_vera25_bars4_r1, FunMap_vera25_bar, width = barWidth, color = '#59BDC0', label='FunMap+RocketRML')
	plt.bar(rocketrml_simple_vera25_bars4_r2, FunMapMinus_vera25_bar, width = barWidth, color = '#b8d8d8ff', label='FunMap$^-$+RocketRML')
	plt.bar(rocketrml_simple_vera25_bars4_r3, Current_vera25_bar, width = barWidth, color = '#f6b7a1ff', label='RocketRML**(RML+FnO)')
	# Create legend
	plt.legend()
	# Text below each barplot with a rotation at 90°
	plt.xticks([r + barWidth for r in range(len(rocketrml_simple_vera75_bars4_r1))], ['4', '6','8', '10'])
	# Adjust the margins
	plt.subplots_adjust(bottom= 0.30, left= 0.11)
	plt.ylabel("Time (s)")
	plt.xlabel("Number of repetition of the same simple function in mapping rules")
	plt.legend()
	plt.savefig("./Figure7_e.png", dpi=700)

def handler():

	FunMap_rocketrml = pd.read_csv("./results-rocketrml.csv")
	FunMapMinus_rocketrml = pd.read_csv("./results-funmap-rocketrml.csv")
	rocketrml_FnO = pd.read_csv("./results-funmap-basic-rocketrml.csv")
	rocketrml(FunMap_rocketrml,FunMapMinus_rocketrml,rocketrml_FnO)

if __name__ == "__main__":results-rocketrml.csv
	handler()

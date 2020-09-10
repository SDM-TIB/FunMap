
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
	plt.savefig("/path_to_save/veracity75_sdmrdfizer_simple.png", dpi=700)


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
	plt.savefig("/path_to_save/veracity25_sdmrdfizer_simple.png", dpi=700)


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
	plt.savefig("/path_to_save/veracity75_sdmrdfizer_complex.png", dpi=700)


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
	plt.savefig("/path_to_save/veracity25_sdmrdfizer_complex.png", dpi=700)


def rmlmapper(FunMap_rmlmapper,FunMapMinus_rmlmapper,rmlmapper_FnO):

	######### Create bars #######
	barWidth = 0.25

	################## simple functions, veracity75 data
	FunMap_vera75_bar = FunMap_rmlmapper.iloc[0:4,2]
	FunMapMinus_vera75_bar = FunMapMinus_rmlmapper.iloc[0:4,2]
	Current_vera75_bar = rmlmapper_FnO.iloc[0:4,2]
	#rmlmapper_simple_vera75_bars4 = FunMap_vera75_bar + FunMapMinus_vera75_bar + Current_vera75_bar 
	rmlmapper_simple_vera75_bars4_r1 = np.arange(len(FunMap_vera75_bar))
	rmlmapper_simple_vera75_bars4_r2 = [x + barWidth for x in rmlmapper_simple_vera75_bars4_r1]
	rmlmapper_simple_vera75_bars4_r3 = [x + barWidth for x in rmlmapper_simple_vera75_bars4_r2]
	# Create barplot
	plt.bar(rmlmapper_simple_vera75_bars4_r1, FunMap_vera75_bar, width = barWidth, color = '#59BDC0', label='FunMap+RMLMapper')
	plt.bar(rmlmapper_simple_vera75_bars4_r2, FunMapMinus_vera75_bar, width = barWidth, color = '#b8d8d8ff', label='FunMap$^-$+RMLMapper')
	plt.bar(rmlmapper_simple_vera75_bars4_r3, Current_vera75_bar, width = barWidth, color = '#f6b7a1ff', label='RMLMapper**(RML+FnO)')
	# Create legend
	plt.legend()
	# Text below each barplot with a rotation at 90°
	plt.xticks([r + barWidth for r in range(len(rmlmapper_simple_vera75_bars4_r1))], ['4', '6','8', '10'])
	# Adjust the margins
	plt.subplots_adjust(bottom= 0.30, left= 0.11)
	plt.ylabel("Time (s)")
	plt.xlabel("Number of repetition of the same simple function in mapping rules")
	plt.legend()
	plt.savefig("/path_to_save/veracity75_rmlmapper_simple.png", dpi=700)


	################## simple functions, veracity25 data
	FunMap_vera25_bar = FunMap_rmlmapper.iloc[4:8,2]
	FunMapMinus_vera25_bar = FunMapMinus_rmlmapper.iloc[4:8,2]
	Current_vera25_bar = rmlmapper_FnO.iloc[4:8,2]
	#rmlmapper_simple_vera75_bars4 = FunMap_vera75_bar + FunMapMinus_vera75_bar + Current_vera75_bar 
	rmlmapper_simple_vera25_bars4_r1 = np.arange(len(FunMap_vera25_bar))
	rmlmapper_simple_vera25_bars4_r2 = [x + barWidth for x in rmlmapper_simple_vera25_bars4_r1]
	rmlmapper_simple_vera25_bars4_r3 = [x + barWidth for x in rmlmapper_simple_vera25_bars4_r2]
	# Create barplot
	plt.bar(rmlmapper_simple_vera25_bars4_r1, FunMap_vera25_bar, width = barWidth, color = '#59BDC0', label='FunMap+RMLMapper')
	plt.bar(rmlmapper_simple_vera25_bars4_r2, FunMapMinus_vera25_bar, width = barWidth, color = '#b8d8d8ff', label='FunMap$^-$+RMLMapper')
	plt.bar(rmlmapper_simple_vera25_bars4_r3, Current_vera25_bar, width = barWidth, color = '#f6b7a1ff', label='RMLMapper**(RML+FnO)')
	# Create legend
	plt.legend()
	# Text below each barplot with a rotation at 90°
	plt.xticks([r + barWidth for r in range(len(rmlmapper_simple_vera75_bars4_r1))], ['4', '6','8', '10'])
	# Adjust the margins
	plt.subplots_adjust(bottom= 0.30, left= 0.11)
	plt.ylabel("Time (s)")
	plt.xlabel("Number of repetition of the same simple function in mapping rules")
	plt.legend()
	plt.savefig("/path_to_save/veracity25_rmlmapper_simple.png", dpi=700)


	################## complex functions, veracity75 data
	FunMap_vera75_bar = FunMap_rmlmapper.iloc[8:12,2]
	FunMapMinus_vera75_bar = FunMapMinus_rmlmapper.iloc[8:12,2]
	Current_vera75_bar = rmlmapper_FnO.iloc[8:12,2]
	#rmlmapper_simple_vera75_bars4 = FunMap_vera75_bar + FunMapMinus_vera75_bar + Current_vera75_bar 
	rmlmapper_complex_vera75_bars4_r1 = np.arange(len(FunMap_vera75_bar))
	rmlmapper_complex_vera75_bars4_r2 = [x + barWidth for x in rmlmapper_complex_vera75_bars4_r1]
	rmlmapper_complex_vera75_bars4_r3 = [x + barWidth for x in rmlmapper_complex_vera75_bars4_r2]
	# Create barplot
	plt.bar(rmlmapper_complex_vera75_bars4_r1, FunMap_vera75_bar, width = barWidth, color = '#59BDC0', label='FunMap+RMLMapper')
	plt.bar(rmlmapper_complex_vera75_bars4_r2, FunMapMinus_vera75_bar, width = barWidth, color = '#b8d8d8ff', label='FunMap$^-$+RMLMapper')
	plt.bar(rmlmapper_complex_vera75_bars4_r3, Current_vera75_bar, width = barWidth, color = '#f6b7a1ff', label='RMLMapper**(RML+FnO)')
	# Create legend
	plt.legend()
	# Text below each barplot with a rotation at 90°
	plt.xticks([r + barWidth for r in range(len(rmlmapper_complex_vera75_bars4_r1))], ['4', '6','8', '10'])
	# Adjust the margins
	plt.subplots_adjust(bottom= 0.30, left= 0.11)
	plt.ylabel("Time (s)")
	plt.xlabel("Number of repetition of the same simple function in mapping rules")
	plt.legend()
	plt.savefig("/path_to_save/veracity75_rmlmapper_complex.png", dpi=700)


	################## complex functions, veracity75 data	
	FunMap_vera25_bar = FunMap_rmlmapper.iloc[12:,2]
	FunMapMinus_vera25_bar = FunMapMinus_rmlmapper.iloc[12:,2]
	Current_vera25_bar = rmlmapper_FnO.iloc[12:,2]	
	#rmlmapper_simple_vera75_bars4 = FunMap_vera75_bar + FunMapMinus_vera75_bar + Current_vera75_bar 
	rmlmapper_complex_vera25_bars4_r1 = np.arange(len(FunMap_vera25_bar))
	rmlmapper_complex_vera25_bars4_r2 = [x + barWidth for x in rmlmapper_complex_vera25_bars4_r1]
	rmlmapper_complex_vera25_bars4_r3 = [x + barWidth for x in rmlmapper_complex_vera25_bars4_r2]
	# Create barplot
	plt.bar(rmlmapper_complex_vera25_bars4_r1, FunMap_vera25_bar, width = barWidth, color = '#59BDC0', label='FunMap+RMLMapper')
	plt.bar(rmlmapper_complex_vera25_bars4_r2, FunMapMinus_vera25_bar, width = barWidth, color = '#b8d8d8ff', label='FunMap$^-$+RMLMapper')
	plt.bar(rmlmapper_complex_vera25_bars4_r3, Current_vera25_bar, width = barWidth, color = '#f6b7a1ff', label='RMLMapper**(RML+FnO)')
	# Create legend
	plt.legend()
	# Text below each barplot with a rotation at 90°
	plt.xticks([r + barWidth for r in range(len(rmlmapper_complex_vera25_bars4_r1))], ['4', '6','8', '10'])
	# Adjust the margins
	plt.subplots_adjust(bottom= 0.30, left= 0.11)
	plt.ylabel("Time (s)")
	plt.xlabel("Number of repetition of the same simple function in mapping rules")
	plt.legend()
	plt.savefig("/path_to_save/veracity25_rmlmapper_complex.png", dpi=700)



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
	plt.savefig("/path_to_save/veracity75_rocketrml_simple.png", dpi=700)


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
	plt.savefig("/path_to_save/veracity25_rocketrml_simple.png", dpi=700)



def handler():

	FunMap_sdm = pd.read_csv("/mnt/e/.csv")
	FunMapMinus_sdm = pd.read_csv("/mnt/e/.csv")
	sdm_FnO = pd.read_csv("/mnt/e/.csv")
	sdmrdfizer(FunMap_sdm,FunMapMinus_sdm,sdm_FnO)

	FunMap_rmlmapper = pd.read_csv("/mnt/e/.csv")
	FunMapMinus_rmlmapper = pd.read_csv("/mnt/e/.csv")
	rmlmapper_FnO = pd.read_csv("/mnt/e/.csv")
	rmlmapper(FunMap_rmlmapper,FunMapMinus_rmlmapper,rmlmapper_FnO)

	FunMap_rocketrml = pd.read_csv("/mnt/e/.csv")
	FunMapMinus_rocketrml = pd.read_csv("/mnt/e/.csv")
	rocketrml_FnO = pd.read_csv("/mnt/e/.csv")
	rocketrml(FunMap_rocketrml,FunMapMinus_rocketrml,rocketrml_FnO)

if __name__ == "__main__":
	handler()

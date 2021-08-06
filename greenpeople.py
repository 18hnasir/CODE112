import csv
import glob, os

os.chdir(os.getcwd())
title = "title.csv"
datesOutput = "dates.csv"
RecyclingOutput = "RecyclingData.csv"
SolidWasteDataOutput = "SolidWasteData.csv"
HazardousWasteDataOutput = "HazardousWasteData.csv"
OrganicDataOutput = "OrganicsData.csv" 
TotalDataOutput = "TotalData.csv"
RecyclingTonsDataOutput = "RecyclingTonsData.csv"
SolidWasteTonsDataOutput = "SolidWasteTonsData.csv"
HazardousWasteTonsDataOuput = "HazardousWasteTonsData.csv"
OrganicsTonsDataOutput = "OrganicsTonsData.csv"
TotalTonsDataOuput = "TotalTonsData.csv"


count = 0
s1 = ['Wastestream']
s2 = ['Recycling']
s3 = ['Solid Waste']
s4 = ['Hazardous Waste']
s5 = ['Organics']
s6 = ['Total:']
s7 = ['Recycling (TONS)']
s8 = ['Solid Waste (TONS)']
s9 = ['Haz Waste (TONS)']
s10 = ['Organics (TONS)']
s11 = ['Total (TONS)']
reportName = []
valueType = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11]
dates = []
RecyclingData = []
SolidWasteData = []
HazardousWasteData = []
OrganicsData = []
TotalData = []
RecyclingTonsData = []
SolidWasteTonsData = []
HazardousWasteTonsData = []
OrganicsTonsData = []
TotalTonsData = []

with open('plantdata.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
    	row_reader = csv.reader(row, delimiter='\"')
    	for token in row_reader:
    		if (token == []):
    			continue
    		if (count == 0):
    			reportName.append(token)
    			count += 1
    			continue
    		if (token==s1 or token==s2 or token==s3 or token==s4 or token==s5 or token==s6 or token==s7 or token==s8 or token==s9 or token==s10 or token==s11):
    			count += 1
    			continue
    		if (count == 2):
    			dates.append(token)
    		if (count == 3):
    			RecyclingData.append(token)
    		if (count == 4):
    			SolidWasteData.append(token)
    		if (count == 5):
    			HazardousWasteData.append(token)
    		if (count == 6):
    			OrganicsData.append(token)
    		if (count == 7):
    			TotalData.append(token)
    		if (count == 8):
    			RecyclingTonsData.append(token)
    		if (count == 9):
    			SolidWasteTonsData.append(token)
    		if (count == 10):
    			HazardousWasteTonsData.append(token)
    		if (count == 11):
    			OrganicsTonsData.append(token)
    		if (count == 12):
    			TotalTonsData.append(token)
    for i in dates:
    	temp = i[0].replace(", ", " ")
    	i[0] = temp
    for i in RecyclingData:
    	temp = i[0].replace(", ", " ")
    	i[0] = temp
    for i in SolidWasteData:
    	temp = i[0].replace(", ", " ")
    	i[0] = temp
    for i in HazardousWasteData:
    	temp = i[0].replace(", ", " ")
    	i[0] = temp
    for i in OrganicsData:
    	temp = i[0].replace(", ", " ")
    	i[0] = temp
    for i in TotalData:
    	temp = i[0].replace(", ", " ")
    	i[0] = temp
    for i in RecyclingTonsData:
    	temp = i[0].replace(", ", " ")
    	i[0] = temp
    for i in SolidWasteTonsData:
    	temp = i[0].replace(", ", " ")
    	i[0] = temp
    for i in HazardousWasteTonsData:
    	temp = i[0].replace(", ", " ")
    	i[0] = temp
    for i in OrganicsTonsData:
    	temp = i[0].replace(", ", " ")
    	i[0] = temp
    for i in TotalTonsData:
    	temp = i[0].replace(", ", " ")
    	i[0] = temp

    reportNameFile = [[reportName]]
    datesFile = [[s1, dates]]
    RecyclingDataFile = [[s2, RecyclingData]]
    SolidWasteDataFile = [[s3, SolidWasteData]]
    HazardousWasteDataFile = [[s4, HazardousWasteData]]
    OrganicsDataFile = [[s5, OrganicsData]]
    TotalDataFile = [[s6, TotalData]]
    RecyclingTonsDataFile = [[s7, RecyclingTonsData]]
    SolidWasteTonsDataFile = [[s8, SolidWasteTonsData]]
    HazardousWasteTonsDataFile = [[s9, HazardousWasteTonsData]]
    OrganicsTonsDataFile = [[s10, OrganicsTonsData]]
    TotalTonsDataFile = [[s11, TotalTonsData]]

    with open(title, 'a') as csvfile2:
    	csvwriter = csv.writer(csvfile2, delimiter = ',')
    	csvwriter.writerows(reportNameFile)
    with open(datesOutput, 'a') as csvfile3:
    	csvwriter = csv.writer(csvfile3, delimiter = ',')
    	csvwriter.writerows(datesFile)
    with open(RecyclingOutput, 'a') as csvfile4:
    	csvwriter = csv.writer(csvfile4, delimiter = ',')
    	csvwriter.writerows(RecyclingDataFile)
    with open(SolidWasteDataOutput, 'a') as csvfile5:
    	csvwriter = csv.writer(csvfile5, delimiter = ',')
    	csvwriter.writerows(SolidWasteDataFile)
    with open(HazardousWasteDataOutput, 'a') as csvfile6:
    	csvwriter = csv.writer(csvfile6, delimiter = ',')
    	csvwriter.writerows(HazardousWasteDataFile)
    with open(OrganicDataOutput, 'a') as csvfile7:
    	csvwriter = csv.writer(csvfile7, delimiter = ',')
    	csvwriter.writerows(OrganicsDataFile)
    with open(TotalDataOutput, 'a') as csvfile8:
    	csvwriter = csv.writer(csvfile8, delimiter = ',')
    	csvwriter.writerows(TotalDataFile)
    with open(RecyclingTonsDataOutput, 'a') as csvfile9:
    	csvwriter = csv.writer(csvfile9, delimiter = ',')
    	csvwriter.writerows(RecyclingTonsDataFile)
    with open(SolidWasteTonsDataOutput, 'a') as csvfile10:
    	csvwriter = csv.writer(csvfile10, delimiter = ',')
    	csvwriter.writerows(SolidWasteTonsDataFile)
    with open(HazardousWasteTonsDataOuput, 'a') as csvfile11:
    	csvwriter = csv.writer(csvfile11, delimiter = ',')
    	csvwriter.writerows(HazardousWasteTonsDataFile)
    with open(OrganicsTonsDataOutput, 'a') as csvfile12:
    	csvwriter = csv.writer(csvfile12, delimiter = ',')
    	csvwriter.writerows(OrganicsTonsDataFile)
    with open(TotalTonsDataOuput, 'a') as csvfile13:
    	csvwriter = csv.writer(csvfile13, delimiter = ',')
    	csvwriter.writerows(TotalTonsDataFile)
    

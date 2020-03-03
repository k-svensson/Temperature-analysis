# Temperature analysis
 
Demo analysis of temperature observations from a private weather station compared to the official meteorological service and the normal temperatures 1961-90.

Period analysed: 1 September 2019 - 25 February 2020.

Conclusion: Yes, this winter has been very mild!



## Main files in this repo:

[PDF report, including case description and illustrations](Report_temperature_analysis.pdf)

[Power BI desktop visualization](Temp_analysis.pbix)

[Report in markdown format (no graphics)](Report.md)  


--  
Python files:

[Python script to download historical WU data](WU_downloader.py)

[Python script to prepare WU data](WU_prepare.py)


--  
Input files:

[Normal daily temperature at Blindern](Døgnnormal_Blindern.txt)

[Observed daily temperature at Blindern](Døgnverdier_Blindern_190820-200225.txt)

[Sample JSON result from Weather Underground query](WUdata-20200215.json)

[Weather Underground data converted to daily average CSV file](Galgeberg2.csv)

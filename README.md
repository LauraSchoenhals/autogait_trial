# autogait_trial
Convert data from SMR to XLSX and from phase to annotation table to enable testing of Auto Gait A

What you should do: 
1) clone this repo and also AutoGaitA https://github.com/mahan-hosseini/AutoGaitA
2) run AutoGaitA per their documentation; use WT_Levelwalk_for_AutoGaitA folder as this contains csv & annotation table
3) see format of data + results

See also: 
https://github.com/mahan-hosseini/AutoGaitA

Of note:
- AutoGait A says in a couple of places that gp#m# names are not compatible with this software. I changed them to "mouse" + the group number + a 2 digit mouse number (adding a 0 if needed)
- ie: gp5m3 becomes mouse503
- However, the documentation also says that gp#m# names should work just fine. 
